# POD — RECONCILIAÇÃO CANÔNICA F1 — 05/10/2026

**Status:** PROVEN_CANONICAL  
**Escopo:** raiz canônica, contratos F1, prova formal, Privacy/Sensitive Data, ADE, Execution Fabric e Capability Engine  
**Fase 2:** NOT_STARTED

## 1. Objetivo concluído

Foram eliminadas as divergências entre documentação e artefatos F1, reconciliado trabalho concorrente sem perda e restaurada `main` como única raiz canônica continuável.

## 2. Precedência

```text
OWNER / LEI / LIMITES REAIS
→ README.md (entrada canônica)
→ POD_DOCUMENTACAO_CONSOLIDADA_CANONICA.md
→ POD_BASELINE_CANONICA_AQUISICAO_EVOLUCAO_HIGIENE.md
→ este documento de reconciliação
→ ADR/ posteriores
→ SCHEMAS/ + CONTRACTS/
→ STANDARDS/
→ RUNBOOKS/ + EVIDENCE/ + RELEASES/
→ HISTORY/ (NORMATIVE=false)
```

O DOCSET V004 permanece histórico e não compete com esta raiz.

## 3. Lacunas fechadas

### Privacy/Sensitive Data

Requisitos válidos do DOCSET V005 foram absorvidos: Privacy Gate, `DataPolicyEnvelope`, `PrivacyDecision`, Sensitive Data Product Profile, criptografia, separação de chave, backup criptografado e MFA para autoridade humana privilegiada.

### MISSION_PROVEN

O modelo formal exige evidência, aceite, regressão, checkpoint, segurança, recovery, isolamento, donor decoupling, gates condicionais de privacidade e verdict fresco.

### Lease/fencing

Worker retém o token recebido. Escrita requer holder atual + token atual. Token stale não altera `resourceVersion`.

### ADE

Contratos F1 explícitos cobrem inspeção, planejamento, changeset, execução, teste, diagnóstico, correção, reteste, regressão, checkpoint e prova ADE.

### Execution Fabric

Contratos F1 explícitos cobrem dispatch, ACK durável, inbox/idempotência, routing, capability snapshot e reconciliation.

### Capability Engine

O commit concorrente `2d4ccddff3c59c257424f365af38b376d24b4687` foi preservado como ancestral do commit convergente. Seu Capability Engine e aquisição de 19 referências foram normalizados na raiz atual; as alterações que tentavam manter DOCSET V004 ativo não foram reintroduzidas.

```text
CAPABILITY_REFERENCE_ACQUISITION_V001 = HISTORICALLY_VERIFIED + STRUCTURE_REVALIDATED
RUNTIME_COMPONENT_ACQUISITION = NOT_EXECUTED
RUNTIME_CAPABILITY_ENGINE = NOT_IMPLEMENTED
```

## 4. Prova

Candidato inicial `f65a2b34cfbc8ca427fd4943f8b676de2e5b80ee`:

- GitHub Actions `37344078596`: SUCCESS.

Commit convergente `180d98575ed9effe7b192a9285c2ef8a7d553863`, contendo ambos os ancestrais `2d4ccdd` + `f65a2b34`:

- branch de reconciliação, GitHub Actions `37345339206`: SUCCESS;
- `main`, GitHub Actions `37345457823`: SUCCESS.

Resultados observados no commit convergente:

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
TLA+ = 3,735,315 states generated
TLA+ = 755,806 distinct states
TLA+ = 0 states left on queue
TLA+ = no error
REGRESSION = 20/20 PASS
```

`external_sources_verified=not_requested` significa que os arquivos físicos externos da aquisição não foram baixados novamente no runner. A prova física anterior permanece registrada historicamente e não foi promovida a “fresh verification”.

## 5. Estado terminal desta missão

```text
F0_BASELINE_RECONCILED = PROVEN
F1_CORE_CONTRACTS_DEFINED = PROVEN
F1_HARDENING_2026_10_05 = PROVEN
CANONICAL_ROOT = main

F2_MVP = NOT_STARTED
POD_RUNTIME = NOT_IMPLEMENTED
PRIVACY_RUNTIME = NOT_IMPLEMENTED
ADE_RUNTIME = NOT_IMPLEMENTED
EXECUTION_FABRIC_RUNTIME = NOT_IMPLEMENTED
CAPABILITY_ENGINE_RUNTIME = NOT_IMPLEMENTED
```

A continuidade correta é iniciar uma nova missão F2 a partir deste checkpoint, sem recriar arquitetura paralela.
