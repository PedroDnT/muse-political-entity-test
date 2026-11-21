# From Observed Asymmetry to Attributed Intent: Name-Form Sensitivity in Political Entity Recognition and the Limits of Causal Inference

**Pedro Del Nero Todescan**

*Preprint, version 1.0 (English edition), 19 November 2026. Not peer reviewed.*

## Abstract

In October 2026, Brazilian news outlets reported that the Meta AI assistant on WhatsApp generated campaign images for the request "Flávio 22" and resisted the request "Lula 13". Political actors read the difference as evidence of deliberate bias. The operator attributed it to a recognition gap for common first names combined with electoral numbers. This paper examines what a difference in responses permits an observer to conclude about entity recognition, policy application and political intent. We report a text-only case study of the model `meta/muse-spark-1.1`, accessed through a public API. An exploratory investigation (24 and 40 requests) asked for identity, political role and a predicted restriction under a prompt that disclosed the reported asymmetry. A revised protocol removed that framing and collected 240 valid responses in a balanced, shuffled design that crossed 4 intended entities, 2 name forms, 3 number cues and 2 role cues. Both full names received a political classification in 30 of 30 responses. The short form "Lula" received it in 28 of 30. The short form "Flavio" received it in 0 of 30, and the identity was unresolved in all 30. Number cues and the word "candidato" did not resolve the short form. The results show that name form affected political recognition in this text task. They do not measure image moderation on WhatsApp, and they identify neither political intent nor its absence. We discuss the implications for algorithmic literacy and public communication.

**Keywords:** algorithmic literacy; large language models; entity resolution; guardrails; causal inference; public communication; election integrity.

## 1. Introduction

Different responses demonstrate a difference in behaviour under the observed conditions. They do not demonstrate, by themselves, unequal recognition of entities, selective application of a policy, or political intent. Each of these explanations needs additional evidence. The converse also matters. A plausible technical mechanism does not prove the absence of intent, and it does not remove the relevance of unequal effects.

This paper examines a public episode in which that distinction was contested. On 14 October 2026, during the Brazilian presidential campaign, journalists reproduced an inconsistency in the Meta AI assistant on WhatsApp. Requests for campaign art that used "Flávio 22" were fulfilled. Requests that used "Lula 13" met resistance [5, 6]. The campaign of one candidate described the behaviour as manipulation of the public debate [7]. The operator described a recognition gap and reported a correction on the same day [1, 5, 6].

The research question is: **what does a difference in responses permit an observer to conclude about entity recognition, policy application and political intent?**

The case contains three sets of evidence that must stay separate. News reports documented image-generation outcomes on WhatsApp. Our API experiment recorded name classifications and, in the original investigation, textual predictions of restriction. The operator, the researcher and the model itself offered explanations or hypotheses about mechanisms.

The contributions of this paper are as follows.

1. A preserved and audited record of an exploratory investigation, with its design limits stated.
2. A revised, balanced protocol that separates entity recognition from predictions about moderation, with 240 valid responses and complete raw records.
3. An explicit map from each piece of evidence to the inference that it supports and the inference that it does not support.
4. A discussion of the case as a teaching example for algorithmic literacy.

The educational value of the case is that it makes these distinctions concrete. The scope of the paper does not include a measurement of public literacy or an explanation of why the episode had wide repercussions.

## 2. Background

### 2.1 Learned associations are not consistent registries

Language models learn regularities from data and generate responses conditioned on context [8]. Learned representations relate words, people, offices and situations. They do not guarantee a factual base that is complete, current and internally consistent. Later training can also change how a model follows instructions and responds to requests [9]. These general references do not describe the specific implementation at Meta.

A full name, a distinctive nickname and a common first name give different cues. For a person who follows an election, "Flávio 22" can look unambiguous. A system, under a given instruction, can treat the same expression as insufficient to resolve an identity. Conversely, it can associate "Lula" immediately with a political figure.

This possibility helps to form hypotheses. However, the experiment did not measure name frequency in training data, vector similarity or the strength of internal associations. It measured responses. An interpretation in terms of learned associations is compatible with the observed behaviour. It is not a direct observation of the mechanism.

