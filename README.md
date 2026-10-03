# POD — Plataforma Orquestradora Durável

O POD é uma Plataforma Orquestradora Durável, soberana e multiprojeto. Recebe objetivos humanos e assume a complexidade técnica necessária até produzir resultados funcionais, integrados, seguros, recuperáveis, documentados e comprovados.

## Fonte canônica atual

A linha documental ativa desta Baseline é:

1. [`POD_DOCUMENTACAO_CONSOLIDADA_CANONICA.md`](POD_DOCUMENTACAO_CONSOLIDADA_CANONICA.md) — fonte arquitetural consolidada, versão 4.0.0-DRAFT-CANONICAL;
2. [`POD_BASELINE_CANONICA_AQUISICAO_EVOLUCAO_HIGIENE.md`](POD_BASELINE_CANONICA_AQUISICAO_EVOLUCAO_HIGIENE.md) — política canônica de aquisição, evolução e higiene;
3. [`ADR/`](ADR/) — decisões arquiteturais posteriores;
4. [`SCHEMAS/`](SCHEMAS/) e [`CONTRACTS/`](CONTRACTS/) — contratos formais e instanciados;
5. [`STANDARDS/`](STANDARDS/) — normas transversais especializadas;
6. [`RUNBOOKS/`](RUNBOOKS/), [`EVIDENCE/`](EVIDENCE/) e [`RELEASES/`](RELEASES/) — operação, prova e manifestos;
7. [`HISTORY/`](HISTORY/) — material histórico com `NORMATIVE=false`.

A síntese v3 anterior foi preservada em `HISTORY/POD_PROJETO_CONSOLIDADO_v3.0.md` e não compete com a Baseline ativa.

## GitHub nativo

Repositório canônico: `https://github.com/andrebarros78/pod`

O GitHub é o SCM nativo do POD para código, branches, pull requests, tags, releases, checks e trilha de integração. A soberania de missão pertence ao Governador do POD; GitHub não substitui estado operacional de missão nem autoridade de prova.

## Estratégia de evolução

A Baseline adota `REUSE FIRST`:

`PESQUISAR → ADQUIRIR QUANDO VANTAJOSO → SANITIZAR → NORMALIZAR → CONTEXTUALIZAR → VALIDAR → CONTRATUALIZAR → INTEGRAR → PROVAR → CONSTRUIR SOMENTE O DIFERENCIAL AUSENTE`

Componente existente não é componente qualificado; componente qualificado não é componente integrado; componente integrado não é capacidade provada.

## Estado da construção

- Fase 0 — `BASELINE_RECONCILED`: reconciliada documentalmente com a Baseline v4.
- Fase 1 — `CORE_CONTRACTS_DEFINED`: comprovada; contratos v1 e modelo formal preservados.
- Fase 2 — `MVP_PROVEN`: **não iniciada por ordem do Owner**.

O estado operacional persistente está em [`MISSION_STATE.json`](MISSION_STATE.json).

## Regra de prova

Código escrito, build verde, processo rodando, endpoint respondendo, componente instalado, agente registrado, commit criado ou painel verde não equivalem a conclusão comprovada.

## Validação local

```bash
python3 scripts/validate_governance.py
python3 scripts/validate_contracts.py
python3 scripts/validate_formal.py
python3 -m unittest discover -s tests -v
```
