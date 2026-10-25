# Da assimetria observada à atribuição de intenção

## Alfabetização algorítmica, opacidade da IA e limites da inferência causal

**Autor:** Pedro Del Nero Todescan  
**Versão:** 1.0 — 25 de outubro de 2026  
**Natureza:** white paper / relatório de pesquisa, sem revisão por pares  
**Estudo de caso:** muse-political-entity-test  
**Preparação do texto:** com assistência de inteligência artificial.

**Palavras-chave:** alfabetização algorítmica; modelos de linguagem; resolução de entidades; guardrails; inferência causal; comunicação pública.

## 1. Resumo e pergunta de pesquisa

**Respostas diferentes demonstram uma diferença de comportamento nas condições observadas. Não demonstram, por si, reconhecimento desigual de entidades, aplicação seletiva de uma política ou intenção política.** Cada uma dessas explicações exige evidências adicionais. A recíproca também importa: apresentar um mecanismo técnico plausível não prova ausência de intenção nem elimina a relevância de efeitos desiguais.

Este trabalho examina o repositório muse-political-entity-test, que investiga respostas associadas a Lula e Flávio Bolsonaro. Considera o notebook exploratório arquivado, o CSV original, a consulta denominada “forense”, a tabela do fatorial recuperada do Colab ampliado, a revisão metodológica e os registros da rodada revisada. A base documental desta versão é a revisão e020e9e0b5b20bfe0a37bbee8d8ff7755706f373 do repositório. [1–4]

A pergunta de pesquisa é: **o que uma diferença de resposta permite concluir sobre reconhecimento de entidades, aplicação de políticas e intenção política?**

O caso reúne três conjuntos de evidências que precisam permanecer separados. Reportagens documentaram resultados de geração de imagens no WhatsApp. O experimento por API registrou classificações de nomes e, na investigação original, previsões textuais de restrição. O operador, o pesquisador e o modelo ofereceram explicações ou hipóteses sobre mecanismos.

A rodada revisada sustenta uma conclusão delimitada: a forma do nome afetou o reconhecimento político na tarefa textual estudada. A investigação original acrescenta que reconhecer uma figura política, identificá-la como candidata presidencial e prever uma restrição podem produzir respostas divergentes. Nenhuma das rodadas identifica, isoladamente, a causa interna do comportamento anterior do WhatsApp.

O valor educacional do caso está em tornar essas distinções compreensíveis. Seu alcance não inclui medir a alfabetização do público ou explicar por que o episódio repercutiu.

## 2. LLMs, associações aprendidas, similaridade e guardrails

### Associações não equivalem a cadastros consistentes

Modelos de linguagem aprendem regularidades em dados e geram respostas condicionadas pelo contexto. Representações aprendidas permitem relacionar palavras, pessoas, cargos e situações, mas não garantem uma base factual completa, atualizada e internamente consistente. O treinamento posterior também pode modificar como o modelo segue instruções e responde a solicitações. Essas referências gerais não descrevem a implementação específica da Meta. [8–9]

Um nome completo, um apelido distintivo e um primeiro nome comum oferecem pistas diferentes. Para uma pessoa acompanhando uma eleição, “Flávio 22” pode parecer inequívoco. Um sistema, sob determinada instrução, pode considerar essa expressão insuficiente para resolver a identidade. Inversamente, pode associar “Lula” imediatamente a uma figura política.

Essa possibilidade ajuda a formular hipóteses, mas o experimento não mediu frequência de nomes nos dados de treinamento, similaridade vetorial ou intensidade de associações internas. Mediu respostas. A interpretação em termos de associações aprendidas é compatível com o comportamento observado, sem constituir observação direta do mecanismo.

### Quatro operações diferentes

| Operação | O que significa | O que não garante |
|---|---|---|
| Resolução de identidade | Relacionar a expressão a uma pessoa específica | Conhecer corretamente seus papéis atuais |
| Classificação política e de papel | Classificá-la como política, senadora, presidente ou candidata | Aplicar determinada política de imagens |
| Previsão textual de restrição | Produzir uma afirmação sobre provável bloqueio | Acessar a decisão real de moderação |
| Bloqueio observado no produto | Recusar explicitamente ou impedir a entrega solicitada | Revelar automaticamente a causa da recusa |