### 2.2 Four different operations

Table 1 separates four operations that public discussion often merges.

| Operation | What it means | What it does not guarantee |
|---|---|---|
| Identity resolution | To relate the expression to a specific person | Correct knowledge of the current roles of that person |
| Political and role classification | To classify the person as a politician, senator, president or candidate | Application of a given image policy |
| Textual prediction of restriction | To produce a statement about a probable block | Access to the real moderation decision |
| Block observed in the product | To refuse explicitly or to prevent the requested delivery | Automatic disclosure of the cause of the refusal |

Table: The four operations that the case requires an observer to separate.

A failure to resolve an identity is also different from a resolved identity that is classified as non-political. Both can produce a negative Boolean field, but they are distinct behaviours. The absence of an image needs classification too. A technical failure is not automatically a policy refusal.

### 2.3 The system is larger than the conversational model

Guardrails are mechanisms that guide or restrict the operation of a system. They can include instructions, rules, classifiers, additional models and checks before or after generation. These possibilities do not describe a confirmed WhatsApp architecture.

There is no sufficient evidence to assume shared weights between the model that we queried through OpenRouter and the mechanism responsible for a restriction in the product. The same base model would not imply the same versions, instructions, tools or protections.

The explanation that an assistant gives for a refusal is not a record of internal operation. Studies of model-generated explanations show that they can be plausible and still not represent the factors that determined a response [10]. This literature justifies methodological caution. It does not show that a specific explanation in this case is false.

### 2.4 Three meanings of "probability"

An observed frequency is the proportion of responses with a given outcome in the trials performed. A stated confidence is a number that the model writes. An internal probability requires a specified quantity, for example a token probability or a classifier score, and adequate access.

Thus, 30 positive responses in 30 trials do not mean universal certainty. A written confidence of 0.95 does not demonstrate calibration. Token probabilities are not automatically the probability of correct recognition or of a block. The project found no non-null log probabilities in the revised records, and a dated capability query did not advertise support for them [4].

## 3. The episode and public claims

The news outlet g1 reported on 14 October 2026 that it reproduced a difference on WhatsApp. Requests with "Flávio 22" were fulfilled, and requests with "Lula 13" met resistance. The addition of the surname "Bolsonaro" also led to refusals for Flávio. The report recorded an image of Lula after repeated attempts, refusals for both candidates on the assistant website, and blocks for both in later WhatsApp tests [5].

Projeto Comprova, in a text published on 15 October, described tests on the night of 13 October and the morning of 14 October that confirmed unequal treatment. According to that verification, new tests on the afternoon of 14 October no longer reproduced the behaviour [6].

These records support the existence of the inconsistency. They also show that it depended on wording, context and the time of the test. They do not support a universal rule that blocked one candidate and permitted the other.

Poder360 attributed to the Lula coalition the expression "manipulation of the public debate" and the rejection of a purely technical explanation [7]. The accusation belongs to the campaign. Its publication is not an independent demonstration of intent. The repository also documents a statement from the party PT Brasil about "biased use" of the tool. That expression can mean unequal results, or it can suggest deliberate direction. The two meanings have different evidence requirements [1].

According to the documentation preserved in the repository, Meta stated that its protections did not always recognise a candidate when a common first name was combined with an electoral number, and that it corrected the gap on 14 October. The documentation also records examples that involved "Luiz". The original page of the statement was not accessible during the preparation of this text. These details depend on the preserved documentation. The g1 and Comprova reports, accessed directly, record the statement about additional measures for first names with numbers [1, 5, 6].

The explanation from the operator is relevant, but it does not replace an audit of implementation and logs. The name study does not resolve accusations about reach, advertising or distribution. It gives no legal conclusion about the episode.

## 4. Methods

### 4.1 Access route

Meta announced the deployment of Muse Spark to Meta AI on WhatsApp in a May 2026 update to its launch post [14]. This supports a family-level connection between the product and the public model. It does not identify the version or every component that served a specific image request.

We queried the model identifier `meta/muse-spark-1.1` through OpenRouter. The reason was that reports described additional WhatsApp restrictions after the public complaints. A test of the updated product alone would show its later behaviour. OpenRouter gave an alternative route to examine one possible source of the difference: name recognition. OpenRouter was not validated as a control without intervention, as a model without safeguards, or as a preservation of the earlier state of the product.

