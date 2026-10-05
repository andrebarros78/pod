# ADR-005 — Portões humanos e dependências externas

**Identificador:** POD-ADR-005
**Versão:** 1.0.0
**Status:** ACCEPTED
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Decisão de produto:** André Barros
**Autoridade técnica:** Pipo
**Substitui:** interpretação de que somente gasto novo exige decisão humana

## Contexto

O DNA V001 tratava gasto financeiro como única barreira humana obrigatória. A baseline e o pacote normativo anterior também protegiam produção, publicação, efeitos irreversíveis, credenciais, MFA, CAPTCHA, elevação e decisões jurídicas ou comerciais.

## Problema

Misturar decisão do Owner com indisponibilidade externa cria bypass ou solicitações erradas. Reduzir todos os portões a gasto permite efeitos irreversíveis sem consentimento.

## Decisão

Existem três classes:

### WAITING_FINANCIAL_AUTHORIZATION

Usar para novo:

- gasto;
- compra;
- assinatura;
- licença paga;
- API ou infraestrutura paga;
- contratação;
- obrigação financeira.

### WAITING_OWNER_APPROVAL

Usar para:

- publicação ou exposição pública;
- produção ainda não autorizada;
- ação externa irreversível;
- exclusão ou migração destrutiva;
- elevação material de privilégio;
- mudança de objetivo ou restrição de negócio;
- decisão jurídica ou comercial;
- aceitação explícita de risco alto.

### WAITING_EXTERNAL

Usar para condição que não é decisão técnica do POD:

- credencial indispensável ausente;
- MFA;
- CAPTCHA;
- confirmação fora do sistema;
- ação física;
- hardware;
- conexão ou serviço indispensável indisponível.

## Regras comuns

1. bloquear somente o ramo dependente;
2. persistir estado, razão, impacto e próxima condição;
3. continuar ramos seguros independentes;
4. nunca contornar a barreira;
5. notificar sem expor segredo;
6. expirar aprovação conforme policy;
7. revalidar contexto antes de retomar;
8. registrar ator, escopo e evidence_ref.

## Alternativas consideradas

### Um único WAITING_EXTERNAL

Rejeitada: perde responsabilidade e auditoria.

### Somente portão financeiro

Rejeitada: permite ações irreversíveis ou públicas não autorizadas.

### Aprovação humana para toda ação técnica

Rejeitada: converte Owner em operador e destrói autonomia.

## Consequências

- estado de missão ganha WAITING_OWNER_APPROVAL;
- Approval possui type e scope;
- UI mostra claramente o motivo;
- regras automáticas diferenciam decisão, conexão e gasto;
- tarefas reversíveis continuam autônomas.

## Migração

- mapear waiting genérico para uma das três classes;
- invalidar aprovação sem tipo;
- criar testes T-HUM-001 a T-HUM-006;
- corrigir DNA, baseline, contratos e painel.

## Rollback

Antes da implementação, reversão documental por Git. Após implementação, não reduzir portões sem novo ADR e análise de risco.

## Segurança

Approval é capability limitada, vinculada a actor, ação, escopo, valor quando financeiro, expiração e payload_hash. Aprovação não concede acesso global.

## Compatibilidade

Estados antigos WAITING_FINANCIAL_AUTHORIZATION e WAITING_EXTERNAL continuam válidos. WAITING_OWNER_APPROVAL é adição incompatível apenas para consumidores com enum fechado; versionamento de contrato é obrigatório.

## Evidência

- conflito confirmado entre DNA V001 e baseline anterior;
- taxonomia consolidada em POD-DOC-003, POD-DOC-006 e POD-DOC-007;
- matriz inclui requisitos específicos.

## Condição de revisão

Revisar quando uma nova classe soberana não puder ser representada por type e scope de Approval.

## Documentos relacionados

- POD-DOC-002;
- POD-DOC-003;
- POD-DOC-006;
- POD-DOC-007;
- POD-DOC-010.
