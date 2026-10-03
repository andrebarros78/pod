# ADR-007 — Núcleo de segurança desde a fundação

**Identificador:** POD-ADR-007
**Versão:** 1.0.0
**Status:** ACCEPTED
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Decisão de produto:** André Barros
**Autoridade técnica:** Pipo
**Substitui:** concentração dos controles essenciais de segurança na Fase 10

## Contexto

O plano V001 colocava segurança transversal e Sistema Imunológico em F10, depois de Engine, IA e federação. Esses componentes já dependem de identidade, autorização, segredo, isolamento, audit trail e revogação.

## Problema

Construir capacidades materiais antes dos controles que as limitam produz retrofit inseguro, contratos incompletos e fases impossíveis de aceitar.

## Decisão

Segurança é construída em duas camadas.

### Núcleo obrigatório em F0–F2

- identidade e actor;
- ownership_scope;
- policy_version;
- capability;
- deny by default;
- portões humanos;
- redaction;
- SecretRef e Vault Port;
- audit record atômico;
- isolamento de projeto;
- idempotência;
- generation e fencing;
- limites de efeito;
- testes de autorização.

### Capacidades avançadas em F10

- correlação de ameaças;
- detecção comportamental;
- quarentena automatizada;
- playbooks de incidente;
- rotação coordenada;
- análise de supply chain;
- políticas avançadas de produto;
- resposta adaptativa.

Nenhuma fase pode adiar controle necessário ao efeito que introduz.

## Alternativas consideradas

### Implementar segurança somente em F10

Rejeitada: exigiria retrofit em todos os contratos e deixaria fases anteriores sem base segura.

### Implementar todo o Sistema Imunológico em F0

Rejeitada: complexidade prematura sem superfície operacional suficiente.

### Confiar no ambiente local até F10

Rejeitada: localidade não implica confiança ou escopo.

## Consequências

- F0 cresce para incluir tipos e portas de segurança;
- F1 registra auditoria na mesma transação;
- F2 implementa Policy e gates;
- cada fase adiciona ameaça e teste correspondente;
- F10 continua relevante como expansão, não primeira proteção.

## Migração

- reordenar Plano Mestre;
- incluir requisitos SEC em todas as fases;
- fazer Definition of Done exigir threat review;
- criar testes T-SEC-001 a T-SEC-009.

## Rollback

Controles implementados não podem ser removidos para simplificar fase. Mudança exige novo ADR, teste de risco e proteção equivalente.

## Segurança

Esta decisão é a própria fundação de segurança. Nenhum segredo é persistido em documento ou log.

## Compatibilidade

Compatível com evolução incremental. Adapters futuros devem cumprir as portas desde sua introdução.

## Evidência

- dependência invertida confirmada no plano V001;
- POD-DOC-007 define o núcleo;
- POD-DOC-009 distribui os gates desde F0;
- POD-DOC-010 define testes por fase.

## Condição de revisão

Revisar apenas se uma fase não possuir ação material nem dado protegido. O gate pode ser não aplicável com justificativa, mas o contrato permanece.

## Documentos relacionados

- POD-DOC-002;
- POD-DOC-005;
- POD-DOC-007;
- POD-DOC-009;
- POD-DOC-010.
