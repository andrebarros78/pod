# POD — Plataforma Orquestradora Durável

O POD é um construtor soberano de software. Recebe um objetivo humano e assume a responsabilidade de entregá-lo construído, testado, recuperável e comprovado.

## Fonte normativa

A fonte normativa única desta linha de construção é:

- [`POD_PROJETO_CONSOLIDADO.md`](POD_PROJETO_CONSOLIDADO.md)

Decisões arquiteturais posteriores ficam em [`ADR/`](ADR/). O material documental anterior foi preservado em [`HISTORY/`](HISTORY/) com `NORMATIVE=false`.

## GitHub nativo

Repositório canônico: `https://github.com/andrebarros78/pod`

O GitHub é o SCM nativo do POD para código, branches, pull requests, tags, releases, checks e trilha de integração. A soberania de missão continua pertencendo ao Governador do POD; GitHub não substitui estado operacional de missão.

## Estado da construção

A construção segue a sequência definida em `POD_PROJETO_CONSOLIDADO.md`:

`BASELINE_RECONCILED → CORE_CONTRACTS_DEFINED → MVP_PROVEN → GOVERNOR_PROVEN → BRAIN_PROVEN → CROSS_PLATFORM_PROVEN → CONSTRUCTION_PROVEN → TERMINAL_PROVEN → PRODUCT_PROVEN → SEALED`

O estado operacional persistente desta missão está em [`MISSION_STATE.json`](MISSION_STATE.json).

## Regra de prova

Código escrito, build verde, processo rodando, endpoint respondendo ou commit criado não equivalem a prova final. Estados de prova só avançam pelos critérios definidos no documento normativo.

## Validação da governança

```bash
python3 scripts/validate_governance.py
python3 -m unittest discover -s tests -v
```