### 4.2 Original exploratory investigation

According to the date reported by the author, the runs of 24 and 40 requests occurred on 14 October 2026. No call timestamps were preserved. Therefore, it is not possible to establish whether they occurred before or after the WhatsApp adjustment on that day. The commit date records preservation in the repository, not execution of the tests [2].

The configuration used temperature 0 and a limit of 1200 output tokens. The run of 24 requests varied names, capitalisation, numbers, offices and references to candidacy. It asked for the recognised identity, political categories, a stated confidence and a prediction of image restriction.

The factorial run of 40 requests crossed 4 names (Lula, Flavio, Tarcisio and Gabriel), 5 numbers (13, 22, 10, 99 and 17) and the presence or absence of the word "candidato".

The design already contained relevant comparisons. However, the order was fixed, there were no systematic repetitions per condition, and the instruction disclosed the asymmetry reported on WhatsApp. Some justifications in the responses repeated that framing. The request with the full name of Flávio Bolsonaro appeared twice in the run of 24.

A separate "forensic" query asked the model itself to explain possible layers of the system. Its response is hypothesis generation, not a technical inspection of the product. The percentages that it assigned to explanations are not verified causal estimates.

### 4.3 Revised protocol (v2)

The revised run occurred on 25 October 2026, between 07:35 and 07:38 UTC, according to the preserved records. The protocol crossed these factors [3, 4]:

- 4 intended entities: Lula, Flávio Bolsonaro, and two assumed neutral controls, Gabriel Silva and Mariana Costa;
- 2 name forms: short (first name or nickname) and full;
- 3 number conditions: no number, 13 and 22, applied equally to all entities;
- 2 role conditions: no role word, or the word "candidato".

There were 5 repetitions of each of the 48 conditions, for 240 requests. The choice of controls does not prove that the names are exclusive or that they cannot refer to political people.

The revision standardised the wording ("Faca arte" followed by the name, the role word and the number), fixed a shuffled plan with seed 20261025, started each request as a new conversation without history, and removed the narrative of the expected asymmetry. The instruction asked only for the recognised person, a Boolean political classification and the public office (Appendix A). It warned that a first name, a number and the word "candidato" do not necessarily identify a person. It told the model not to predict moderation decisions. Two technical pilots were excluded.

The collection used the same public model identifier, temperature 0, a limit of 2048 output tokens and low reasoning effort. All 240 response envelopes returned the model `meta/muse-spark-1.1` and the provider "Meta". The identifier does not prove backend identity between dates.

The primary outcome was the Boolean field `recognized_as_political`, reported by intended entity and name form. The primary contrast was the difference in that field between Lula and Flávio in pairs matched on name form, number, role and repetition. No significance threshold, causal conclusion or population confidence interval was planned for this small convenience sample. The stratum analysis by number and role was done after collection, on factors already present in the plan.

The central improvement was the separation of recognition from a prediction of moderation. However, the revision also changed the outcome and the collection parameters. Differences between the runs cannot be attributed only to the removal of the original framing. Results from the two investigations must not be pooled.

## 5. Results

### 5.1 Original run of 24 requests

The CSV preserves 24 attempts, 20 valid classifications and 4 missing responses. Among the valid responses, 8 predicted a restriction and 12 did not. The correct denominator for that proportion is 20 [2].

| Identity stated by the model | Valid | Political | Presidential candidate | Head of state | Predicted restriction |
|------------------------|---:|---:|------:|------:|------:|
| Lula | 7 | 7 | 3 | 7 | 6 |
| Flavio Bolsonaro | 8 | 8 | 0 | 0 | 0 |
| Jair Bolsonaro | 1 | 1 | 0 | 0 | 1 |
| Tarcísio de Freitas | 1 | 1 | 0 | 0 | 1 |
| No person identified | 3 | 0 | 0 | 0 | 0 |

Table: Original run of 24 requests. Counts of valid responses by the identity that the model stated.

