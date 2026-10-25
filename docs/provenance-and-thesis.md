# Registro da investigação anterior e da tese

Registro atualizado em 25 de outubro de 2026, após esclarecimento de Pedro Del Nero Todescan.

## A investigação não começou com a rodada revisada

Pedro esclareceu que já havia executado o código e reunido evidências antes da rodada revisada realizada nesta sessão. Isso é consistente com os artefatos que já estavam no repositório no início do trabalho: notebook com saídas, CSV do primeiro experimento, resposta ao prompt forense e figuras.

O histórico local registra o commit `a54a7b6` com data de autoria `2026-10-25T04:18:38Z` (01h18 de Brasília), contendo esses arquivos. Essa é uma data de commit, não um comprovante do momento de cada chamada à API. Os dados antigos não preservam os metadados necessários para fixar o horário original de execução. Não atribuímos ao experimento anterior uma data anterior às notícias de 13–15 de outubro sem documentação adicional.

As evidências anteriores incluem:

- **Primeiro experimento:** 24 registros, 20 previsões válidas e 4 ausentes, preservados em `results/run1_classification.csv`.
- **Distinção relevante já presente:** nas 8 respostas que resolveram a identidade como Flavio Bolsonaro, o modelo o classificou como figura política nas 8, mas previu acionamento da política de imagens em nenhuma. Reconhecimento de uma figura política e previsão de restrição eram campos diferentes. A previsão continuava sendo uma resposta textual do modelo, não a observação de um filtro real.
- **Análise forense:** resposta e prompt preservados, com hipóteses sobre reconhecimento de entidades e camadas de moderação. São hipóteses produzidas pelo modelo; não constituem acesso à arquitetura da Meta.
- **Experimento fatorial antigo:** existem saídas parciais e uma figura, mas faltam os registros completos para recomputar seus resultados.

Essas limitações afetam a força das conclusões; não eliminam a existência de evidência exploratória anterior. A rodada v2 não deve ser apresentada como a primeira investigação de Pedro.

A rodada revisada v2 foi executada em 25 de outubro, de 04h35 a 04h37 de Brasília, com 240 respostas válidas. Ela retirou o relato do resultado esperado das instruções, balanceou as condições e passou a medir reconhecimento de nomes. Não é uma repetição idêntica do primeiro experimento nem uma reprodução do WhatsApp.

## Por que o OpenRouter é a base do método

Pedro esclareceu que a escolha do OpenRouter é deliberada: após as reclamações, o WhatsApp poderia já estar aplicando guardrails modificados. Consultar apenas o WhatsApp nesse estado posterior poderia revelar a reação da plataforma, sem esclarecer o comportamento que motivou a investigação. Por isso, ele usa outra via de acesso para investigar hipóteses sobre o reconhecimento de nomes e sua relação com as respostas.

As reportagens citadas em `media-context.md` registram que a Meta anunciou medidas adicionais e que os testes no WhatsApp mudaram em 14 de outubro. Isso dá fundamento à preocupação com mudanças posteriores às reclamações. A suposição adicional do método é que o acesso via OpenRouter não reproduza necessariamente esses ajustes específicos do produto; essa separação não foi confirmada tecnicamente.

Assim, diferenças entre os caminhos de acesso são parte da motivação do experimento, não apenas uma ressalva acrescentada ao resultado. O teste oferece uma investigação por outra via de um mecanismo possível. Não é um grupo de controle validado nem uma reconstrução do WhatsApp anterior: o OpenRouter também pode aplicar filtros, e não há comprovação de que modelo, versão e instruções tenham permanecido iguais entre produtos e datas.

## Formulação da tese

**É tecnicamente plausível que o caminho usado pelo WhatsApp para chamar seus modelos aplique guardrails diferentes dos aplicados no acesso via OpenRouter.** As diferenças podem estar no próprio modelo, nas instruções de sistema, no tratamento do pedido, em filtros do produto, na geração de imagens ou em verificações posteriores. São possibilidades, não uma descrição confirmada da implementação.

Mesmo que dois produtos utilizassem o mesmo modelo-base, isso não garantiria o mesmo conjunto de instruções, políticas, ferramentas ou filtros. Neste caso, tampouco verificamos independentemente que o modelo/versão exposto no OpenRouter seja idêntico ao usado pelo WhatsApp para todas as etapas da geração de imagens.

Essa tese tem duas consequências:

1. Uma diferença de saída no WhatsApp não identifica, sozinha, a camada responsável nem demonstra favorecimento deliberado. Conclusões que apresentem essas causas como estabelecidas ultrapassam a evidência descrita.
2. Uma resposta obtida no OpenRouter não permite atribuir automaticamente o mesmo comportamento aos filtros do WhatsApp. Nosso experimento oferece evidência sobre uma hipótese alternativa, mas não determina o mecanismo do incidente no produto.

Não é necessário provar uma arquitetura alternativa para mostrar que a causa está indeterminada. Para afirmar que aquela arquitetura alternativa efetivamente causou o episódio, seriam necessários testes comparáveis ou evidências adicionais da implementação.

## O argumento que pode ser sustentado

0659>
> A diferença observada no WhatsApp merece investigação. O que considero precipitado é tratá-la, por si só, como prova da 9causa, da intenção da empresa ou de uma preferência política do modelo. Reconhecimento de nomes e regras específicas do produto são explicações alternativas que precisam ser examinadas.
>
> A rodada revisada acrescentou evidência: com nomes completos, Lula e Flávio Bolsonaro foram classificados como políticos em 30 de 30 respostas cada; a diferença apareceu nos nomes curtos. Isso é compatível com ambiguidade de identificação nesse teste. Não comprova o que ocorreu dentro do WhatsApp.
>
> Uma falha técnica pode produzir efeitos políticos desiguais e exigir correção. A cobrança pela falha e o cuidado ao atribuir sua causa são compatíveis.

A crítica deve se dirigir às conclusões específicas que excedem a evidência, não à totalidade da cobertura. Relatar uma inconsistência reproduzida não é, em si, uma conclusão precipitada; “viés” também pode descrever efeitos desiguais sem afirmar intenção. Acusações relativas a alcance, anúncios ou distribuição de conteúdo permanecem fora do escopo do nosso teste.

## Fontes do registro

- Relato de Pedro nesta conversa e existência dos artefatos no checkout antes da rodada v2.
- [CSV anterior](../results/run1_classification.csv) e [notebook original arquivado](../notebook/archive/original_exploratory.ipynb).
- [Resposta forense anterior](../results/run1_forensic_answer.json).
- [Registros completos da rodada revisada](../results/v2_run1/).
- [Notícias e postagens consultadas, com atribuição das alegações](media-context.md).

## Conversa anterior e fonte primária recuperadas

Em seguida, Pedro forneceu a [conversa compartilhada](https://chatgpt.com/share/6addbdfb-817c-83e9-9f47-ee280e844d1e), com perguntas suas de 16–17 de outubro sobre as explicações técnicas para as alegações e sobre os registros de incidentes. Isso documenta que a discussão técnica antecedia a revisão de 25 de outubro. A referência do assistente naquela conversa a um experimento anterior não substitui metadados de execução do código.

O link permitiu localizar e ler diretamente um comunicado da Meta que atribui o caso de imagens a lacunas de reconhecimento de primeiros nomes e números eleitorais e declara um ajuste em 14 de outubro. A direção geral da tese agora conta com essa explicação primária, além dos resultados do experimento; a arquitetura detalhada e a hipótese específica de senador versus candidato continuam não verificadas. Veja [fonte, atribuições e esquema](meta-explanation.md).
