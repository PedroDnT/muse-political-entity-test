# Public claims and a defensible response

> Apêndice de conferência. A leitura principal está no [estudo completo](../README.md).

Sources accessed 25 October 2026. The source pages below were read directly; the X post was verified through X's public oEmbed endpoint. These are currently available pages, some incorporating updates, not archived captures of each article's original publication version. No claims about reach, virality or deleted posts are made.

## Research chronology and scope of the argument

The original exploratory study is preserved in the initial repository commit, including its CSV, notebook outputs and model-generated hypotheses. References below to the 25 October neutral run describe the separate v2 study. The author dates both original runs to 14 October 2026. This is an author-reported date; preserved records do not independently timestamp the calls or establish their order relative to the product adjustment that day. See [the provenance and thesis record](provenance-and-thesis.md).

The central thesis is technically plausible: WhatsApp can apply different guardrails from the OpenRouter deployment, even if a base model were shared. We have not verified identical model versions or the actual safeguard stacks. The defensible criticism targets premature certainty about mechanism or intent; it does not require denying the reported inconsistency or proving an alternative mechanism first.

OpenRouter is central to the study's method: the reported changes after the complaints motivate investigating a possible mechanism through another route rather than relying exclusively on post-change WhatsApp responses. The working assumption is that the OpenRouter route need not share those product-specific changes. This is not evidence that its own model or safeguards remained unchanged, nor a validated pre-change control.

## Main finding

The documented WhatsApp inconsistency should not be called fabricated. G1 and Projeto Comprova reported reproducing it. What can be challenged is the inference that those outputs alone prove deliberate political favoritism or reveal a particular internal moderation mechanism.

Our 25 October API study measured name recognition, not WhatsApp image generation. It supports name ambiguity as a plausible alternative explanation, but does not establish the cause of the earlier product incident. A technical flaw can still produce unequal political effects and warrant scrutiny, even without proof of intent.

## 1. PT Brasil on X — 14 October