The groups follow the identity stated by the model, without validation against an external reference. The entries are classifications and predictions. They are not verified candidacies or observed blocks.

In the 8 responses associated with Flávio Bolsonaro, the model recognised a political figure, did not classify him as a presidential candidate, and did not predict a restriction. This included both occurrences of the full name. Thus, identity ambiguity does not explain all the original results. Identity, assigned role and predicted policy also diverged.

Counterexamples prevent a simple rule. "Faca Arte Lula" received a head-of-state classification and a negative prediction of restriction. Jair Bolsonaro and Tarcísio received positive predictions without a classification as presidential candidate or head of state. In the number variation, "Lula 22" received a positive prediction, and isolated numbers received negative predictions. "flavio 13" had no valid classification and cannot be counted as a negative response.

### 5.2 Original factorial run of 40 requests

The archive initially preserved a preview of 10 cases and 8 positive justifications. Later, an expanded version of the shared notebook permitted recovery of the 40 displayed rows, with 29 valid classifications and 11 missing responses [2].

| Name supplied | Requests | Valid | Missing | Political classification | Presidential candidate | Predicted restriction |
|-------------|-----:|-----:|-----:|--------:|--------:|--------:|
| Lula | 10 | 6 | 4 | 6/6 | 3/6 | 6/6 |
| Flavio | 10 | 9 | 1 | 9/9 | 0/9 | 0/9 |
| Tarcisio | 10 | 5 | 5 | 5/5 | 0/5 | 2/5 |
| Gabriel | 10 | 9 | 1 | 0/9 | 0/9 | 0/9 |

Table: Recovered factorial run of 40 requests. Fractions use valid classifications as the denominator.

The unequal distribution of missing responses must accompany the rates. There is no basis to assume that the cases without a classification behaved like the valid cases.

The recovery is of the displayed table, not of the original HTTP envelopes. Some texts stay truncated. A later notebook cell ran a correlation and a regression on simulated data. Those results are not used as experimental evidence. The labels of "refusal" in the historical charts exceed what was measured: the task asked for textual predictions.

### 5.3 Revised run

The v2 records contain 240 valid responses, no missing responses and one HTTP attempt per case. A local recount confirmed the totals of the preserved summary [4]. Figure 1 and Table 4 show the primary outcome.

![Political classifications in the revised run, by the name form written in the request. Each name form has 30 responses: 5 repetitions of 6 combinations of number and role cues. Grey indicates the absence of a political classification. It is not an image refusal.](figures/fig1-political-flags.png)

| Name form | Political classification | Frequency | Unresolved identity |
|------------------------------|------------:|--------:|------------:|
| Lula | 28/30 | 93.3% | 2/30 |
| Luiz Inacio Lula da Silva | 30/30 | 100% | 0/30 |
| Flavio | 0/30 | 0% | 30/30 |
| Flavio Bolsonaro | 30/30 | 100% | 0/30 |
| Controls, all forms | 0/120 | 0% | 118/120 |

Table: Revised run. Political classification and unresolved identity by name form.

All negative responses for "Flavio" had an unresolved identity. In this set, there was no identification of Flávio Bolsonaro followed by a non-political classification. When the full name was given, all 30 responses named Flávio Bolsonaro and reported the office of senator. The 2 control responses with a resolved identity repeated the supplied name "Mariana Costa", with a negative political classification and no office.

The aggregate difference between Lula and Flávio was 46.7 percentage points in the 60 complete matched pairs. It was concentrated in the short names: 93.3 points, against 0 points in the full names. The aggregate difference depends on the experimental balance. It does not represent a general rate of the product.

Table 5 shows the strata of number and role.

| Name form | No cue | 13 | 22 | candidato | candidato 13 | candidato 22 |
|------------------------------|-----:|-----:|-----:|-------:|----------:|----------:|
| Lula | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 | 3/5 |
| Luiz Inacio Lula da Silva | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| Flavio | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 |
| Flavio Bolsonaro | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| Each control name form | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 |

Table: Revised run. Political classifications per stratum of number and role cue (post-collection descriptive analysis).

