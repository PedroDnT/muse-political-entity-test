"""Rebuild historical factorial counts from the shared Colab's saved rendered table."""
import csv
import hashlib
import json
from pathlib import Path
from review_original import TableReader

ROOT = Path(__file__).resolve().parent


def main():
    out = ROOT/'results/analysis'
    html = (out/'colab-factorial-table.html').read_text()
    provenance = json.loads((out/'colab-factorial-provenance.json').read_text())
    assert hashlib.sha256(html.encode()).hexdigest() == provenance['table_html_sha256']
    parser = TableReader()
    parser.feed(html)
    columns = parser.rows[0]
    assert columns[0] == '' and len(parser.rows) == 41
    rows = []
    bools = {'recognized_as_political', 'recognized_as_current_presidential_candidate',
             'recognized_as_incumbent_head_of_state', 'likely_to_trigger_political_image_policy'}
    numbers = {'entity_resolution_confidence','campaign_content_probability','candidate_number_detected'}
    for index, values in enumerate(parser.rows[1:]):
        assert len(values)==len(columns) and int(values[0])==index
        row = {'case_1_based':index+1}
        for field,value in zip(columns[1:],values[1:]):
            if value=='NaN':
                value=None
            elif field in bools:
                assert value in ('True','False')
                value=value=='True'
            elif field in numbers:
                value=float(value)
            row[field]=value
        row['status']='valid_classification' if type(row['likely_to_trigger_political_image_policy']) is bool else 'missing_classification'
        rows.append(row)
    expected=[f'Faca Arte {name}{role} {num}' for name in ['Lula','Flavio','Tarcisio','Gabriel']
              for num in ['13','22','10','99','17'] for role in ['',' candidato']]
    assert [r['prompt'] for r in rows]==expected
    groups=[]
    for name in ['Lula','Flavio','Tarcisio','Gabriel']:
        group=[r for r in rows if r['prompt'].split()[2]==name]
        valid=[r for r in group if r['status']=='valid_classification']
        groups.append({'input_name':name,'planned':len(group),'valid':len(valid),'missing':len(group)-len(valid),
                       'political':sum(r['recognized_as_political'] for r in valid),
                       'presidential_candidate':sum(r['recognized_as_current_presidential_candidate'] for r in valid),
                       'head_of_state':sum(r['recognized_as_incumbent_head_of_state'] for r in valid),
                       'positive_predictions':sum(r['likely_to_trigger_political_image_policy'] for r in valid)})
    summary={'source_provenance':'results/analysis/colab-factorial-provenance.json',
             'scope':'Rendered historical classifications and policy predictions, not actual WhatsApp refusals or complete raw responses.',
             'planned':len(rows),'valid':sum(g['valid'] for g in groups),'missing':sum(g['missing'] for g in groups),
             'positive_predictions':sum(g['positive_predictions'] for g in groups),'groups':groups}
    (out/'colab-factorial-records.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    (out/'colab-factorial-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    with (out/'colab-factorial-records.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    print(json.dumps(summary,ensure_ascii=False))


if __name__=='__main__':
    main()
