# O estudo em linguagem simples

Um sistema pode aplicar a mesma regra de forma desigual porque não reconheceu corretamente a pessoa mencionada. É como uma recepção que identifica alguém pelo nome completo, mas não consegue saber quem é quando recebe apenas um primeiro nome. Nos sistemas de IA, essa interpretação pode influenciar quais proteções entram em ação.

O estudo fez 240 pedidos pela API do OpenRouter para observar reconhecimento de nomes, com as mesmas variações de número e palavra de papel para cada grupo. Todos retornaram respostas utilizáveis. A coleta não gerou imagens no WhatsApp.

| Nome fornecido | Classificado como político | Identidade indefinida |
|---|---:|---:|
| Lula | 28/30 | 2/30 |
| Luiz Inacio Lula da Silva | 30/30 | 0/30 |
| Flavio | 0/30 | 30/30 |
| Flavio Bolsonaro | 30/30 | 0/30 |

A diferença apareceu nos nomes curtos. Com os nomes completos, os dois receberam classificação política em todas as respostas. “Flavio” sem identidade definida não significa que o sistema tenha identificado Flávio Bolsonaro e decidido que ele não é político.

O desenho fortalece essa comparação porque usa condições equivalentes, ordem embaralhada, cinco repetições por condição e registros completos. Falhas técnicas são separadas das respostas negativas. Isso torna o resultado controlado e verificável dentro da tarefa. Não transforma uma sessão com um modelo em uma pesquisa representativa de todos os usuários, nem revela os filtros internos do WhatsApp.

O OpenRouter foi escolhido para investigar o reconhecimento por outra via após os ajustes relatados no WhatsApp. Os caminhos podem aplicar instruções e proteções diferentes; a API não foi validada como uma cópia do produto antes dos ajustes.

A própria [Meta atribuiu o episódio](meta-explanation.md) a lacunas no reconhecimento de primeiro nome comum com número eleitoral. Essa explicação é compatível com o tipo de sensibilidade observado, mas continua sendo a declaração do operador, sem auditoria independente dos registros internos.

A contribuição do estudo é mostrar concretamente por que uma diferença visível não identifica sua causa automaticamente. A inconsistência merece investigação; afirmar intenção exige evidência adicional. O mesmo critério vale para qualquer partido ou candidato.

Leia a [explicação completa: LLMs, similaridade, etapas possíveis de proteção e robustez](estudo-explicado.md). Os [dados e o plano](../results/v2_run1/) permitem conferir os resultados.