Também se deve separar não resolver uma identidade de resolver a identidade e classificá-la como não política. Embora ambos possam resultar em um campo booleano negativo, representam comportamentos distintos. A simples ausência de uma imagem também exige classificação: uma falha técnica não deve ser automaticamente contabilizada como recusa de política.

### O sistema excede o modelo conversacional

Guardrails são mecanismos que orientam ou restringem o funcionamento de um sistema. Podem incluir instruções, regras, classificadores, modelos adicionais e verificações antes ou depois da geração. Essas possibilidades não descrevem uma arquitetura comprovada do WhatsApp.

Não há evidência suficiente para presumir pesos compartilhados entre o modelo consultado via OpenRouter e o mecanismo responsável por uma restrição no produto. Mesmo o uso de um mesmo modelo-base não implicaria igualdade de versões, instruções, ferramentas ou proteções.

A explicação do assistente sobre uma recusa não deve ser tratada como registro dos bastidores. Estudos sobre explicações geradas por modelos mostram que elas podem ser plausíveis sem representar fielmente os fatores que determinaram uma resposta. Essa literatura justifica cautela metodológica; não demonstra que uma explicação específica do caso seja falsa. [10]

### Três sentidos diferentes de “probabilidade”

Frequência observada é a proporção de respostas com determinado resultado nas tentativas realizadas. Confiança declarada é um número escrito pelo modelo. Probabilidade interna exige especificar a quantidade examinada — por exemplo, probabilidade de tokens ou escore de um classificador — e dispor de acesso adequado.

Assim, 30 respostas positivas em 30 tentativas não significam certeza universal; uma confiança escrita de 0,95 não demonstra calibração; probabilidades de tokens não equivalem automaticamente à probabilidade de reconhecimento correto ou de bloqueio. O projeto não encontrou logprobs não nulos nos registros da v2 e preservou uma consulta datada de capacidades que não anunciava seu suporte. [4]

## 3. Contexto do episódio e alegações públicas

O g1, em reportagem de 14 de outubro de 2026, informou ter reproduzido uma diferença no WhatsApp: solicitações com “Flávio 22” eram atendidas, enquanto pedidos com “Lula 13” encontravam resistência. A inclusão do sobrenome “Bolsonaro” também levou a recusas para Flávio. A reportagem registrou geração de imagem de Lula após tentativas reiteradas, recusas para ambos no site do assistente e bloqueios para ambos em testes posteriores no WhatsApp. [5]

O Projeto Comprova, em texto publicado em 15 de outubro, relatou testes na noite de 13 e na manhã de 14 de outubro que confirmaram tratamento desigual. Segundo a verificação, novos testes na tarde do dia 14 já não reproduziram o mesmo comportamento. [6]

Esses registros sustentam a existência da inconsistência. Também mostram que ela dependia da formulação, do contexto e do momento do teste. Não sustentam uma regra universal de bloqueio para um candidato e permissão para outro.

O Poder360 atribuiu à coligação de Lula a expressão “manipulação do debate público” e a rejeição de uma explicação puramente técnica. A reportagem apresentou testes próprios e descreveu alegações adicionais sobre anúncios e distribuição. A acusação deve ser atribuída à campanha; sua publicação não constitui demonstração independente de intenção. [7]

O repositório documenta uma manifestação do PT Brasil sobre “uso enviesado” da ferramenta. Essa expressão pode designar resultados desiguais ou sugerir direcionamento deliberado. Convém explicitar qual sentido está sendo discutido, pois os requisitos de evidência são diferentes. A publicação é considerada conforme preservada na documentação, sem nova verificação independente do post nesta análise. [1]

Segundo o apêndice sobre a explicação pública da Meta, a empresa declarou que suas proteções nem sempre reconheciam candidatos quando primeiros nomes comuns eram combinados com números eleitorais e que corrigiu essa lacuna em 14 de outubro. O documento registra ainda exemplos envolvendo “Luiz”. A página original do comunicado permaneceu inacessível nas tentativas de consulta para este texto; esses detalhes dependem da documentação preservada. O g1 e o Comprova, acessados diretamente, registram a declaração sobre medidas adicionais para primeiros nomes acompanhados de números. [1, 5–6]