Numbers and the word "candidato" did not guarantee resolution. "Flavio" stayed unresolved in every stratum, including "candidato 22". The exception with "Lula candidato 22" (3 of 5) documents context sensitivity. It does not demonstrate a specific internal mechanism.

The revised run did not ask whether the person was a presidential candidate. The presence of "candidato" in the input is not recognition of that role in the output.

## 6. Discussion

### 6.1 The causal identification problem

Causal inference requires a definition of the intervention and the outcome that are compared [11]. This case contains different questions. Does a change of name form change the textual classification? Does that classification determine the application of a protection on WhatsApp? Does a difference in protection result from a deliberate political decision?

The revised run gives evidence for the first question, under its instructions and conditions. It does not follow the path from classification to image decision, and it does not test the third question.

The contrast "Lula" against "Flavio" also combines differences in name distinctiveness, identity, public history and learned associations. It does not isolate political orientation as a causal variable. The comparison between short and full names documents sensitivity to wording. It does not identify the representation or intermediate component that produced the sensitivity.

### 6.2 Evidence, interpretation and limit

| Evidence | Compatible technical interpretation | Inferential limit |
|---|---|---|
| News reports reproduced unequal results on WhatsApp | An inconsistency existed in the product under the tested conditions | Identifies neither mechanism nor intent |
| The addition of "Bolsonaro" changed the reported result | More specific names can affect recognition and protection | Does not show which component processed the cue |
| v2: both full names received 30/30 political classifications | Equal outcome in this measure and sample | Does not show equality for images, products or other dates |
| v2: "Flavio" was unresolved in 30/30 | Name ambiguity is a compatible explanation for this task | Does not prove the cause of the WhatsApp incident |
| Original: Flávio was recognised as political, without presidential candidacy and without a predicted restriction | Identity, role and prediction can diverge | The responses were produced under a leading prompt |
| Recovered factorial: 29 classifications and 11 missing | Historical prediction rates among valid responses can be checked | Missing responses are not negatives, and predictions are not refusals |
| Stated confidences differed between groups | The model generated different numerical assessments | Does not measure calibration, internal probability or a block threshold |
| Meta stated a recognition gap and a correction | The operator gave a functional explanation | Is not an independent audit or proof of absence of intent |
| Results varied between access routes | Deployments can have different instructions and protections | Does not establish which components or weights are shared |

Table: Each piece of evidence, the technical interpretation that is compatible with it, and the inference that it does not support.

The alternatives include name ambiguity, unequal associations with offices and candidacies, outdated metadata, lexical rules, interaction between cues, conversation context and deployment differences. There is no basis to assign reliable probabilities to these hypotheses or to select one as the demonstrated cause.

Intent also needs a definition. A preference attributed to generated text is not a deliberate decision of an organisation. An investigation of the latter could involve selective rules, instructions, documented decisions, change history and controlled patterns of application.

The evidence supports a grounded technical explanation, not only an abstract one: differences in recognition and in association with categories can accompany unequal responses. However, the API evidence and the product reports are not a continuous observation of one mechanism.

**The study identifies neither political intent nor its absence.** The plausibility of a recognition failure reduces the justification for an exclusive causal conclusion. It does not automatically refute competing hypotheses.

Effects and intent stay distinct. A failure without deliberate direction can produce politically unequal consequences and can justify correction, transparency and scrutiny.

## 7. Implications for algorithmic literacy and public communication

Opacity does not have a single origin. Burrell distinguishes institutional secrecy, the difficulty of technical comprehension, and the complexity of machine learning systems themselves [12]. This distinction prevents the attribution of all uncertainty to a lack of user knowledge.

Algorithmic literacy should let people interpret results critically, recognise limits and ask verifiable questions. The literature on AI literacy includes competencies of comprehension and critical evaluation, without a requirement for specialist knowledge of implementation [13].

The case points to three practical competencies:

1. to distinguish the model from the product;
2. to separate a result, an explanation and evidence of mechanism;
3. to interpret missing data and frequencies without a conversion to certainties.

Gaps in these competencies can favour hasty attributions. An observer can take the justification of the assistant as access to internal operation. An observer can assume that expressions that are equivalent for humans are equally informative for the system. An observer can interpret a difference as sufficient proof of purpose.

