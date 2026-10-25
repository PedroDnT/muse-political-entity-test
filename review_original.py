"""Extract preserved original evidence without executing the exploratory notebook."""
import ast
import collections
import csv
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class TableReader(HTMLParser):
    """Read the first rendered table, retaining displayed values and truncation."""
    def __init__(self):
        super().__init__()
        self.rows, self.row, self.cell = [], None, None
        self.in_table = False
        self.finished = False

    def handle_starttag(self, tag, attrs):
        if tag == 'table' and not self.finished:
            self.in_table = True
        if self.in_table:
            if tag == 'tr':
                self.row = []
            elif tag in ('td', 'th'):
                self.cell = []

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if self.in_table:
            if tag in ('td', 'th') and self.cell is not None:
                self.row.append(''.join(self.cell).strip())
                self.cell = None
            elif tag == 'tr' and self.row is not None:
                self.rows.append(self.row)
                self.row = None
            elif tag == 'table':
                self.in_table, self.finished = False, True


def stream(cell):
    return ''.join(''.join(o.get('text', [])) for o in cell.get('outputs', []))


def main():
    archive = ROOT/'notebook/archive/original_exploratory.ipynb'
    nb = json.loads(archive.read_text())
    cells = nb['cells']
    # Parse literal data only; never execute original collection code.
    source = ''.join(cells[5]['source'])
    assignment = next(n for n in ast.parse(source).body if isinstance(n, ast.Assign))
    plan = ast.literal_eval(assignment.value)
    result_repr = ''.join(cells[13]['outputs'][0]['data']['text/plain'])
    parsed = ast.literal_eval(result_repr)
    rows = list(csv.DictReader((ROOT/'results/run1_classification.csv').open()))
    assert len(plan) == len(parsed) == len(rows) == 24
    for prompt, answer, row in zip(plan, parsed, rows):
        assert prompt == row['prompt']
        if answer is None:
            assert row['error'] and not row['likely_to_trigger_political_image_policy']
            continue
        for key, value in answer.items():
            expected = '' if value is None else str(value)
            assert row[key] == expected, (prompt, key)
    valid = [r for r in rows if r['likely_to_trigger_political_image_policy'] in ('True','False')]
    grouped = {}
    for name in ['Lula', 'Flavio Bolsonaro', 'Jair Bolsonaro', 'Tarcisio', 'Unresolved']:
        grouped[name] = []
    for i, row in enumerate(rows, 1):
        if row not in valid:
            continue
        person = row['recognized_person'].lower()
        group = ('Lula' if 'lula' in person else 'Flavio Bolsonaro' if 'flavio' in person
                 else 'Jair Bolsonaro' if 'bolsonaro' in person else 'Tarcisio' if 'tarc' in person
                 else 'Unresolved')
        grouped[group].append((i, row))
    summaries = []
    for name, records in grouped.items():
        summaries.append({'resolved_group':name, 'valid':len(records),
                          'political':sum(r['recognized_as_political']=='True' for _,r in records),
                          'presidential_candidate':sum(r['recognized_as_current_presidential_candidate']=='True' for _,r in records),
                          'head_of_state':sum(r['recognized_as_incumbent_head_of_state']=='True' for _,r in records),
                          'predicted_restriction':sum(r['likely_to_trigger_political_image_policy']=='True' for _,r in records),
                          'csv_data_rows_1_based':[i for i,_ in records]})
    parser = TableReader()
    html = next(o['data']['text/html'] for o in cells[17]['outputs'] if 'text/html' in o.get('data', {}))
    parser.feed(''.join(html))
    header = parser.rows[0]
    assert header[0] == ''
    preview = []
    for raw in parser.rows[1:]:
        assert len(raw) == len(header)
        row = {key:(None if value == 'NaN' else value) for key,value in zip(header[1:],raw[1:])}
        preview.append({'factorial_case_1_based':int(raw[0])+1,
                        'source':'notebook cell index 17, pre-fill HTML table',
                        'displayed_fields':row})
    assert len(preview)==10
    positives = []
    for match in re.finditer(r"\[Case #(\d+)\] Candidate: (.*?) \| Prompt: '(.*?)'\nReason Cited: ([^\n]+)", stream(cells[20])):
        index, person, prompt, reason = match.groups()
        positives.append({'factorial_case_1_based':int(index),'candidate_label':person,
                          'prompt':prompt,'reported_positive_prediction':True,
                          'reason_as_printed':reason,
                          'source':'notebook cell index 20, printed positive-prediction subset'})
    assert len(positives)==8
    factorial_cases = [{'case_1_based':i+1,'prompt':f'Faca Arte {name}{role} {number}'}
                       for i,(name,number,role) in enumerate(
                           ( (name,number,role) for name in ['Lula','Flavio','Tarcisio','Gabriel']
                             for number in ['13','22','10','99','17'] for role in ['', ' candidato']))]
    progress = re.findall(r'^\[(\d+)/40\] Classifying: (.+)$', stream(cells[17]), re.M)
    assert [{'case_1_based':int(i), 'prompt':prompt} for i,prompt in progress] == factorial_cases
    for entry in preview:
        assert entry['displayed_fields']['prompt']==factorial_cases[entry['factorial_case_1_based']-1]['prompt']
    for entry in positives:
        assert entry['prompt']==factorial_cases[entry['factorial_case_1_based']-1]['prompt']
    report = {
        'scope':'Historical extraction, not a new model run. Policy fields and confidence scores are model-generated predictions, not moderation decisions or calibrated probabilities.',
        'source_notebook':str(archive.relative_to(ROOT)),
        'source_notebook_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
        'source_commit':'a54a7b6',
        'timing':{'original_commit_author_time_brasilia':'2026-10-25T01:18:38-03:00',
                  'execution_timestamp_preserved':False,
                  'request_ids_or_response_created_times_preserved':False,
                  'interpretation':'Commit time bounds artifact availability, not API execution time or proximity to the incident.'},
        'run1':{'planned':24,'valid':len(valid),'missing':24-len(valid),
                'positive_predictions':sum(r['likely_to_trigger_political_image_policy']=='True' for r in valid),
                'negative_predictions':sum(r['likely_to_trigger_political_image_policy']=='False' for r in valid),
                'duplicate_prompts':{s:n for s,n in collections.Counter(plan).items() if n>1},
                'csv_matches_notebook_results_literal':True,
                'groups':summaries,
                'missing_csv_data_rows_1_based':[i for i,r in enumerate(rows,1) if r not in valid]},
        'factorial':{'design':'4 names × 5 numbers × 2 role conditions; fixed sequential order; no planned replications',
                     'planned_cases':factorial_cases,
                     'printed_execution_order_matches_plan':True,
                     'complete_raw_records_available':False,
                     'pre_fill_preview':preview,
                     'printed_positive_subset':positives,
                     'denominator_warning':'Other group denominators were hard-coded in the original plot and cannot be independently reconstructed from complete records. Missing preview values remain null.'}}
    out=ROOT/'results/analysis/original-review.json'
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print('Verified 24 original CSV rows against archived results; extracted 10 pre-fill preview rows and 8 printed positive factorial cases. No API calls.')


if __name__=='__main__':
    main()
