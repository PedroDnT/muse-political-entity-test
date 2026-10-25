"""Reproduce an API study summary and count figure from saved records."""
import argparse
import collections
import json
from pathlib import Path
from experiment import summarize, paired_summary


def load_run(root):
    root = Path(root)
    plan = json.loads((root/'plan.json').read_text())
    records = [json.loads(line) for line in (root/'responses.jsonl').read_text().splitlines() if line.strip()]
    return plan, records


def report(root):
    root = Path(root)
    plan, records = load_run(root)
    groups = summarize(plan, records)
    paired = paired_summary(plan, records)
    costs, models, providers = [], collections.Counter(), collections.Counter()
    for r in records:
        for attempt in r['attempts']:
            try:
                body = json.loads(attempt.get('raw_response', '{}'))
            except json.JSONDecodeError:
                continue
            if not isinstance(body, dict):
                continue
            value = body.get('usage', {}).get('cost')
            if isinstance(value, (int, float)):
                costs.append(value)
            if body.get('model'): models[body['model']] += 1
            if body.get('provider'): providers[body['provider']] += 1
    result = dict(groups=groups, matched=paired, completed_cases=len(records),
                  planned_cases=len(plan['cases']), statuses=dict(collections.Counter(r['status'] for r in records)),
                  returned_models=dict(models), returned_providers=dict(providers),
                  reported_cost_usd=sum(costs), attempts_with_reported_cost=len(costs),
                  scope='API entity recognition only. WhatsApp probably applies different guardrails; no WhatsApp outcomes measured.')
    (root/'summary.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
    return result


def plot_groups(groups, repetitions=5):
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.labelcolor':'#171717',
                         'text.color':'#171717','xtick.color':'#5E6462','ytick.color':'#171717',
                         'svg.fonttype':'none'})
    labels = {'lula':'Lula','flavio':'Flávio Bolsonaro','gabriel_control':'Gabriel (control)', 'mariana_control':'Mariana (control)'}
    fig, ax = plt.subplots(figsize=(10,6.1))
    fig.subplots_adjust(left=.27,right=.97,top=.76,bottom=.22)
    y = [i+(i//2)*.4 for i in range(len(groups))]
    left = [0]*len(groups)
    for key, label, color, hatch in [('political','Political flag: yes','#1F6F5F',None),
                                     ('nonpolitical','Political flag: no','#B6B6B0',None),
                                     ('missing_or_not_run','Missing / not run','#FFFFFF','////')]:
        values = [r[key] for r in groups]
        ax.barh(y, values, left=left, height=.65, color=color, hatch=hatch,
                edgecolor='#5E6462' if hatch else 'none', linewidth=.6, label=label)
        for ypos, width, start in zip(y,values,left):
            if width >= 2:
                ax.text(start+width/2,ypos,str(width),ha='center',va='center',color='white' if key=='political' else '#171717',fontsize=10)
        left = [a+b for a,b in zip(left,values)]
    ax.set_yticks(y, [f"{labels[r['entity']]} · {r['name_form']}" for r in groups])
    ax.invert_yaxis()
    limit=max(r['planned'] for r in groups)
    ax.set_xlim(0,limit)
    ax.set_xticks([0,limit/3,2*limit/3,limit])
    ax.set_xlabel('Number of planned requests')
    for side in ['top','right','left']:ax.spines[side].set_visible(False)
    ax.spines['bottom'].set_color('#E4E7E5')
    ax.tick_params(axis='y',length=0,pad=9)
    ax.legend(loc='lower left',bbox_to_anchor=(0,1.04),frameon=False,ncol=3,fontsize=9,borderaxespad=0)
    fig.text(.27,.94,'API political-person classifications',fontsize=16,weight='semibold')
    fig.text(.27,.89,'meta/muse-spark-1.1 · low reasoning · temperature 0',fontsize=10,color='#5E6462')
    fig.text(.27,.10,f'{repetitions} repetitions × 6 number/role conditions per name form. Descriptive counts.',fontsize=10)
    fig.text(.27,.055,'Direct API only. WhatsApp probably uses different guardrails.',fontsize=10,weight='semibold')
    return fig


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_dir')
    args=parser.parse_args()
    root=Path(args.run_dir)
    result=report(root)
    fig=plot_groups(result['groups'], load_run(root)[0]['repetitions'])
    fig.savefig(root/'political_flags.png',dpi=200)
    fig.savefig(root/'political_flags.svg')
    print(json.dumps(result,indent=2))
