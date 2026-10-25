# Reconhecimento de nomes políticos e proteções em IA

Estudo independente sobre como a forma de um nome altera sua identificação por um modelo de linguagem. O objetivo é explicar um mecanismo capaz de produzir respostas desiguais e distinguir o resultado observado das conclusões sobre sua causa ou intenção política.

**Na rodada controlada, os nomes completos de Lula e Flávio Bolsonaro foram classificados como políticos em 30 de 30 respostas cada. A diferença apareceu nos nomes curtos.** A coleta usou a API do OpenRouter e não mediu geração ou recusa de imagens no WhatsApp.

## Entenda o teste em um minuto

![Exemplos reais de variações, pergunta ao Muse e respostas](figures/guide/como-testamos.png)

**[Guia visual: o que perguntamos, as respostas e por que usamos outra via](docs/guia-visual.md).** Inclui a cronologia do ajuste no WhatsApp, a fonte oficial sobre Muse Spark e a diferença entre reaproveitar um texto e enviar uma instrução idêntica.

## Comece por aqui

- **[Estudo explicado](docs/estudo-explicado.md):** LLMs e similaridade, possíveis etapas de guardrail, escolha do OpenRouter, método, resultados e em que sentido o desenho é robusto.
- [Resumo para leitores não técnicos](docs/assessment.md).
- [Explicação declarada pela Meta e seu esquema](docs/meta-explanation.md).
- [Hipótese de reconhecer um político sem acionar uma restrição](docs/esquema-mecanismo.md).
- [Notícias e alegações públicas](docs/media-context.md), [procedência dos dados](docs/provenance-and-thesis.md) e [protocolo técnico](docs/methodology.md).

## A ideia em um esquema

Uma proteção pode depender de reconhecer a pessoa e associá-la à categoria coberta pela regra. As etapas abaixo são uma ilustração funcional, não uma descrição verificada da arquitetura da Meta.

```mermaid
flowchart LR
    A[Pedido] --> B[Reconhecimento da pessoa]
    B --> C[Categoria relevante]
    C --> D[Aplicação da regra]
    D --> E[Gerar ou recusar]
```

Em texto: **pedido → reconhecimento → categoria → regra → resposta**. O produto pode acrescentar instruções, filtros de entrada e verificações da imagem gerada. Uma falha de reconhecimento pode mudar a aplicação de uma regra uniforme.

