# Avaliação de desempenho e dimensionamento de máquinas virtuais em nuvem

Trabalho 07 sobre Redes de Petri Estocásticas (SPNs), desenvolvido por **Rais Eliete de Sousa**, da **Universidade Federal do Piauí**, em Picos-PI, Brasil.

Contato: rais.sousa@ufpi.edu.br

## Objetivo

Avaliar como a demanda, a quantidade de máquinas virtuais e a capacidade da fila afetam o desempenho de um serviço em nuvem. O estudo utiliza um modelo SPN no Jupiter Analytics e considera vazão, tempo médio de resposta, tempo médio de espera, utilização das VMs e probabilidade de descarte.

## Apresentação em vídeo

[Assistir à apresentação no Google Drive](https://drive.google.com/file/d/1r0zUEZ-HTNkOxSzZm_K4DD1HS4JBRgOu/view?usp=sharing)

## Arquivos do projeto

| Caminho | Conteúdo |
| --- | --- |
| [nuvem-vms-jupiter.json](nuvem-vms-jupiter.json) | Modelo SPN com os parâmetros e marcações iniciais ajustados para o cenário de referência do artigo. |
| [artigo/artigo-organizado.tex](artigo/artigo-organizado.tex) | Fonte LaTeX do artigo em formato IEEE. |
| [artigo/referencias.bib](artigo/referencias.bib) | Referências bibliográficas. |
| [artigo/figuras/](artigo/figuras/) | Figuras utilizadas no artigo. |
| [resultados/resultados-jupiter.csv](resultados/resultados-jupiter.csv) | Resultados consolidados dos experimentos E1 a E4. |
| [resultados/comparativo/](resultados/comparativo/) | Resultados da comparação entre configurações de VMs. |
| [resultados/comparativo/proveniencia.txt](resultados/comparativo/proveniencia.txt) | Origem dos dados e identificação do ponto transcrito da interface. |
| [configuracoes/](configuracoes/) | Parâmetros de todos os cenários e configuração de execução preparada para reprodução. |
| [resultados/configuracoes/](resultados/configuracoes/) | Exportações originais das configurações, preservadas como registro das rodadas. |
| [gerar_graficos.py](gerar_graficos.py) | Script para gerar os gráficos a partir dos arquivos CSV. |
| [output/pdf/](output/pdf/) | Gráficos exportados em PDF, incluindo versões separadas e agrupadas. |
| [output/apresentacao/trabalho07-slides-roteiro-simplificado.pptx](output/apresentacao/trabalho07-slides-roteiro-simplificado.pptx) | Slides com os seis gráficos e notas para apresentação. |
| [output/apresentacao/roteiro-gravacao-simplificado.md](output/apresentacao/roteiro-gravacao-simplificado.md) | Roteiro explicativo para gravação do vídeo. |

## Funcionamento do modelo

As tarefas chegam ao sistema e passam por uma decisão de admissão. Quando existe espaço, entram em uma fila compartilhada e aguardam uma VM disponível. Cada VM executa uma tarefa por vez. Após a conclusão, a tarefa deixa o sistema e a VM fica livre para um novo atendimento. Quando a fila está cheia, a nova tarefa é descartada.

O modelo considera VMs idênticas, chegadas de Poisson e tempos de serviço exponenciais. A transição de conclusão utiliza a política *Infinite Server*, com o paralelismo limitado pela quantidade de marcas que representam as VMs disponíveis.

## Cenário de referência

| Parâmetro no Jupiter | Significado | Valor utilizado no artigo |
| --- | --- | --- |
| `TAXA_CHEGADA` | Taxa média de chegada | 20 tarefas/s |
| `TEMPO_SERVICO` | Tempo médio de serviço por tarefa | 0,1 s |
| `NUM_VMS` | Quantidade de máquinas virtuais | 3 |
| `CAP_FILA` | Quantidade de posições de espera | 20 |

A capacidade da fila contabiliza apenas tarefas em espera. As tarefas em processamento ocupam as VMs.

## Experimentos

Em cada experimento, os parâmetros não indicados na tabela permanecem nos valores de referência.

| Experimento | Parâmetros avaliados |
| --- | --- |
| E1 — Demanda | Taxas de chegada de 10, 20, 30, 40 e 50 tarefas/s. |
| E2 — Quantidade de VMs | Configurações com 2, 3 e 4 VMs. |
| E3 — Capacidade da fila | Filas com 10, 20 e 30 vagas. |
| E4 — Demanda e recursos combinados | Pares de chegada e VMs: (20, 2), (30, 3) e (40, 4). |
| Comparação complementar | Configurações de 2 a 6 VMs, cada uma sob taxas de chegada de 10 a 50 tarefas/s, em passos de 10. |

As métricas são `TP` (vazão, tarefas/s), `MRT` (resposta, s), `MQT` (espera, s), `U` (utilização, %) e `DP` (descarte, %).

## Como repetir as avaliações

1. Abra o Jupiter Analytics e importe o arquivo `nuvem-vms-jupiter.json`.
2. Confira as definições do modelo. O arquivo disponibilizado já contém os valores do cenário de referência apresentados acima.
3. Confira as marcações iniciais dos lugares `VagasFila` e `VMsLivres`, que devem acompanhar `CAP_FILA` e `NUM_VMS`. Os lugares de tarefas começam vazios.
4. Use `configuracoes/execucao-referencia.json` como referência para configurar a simulação estacionária: horizonte de 10.000 s, aquecimento de 1.000 s, confiança de 95%, erro relativo máximo de 5% e limite de 20 milhões de eventos. Se a ferramenta permitir importar configurações de execução, importe esse JSON. Caso contrário, preencha as opções na interface.
5. Execute os cenários listados em `configuracoes/cenarios.csv`, ajustando as definições do modelo e mantendo fixos os demais parâmetros. O arquivo lista a referência, os experimentos E1 a E4 e a comparação complementar.
6. Exporte os resultados e identifique cada cenário pelos parâmetros utilizados.

**Conferência das configurações:** os JSONs de execução preservados incluem ajustes de rodadas anteriores. Por exemplo, `config-execucao-E4_1.json` registra aquecimento nulo e limite de 200 mil eventos. Esses arquivos não documentam, por si só, todos os ajustes finais descritos no artigo. O arquivo `configuracoes/execucao-referencia.json` foi preparado para novas execuções conforme o método do artigo. Ele não substitui os registros originais nem comprova retrospectivamente os ajustes de cada rodada. Confira as opções na interface antes de executar e preserve os novos resultados e suas configurações.

No ponto de 40 tarefas/s com 6 VMs, o estudo ampliou o limite de tempo computacional para 300 s após uma interrupção. A origem e a precisão dos valores desse ponto estão descritas em `resultados/comparativo/proveniencia.txt`.

## Como gerar os gráficos

É necessário ter Python 3 e Matplotlib instalados. Na pasta do projeto, execute:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 gerar_graficos.py
```

O script lê os dados existentes em `resultados/` e grava as figuras em `output/pdf/`. Ele gera os gráficos de capacidade da fila e cenários combinados, além da comparação de utilização, resposta, descarte e espera. Os quatro gráficos comparativos individuais ficam em `output/pdf/comparativo-separados/`.

Esse procedimento gera figuras a partir dos resultados salvos. Para obter novas estimativas, execute o modelo no Jupiter.

## Artigo

Para compilar no Overleaf, envie o conteúdo da pasta `artigo/`, preservando a subpasta `figuras/`, e selecione `artigo-organizado.tex` como documento principal. O projeto inclui a classe `IEEEtran.cls` e utiliza BibTeX com o arquivo `referencias.bib`.

O artigo deve respeitar o limite de seis páginas, incluindo as referências. Após a publicação do repositório, insira seu endereço no artigo e confira os links do vídeo e dos materiais.

## Publicação do repositório

Envie os arquivos desta pasta, incluindo o README, as configurações, os dados e os materiais finais. O `.gitignore` exclui ambientes locais e arquivos temporários. A pasta não precisa incluir credenciais nem arquivos internos das ferramentas de edição.

O PDF final de entrega deve ser exportado do Overleaf após recompilar o artigo. Publique esse PDF em `artigo/` quando estiver atualizado. O endereço do repositório só pode ser incluído no artigo depois de sua criação no GitHub.

## Interpretação dos resultados

O aumento da demanda eleva a ocupação das VMs e pode ampliar a espera e o descarte. Acrescentar VMs reduz a disputa pelo processamento. Uma fila maior reduz a rejeição por falta de espaço, mas pode aumentar o tempo de permanência das tarefas admitidas.

Os resultados apresentados são estimativas pontuais. Os dados usados nos gráficos não incluem os limites dos intervalos de confiança, portanto diferenças pequenas entre configurações exigem cautela. As conclusões se restringem às hipóteses do modelo e não representam medições de uma aplicação real.