A explicação do operador é relevante, mas não substitui auditoria de implementação e logs. O estudo de nomes não resolve acusações sobre alcance, publicidade ou distribuição, nem oferece uma conclusão jurídica sobre o episódio: esses problemas exigem investigações próprias.

## 4. Desenho original e metodologia revisada

### A investigação original

**Conforme a data informada pelo autor, as rodadas de 24 e 40 pedidos ocorreram em 14 de outubro de 2026.** Não há horários preservados das chamadas. Portanto, não é possível estabelecer se ocorreram antes ou depois do ajuste no WhatsApp naquele dia. A data do commit registra preservação no repositório, não execução dos testes. [2]

O modelo configurado era meta/muse-spark-1.1, via OpenRouter, com temperatura zero. A rodada de 24 pedidos variava nomes, capitalização, números, cargos e referências a candidatura. Solicitava identidade reconhecida, categorias políticas, confiança declarada e previsão de restrição de imagens.

O fatorial de 40 pedidos cruzava quatro nomes — Lula, Flavio, Tarcisio e Gabriel —, cinco números — 13, 22, 10, 99 e 17 — e presença ou ausência de “candidato”.

O desenho já continha comparações pertinentes. Entretanto, a ordem era fixa, não havia repetições sistemáticas por condição e a instrução apresentava a assimetria relatada no WhatsApp. Algumas justificativas retomavam esse enquadramento. O pedido com o nome completo de Flávio Bolsonaro aparecia duas vezes na rodada de 24.

A consulta “forense” solicitava ao próprio modelo explicações sobre possíveis camadas do sistema. Sua resposta constitui geração de hipóteses, não inspeção técnica do produto. Percentuais atribuídos a explicações não são estimativas causais verificadas.

### A rodada revisada

A v2 ocorreu em 25 de outubro de 2026, entre aproximadamente 04h35 e 04h37 de Brasília, segundo os registros preservados. O protocolo combinou quatro entidades pretendidas, duas formas nominais, três condições numéricas — ausência, 13 e 22 — e duas condições de papel — ausência ou presença de “candidato”. Foram cinco repetições por combinação: 48 condições e 240 pedidos. [3–4]

Gabriel Silva e Mariana Costa funcionaram como controles presumidos neutros. Essa escolha não comprova que os nomes sejam exclusivos ou que não possam designar pessoas políticas.

A revisão padronizou formulações, fixou um plano embaralhado, iniciou conversas sem histórico e retirou a narrativa da assimetria esperada. A instrução solicitava apenas pessoa reconhecida, classificação política e cargo público, advertindo que primeiro nome, número e “candidato” não identificam necessariamente alguém. Dois pilotos técnicos foram excluídos.

A coleta usou o mesmo identificador público de modelo, temperatura zero, limite de 2048 tokens de saída e esforço de raciocínio baixo. O identificador não comprova identidade de backend entre datas. A rodada original não especificava esse mesmo esforço de raciocínio e tinha outro limite de saída.

A melhoria central foi separar reconhecimento de previsão de moderação. Entretanto, a revisão também alterou o desfecho e parâmetros da coleta. Ela não permite atribuir diferenças entre rodadas apenas à retirada do enquadramento original.

O OpenRouter ofereceu uma via alternativa diante das mudanças relatadas no WhatsApp. Não foi validado como controle sem intervenção nem como preservação do estado anterior do produto.

## 5. Resultados: variações de nome, número e papel político

### Rodada original de 24 pedidos

O CSV preserva 24 tentativas, 20 classificações válidas e quatro ausências. Entre as respostas válidas, oito previram restrição e 12 não a previram. O denominador correto para essa proporção é 20. [2]

| Identidade declarada | Válidas | Política | Candidato presidencial | Chefe de Estado | Previsão de restrição |
|---|---:|---:|---:|---:|---:|
| Lula | 7 | 7 | 3 | 7 | 6 |
| Flavio Bolsonaro | 8 | 8 | 0 | 0 | 0 |
| Jair Bolsonaro | 1 | 1 | 0 | 0 | 1 |
| Tarcísio de Freitas | 1 | 1 | 0 | 0 | 1 |
| Sem pessoa identificada | 3 | 0 | 0 | 0 | 0 |

Os grupos seguem a identidade declarada pelo modelo, sem validação por gabarito externo. São classificações e previsões, não candidaturas verificadas ou bloqueios observados.

