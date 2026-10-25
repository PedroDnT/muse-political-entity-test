# Political-name recognition through a direct model API

This independent project tests how a model identifies political figures under matched wording. It takes no political side. The standard is consistent measurement, transparent evidence and conclusions limited to what was actually tested.

## Explicação e esquemas em português

- [Explicação pública da Meta, esquema visual e texto para apresentação](docs/meta-explanation.md): distingue a declaração da empresa dos resultados do experimento.
- [Como reconhecer um político e ainda assim não acionar uma restrição](docs/esquema-mecanismo.md): esquema didático da hipótese de categorias políticas.
- [Proveniência dos testes e motivo da escolha do OpenRouter](docs/provenance-and-thesis.md).
- [Notícias, publicações e limites das conclusões](docs/media-context.md).

Os esquemas aparecem diretamente nas páginas dos documentos no GitHub. A Meta atribui o episódio a uma lacuna de reconhecimento de primeiro nome comum com número eleitoral; a hipótese específica de senador versus candidato permanece sem confirmação.

## Scope

**The direct OpenRouter API probably does not use the same guardrails as WhatsApp.** WhatsApp may apply additional policies, classifiers, prompt rewriting and image-generation checks. We cannot verify the exact overlap. API answers therefore cannot establish WhatsApp refusal rates, explain a specific product refusal or demonstrate deliberate political favoritism.

## What changed

The original exploratory test told the model that a Lula image request was refused and a Flavio request succeeded, then asked it to predict policy outcomes. That wording could influence its answers. Some failures were counted as negative observations, and the notebook depended on unsaved variables.

Version 2 asks a narrower question: **how does the API identify names and political roles when each entity receives the same prompt variations?** It does not ask the model to explain WhatsApp or predict image restrictions.

- Neutral classification instructions without the reported outcome.
- Four entities, two name forms, three number conditions and two role conditions.
- Five repetitions, shuffled with a fixed seed: **240 planned requests**.
- Strict response validation and separate failure states; missing answers never become `False`.
- Raw responses, request settings and attempts retained in a new directory for each run.
- Matched comparisons, explicit missingness and descriptive conclusions.

**Version 2 has now completed 240/240 requests, all schema-valid, with no failed or unrun cases.** OpenRouter reported about **US$0.50** for the main study; two separate technical pilots cost about US$0.007 in total.

| Input name | Classified as political | Unresolved identity |
|---|---:|---:|
| Lula | 28/30 | 2/30 |
| Luiz Inacio Lula da Silva | 30/30 | 0/30 |
| Flavio | 0/30 | 30/30 |
| Flavio Bolsonaro | 30/30 | 0/30 |
| Neutral-name controls, all forms | 0/120 | 118/120 |

The full names received the same political classification rate. The short-name difference is consistent with name ambiguity in this task: every negative Flavio short-name answer left identity unresolved. This does not establish favoritism or explain WhatsApp moderation. These are descriptive results from one model, wording and collection session; repeated prompts are not independent population samples.

![Political-person classifications through the API](results/v2_run1/political_flags.png)

[Nontechnical assessment](docs/assessment.md) · [Raw responses and frozen plan](results/v2_run1/) · [Computed summary](results/v2_run1/summary.json)
 See [the full protocol](docs/methodology.md) for outcomes, controls, limitations and a separate WhatsApp study.

## Run locally

Tested with Python 3.12. Direct dependencies are pinned; this is not a complete transitive lockfile.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
jupyter notebook notebook/muse_political_entity_test.ipynb
```

The notebook runs offline by default. It inspects the frozen plan, corrects the historical Run 1 denominator, and analyzes the bundled neutral run. It does not make API calls. To inspect a different run, set `MUSE_RUN_DIR` to that run's directory before starting Jupyter.

For live collection, securely configure `OPENROUTER_API_KEY` for `openrouter.ai`. Verify model availability and current pricing first. Never put the key in source or a command you will publish. The model ID and authentication passed a technical pilot; that pilot is excluded from the main study.

```bash
# A new directory is required. Every retry also consumes the call limit.
python experiment.py collect --plan results/v2_plan.json --out results/runs/v2-001 --max-calls 240 --workers 4
python experiment.py summarize results/runs/v2-001
```

The collector stops on authentication failures. A request ceiling can leave part of the plan unrun; the summary reports that explicitly. Retries are not extra experimental repetitions. Use a separately labeled pilot if checking API compatibility before the full experiment. Do not pool a changed pilot with the frozen plan.

## Historical evidence

The original 24-prompt run contains **20 valid classifications, 4 missing classifications, 8 positive policy predictions and 12 negative predictions**. The valid-answer prediction rate is 8/20 (40%). This describes a leading-prompt API experiment, not actual image refusals.

The original factorial run's full raw records were not saved. Its reported rates cannot be independently recomputed. The historical images in `figures/` label predictions as refusals; they are retained as original artifacts and must not be presented as verified product measurements. No new dataset has been invented to reconstruct them.

- [Original Run 1 CSV](results/run1_classification.csv)
- [Original forensic prompt](results/forensic_prompt.txt) and [model-generated hypotheses](results/run1_forensic_answer.json)
- [Archived exploratory notebook](notebook/archive/original_exploratory.ipynb), including original outputs and known execution defects

The forensic answer is a model's speculation, not access to Meta's internal systems. Political context supplied in that prompt is user-provided and requires dated independent sources before reuse as factual evidence.

## For nontechnical readers

A reported difference in how WhatsApp handled two political names raises a reasonable question about consistency. The revised study checks whether a separately accessed model identifies names differently when tested under the same conditions. Even a consistent difference would not by itself establish favoritism: identity ambiguity, public-role knowledge and other factors can affect answers.

The API and WhatsApp are different deployments and probably apply different safeguards. To establish whether WhatsApp treats equivalent requests consistently, its actual image responses must be tested separately. The aim is fair comparison and clear reporting, regardless of politician or party.

## Files

- `experiment.py`: design, collection, validation and summaries.
- `report_run.py`: reproducible count figure and summary (`python report_run.py results/v2_run1`).
- `results/v2_plan.json`: frozen randomized plan and prompt hashes.
- `notebook/muse_political_entity_test.ipynb`: runnable offline analysis and optional run inspection.
- `docs/methodology.md`: protocol and publication limits.
- `tests/`: offline tests of design balance, failures, pairing and collection behavior.

Author of the original experiment: Pedro Del Nero Todescan, October 2026. This project is independent of Meta and OpenRouter.
