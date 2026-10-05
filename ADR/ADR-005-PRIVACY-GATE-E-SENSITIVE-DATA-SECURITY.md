# ADR-005 — Privacy Gate nativo e Sensitive Data Security

**Status:** ACCEPTED  
**Data:** 2026-10-05  
**Autoridade:** decisão de reconciliação solicitada pelo Owner  
**Escopo:** F0/F1 e implementação futura

## Contexto

O DOCSET V005 anexado contém requisitos de Privacy/LGPD e proteção nativa de dados sensíveis que não estavam integralmente materializados na raiz canônica reconciliada em 03/10.

A numeração V005 não lhe dá precedência cronológica sobre decisões posteriores. Seus requisitos válidos devem ser absorvidos sem regredir Core selado, ADE, Execution Fabric, REUSE FIRST ou a Baseline canônica de 03/10.

## Decisão

1. O POD adota `NO_PRIVACY_GATE = NO_DATA_OPERATION` como invariante para operações de dados às quais Privacy Gate seja aplicável.
2. Privacy Gate é independente e cumulativo com Security Gate.
3. `DataPolicyEnvelope` e `PrivacyDecision` passam a ser contratos versionados.
4. Dados sensíveis ativam `SENSITIVE_DATA_PRODUCT_PROFILE`.
5. Criptografia em repouso, separação de chaves, backup criptografado e MFA para autoridade humana privilegiada tornam-se gates quando aplicáveis.
6. Provider de IA, executor privilegiado, worker, Fabric, backup e restore não podem contornar Privacy Gate.
7. Nesta Fase 1 apenas contratos, normas e invariantes são considerados implementados; runtime de privacidade permanece `NOT_IMPLEMENTED`.

## Consequências

- a futura Fase 2 já nasce com fronteira de dados governada;
- prova de missão passa a representar explicitamente privacy/sensitive-data gates;
- qualquer implementação futura que trate dados pessoais sem estes gates será não conforme.

## Migração

Os requisitos são absorvidos em `STANDARDS/POD_PRIVACY_LGPD_SENSITIVE_DATA_STANDARD_V001.md`, schemas e Protobuf aditivo.

## Rollback

Rollback documental só pode ocorrer por ADR posterior que preserve requisitos legais/técnicos aplicáveis e demonstre equivalência ou melhoria.

## Segurança

Fail closed. Nenhum prompt, modelo, provider ou privilégio administrativo substitui a decisão do gate.

## Compatibilidade

Aditiva para F1. Não altera mensagens existentes em `pod.proto`; os novos contratos ficam em `pod_hardening.proto`.

## Evidência

CI deve validar schemas, Protobuf, testes negativos e modelo formal antes de promoção à `main`.

## Condição de revisão

Revisar ao iniciar o runtime de dados, escolher vault/KMS/keystore, implementar autenticação privilegiada ou processar dados pessoais/sensíveis reais.

## Documentos relacionados

- `POD_DOCUMENTACAO_CONSOLIDADA_CANONICA.md`
- `POD_BASELINE_CANONICA_AQUISICAO_EVOLUCAO_HIGIENE.md`
- `STANDARDS/POD_PRIVACY_LGPD_SENSITIVE_DATA_STANDARD_V001.md`
- `SCHEMAS/v1/pod_hardening.proto`