Nas oito respostas associadas a Flávio Bolsonaro, o modelo reconheceu uma figura política, não a classificou como candidata presidencial e não previu restrição. Isso incluiu as duas ocorrências do nome completo. A ambiguidade de identidade não esgota os resultados originais: houve também divergência entre identidade, papel atribuído e previsão de política.

Os contrapontos impedem uma regra simples. “Faca Arte Lula” recebeu classificação como chefe de Estado, mas previsão negativa de restrição. Jair Bolsonaro e Tarcísio receberam previsões positivas sem classificação como candidato presidencial ou chefe de Estado.

Na variação numérica, “Lula 22” recebeu previsão positiva, enquanto números isolados receberam previsões negativas. “flavio 13” ficou sem classificação válida e não pode ser contado como resposta negativa.

### Fatorial original de 40 pedidos: tabela recuperada

O arquivo inicialmente arquivado preservava uma prévia de dez casos e oito justificativas positivas. Posteriormente, a versão ampliada do Colab permitiu recuperar as 40 linhas exibidas, com 29 classificações válidas e 11 ausências. O repositório preserva tabela de origem, procedência, CSV, JSON e resumo calculado. [2]

| Nome fornecido | Pedidos | Válidas | Ausentes | Classificação política | Candidato presidencial | Previsão de restrição |
|---|---:|---:|---:|---:|---:|---:|
| Lula | 10 | 6 | 4 | 6/6 | 3/6 | 6/6 |
| Flavio | 10 | 9 | 1 | 9/9 | 0/9 | 0/9 |
| Tarcisio | 10 | 5 | 5 | 5/5 | 0/5 | 2/5 |
| Gabriel | 10 | 9 | 1 | 0/9 | 0/9 | 0/9 |

As frações usam classificações válidas como denominador. A distribuição desigual de ausências precisa acompanhar as taxas: não há fundamento para supor que os casos sem classificação tenham o mesmo comportamento dos casos válidos.

Os denominadores digitados no gráfico antigo podem agora ser conferidos com a tabela recuperada. Suas taxas de 100%, 0%, 40% e 0%, respectivamente, são previsões de restrição entre classificações válidas. Os rótulos de “recusa” dos gráficos históricos excedem o que foi medido.

A recuperação é da tabela exibida, não dos envelopes HTTP originais. Alguns textos permanecem truncados. Uma célula posterior registra execução de correlação e regressão com dados simulados; esses resultados não são usados como evidência experimental. Preencher ausências com zero e False tampouco constitui recuperação de respostas.

### Rodada revisada

Os registros da v2 contêm 240 respostas válidas, sem ausências e com uma tentativa HTTP por caso. A recontagem local deste trabalho confirmou os totais do resumo preservado. [4]

| Forma nominal | Classificação política | Frequência | Identidade não resolvida |
|---|---:|---:|---:|
| Lula | 28/30 | 93,3% | 2/30 |
| Luiz Inacio Lula da Silva | 30/30 | 100% | 0/30 |
| Flavio | 0/30 | 0% | 30/30 |
| Flavio Bolsonaro | 30/30 | 100% | 0/30 |
| Controles, todas as formas | 0/120 | 0% | 118/120 |

Todas as respostas negativas para “Flavio” acompanharam identidade não resolvida. Não houve, nesse conjunto, identificação de Flávio Bolsonaro seguida de classificação como não político.

A diferença agregada entre Lula e Flávio foi de 46,7 pontos percentuais nos 60 pares completos. Ela se concentrou nos nomes curtos: 93,3 pontos, contra zero nos nomes completos. A diferença agregada depende do balanceamento experimental e não representa uma taxa geral do produto.

Nos estratos de número e papel, os nomes completos receberam classificação política em 5/5 respostas de cada combinação. “Flavio” permaneceu não resolvido em todas, inclusive com “candidato 22”. “Lula” recebeu 5/5 classificações políticas em cinco combinações e 3/5 em “Lula candidato 22”. A análise por subgrupos foi realizada após a coleta, sobre fatores já previstos no plano. [4]

Números e “candidato”, portanto, não garantiram resolução. A exceção com “Lula candidato 22” documenta sensibilidade contextual, mas não demonstra um mecanismo interno específico.

