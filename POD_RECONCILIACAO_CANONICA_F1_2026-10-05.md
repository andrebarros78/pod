# POD — RECONCILIAÇÃO CANÔNICA F1 — 05/10/2026

**Status:** CANDIDATE_UNTIL_CI_PASS  
**Escopo:** raiz canônica, contratos F1, prova formal, Privacy/Sensitive Data, ADE e Execution Fabric  
**Não inicia:** Fase 2 / runtime MVP

## 1. Objetivo

Eliminar a divergência entre a documentação vigente e os artefatos F1, consolidar a raiz canônica e deixar o próximo executor capaz de continuar sem reconstruir contexto.

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

Em conflito, ADR posterior e este fechamento F1 prevalecem apenas no assunto explicitamente reconciliado.

## 3. Lacunas fechadas

### Privacy/Sensitive Data

Absorvidos do DOCSET V005 os requisitos de Privacy Gate, DataPolicyEnvelope, PrivacyDecision, Sensitive Data Product Profile, criptografia, separação de chave, backup criptografado e MFA de autoridade humana privilegiada.

### MISSION_PROVEN

O modelo formal deixa de aceitar `validated=true` como semântica suficiente. Prova completa exige evidência, aceite, regressão, checkpoint, segurança, recovery, isolamento, donor decoupling e gates condicionais de privacidade, além de verdict fresco.

### Lease/fencing

Worker antigo conserva token anterior no modelo. Escrita só é autorizada ao holder atual com token atual.

### ADE

Contratos F1 explícitos adicionados sem promover ADE a Governador ou autoridade de prova.

### Execution Fabric

Dispatch, ACK durável, inbox, routing, capability snapshot e reconciliation passam a ter contratos explícitos.

## 4. Estado que continua verdadeiro

```text
F0_BASELINE_RECONCILED = PROVEN
F1_CORE_CONTRACTS_DEFINED = PROVEN_PREVIOUSLY
F1_HARDENING_2026_10_05 = CANDIDATE_UNTIL_CI_PASS

F2_MVP = NOT_STARTED
POD_RUNTIME = NOT_IMPLEMENTED
PRIVACY_RUNTIME = NOT_IMPLEMENTED
ADE_RUNTIME = NOT_IMPLEMENTED
EXECUTION_FABRIC_RUNTIME = NOT_IMPLEMENTED
```

## 5. Regra terminal desta reconciliação

Somente após GitHub Actions aprovar governança, contratos, model checking e regressão:

```text
F1_HARDENING_2026_10_05 = PROVEN
CANONICAL_ROOT = main
NEXT_ALLOWED_PHASE = F2_MVP
```

A promoção da raiz não equivale a iniciar F2.