O acesso pelo OpenRouter provavelmente não usa exatamente os mesmos guardrails do WhatsApp. Essa diferença é a motivação para investigar por outra via após os ajustes relatados no produto. A Meta anunciou Muse Spark no WhatsApp, mas não foram verificadas versões ou proteções idênticas nos dois acessos, nem que a API preserve o estado anterior do produto. Veja a [fonte oficial e a cronologia ilustrada](docs/guia-visual.md#por-que-testar-o-muse-pelo-openrouter).

A [Meta declarou](docs/meta-explanation.md) que algumas combinações de primeiro nome comum e número eleitoral escapavam às proteções, inclusive com “Flávio” e “Luiz”, e que corrigiu a lacuna em 14 de outubro. O comunicado é uma fonte primária sobre a explicação da empresa; o experimento não auditou seus registros internos.

## Desenho e resultados

O plano cruzou quatro grupos de nomes, duas formas por nome, três condições numéricas e duas condições de papel, com cinco repetições: **240 pedidos**. As mesmas variações foram aplicadas a todos os grupos, em ordem embaralhada e sem histórico de conversa. As instruções pediam identificação, não geração de imagem ou previsão de moderação.

| Nome fornecido | Classificado como político | Identidade indefinida |
|---|---:|---:|
| Lula | 28/30 | 2/30 |
| Luiz Inacio Lula da Silva | 30/30 | 0/30 |
| Flavio | 0/30 | 30/30 |
| Flavio Bolsonaro | 30/30 | 0/30 |
| Controles, todas as formas | 0/120 | 118/120 |

As grafias reproduzem os pedidos coletados. Cada nome tem seis combinações de número e papel, repetidas cinco vezes. “Flavio” indefinido não significa Flávio Bolsonaro identificado como não político. As instruções orientavam a não inferir identidade única apenas de um primeiro nome, número ou da palavra `candidato`; os resultados são condicionais a essa formulação.

Foram concluídos 240/240 casos, todos válidos, sem falhas ou novas tentativas técnicas. A rodada principal custou aproximadamente US$ 0,50 segundo a API. Dois pilotos técnicos, excluídos da análise, custaram aproximadamente US$ 0,007 no total.

![Contagens de classificação política na API](results/v2_run1/political_flags.png)

[Plano e respostas completas](results/v2_run1/) · [Resumo calculado](results/v2_run1/summary.json) · [Notebook](notebook/muse_political_entity_test.ipynb)

## Por que a comparação é robusta — e até onde

O desenho permite conferir a comparação porque fixa o plano antes da coleta, aplica condições equivalentes, repete cada combinação, preserva todas as respostas e trata falhas separadamente de classificações negativas. Os 60 pares Lula–Flavio comparáveis estão completos. O código permite recalcular contagens e verificar os registros.

Essa robustez é **da medição de reconhecimento nesta tarefa**. As cinco repetições não são uma amostra de usuários independentes; uma sessão, um modelo e uma formulação não demonstram estabilidade entre produtos ou datas. Validade do formato não garante verdade factual. O estudo não mede intenção, alcance de publicações, anúncios ou funcionamento dos guardrails do WhatsApp.

A [explicação completa](docs/estudo-explicado.md#7-em-que-sentido-o-desenho-é-robusto) relaciona cada controle ao problema que ele reduz e ao limite que permanece. A [validação](docs/validation.md) documenta as conferências técnicas.

## Evidência exploratória preservada

A investigação anterior produziu 24 registros, dos quais 20 tinham classificações válidas e quatro estavam ausentes. Houve oito previsões positivas de restrição e 12 negativas: 8/20, ou 40%, entre respostas válidas. Essas previsões textuais não eram recusas reais de imagens. As instruções incluíam o relato do resultado esperado, podendo influenciar as respostas.

A rodada v2 retira esse enquadramento e mede outro desfecho. As etapas são mantidas separadas. Os registros completos do fatorial antigo não estão disponíveis; suas taxas não podem ser recalculadas independentemente. As figuras antigas em `figures/` são artefatos históricos e não devem ser lidas como medições verificadas do produto.

- [CSV original](results/run1_classification.csv).
- [Prompt forense](results/forensic_prompt.txt) e [hipóteses produzidas pelo modelo](results/run1_forensic_answer.json).
- [Notebook exploratório arquivado](notebook/archive/original_exploratory.ipynb), com saídas e limitações originais.

## Reproduzir a análise

Ambiente testado com Python 3.12. As dependências diretas têm versões fixadas; não há um arquivo de resolução completa das dependências transitivas.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python report_run.py results/v2_run1
jupyter notebook notebook/muse_political_entity_test.ipynb
```

O notebook usa os registros preservados e executa offline, sem chamadas pagas. Para analisar outra rodada, defina `MUSE_RUN_DIR` com o caminho dos registros antes de iniciá-lo. Recalcular os resultados preservados não garante que uma futura API produza respostas idênticas.

### Nova coleta pela API

Configure `OPENROUTER_API_KEY` como variável de ambiente, sem incluir a chave em arquivos publicados. Confira disponibilidade do modelo e preços antes da coleta.

```bash
# O diretório deve ser novo. Cada tentativa técnica também consome o limite.
python experiment.py collect --plan results/v2_plan.json --out results/runs/v2-001 --max-calls 240 --workers 4
python experiment.py summarize results/runs/v2-001
```

O coletor interrompe novos pedidos em falhas de autenticação, separa tipos de falha e não sobrescreve diretórios de resultados. Novas tentativas técnicas não são repetições experimentais adicionais. Mudanças de instruções ou configurações exigem um novo plano identificado; pilotos não são misturados com a rodada principal.

## Organização

| Arquivo ou diretório | Conteúdo |
|---|---|
| `docs/` | Explicações, fontes, metodologia e validação |
| `experiment.py` | Plano, coleta, validação e resumos |
| `report_run.py` | Resumo e gráfico reproduzíveis |
| `render_guide.py` | Figuras didáticas e exemplos extraídos dos registros |
| `results/v2_plan.json` | Plano fixado e hashes dos prompts |
| `results/v2_run1/` | Evidência da rodada controlada e código da coleta |
| `notebook/` | Análise offline e arquivo histórico |
| `tests/` | Verificação de balanceamento, falhas, pareamento e coleta |

Autoria do experimento original: Pedro Del Nero Todescan, outubro de 2026. Projeto independente da Meta e do OpenRouter.
