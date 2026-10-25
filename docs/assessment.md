# What the revised test shows

**Research provenance:** Pedro had already run the original code and collected exploratory evidence before this revised run. The original notebook outputs, CSV and forensic answer were present when this work began. The 240-request study extends that earlier investigation; it is not its starting point. See [the chronology and thesis record](provenance-and-thesis.md) for evidence, timing limits and the distinction between the two experiments.

The revised experiment found that the model recognized both politicians when given their full names. Short names produced a different result: “Lula” usually identified a political figure, while “Flavio” did not identify a specific person.

**Why OpenRouter was chosen:** reports describe changes to WhatsApp's restrictions after the complaints. Pedro deliberately used another access route to investigate name-recognition hypotheses instead of relying solely on the product's post-complaint behavior. The working assumption is that OpenRouter does not necessarily reproduce those WhatsApp-specific changes. This is a methodological motivation, not proof that OpenRouter preserves the earlier model state or provides an unfiltered control.

We tested 240 requests through OpenRouter, using neutral instructions and the same name, number and role variations for each group. Every request returned a usable answer. Each condition was repeated five times in randomized order, and all responses were retained.

| Name supplied | Answers identifying a political figure |
|---|---:|
| Lula | 28 of 30 |
| Luiz Inacio Lula da Silva | 30 of 30 |
| Flavio | 0 of 30 |
| Flavio Bolsonaro | 30 of 30 |

In all 30 requests using “Flavio,” the model left the person's identity unresolved. That is different from identifying Flávio Bolsonaro and deciding he is not a politician. The neutral-name controls produced no political flags across 120 requests.

The findings are consistent with a difference in how easily a nickname or first name identifies someone. They do not establish deliberate political favoritism. The test covers one model, one instruction format and one collection session; repeated answers are not a representative survey of every way the system might respond.

**The central thesis is that the WhatsApp deployment can plausibly apply different guardrails from access through OpenRouter.** Even use of the same base model would not imply identical system instructions, product policies or image-generation checks. We have not independently established that the underlying model versions are identical. WhatsApp may use additional filters, policies and image-generation checks. We cannot confirm the exact overlap between the two systems. This experiment classified text through an API; it did not ask WhatsApp to generate images.

Consequently, the results do not tell us whether WhatsApp would allow or refuse equivalent requests, or why the originally reported difference occurred. That requires a separate test of WhatsApp itself, with matched prompts and recorded image outcomes.

The revised test makes the name-recognition question clearer. The appropriate standard for any further investigation remains the same: equivalent conditions, complete records and conclusions that apply equally regardless of politician or party.

Source: [frozen plan, all 240 responses and computed summary](../results/v2_run1/). Method: [neutral protocol v2](methodology.md). Historical leading-prompt results remain separate.

For examples of public claims and the limits of a rebuttal, see [media context and suggested response](media-context.md). G1 and Projeto Comprova documented the original WhatsApp inconsistency and subsequent changes on 14 October; the later API experiment does not disprove those observations.

A subsequently located [Meta statement](https://about.fb.com/br/news/2026/10/a-meta-nao-esta-interferindo-nas-eleicoes-brasileiras-estes-sao-os-fatos/) explicitly attributes the image incident to gaps in recognizing common first names combined with electoral numbers, says Luiz-based prompts also exposed the gap, and reports a correction on 14 October. This is the operator's documented explanation, not an independent log audit. See [the source-based mechanism diagram](meta-explanation.md).
