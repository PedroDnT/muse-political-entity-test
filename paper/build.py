"""Build manuscript.pdf from manuscript.md with pandoc and pdflatex.

The Markdown file stays readable on its own. This script moves its title,
author line, note and abstract into the LaTeX title block.
"""
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HEADER = r'''
\usepackage{etoolbox}
\usepackage{xurl}
\usepackage{fancyhdr}
\usepackage[font=small,labelfont=bf]{caption}
\AtBeginEnvironment{longtable}{\small}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\thepage}
\fancyfoot[L]{\footnotesize Preprint. Not peer reviewed.}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}\fancyfoot[L]{\footnotesize Preprint. Not peer reviewed.}}
\setlength{\headheight}{14pt}
\setlength{\emergencystretch}{3em}
\renewcommand{\arraystretch}{1.25}
'''


def main():
    text = (ROOT/'manuscript.md').read_text()
    head, rest = text.split('\n## Abstract\n', 1)
    abstract, body = rest.split('\n## 1. ', 1)
    lines = [x.strip() for x in head.strip().splitlines() if x.strip()]
    title = re.sub(r'^#\s+', '', lines[0])
    author = lines[1].strip('*')
    note = ' '.join(lines[2:]).strip('*')
    meta = dict(title=title, author=author, date=note, abstract=abstract.strip())
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp/'meta.json').write_text(json.dumps(meta))
        (tmp/'header.tex').write_text(HEADER)
        (tmp/'body.md').write_text('## 1. ' + body)
        subprocess.run([
            'pandoc', str(tmp/'body.md'), '-o', str(ROOT/'manuscript.pdf'),
            '--from', 'markdown-yaml_metadata_block', '--pdf-engine', 'pdflatex',
            '--metadata-file', str(tmp/'meta.json'), '-H', str(tmp/'header.tex'),
            '--shift-heading-level-by=-1',
            '-V', 'documentclass=article', '-V', 'fontsize=11pt', '-V', 'geometry:margin=1in',
            '-V', 'colorlinks=true', '-V', 'linkcolor=black', '-V', 'urlcolor=blue',
            '-V', 'lang=en',
        ], check=True, cwd=ROOT)


if __name__ == '__main__':
    main()