A v2 não perguntou se a pessoa era candidata presidencial. A presença de “candidato” na entrada não equivale a reconhecimento desse papel na saída.

## 6. Interpretação das evidências e explicações alternativas

### O problema de identificação causal

A inferência causal exige definir qual intervenção e qual resultado estão sendo comparados. [11] Neste caso, existem perguntas diferentes: alterar o nome muda a classificação textual? Essa classificação determina a aplicação de uma proteção no WhatsApp? Uma eventual diferença de proteção resulta de decisão política deliberada?

A v2 oferece evidência para a primeira pergunta, sob suas instruções e condições. Não acompanha a passagem da classificação à decisão de imagem e não testa a terceira.

Mesmo “Lula” versus “Flavio” reúne diferenças de distintividade nominal, identidade, trajetória pública e associações aprendidas. O contraste não isola orientação política como variável causal. A comparação entre nome curto e completo documenta sensibilidade à formulação, mas não identifica qual representação ou componente intermediário a produziu.

### Evidência, interpretação e limite

| Evidência | Interpretação técnica compatível | Limite inferencial |
|---|---|---|
| Reportagens reproduziram resultados desiguais no WhatsApp | Existiu inconsistência no produto nas condições testadas | Não identifica mecanismo ou intenção |
| Acrescentar “Bolsonaro” alterou o resultado relatado | Maior especificidade nominal pode afetar reconhecimento e proteção | Não revela qual componente processou a pista |
| V2: ambos os nomes completos receberam 30/30 classificações políticas | Houve igualdade nesse desfecho e recorte | Não demonstra igualdade em imagens, produtos ou outras datas |
| V2: “Flavio” ficou não resolvido em 30/30 | Ambiguidade nominal é explicação compatível com essa tarefa | Não comprova a causa do incidente no WhatsApp |
| Original: Flávio foi reconhecido como político, sem candidatura presidencial e sem previsão de restrição | Identidade, papel e previsão podem divergir | As respostas foram produzidas sob enquadramento direcionado |
| Fatorial recuperado: 29 classificações e 11 ausências | Permite conferir as taxas históricas de previsão entre respostas válidas | Não transforma ausências em negativas nem previsões em recusas |
| Confianças declaradas diferiram entre grupos | O modelo gerou avaliações numéricas distintas | Não mede calibração, probabilidade interna ou limiar de bloqueio |
| Meta declarou uma lacuna de reconhecimento e correção | O operador apresentou uma explicação funcional | Não constitui auditoria independente ou prova de ausência de intenção |
| Resultados variaram entre vias de acesso | Implantações podem ter instruções e proteções diferentes | Não estabelece quais componentes ou pesos são compartilhados |

Entre as alternativas estão ambiguidade nominal, associações desiguais com cargos e candidaturas, metadados desatualizados, regras lexicais, interação entre pistas, contexto de conversa e diferenças de implantação. Não há base para atribuir probabilidades confiáveis a essas hipóteses ou escolher uma como causa demonstrada.

A intenção também precisa ser definida: uma preferência atribuída ao texto gerado não equivale a uma decisão deliberada da organização. Investigar esta última poderia envolver regras seletivas, instruções, decisões documentadas, histórico de alterações e padrões controlados de aplicação.

O conjunto oferece apoio a uma explicação técnica fundamentada, não apenas abstrata: diferenças de reconhecimento e de associação a categorias podem acompanhar respostas desiguais. A evidência por API e os relatos do produto, porém, não constituem uma observação contínua de um mesmo mecanismo.

**O estudo não identifica intenção política nem sua ausência.** A plausibilidade de uma falha de reconhecimento reduz a justificativa para uma conclusão causal exclusiva; não refuta automaticamente hipóteses concorrentes.

Efeitos e intenção permanecem distintos. Uma falha sem direcionamento deliberado pode produzir consequências politicamente desiguais e justificar correção, transparência e escrutínio.

## 7. Implicações para alfabetização algorítmica e comunicação pública

A opacidade não tem uma única origem. Burrell distingue o segredo institucional, as dificuldades de compreensão técnica e a complexidade dos próprios sistemas de aprendizado de máquina. [12] Essa distinção evita atribuir toda incerteza à falta de conhecimento do usuário.

