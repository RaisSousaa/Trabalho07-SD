# Roteiro de gravação

Duração aproximada de cinco minutos. Use as falas como apoio e faça pequenas pausas ao apontar as curvas. O roteiro explica as tendências sem exigir a leitura dos números.

## Slide 1 — Objetivo do estudo (15 s)

Olá, meu nome é Rais Eliete de Sousa, da Universidade Federal do Piauí. Neste trabalho, analisei como a quantidade de máquinas virtuais influencia o atendimento de tarefas em nuvem. A ideia foi entender quando o sistema começa a ficar sobrecarregado e como a ampliação dos recursos pode melhorar seu desempenho.

## Slide 2 — Arquitetura do serviço (25 s)

Esta figura mostra o caminho das tarefas. Os dispositivos enviam solicitações para o sistema, que verifica se existe espaço na fila. Quando uma máquina virtual fica livre, ela recebe uma tarefa para processar. Depois da conclusão, pode atender a próxima. Se a fila estiver cheia, o sistema descarta a nova solicitação. Por isso, precisamos observar tanto a espera quanto as tarefas que deixam de ser atendidas.

## Slide 3 — Modelo SPN (35 s)

Para estudar esse funcionamento, representei o sistema por meio de uma Rede de Petri Estocástica, que aparece nesta figura. Podemos acompanhar o caminho da esquerda para a direita, desde a chegada até a conclusão das tarefas. O modelo também controla as vagas na fila e as máquinas disponíveis. Assim, a simulação permite observar o que acontece quando chegam mais solicitações ou quando aumentamos a capacidade de atendimento.

## Slide 4 — Planejamento experimental (30 s)

Nos experimentos, alterei a demanda, a quantidade de máquinas e o espaço disponível na fila. Também avaliei situações em que a demanda e os recursos aumentavam juntos. Para comparar os efeitos de cada mudança, mantive as demais condições iguais. Observei principalmente a rapidez do atendimento, a ocupação das máquinas e o descarte de tarefas. A seguir, os gráficos mostram como o sistema reagiu a essas mudanças.

## Slide 5 — Utilização das VMs (25 s)

Neste gráfico, cada linha representa uma quantidade diferente de máquinas virtuais. Conforme a demanda aumenta, as máquinas passam mais tempo ocupadas. Nas configurações menores, essa ocupação se aproxima do limite mais cedo. Com mais máquinas, o trabalho se distribui entre mais recursos, deixando uma margem maior para receber novas tarefas. Portanto, a utilização ajuda a identificar quando o sistema está ficando sobrecarregado.

## Slide 6 — Demanda e capacidade (35 s)

Aqui vemos o tempo total que uma tarefa admitida permanece no sistema, desde a entrada até a conclusão. As curvas mostram que esse tempo aumenta com a demanda, principalmente quando há poucas máquinas disponíveis. Ao acrescentar máquinas, o tempo de resposta diminui, porque as tarefas conseguem iniciar o processamento mais rapidamente. Nas configurações com maior capacidade, a resposta permanece mais próxima do tempo necessário para executar a tarefa.

## Slide 7 — Tempo médio de espera (20 s)

Este gráfico mostra apenas o tempo que as tarefas passam esperando na fila. A espera cresce mais rapidamente nas configurações com menos máquinas. Quando ampliamos os recursos, ela diminui. Isso ajuda a explicar o gráfico anterior, pois grande parte do aumento no tempo de resposta vem da espera para começar o processamento.

## Slide 8 — Saturação e descarte (30 s)

Neste gráfico, observamos o descarte de tarefas. Quando a demanda cresce e as máquinas já estão muito ocupadas, a fila enche com mais frequência. Com isso, o sistema rejeita mais solicitações. As configurações com mais máquinas apresentam menos descarte para a mesma demanda. Esse resultado mostra por que precisamos analisar o descarte junto com o tempo de resposta, já que a resposta considera somente as tarefas que entraram no sistema.

## Slide 9 — Capacidade da fila (25 s)

Agora, a mudança ocorre no tamanho da fila. O gráfico mostra que uma fila maior reduz o descarte, porque permite acomodar mais tarefas enquanto elas aguardam atendimento. Porém, admitir mais tarefas também pode aumentar um pouco o tempo de espera e de resposta. Portanto, ampliar a fila ajuda a evitar rejeições, mas a velocidade de processamento continua dependendo das máquinas disponíveis.

## Slide 10 — Cenários combinados (25 s)

Neste experimento, aumentei a demanda e a quantidade de máquinas ao mesmo tempo. Mesmo recebendo mais tarefas, o sistema apresentou menor tempo de resposta à medida que o conjunto de máquinas cresceu. Ainda assim, as máquinas continuaram bastante ocupadas e houve descarte. Isso mostra que acompanhar o crescimento da demanda com mais recursos melhora o atendimento, mas exige atenção à margem de capacidade disponível.

## Slide 11 — Conclusão (35 s)

Os resultados mostram que a quantidade de máquinas deve acompanhar a demanda esperada. Para a situação de referência, a configuração intermediária apresentou um equilíbrio entre rapidez de atendimento e uso dos recursos. Também vimos que ampliar a fila reduz o descarte, enquanto acrescentar máquinas ajuda a diminuir a espera. Essas conclusões valem para as condições simuladas. Como continuidade, seria interessante comparar o modelo com uma aplicação real e avaliar os custos das configurações. Obrigada.