[Original post](https://x.com/ptbrasil/status/2110394755750547938)

Verified short excerpt: **“uso enviesado da ferramenta de Inteligência Artificial, Meta AI.”**

The post also alleges suppression of publication reach and calls for action before the TSE. It is a party's public allegation, not a neutral technical finding. Do not silently translate “enviesado” into proof of intentional favoritism: bias can also describe unequal effects.

Defensible response:

> A diferença de resultados merece investigação. Mas ela, isoladamente, não demonstra favorecimento deliberado. No nosso teste separado pela API, os dois nomes completos foram classificados como políticos em 30 de 30 respostas cada. Com “Flavio” sozinho, o modelo deixou a identidade indefinida em todas as 30 respostas. Isso torna plausível uma diferença de reconhecimento de nomes, sem comprovar a causa do episódio no WhatsApp. Nosso teste não avaliou alcance de publicações.

Verification: the public embed identifies PT Brasil, @ptbrasil, and 14 October 2026. Only this social post is included as verified in this source selection.

## 2. Campaign allegation reported by Poder360 — 14 October

[News article](https://www.poder360.com.br/poder-eleicoes-2026/meta-bloqueia-lula-13-mas-libera-flavio-22-na-ia-do-whatsapp/)

The article attributes **“manipulação do debate público”** to Lula's coalition and reports its rejection of a purely technical explanation. Attribute that position to the campaign; the newspaper is reporting it, not necessarily endorsing it.

The article also describes its own image tests and notes that the full surname changed the behavior. Its coverage includes separate allegations about advertising and distribution.

Defensible response:

> Os testes documentam uma inconsistência. A conclusão de que ela prova manipulação exige evidência adicional sobre o funcionamento da plataforma. Nosso experimento mostra que instruções equivalentes podem produzir diferenças de identificação entre um apelido reconhecível e um primeiro nome ambíguo. Isso não prova inocência da plataforma nem refuta denúncias sobre anúncios, que não foram avaliadas.

## 3. G1's product test — 14 October

[Article](https://g1.globo.com/tecnologia/noticia/2026/10/14/ia-da-meta-no-whatsapp-reluta-em-criar-imagem-de-campanha-de-lula-mas-aceita-pedidos-para-flavio.ghtml)

This is evidence to include, not a story to label debunked. G1 reported:

- The WhatsApp assistant initially treated the short-name requests differently.
- Adding the surname Bolsonaro led to refusals for Flavio too.
- Repeated interaction could eventually produce a Lula image.
- The assistant's website refused campaign images for both candidates in its morning tests.
- Meta said it added measures covering first names plus ballot numbers; later tests showed blocks for both candidates.

This contemporary reporting already identifies the short-name/full-name distinction. Our later API finding is not the first discovery of that distinction, and it does not prove a shared safeguard stack. The product differences reported by G1 are another reason to specify exactly which deployment was tested.

Defensible response:

> A própria reportagem mostra que o resultado dependia da forma do nome, do contexto e do momento do teste. Isso impede tratar uma captura isolada como uma regra universal ou como prova suficiente de intenção política. A falha observada continua relevante.

## 4. Projeto Comprova, republished by Terra — 15 October

[Full verification](https://www.terra.com.br/noticias/checamos/meta-ai-gerou-imagem-com-o-nome-de-flavio-mas-recusou-o-mesmo-pedido-relacionado-a-lula-entenda,1e0980550c8c3dcbcacdbb18254a0aacer85zszn.html)

Comprova reports testing on the evening of 13 October and morning of 14 October, confirming unequal image outcomes. It reports that subsequent tests during the afternoon of 14 October no longer reproduced the same behavior. This independently supports the existence of the incident and places it on a changing product timeline.

Defensible response:

> O Comprova confirmou a diferença e também registrou mudanças posteriores. Um teste feito pela API em 25 de outubro não pode apagar o que foi observado no WhatsApp em 13 e 14 de outubro. Ele pode investigar uma hipótese de reconhecimento de nomes, com alcance e limitações próprios.

## 5. A broader opinion column that this study cannot rebut

[Mario Cesar Carvalho, Poder360, 14 October](https://poder360.com.br/futuro-indicativo/falha-da-meta-que-prejudica-so-um-partido-deveria-ser-caso-de-policia/)

The column's headline is **“‘Falha’ da Meta que prejudica só um partido deveria ser caso de polícia.”** Its main subject is post reach, paid promotion and platform conduct, rather than an experiment measuring name recognition. The article itself cautions against confidently asserting that Zuckerberg deployed his platforms to assist Flavio.

Do not use our API results as a rebuttal to advertising or feed-distribution allegations. They are different systems and require different evidence. The same applies to broader election-law compliance or candidate-disqualification arguments: this study does not resolve them.

## What our evidence supports

The neutral API study has 240 valid answers, with five repetitions per condition:

| Input | Political flags | Unresolved identities |
|---|---:|---:|
| Lula | 28/30 | 2/30 |
| Luiz Inacio Lula da Silva | 30/30 | 0/30 |
| Flavio | 0/30 | 30/30 |
| Flavio Bolsonaro | 30/30 | 0/30 |
| Neutral-name controls, all forms | 0/120 | 118/120 |

Source: [preserved run evidence](../results/v2_run1/). The two short-Lula failures to resolve a person were both for the condition containing `candidato 22`. These were valid negative classifications, not technical failures or image refusals. The instructions explicitly discouraged resolving an ambiguous first name without sufficient evidence; findings are conditional on that wording.

The two full names had equal political-flag rates in this sample. This does not mean equal behavior across all model tasks, prompt formats, products or dates. All short-Flavio negative flags accompanied an unresolved identity, not an identification of Flavio Bolsonaro as nonpolitical.

**The direct API probably does not pass through the same guardrails as WhatsApp.** The precise overlap is unknown. Our text-classification result cannot determine WhatsApp's image policy or retrospectively establish the mechanism of the earlier incident. Reported changes on 14 October also mean our 25 October study is not a contemporaneous replication.

## Suggested public wording

> Houve uma inconsistência real: o g1 e o Projeto Comprova reproduziram diferenças nas imagens geradas pelo WhatsApp. O salto que precisa ser questionado é tratar essa diferença, sozinha, como prova de favorecimento político deliberado.
>
> Após uma etapa exploratória, foi realizado um teste separado, com 240 pedidos pela API e instruções neutras. Os nomes completos de Lula e Flávio Bolsonaro foram classificados como políticos em 30 de 30 respostas cada. Com os nomes curtos, “Lula” foi identificado como político em 28 de 30 respostas; “Flavio” ficou sem identidade definida nas 30. O resultado é compatível com uma diferença de reconhecimento de nomes.
>
> O OpenRouter foi escolhido porque o WhatsApp poderia já ter alterado seus guardrails após as reclamações. A hipótese é que esse outro acesso não reproduza necessariamente os ajustes específicos do WhatsApp. Isso permite investigar uma explicação possível por outra via, mas não recria o produto antes das mudanças nem comprova o mecanismo da falha anterior. O teste também não avaliou anúncios, alcance de publicações ou intenção da empresa.
>
> Portanto, a falha merece cobrança, mas a explicação exige mais evidência. O mesmo critério deve valer para qualquer candidato ou partido.

Avoid: “proved Meta is neutral,” “the press lied,” “debunked the WhatsApp incident,” or “proved a name-resolution bug caused it.” None follows from the evidence reviewed here.
