"""Draw Figure 1 of the manuscript from the saved v2 summary. No API calls."""
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
LABELS = {
    ('lula', 'short'): '"Lula"',
    ('lula', 'full'): '"Luiz Inacio Lula da Silva"',
    ('flavio', 'short'): '"Flavio"',
    ('flavio', 'full'): '"Flavio Bolsonaro"',
    ('gabriel_control', 'short'): '"Gabriel" (control)',
    ('gabriel_control', 'full'): '"Gabriel Silva" (control)',
    ('mariana_control', 'short'): '"Mariana" (control)',
    ('mariana_control', 'full'): '"Mariana Costa" (control)',
}


def main():
    groups = json.loads((ROOT.parent/'results/v2_run1/summary.json').read_text())['groups']
    plt.rcParams.update({'font.family': 'serif', 'font.size': 10})
    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    y = [i + (i//2)*.4 for i in range(len(groups))]
    political = [g['political'] for g in groups]
    other = [g['nonpolitical'] for g in groups]
    ax.barh(y, political, height=.65, color='#1F6F5F', label='Political flag: true')
    ax.barh(y, other, left=political, height=.65, color='#B6B6B0', label='Political flag: false')
    for yi, p, o in zip(y, political, other):
        if p:
            ax.text(p/2, yi, str(p), ha='center', va='center', color='white', fontsize=9)
        if o:
            ax.text(p + o/2, yi, str(o), ha='center', va='center', color='#171717', fontsize=9)
    ax.set_yticks(y, [LABELS[g['entity'], g['name_form']] for g in groups])
    ax.invert_yaxis()
    ax.set_xlim(0, 30)
    ax.set_xticks([0, 10, 20, 30])
    ax.set_xlabel('Number of responses (30 per name form)')
    for side in ('top', 'right', 'left'):
        ax.spines[side].set_visible(False)
    ax.tick_params(axis='y', length=0)
    ax.legend(loc='lower center', bbox_to_anchor=(.5, 1.0), ncol=2, frameon=False)
    fig.tight_layout()
    out = ROOT/'figures'
    out.mkdir(exist_ok=True)
    fig.savefig(out/'fig1-political-flags.png', dpi=300)
    fig.savefig(out/'fig1-political-flags.pdf')


if __name__ == '__main__':
    main()
