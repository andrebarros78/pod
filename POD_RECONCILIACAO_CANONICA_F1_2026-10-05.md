# POD — RECONCILIAÇÃO CANÔNICA F1 — 05/10/2026

**Status:** CANDIDATE_UNTIL_MERGED_CI_PASS  
**Escopo:** raiz canônica, contratos F1, prova formal, Privacy/Sensitive Data, ADE, Execution Fabric e Capability Engine  
**Não inicia:** Fase 2 / runtime MVP

## 1. Objetivo

Eliminar divergências entre documentação e artefatos F1, reconciliar trabalho concorrente sem perda e deixar `main` como única raiz canônica continuável.

## 2. Precedência após promoção

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

Em conflito, este fechamento e ADR posterior prevalecem apenas no assunto explicitamente reconciliado. O DOCSET V004 permanece histórico, não volta a ser uma segunda raiz normativa.

## 3. Lacunas fechadas

### Privacy/Sensitive Data

Absorvidos do DOCSET V005 os requisitos de Privacy Gate, `DataPolicyEnvelope`, `PrivacyDecision`, Sensitive Data Product Profile, criptografia, separação de chave, backup criptografado e MFA de autoridade humana privilegiada.

### MISSION_PROVEN

O modelo formal deixa de aceitar uma flag genérica de validação como semântica suficiente. Prova completa exige evidência, aceite, regressão, checkpoint, segurança, recovery, isolamento, donor decoupling, gates condicionais de privacidade e verdict fresco.

### Lease/fencing

Worker retém o token recebido. Escrita só é autorizada ao holder atual com token atual; tentativa stale não altera `resourceVersion`.

### ADE

Contratos F1 explícitos cobrem inspeção, planejamento, changeset, execução, teste, diagnóstico, correção, reteste, regressão, checkpoint e prova ADE sem promover o ADE a Governador.

### Execution Fabric

Contratos F1 explícitos cobrem dispatch, ACK durável, inbox/idempotência, routing, capability snapshot e reconciliation.

### Capability Engine

Durante o CI do primeiro candidato, `main` avançou para o commit concorrente `2d4ccddff3c59c257424f365af38b376d24b4687`. A mudança registrava Capability Engine e aquisição controlada de 19 referências externas, mas sobre o DOCSET V004 anterior.

A reconciliação preserva esse commit como ancestral Git e absorve seletivamente na raiz atual:

- Capability Engine nativo;
- manifesto das 19 fontes;
- catálogo normalizado de comportamentos;
- prova histórica da aquisição;
- contratos `CapabilityVersion`, `CapabilityEvaluation`, `CapabilityPromotionDecision` e `CapabilityLoadRequest`;
- validator de proveniência/zero donor runtime coupling.

Não são reativados os índices/manifests V003/V004 modificados pelo commit concorrente. Eles continuam históricos.

Distinção obrigatória:

```text
CAPABILITY_REFERENCE_ACQUISITION_V001 = HISTORICALLY_VERIFIED + STRUCTURE_REVALIDATED
RUNTIME_COMPONENT_ACQUISITION = NOT_EXECUTED
RUNTIME_CAPABILITY_ENGINE = NOT_IMPLEMENTED
```

Logo, a aquisição das 19 referências não contradiz `ACQUISITION=NOT_EXECUTED` da Baseline para componentes runtime selecionados.

## 4. Provas observadas antes da convergência

O candidato `f65a2b34cfbc8ca427fd4943f8b676de2e5b80ee` passou no GitHub Actions run `37344078596`:

```text
POD_GOVERNANCE_VALID
POD_CONTRACTS_VALID
POD_FORMAL_VALID
REGRESSION = 16/16 PASS
TLA+ = 3,735,315 states generated / 755,806 distinct / 0 queue / no error
```

Essa prova é válida para o candidato pré-merge. O commit de convergência com `2d4ccdd` deve passar novamente antes da promoção.

## 5. Estado que continua verdadeiro

```text
F0_BASELINE_RECONCILED = PROVEN
F1_CORE_CONTRACTS_DEFINED = PROVEN_PREVIOUSLY
F1_HARDENING_2026_10_05 = CANDIDATE_UNTIL_MERGED_CI_PASS

F2_MVP = NOT_STARTED
POD_RUNTIME = NOT_IMPLEMENTED
PRIVACY_RUNTIME = NOT_IMPLEMENTED
ADE_RUNTIME = NOT_IMPLEMENTED
EXECUTION_FABRIC_RUNTIME = NOT_IMPLEMENTED
CAPABILITY_ENGINE_RUNTIME = NOT_IMPLEMENTED
```

## 6. Regra terminal desta reconciliação

Somente após o commit de convergência e depois a própria `main` aprovarem governança, contratos, acquisition validator, model checking e regressão:

```text
F1_HARDENING_2026_10_05 = PROVEN
CANONICAL_ROOT = main
NEXT_ALLOWED_PHASE = F2_MVP
```

A promoção da raiz não inicia F2.
