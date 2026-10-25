# Procedência dos dados e escolha da via de acesso

> Apêndice de conferência. A leitura principal está no [estudo completo](../README.md).

## Evidência exploratória anterior

A investigação começou com uma rodada exploratória preservada no commit `a54a7b6`: notebook com saídas, CSV, resposta a um prompt forense e figuras. A data de autoria do commit é `2026-10-25T04:18:38Z` (01h18 de Brasília). Essa é uma data do histórico de versionamento; os arquivos antigos não permitem fixar o horário de cada chamada à API.

O [CSV original](../results/run1_classification.csv) contém 24 registros: 20 classificações válidas e quatro ausentes. Nas oito respostas que identificaram Flavio Bolsonaro, o modelo o classificou como político, mas não como candidato presidencial ou chefe de Estado, e não previu acionamento de uma restrição hipotética de imagens.

Esses campos eram respostas textuais. Não eram registros de decisões internas de moderação nem resultados de geração de imagens. As instruções incluíam o relato da assimetria no WhatsApp, o que pode ter influenciado as respostas. O [prompt forense](../results/forensic_prompt.txt) e sua [resposta](../results/run1_forensic_answer.json) também contêm hipóteses, não observações da arquitetura da Meta.

O experimento fatorial antigo deixou saídas parciais e figuras, mas não todos os registros necessários para recomputar seus resultados. O [notebook original](../notebook/archive/original_exploratory.ipynb) permanece arquivado como evidência histórica, com suas limitações de execução e interpretação.

## Rodada controlada

A rodada v2 ocorreu em 25 de outubro de 2026, entre 07h35 e 07h37 UTC (04h35–04h37 de Brasília). Foram obtidas 240 respostas válidas. O plano fixou as condições antes da coleta, balanceou as variações e retirou das instruções o relato do resultado esperado. Dois pilotos técnicos foram excluídos da rodada principal.

A v2 mede reconhecimento de nomes e papéis políticos. A rodada anterior pedia também previsões sobre restrições. São etapas distintas: seus resultados não são somados como se medissem o mesmo desfecho.

Os [registros da v2](../results/v2_run1/) preservam o plano, respostas, metadados e fonte do coletor. Veja o [protocolo](methodology.md) e a [explicação do desenho e de sua robustez](../README.md).

## Por que usar OpenRouter após os ajustes no WhatsApp

As [reportagens consultadas](media-context.md) registram mudanças no comportamento do WhatsApp em 14 de outubro. A [Meta também declarou](meta-explanation.md) ter corrigido nesse dia uma lacuna de reconhecimento de primeiros nomes comuns combinados com números eleitorais.

A escolha do OpenRouter permite investigar reconhecimento por outra via, sem depender exclusivamente do comportamento posterior do WhatsApp. A hipótese de trabalho é que esse acesso não reproduza necessariamente os ajustes específicos do produto. Essa diferença de implantação é parte da motivação metodológica.

O OpenRouter não foi validado como controle sem intervenção nem como preservação do estado anterior. Ele e o provedor podem aplicar filtros; modelos, versões e instruções podem diferir. Mesmo compartilhar um modelo-base não garantiria compartilhar as mesmas proteções.

## Relação entre as evidências

Os relatos jornalísticos documentam saídas no produto; a Meta apresenta uma explicação para o incidente; o experimento registra respostas de reconhecimento por API. O estudo demonstra sensibilidade à forma do nome na tarefa definida, mas não identifica sozinho a causa interna do episódio no WhatsApp.

A diferença de resultados não basta para identificar intenção política. Uma explicação alternativa plausível também não basta para excluir toda intencionalidade. A análise mantém separadas observação, explicação do operador e hipótese técnica.
