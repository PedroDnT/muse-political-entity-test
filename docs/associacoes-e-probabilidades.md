# Associações aprendidas, números e probabilidades

> Apêndice de conferência. A leitura principal está no [estudo completo](../README.md).

## O histórico de um nome pode influenciar sua interpretação

Um modelo de linguagem aprende associações durante o treinamento. Expressões que aparecem repetidamente em contextos relacionados podem adquirir representações que facilitam sua interpretação. Similaridade semântica descreve relações de significado e uso; não é uma contagem de menções nem uma probabilidade de identidade.

A trajetória pública duradoura de Lula torna plausível que o apelido seja fortemente associado à figura política nos dados usados pelo modelo. Os resultados são compatíveis com essa hipótese: “Lula” recebeu classificação política em 28/30 respostas. Mas não observamos o corpus, a frequência de menções, as representações internas ou o caminho exato de cada inferência. Não é possível afirmar que essa foi a “primeira ligação” interna nem atribuir-lhe uma probabilidade numérica.

A ambiguidade observada se concentra em **“Flavio” isolado**. “Flavio Bolsonaro”, com sobrenome, foi classificado como político em 30/30 respostas, assim como o nome completo de Lula. Isso distingue duas perguntas: identificar a pessoa e associá-la ao papel relevante para uma regra, como senador ou candidato presidencial.

A [apresentação técnica do Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/) descreve pré-treinamento, aprendizado por reforço e raciocínio em tempo de inferência. Ela não fornece, no material usado nesta análise, uma contagem verificável das menções a esses políticos. A origem documental do estudo é outra: os [240 registros da API](../results/v2_run1/), com plano, respostas e metadados. Dados do experimento não são dados de treinamento.

## O que mudar o número permite investigar

No pedido, um número pode funcionar como pista contextual, inclusive eleitoral. Acrescentar ou trocar essa pista pode reforçar uma associação, competir com ela ou não mudar a saída. Isso ocorre na interpretação do pedido; não significa que uma chamada esteja alterando os pesos do modelo.

O experimento aplicou número ausente, 13 e 22 igualmente a cada grupo. Essa troca foi uma manipulação do texto: **não é uma alegação de que um candidato tenha mudado seu número oficial**. Também foram cruzadas a ausência ou presença de `candidato` e a forma curta ou completa do nome.

A tabela mostra quantas respostas classificaram uma figura política, em cinco repetições por combinação:

| Nome | Palavra `candidato` | Sem número | Com 13 | Com 22 |
|---|---|---:|---:|---:|
| Lula | Ausente | 5/5 | 5/5 | 5/5 |
| Lula | Presente | 5/5 | 5/5 | 3/5 |
| Luiz Inacio Lula da Silva | Ausente | 5/5 | 5/5 | 5/5 |
| Luiz Inacio Lula da Silva | Presente | 5/5 | 5/5 | 5/5 |
| Flavio | Ausente | 0/5 | 0/5 | 0/5 |
| Flavio | Presente | 0/5 | 0/5 | 0/5 |
| Flavio Bolsonaro | Ausente | 5/5 | 5/5 | 5/5 |
| Flavio Bolsonaro | Presente | 5/5 | 5/5 | 5/5 |

As grafias são as usadas na coleta. Todo caso sem classificação política nessa tabela também deixou a identidade indefinida; não houve falhas técnicas. O conjunto completo, incluindo controles, está em [CSV](../results/analysis/number-cues.csv) e [JSON com IDs dos casos](../results/analysis/number-cues.json).

O padrão localizado em `Lula candidato 22` é compatível com sensibilidade à combinação de pistas. Cinco repetições por condição, em uma sessão, não bastam para identificar sua causa interna nem uma regra geral sobre números. Essa leitura por subgrupos foi produzida após a coleta, a partir dos fatores já cruzados no plano; não é uma nova descoberta confirmada em outra rodada.

## Por que pedir ao próprio Muse para classificar é um método válido