Alfabetização algorítmica deve permitir interpretar criticamente resultados, reconhecer limites e formular perguntas verificáveis. A literatura sobre alfabetização em IA inclui competências de compreensão e avaliação crítica, sem exigir domínio especializado de implementação. [13]

O caso destaca três competências práticas: diferenciar modelo e produto; separar resultado, explicação e evidência de mecanismo; e interpretar ausências e frequências sem convertê-las em certezas.

Lacunas nessas competências podem favorecer atribuições precipitadas. É possível tomar a justificativa do assistente como acesso aos bastidores, presumir que expressões equivalentes para humanos sejam igualmente informativas para o sistema ou interpretar uma diferença como prova suficiente de propósito.

O erro inverso é igualmente relevante: usar uma explicação técnica sofisticada para encerrar a investigação. Conhecimento técnico deve melhorar a exigência de evidência, não substituir uma narrativa categórica por outra.

**O experimento não mediu alfabetização do público, recepção das notícias ou causas da repercussão.** Não permite afirmar que desconhecimento causou as denúncias, nem explicar a motivação dos atores envolvidos.

Na comunicação pública, o resultado observado deve aparecer junto das condições de teste. Explicações precisam ser atribuídas a quem as oferece, e hipóteses devem conservar esse estatuto. A documentação jornalística de sobrenomes, tentativas reiteradas e mudanças no tempo ampliou a compreensão do episódio. A plataforma pode contribuir com registros verificáveis sobre escopo, diagnóstico e correção.

Alfabetização do público e transparência institucional são complementares. A primeira não transfere aos usuários a responsabilidade de explicar sistemas aos quais não têm acesso.

## 8. Limitações, reprodutibilidade e referências

### Limitações

A principal limitação é a distância entre a tarefa por API e a geração de imagens no WhatsApp. Somam-se a ela o enquadramento da investigação original, a ausência de horários das chamadas originais e as mudanças de tarefa e parâmetros entre rodadas.

A recuperação da tabela do Colab resolveu a ausência das 40 linhas exibidas, mas não recuperou envelopes HTTP, horários ou textos integralmente truncados. A distribuição de 11 ausências continua relevante para qualquer comparação do fatorial.

O teste de Welch apresentado no notebook original, com p aproximado de 0,0037, compara confiança declarada entre grupos definidos pela previsão do próprio modelo. Dependência entre campos, composição dos grupos e repetição de texto impedem tratá-lo como validação de probabilidade interna, mecanismo de proteção ou intenção. As análises posteriores com dados simulados são excluídas.

Na preparação inicial do texto, o conector não conseguiu recuperar o arquivo bruto da v2. Na preparação desta versão para o repositório, uma cópia local permitiu recontar 240 registros válidos e únicos e conferir as classificações por nome. Seu identificador Git de conteúdo, f323924c263bdf01f7ed9bd9d3169c8a96f9078b, coincide com o arquivo da revisão documental citada. A conferência numérica não equivale a uma auditoria semântica independente de cada identidade e cargo retornados.

O comunicado original da Meta permaneceu inacessível nas tentativas de consulta para este texto. Seus detalhes são atribuídos à documentação preservada e, quando possível, corroborados pela cobertura acessada. As páginas jornalísticas consultadas podem incorporar atualizações; não são capturas arquivadas de cada versão original.

### Reprodutibilidade e pesquisa posterior

Reprodutibilidade exige distinguir recalcular resultados preservados de obter os mesmos resultados em novas chamadas. O repositório oferece notebook, CSV, scripts, plano e metadados para conferência. Uma coleta futura pode diferir por alterações de modelo ou implantação, mesmo conservando um identificador público.

A partir da raiz do repositório, a conferência offline pode usar:

~~~bash
python review_original.py
python extract_colab_factorial.py
python report_run.py results/v2_run1
python analyze_number_cues.py
~~~

Os dois primeiros comandos examinam registros históricos e a tabela recuperada; os demais resumem a v2 e seus estratos. Não são comandos de nova coleta por API. As dependências e o ambiente são descritos no README.

Uma investigação posterior do produto deveria preservar pedidos exatos, horários, ordem, contexto, localidade e resultados visuais, com categorias separadas para imagem entregue, recusa explícita, falha técnica e resultado ambíguo. Comparações balanceadas e repetidas ajudariam a caracterizar o comportamento; logs e documentação de implantação seriam necessários para aproximar a atribuição de mecanismo.

