# EVIDENCE — F1 HARDENING RECONCILIATION — 05/10/2026

**Status:** CANDIDATE_NOT_PROVEN

## Objetivo

Comprovar a reconciliação entre documentação e contratos F1 para:

- Privacy/LGPD e Sensitive Data;
- `MISSION_PROVEN`;
- lease/fencing;
- ADE;
- Execution Fabric;
- raiz canônica em `main`.

## Antes do CI

Os artefatos foram preparados como candidato. Nenhum resultado de GitHub Actions é presumido.

## Gate exigido

```text
GOVERNANCE = PASS
PROTOBUF + JSON SCHEMAS = PASS
NEGATIVE CONTRACT TESTS = PASS
TLA+ MODEL CHECK = PASS
REGRESSION TESTS = PASS
```

A promoção à `main` e o estado `PROVEN` só podem ocorrer após observar esses resultados no GitHub.