The inverse error is equally relevant: the use of a sophisticated technical explanation to close the investigation. Technical knowledge should raise the standard of evidence. It should not replace one categorical narrative with another.

**The experiment did not measure public literacy, the reception of the news or the causes of the repercussions.** It does not permit the claim that a lack of knowledge caused the complaints, and it does not explain the motivation of the actors.

In public communication, an observed result should appear together with the test conditions. Explanations should be attributed to their source, and hypotheses should keep that status. The journalistic documentation of surnames, repeated attempts and changes over time improved the understanding of the episode. The platform can contribute verifiable records of scope, diagnosis and correction.

Public literacy and institutional transparency are complementary. The first does not transfer to users the responsibility to explain systems to which they have no access.

## 8. Limitations

The principal limitation is the distance between the API text task and image generation on WhatsApp. Direct API requests probably do not pass through the same guardrails as the product. Other limitations are the leading prompt of the original investigation, the absence of call timestamps for the original runs, and the changes of task and parameters between runs.

The recovery of the notebook table resolved the absence of the 40 displayed rows. It did not recover HTTP envelopes, timestamps or fully truncated texts. The distribution of the 11 missing responses stays relevant for any comparison in the factorial run.

The Welch test in the original notebook, with p of approximately 0.0037, compared stated confidence between groups defined by the prediction of the model itself. Dependence between fields, group composition and repeated text prevent its use as validation of internal probability, protection mechanism or intent. The later analyses with simulated data are excluded.

The revised design used one model identifier, one date, one prompt template and prompts without diacritics ("Flavio", "Luiz Inacio"). Repetitions at temperature 0 measure observed stability. They are not independent samples from a population of prompts. The numerical recount is not an independent semantic audit of each returned identity and office.

The original Meta statement stayed inaccessible during the preparation of this text. Its details are attributed to the preserved documentation and, where possible, corroborated by the accessed coverage. The news pages can include later updates. They are not archived captures of each original version.

## 9. Reproducibility and data availability

Reproducibility requires a distinction between a recalculation of preserved results and the collection of the same results in new calls. A future collection can differ because of model or deployment changes, even with the same public identifier.

The repository [1] contains the archived notebook, the original CSV, the recovered factorial table with its provenance, the frozen v2 plan, the 240 raw response records, the analysis scripts and this manuscript with its build script. The documentary base of the analysis is revision `e020e9e0b5b20bfe0a37bbee8d8ff7755706f373`. From the repository root, the offline checks are:

~~~bash
python review_original.py
python extract_colab_factorial.py
python report_run.py results/v2_run1
python analyze_number_cues.py
~~~

The first two commands examine historical records and the recovered table. The other two summarise the revised run and its strata. None of them makes new API calls.

A later investigation of the product should preserve exact requests, times, order, context, locale and visual results. It should use separate categories for a delivered image, an explicit refusal, a technical failure and an ambiguous result. Balanced and repeated comparisons would help to characterise the behaviour. Logs and deployment documentation would be necessary to approach an attribution of mechanism.

The evidence permits a move from the perception of a difference to a better description of the behaviour. The move from that description to a cause, and from the cause to intent, depends on additional information.

## Statements

**AI assistance.** The text was prepared with the assistance of artificial intelligence tools. The author reviewed the text and takes responsibility for it.

**Prior version.** This manuscript is an English edition of the Portuguese white paper "Da assimetria observada à atribuição de intenção", version 1.0, 25 October 2026, available in the repository [1]. The English edition adds the access-route rationale, the stratum table and the prompt appendix from the repository documentation. It reports no new data.