A evidência permite avançar da percepção de diferença para uma descrição melhor do comportamento. A passagem dessa descrição à causa, e da causa à intenção, permanece dependente de informação adicional.

### Referências

[1] PedroDnT. *muse-political-entity-test*. [Revisão documental consultada](https://github.com/PedroDnT/muse-political-entity-test/tree/e020e9e0b5b20bfe0a37bbee8d8ff7755706f373). Inclui [contexto público](media-context.md), [procedência](provenance-and-thesis.md) e [explicação atribuída à Meta](meta-explanation.md). A documentação aponta para o [comunicado original](https://about.fb.com/br/news/2026/10/a-meta-nao-esta-interferindo-nas-eleicoes-brasileiras-estes-sao-os-fatos/), com a limitação de acesso descrita acima.

[2] PedroDnT. [Notebook original arquivado](../notebook/archive/original_exploratory.ipynb), [CSV original](../results/run1_classification.csv), [prompt forense](../results/forensic_prompt.txt), [resposta forense](../results/run1_forensic_answer.json), [revisão do desenho](original-study-review.md), [tabela recuperada](../results/analysis/colab-factorial-table.html), [procedência da extração](../results/analysis/colab-factorial-provenance.json) e [resumo do fatorial](../results/analysis/colab-factorial-summary.json).

[3] PedroDnT. [*Neutral entity-resolution protocol, version 2*](methodology.md) e [plano preservado](../results/v2_run1/plan.json).

[4] PedroDnT. Rodada revisada: [respostas brutas](../results/v2_run1/responses.jsonl), [resumo](../results/v2_run1/summary.json), [estratos de nome, número e papel](../results/analysis/number-cues.csv), [capacidades de probabilidade](../results/analysis/probability-capability.json) e [validação](validation.md).

[5] Helder, D.; Giacomassi, F. g1, 14 out. 2026. [*Meta AI aceita “Flávio 22”, mas nega “Lula 13” e “Flávio Bolsonaro 22”*](https://g1.globo.com/tecnologia/noticia/2026/10/14/ia-da-meta-no-whatsapp-reluta-em-criar-imagem-de-campanha-de-lula-mas-aceita-pedidos-para-flavio.ghtml).

[6] Projeto Comprova. Terra, 15 out. 2026. [*Meta AI gerou imagem com o nome de Flávio, mas recusou o mesmo pedido relacionado a Lula; entenda*](https://www.terra.com.br/noticias/checamos/meta-ai-gerou-imagem-com-o-nome-de-flavio-mas-recusou-o-mesmo-pedido-relacionado-a-lula-entenda,1e0980550c8c3dcbcacdbb18254a0aacer85zszn.html).

[7] Poder360, 14 out. 2026. [*Meta bloqueia “Lula 13”, mas libera “Flávio 22” na IA do WhatsApp*](https://www.poder360.com.br/poder-eleicoes-2026/meta-bloqueia-lula-13-mas-libera-flavio-22-na-ia-do-whatsapp/).

[8] Vaswani, A. et al. (2017). [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762).

[9] Ouyang, L. et al. (2022). [*Training language models to follow instructions with human feedback*](https://arxiv.org/abs/2203.02155).

[10] Turpin, M. et al. (2023). [*Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*](https://arxiv.org/abs/2305.04388). NeurIPS.

[11] Hernán, M. A.; Robins, J. M. (2020). [*Causal Inference: What If*](https://miguelhernan.org/whatifbook). Chapman & Hall/CRC.

[12] Burrell, J. (2016). [*How the machine “thinks”: Understanding opacity in machine learning algorithms*](https://doi.org/10.1177/2053951715622512). *Big Data & Society*, 3(1).

[13] Long, D.; Magerko, B. (2020). [*What is AI Literacy? Competencies and Design Considerations*](https://doi.org/10.1145/3313831.3376727). CHI ’20, p. 1–16.

---

**Registro e versões:** esta versão está disponibilizada no repositório. Não há DOI ou depósito no Zenodo declarado neste documento. Uma eventual publicação externa deve preservar a versão, identificar o commit dos materiais analisados e atualizar seus metadados; veja a [nota de publicação](publicacao.md).
