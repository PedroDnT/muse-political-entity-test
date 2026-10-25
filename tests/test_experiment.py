import collections
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from experiment import make_plan, parse_response, summarize, paired_summary, collect

ANSWER = {'recognized_person':'Lula', 'recognized_as_political':True, 'public_office':None}

def envelope(answer):
    return {'choices':[{'finish_reason':'stop','message':{'content':json.dumps(answer)}}]}

class Response:
    def __init__(self, status, body):
        self.status_code = status
        self.text = json.dumps(body)

class Session:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.calls = 0
    def post(self, *args, **kwargs):
        self.calls += 1
        return next(self.responses)

class ExperimentTests(unittest.TestCase):
    def test_balanced_reproducible_design(self):
        p = make_plan()
        self.assertEqual(p, make_plan())
        self.assertEqual(len(p['cases']), 240)
        self.assertEqual(len({c['case_id'] for c in p['cases']}), 240)
        counts = collections.Counter((c['entity'],c['name_form'],c['number'],c['role']) for c in p['cases'])
        self.assertEqual(set(counts.values()), {5})
        self.assertNotIn('was refused', p['cases'][0]['prompt'])
        self.assertNotIn('WhatsApp', p['cases'][0]['prompt'])

    def test_strict_schema(self):
        for value in ['false', 0, None]:
            self.assertEqual(parse_response(envelope(dict(ANSWER,recognized_as_political=value)))[0], 'invalid_schema')
        self.assertEqual(parse_response(envelope({}))[0], 'invalid_schema')
        self.assertEqual(parse_response(envelope(ANSWER)), ('valid', ANSWER))

    def test_response_failures_remain_distinct(self):
        self.assertEqual(parse_response({})[0], 'invalid_envelope')
        for content, expected in [(None,'empty_content'), ('not JSON','invalid_json'), ([], 'invalid_envelope')]:
            self.assertEqual(parse_response({'choices':[{'message':{'content':content}}]})[0], expected)
        body = envelope(ANSWER)
        body['choices'][0]['finish_reason'] = 'length'
        self.assertEqual(parse_response(body)[0], 'truncated')
        body['choices'][0] = {'message':{'refusal':'Cannot answer'}}
        self.assertEqual(parse_response(body)[0], 'api_refusal')

    def test_failures_and_unrun_are_never_negative(self):
        p = make_plan(1)
        c = p['cases'][0]
        records = [{'case_id':c['case_id'], 'status':'http_error', 'answer':None}]
        rows = summarize(p, records)
        self.assertEqual(sum(r['nonpolitical'] for r in rows), 0)
        self.assertEqual(sum(r['missing_or_not_run'] for r in rows), 48)
        self.assertTrue(all(r['political_rate'] is None for r in rows))

    def test_complete_pairs_only(self):
        p = make_plan(1)
        cases = [c for c in p['cases'] if c['name_form']=='full' and c['number']=='13' and c['role']=='']
        records = [{'case_id':c['case_id'], 'status':'valid', 'answer':dict(ANSWER,recognized_as_political=c['entity']=='lula')}
                   for c in cases if c['entity'] in ('lula','flavio')]
        result = paired_summary(p, records)
        self.assertEqual(result['complete_pairs'], 1)
        self.assertEqual(result['incomplete_pairs'], 11)
        self.assertEqual(result['mean_political_flag_difference'], 1)

    def test_other_protocol_cannot_be_pooled(self):
        p = make_plan(1)
        record = {'case_id':p['cases'][0]['case_id'],'plan_sha256':'different-plan','status':'valid','answer':ANSWER}
        with self.assertRaises(ValueError): summarize(p,[record])

    def test_duplicate_results_rejected(self):
        p = make_plan(1)
        r = {'case_id':p['cases'][0]['case_id'],'status':'empty_content','answer':None}
        with self.assertRaises(ValueError): summarize(p, [r,r])

    def test_retry_retains_attempts_and_counts_against_budget(self):
        p = make_plan(1)
        session = Session([Response(429, {'error':'temporary'}), Response(200,envelope(ANSWER))])
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, OPENROUTER_API_KEY='test-only-token'):
            out = collect(p, Path(directory)/'run', 2, session=session, sleep=lambda _:None)
            rows = [json.loads(line) for line in (out/'responses.jsonl').read_text().splitlines()]
            self.assertEqual(session.calls, 2)
            self.assertEqual(len(rows), 1)
            self.assertEqual(len(rows[0]['attempts']), 2)
            self.assertEqual(rows[0]['status'], 'valid')
            self.assertEqual(sum(r['missing_or_not_run'] for r in summarize(p,rows)),47)
            self.assertEqual(json.loads((out/'plan.json').read_text()),p)

    def test_auth_stops_and_redacts(self):
        session = Session([Response(401, {'error':'test-only-token'})])
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, OPENROUTER_API_KEY='test-only-token'):
            out = collect(make_plan(1), Path(directory)/'run', 10, session=session, sleep=lambda _:None)
            text = (out/'responses.jsonl').read_text()
            self.assertEqual(session.calls, 1)
            self.assertNotIn('test-only-token',text)
            self.assertIn('[REDACTED]',text)

    def test_existing_run_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, OPENROUTER_API_KEY='test-only-token'):
            with self.assertRaises(FileExistsError): collect(make_plan(1), directory, 1)

    def test_parallel_budget_and_evidence(self):
        session = Session([Response(200, envelope(ANSWER)) for _ in range(7)])
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, OPENROUTER_API_KEY='test-only-token'):
            out = collect(make_plan(1), Path(directory)/'run', 7, session=session, sleep=lambda _:None, workers=4)
            records = [json.loads(line) for line in (out/'responses.jsonl').read_text().splitlines()]
            attempts = [json.loads(line) for line in (out/'attempts.jsonl').read_text().splitlines()]
            self.assertEqual(session.calls, 7)
            self.assertEqual(len(records), 7)
            self.assertEqual(len(attempts), 7)
            self.assertEqual(len({r['case_id'] for r in records}), 7)
            self.assertEqual(sum(r['valid'] for r in summarize(make_plan(1),records)),7)

    def test_missing_key_creates_no_run(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ,{},clear=True):
            with self.assertRaises(ValueError): collect(make_plan(1),Path(directory)/'run',1)
            self.assertFalse((Path(directory)/'run').exists())

if __name__ == '__main__': unittest.main()