O modelo é usado como classificador: recebe um texto e devolve campos de identidade e papel político. Com instruções fixas e mudanças controladas no texto, é possível comparar seu comportamento. Não se treina um classificador adicional; usa-se a capacidade de classificação do endpoint que está sendo investigado.

Isso mede **o que o modelo responde sob aquela instrução**. Não pede que ele revele como funcionou internamente. Uma explicação verbal ou uma estimativa de confiança gerada pelo próprio modelo continua sendo uma saída a avaliar, não telemetria dos filtros.

Os **pesos** são os parâmetros numéricos aprendidos durante o treinamento. A identidade do modelo-base pode ser relevante para aproximar os sistemas comparados, mas o uso dos mesmos pesos entre o endpoint e o guardrail do WhatsApp **não foi demonstrado**. O produto pode usar outro classificador, regras externas ou uma versão/configuração diferente. O anúncio de Muse Spark no WhatsApp não identifica todos esses componentes.

Mesmo se os pesos fossem idênticos, instruções, contexto, ferramentas e verificações posteriores poderiam produzir decisões diferentes. Portanto, a validade da classificação comportamental não depende de assumir pesos compartilhados; essa hipótese adicional exigiria evidência da implantação para sustentar inferências sobre o guardrail.

## Podemos medir uma probabilidade?

É necessário especificar qual quantidade se deseja medir:

| Quantidade | O que representa | Situação neste estudo |
|---|---|---|
| Frequência observada | Quantas respostas tiveram uma classificação, sob condições definidas | Disponível: por exemplo, 3/5 em `Lula candidato 22` |
| Confiança declarada pelo modelo | Um número que o modelo escreve ao ser perguntado | Não é automaticamente calibrado nem uma probabilidade interna |
| Probabilidade de tokens (`logprobs`) | Probabilidade atribuída à continuação textual, condicionada ao pedido e ao prefixo | Não consta nas respostas preservadas; não é anunciada pelo endpoint consultado |
| Probabilidade de um filtro bloquear | Frequência ou pontuação de decisões do mecanismo de moderação | Não foi medida pela tarefa de classificação |

**3/5 não significa “o modelo tem 60% de certeza”; 5/5 não significa certeza absoluta.** São frequências de respostas relacionadas, com temperatura 0, no conjunto de condições usado. Não são uma amostra representativa de usuários nem uma medida de confiança calibrada.

Na consulta pública de capacidades realizada em 25 de outubro de 2026, o [endpoint do Muse Spark 1.1](https://openrouter.ai/api/v1/models/meta/muse-spark-1.1/endpoints) não listou `logprobs` nem `top_logprobs` entre os parâmetros suportados. A [fotografia dessa consulta](../results/analysis/probability-capability.json) preserva fonte, horário e parâmetros. Nenhuma das 240 respostas originais contém `logprobs` não nulos. Não foi feita uma chamada paga para testar um parâmetro não anunciado.

A [documentação do OpenRouter](https://openrouter.ai/docs/api_reference/parameters) define essas probabilidades como relativas aos tokens de saída. Mesmo com suporte, seria necessário definir rótulos, considerar sua tokenização e comparar alternativas sob o mesmo prefixo. Uma probabilidade de escrever um rótulo não seria automaticamente a probabilidade de ele estar correto ou de o WhatsApp recusar uma imagem. Uma alegação de confiança calibrada exigiria avaliação em um conjunto de referência separado.

Nesta análise, a medida publicada é a frequência observada, preservando suas condições e denominadores. A ausência de acesso às probabilidades internas não impede o teste comportamental; limita o que ele pode afirmar.

## Reprodução

```bash
python analyze_number_cues.py
```

O comando lê a rodada existente, verifica a correspondência dos registros com o plano e produz os 48 subgrupos. Não consulta o modelo, não altera as respostas originais e não implica custos de API. A consulta de capacidades é um registro separado, pois descreve o serviço no momento da inspeção e não comprova a identidade histórica de seu backend.
