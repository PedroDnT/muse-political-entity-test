"""Recompute number/role strata from preserved responses; no model or network calls."""
import csv
import json
from pathlib import Path

from experiment import ENTITIES, summarize

ROOT = Path(__file__).resolve().parent


def main():
    run = ROOT / 'results/v2_run1'
    plan = json.loads((run/'plan.json').read_text())
    records = [json.loads(line) for line in (run/'responses.jsonl').read_text().splitlines()]
    summarize(plan, records)  # Reject duplicate, unknown or mismatched evidence.
    by_id = {r['case_id']: r for r in records}
    rows = []
    for entity in ENTITIES:
        for form in ('short', 'full'):
            for role in ('', 'candidato'):
                for number in ('', '13', '22'):
                    cases = sorted([c for c in plan['cases'] if
                                    (c['entity'], c['name_form'], c['role'], c['number']) ==
                                    (entity, form, role, number)], key=lambda c: c['repetition'])
                    valid = [by_id[c['case_id']]['answer'] for c in cases
                             if by_id.get(c['case_id'], {}).get('status') == 'valid']
                    rows.append(dict(entity=entity, name_form=form, role=role, number=number,
                                     text=cases[0]['text'], planned=len(cases), valid=len(valid),
                                     political=sum(a['recognized_as_political'] for a in valid),
                                     unresolved=sum(a['recognized_person'] is None for a in valid),
                                     missing=len(cases)-len(valid),
                                     case_ids=[c['case_id'] for c in cases]))
    logprob_counts = {'returned_choices': 0, 'choices_with_nonnull_logprobs': 0}
    for record in records:
        for attempt in record['attempts']:
            raw = attempt.get('raw_response')
            if isinstance(raw, str):
                try:
                    raw = json.loads(raw)
                except json.JSONDecodeError:
                    continue
            if not isinstance(raw, dict):
                continue
            for choice in raw.get('choices', []):
                logprob_counts['returned_choices'] += 1
                logprob_counts['choices_with_nonnull_logprobs'] += choice.get('logprobs') is not None
    out = ROOT / 'results/analysis'
    out.mkdir(exist_ok=True)
    report = {'source_run': 'results/v2_run1',
              'scope': 'Post-collection descriptive strata of the frozen factorial design; not internal probabilities or WhatsApp decisions.',
              'logprob_availability_in_records': logprob_counts, 'groups': rows}
    (out/'number-cues.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    fields = [k for k in rows[0] if k != 'case_ids']
    with (out/'number-cues.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    print(f'Saved {len(rows)} strata; {sum(r["planned"] for r in rows)} planned cases; '
          f'{sum(r["valid"] for r in rows)} valid answers; '
          f'{logprob_counts["choices_with_nonnull_logprobs"]} choices with logprobs.')


if __name__ == '__main__':
    main()
