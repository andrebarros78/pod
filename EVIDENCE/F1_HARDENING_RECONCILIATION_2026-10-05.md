# EVIDENCE — F1 HARDENING RECONCILIATION — 05/10/2026

**Status:** PROVEN

## Objetivo

Comprovar a reconciliação entre documentação e contratos F1 para Privacy/Sensitive Data, `MISSION_PROVEN`, lease/fencing, ADE, Execution Fabric, Capability Engine e raiz canônica.

## Linhagem

- candidato inicial: `f65a2b34cfbc8ca427fd4943f8b676de2e5b80ee`;
- concorrência preservada: `2d4ccddff3c59c257424f365af38b376d24b4687`;
- commit convergente: `180d98575ed9effe7b192a9285c2ef8a7d553863`;
- pais do convergente: `2d4ccdd` e `f65a2b34`.

Nenhuma alteração concorrente foi sobrescrita por force-push.

## Provas GitHub Actions

### Candidato inicial

Run `37344078596`: SUCCESS.

### Commit convergente na branch

Run `37345339206`: SUCCESS.

### Mesmo commit na raiz canônica `main`

Run `37345457823`: SUCCESS.

## Resultados observados

```text
POD_GOVERNANCE_VALID
POD_CONTRACTS_VALID
POD_CAPABILITY_ACQUISITION_VALID
sources=19
github_pinned=14
marketplace_pinned=5
donor_runtime_coupling=0
external_sources_verified=not_requested
POD_FORMAL_VALID
TLC model checking completed: no error
3,735,315 states generated
755,806 distinct states found
0 states left on queue
depth=26
20/20 unit/regression tests PASS
```

## Limite explícito da prova

Os bytes das 19 fontes externas não foram refetchados no runner desta reconciliação. A prova física anterior está preservada em `HISTORY/CAPABILITY_ACQUISITION_V001_LEGACY_PROOF.md`; no CI atual foram revalidados manifesto, estrutura, contratos e zero donor runtime coupling observável no repositório.

## Resultado

```text
F1_HARDENING_RECONCILIATION = PROVEN
CANONICAL_ROOT = main
F2_MVP = NOT_STARTED
RUNTIME_IMPLEMENTATION = NOT_CLAIMED
```
