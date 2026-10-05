# EVIDENCE — F1 HARDENING RECONCILIATION — 05/10/2026

**Status:** CANDIDATE_CONVERGENCE_NOT_PROVEN

## Objetivo

Comprovar a reconciliação entre documentação e contratos F1 para Privacy/Sensitive Data, `MISSION_PROVEN`, lease/fencing, ADE, Execution Fabric, Capability Engine e raiz canônica.

## Candidato inicial comprovado

Commit: `f65a2b34cfbc8ca427fd4943f8b676de2e5b80ee`  
GitHub Actions: `37344078596`  
Resultado: `SUCCESS`

Gates observados:

```text
POD_GOVERNANCE_VALID
POD_CONTRACTS_VALID
POD_FORMAL_VALID
REGRESSION: 16/16 PASS
TLC: 3,735,315 states generated
TLC: 755,806 distinct states
TLC: 0 states left on queue
TLC: no error
```

## Concorrência detectada

Antes de promover o candidato, `main` avançou para `2d4ccddff3c59c257424f365af38b376d24b4687` com Capability Engine e aquisição de 19 referências.

A promoção foi interrompida. Nenhum force-push foi feito em `main`.

## Política de reconciliação

- preservar `2d4ccdd` como ancestral;
- preservar `f65a2b34` como ancestral;
- usar árvore baseada na raiz F1 atual;
- absorver Capability Engine, manifesto, catálogo e prova útil;
- não reativar DOCSET V004 como raiz normativa;
- executar novamente todos os gates no commit de convergência.

## Gate exigido para promoção

```text
GOVERNANCE = PASS
PROTOBUF + JSON SCHEMAS = PASS
CAPABILITY ACQUISITION STRUCTURE = PASS
DONOR RUNTIME COUPLING = 0
NEGATIVE CONTRACT TESTS = PASS
TLA+ MODEL CHECK = PASS
REGRESSION TESTS = PASS
```

Até essa prova ocorrer, `main` não deve ser movida.