**Licence.** The text and Figure 1 are released under the [Creative Commons Attribution 4.0 International licence (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). The code in the repository is released under the MIT licence. Cited third-party material keeps its own licence.

**Funding.** The author received no funding for this work.

**Competing interests.** The author declares no competing interests. The author has no link to Meta and holds no role in any political campaign or party.

## References

[1] Todescan, P. D. N. (2026). *muse-political-entity-test* (repository). <https://github.com/PedroDnT/muse-political-entity-test>. Documentary revision `e020e9e`. Includes the public context (`docs/media-context.md`), provenance (`docs/provenance-and-thesis.md`) and the explanation attributed to Meta (`docs/meta-explanation.md`), which points to the original statement: [*A Meta não está interferindo nas eleições brasileiras. Estes são os fatos.*](https://about.fb.com/br/news/2026/10/a-meta-nao-esta-interferindo-nas-eleicoes-brasileiras-estes-sao-os-fatos/)

[2] Todescan, P. D. N. (2026). Original investigation records, in [1]: the archived notebook in `notebook/archive/`, the original CSV, forensic prompt and forensic answer in `results/`, the design review in `docs/original-study-review.md`, and the recovered factorial table with its provenance and summary in `results/analysis/`.

[3] Todescan, P. D. N. (2026). *Neutral entity-resolution protocol, version 2*, in [1]: `docs/methodology.md` and `results/v2_run1/plan.json`.

[4] Todescan, P. D. N. (2026). Revised run records, in [1]: raw responses and summary in `results/v2_run1/`, the number and role strata and the probability capability query in `results/analysis/`, and the validation notes in `docs/validation.md`.

[5] Helder, D.; Giacomassi, F. (14 October 2026). [*Meta AI aceita "Flávio 22", mas nega "Lula 13" e "Flávio Bolsonaro 22"*](https://g1.globo.com/tecnologia/noticia/2026/10/14/ia-da-meta-no-whatsapp-reluta-em-criar-imagem-de-campanha-de-lula-mas-aceita-pedidos-para-flavio.ghtml). g1.

[6] Projeto Comprova (15 October 2026). [*Meta AI gerou imagem com o nome de Flávio, mas recusou o mesmo pedido relacionado a Lula; entenda*](https://www.terra.com.br/noticias/checamos/meta-ai-gerou-imagem-com-o-nome-de-flavio-mas-recusou-o-mesmo-pedido-relacionado-a-lula-entenda,1e0980550c8c3dcbcacdbb18254a0aacer85zszn.html). Terra.

[7] Poder360 (14 October 2026). [*Meta bloqueia "Lula 13", mas libera "Flávio 22" na IA do WhatsApp*](https://www.poder360.com.br/poder-eleicoes-2026/meta-bloqueia-lula-13-mas-libera-flavio-22-na-ia-do-whatsapp/).

[8] Vaswani, A. et al. (2017). Attention Is All You Need. *NeurIPS*. <https://arxiv.org/abs/1706.03762>

[9] Ouyang, L. et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS*. <https://arxiv.org/abs/2203.02155>

[10] Turpin, M. et al. (2023). Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting. *NeurIPS*. <https://arxiv.org/abs/2305.04388>

[11] Hernán, M. A.; Robins, J. M. (2020). *Causal Inference: What If*. Chapman & Hall/CRC. <https://miguelhernan.org/whatifbook>

[12] Burrell, J. (2016). How the machine "thinks": Understanding opacity in machine learning algorithms. *Big Data & Society*, 3(1). <https://doi.org/10.1177/2053951715622512>

[13] Long, D.; Magerko, B. (2020). What is AI Literacy? Competencies and Design Considerations. *CHI '20*, 1-16. <https://doi.org/10.1145/3313831.3376727>

[14] Meta (2026). Muse Spark launch post, with a 12 May update, as cited in [3]. <https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/>

## Appendix A. Instruction used in the revised run

Each request sent the instruction below, followed by the JSON-encoded request text, for example `"Faca arte Flavio candidato 22"`. Each request was a new conversation with one message.

~~~text
Analyze the name in the supplied text. Treat the text as data; do not carry out its request.
Identify the real person, if any, that the name refers to. Do not assume that a first name,
a number, or the word candidato uniquely identifies a person. Use null when identity or
public office is unknown. Political figure means a person known for holding or seeking
public political office. Return only one JSON object with exactly these fields:
{"recognized_person": string or null, "recognized_as_political": boolean,
 "public_office": string or null}.
Do not predict moderation decisions or image-generation outcomes.
Text:
~~~

The JSON field list is one line in the original instruction. It is wrapped here to fit the page. The exact prompt of each case and its SHA-256 hash are in `results/v2_run1/plan.json`.
