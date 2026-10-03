# ADR-004 — Persistência atômica, journal e outbox

**Identificador:** POD-ADR-004
**Versão:** 1.0.0
**Status:** ACCEPTED
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Decisão de produto:** André Barros
**Autoridade técnica:** Pipo
**Substitui:** sequência PERSISTIR → COMMIT → EVENTO dos documentos V001

## Contexto

Os documentos anteriores registravam estado, executavam commit e somente depois registravam evento. Uma queda entre commit e evento deixaria estado sem história e sem entrega, impossibilitando auditoria e replay confiáveis.

## Problema

Estado, evento e entrega eram gravados como efeitos independentes. Nenhum retry posterior consegue garantir, sozinho, que os três representem exatamente a mesma decisão de domínio.

## Decisão

Toda mutação material local usa uma transação atômica:

~~~text
VALIDATE
→ BEGIN
→ compare-and-set aggregate state/version
→ append immutable domain event
→ insert transactional outbox
→ insert idempotency and audit record
→ COMMIT
→ publish outbox at-least-once
→ CONFIRM
~~~

O aggregate versionado é a visão operacional autorizada. O journal append-only é a história causal. Ambos pertencem ao mesmo commit e, portanto, não são fontes concorrentes.

O barramento é transporte. Read Models e caches são projeções reconstruíveis.

## Falhas

- antes do commit: nenhum efeito é confirmado;
- depois do commit e antes da publicação: outbox pendente é reenviada;
- publicação duplicada: consumidor deduplica por event_id/message_id;
- repetição de comando: idempotency_key devolve outcome anterior;
- divergência entre aggregate e journal: incidente de integridade e bloqueio seguro do escopo.

## Alternativas consideradas

### Estado e evento em commits separados

Rejeitada pela janela de dual write.

### Mensageria exactly-once

Rejeitada como premissa não portátil e insuficiente para efeitos externos.

### Event sourcing obrigatório para todo domínio

Rejeitada por adicionar complexidade prematura. O journal é obrigatório; reconstruir todo aggregate somente por eventos não é requisito inicial.

### Transação distribuída entre bancos e barramento

Rejeitada por custo, fragilidade e dependência de tecnologia.

## Consequências

- o armazenamento inicial deve suportar transação ACID local;
- event, outbox e aggregate devem compartilhar fronteira transacional;
- consumidores devem ser idempotentes;
- efeitos externos exigem protocolo próprio de intenção, execução e reconciliação;
- replay de Read Model torna-se comprovável.

## Migração

- substituir invariantes antigos em documentos ativos;
- criar portas TransactionManager, AggregateStore, EventJournal, Inbox e Outbox;
- criar testes de queda em cada ponto da sequência;
- impedir confirmação anterior ao commit.

## Rollback

Antes da implementação, reverter o commit documental. Após dados reais, rollback exige migração que preserve journal, versões e idempotência; nunca apagar eventos para voltar.

## Segurança

Auditoria integra a mesma transação. Dados sensíveis são referenciados ou redigidos; evento e outbox não armazenam segredo bruto.

## Compatibilidade

Substitui contratos V001. Não existe runtime oficial para migrar.

## Evidência

- janela de falha confirmada nos documentos anteriores;
- outbox já era requisito da baseline, mas não integrava a sequência de commit;
- POD-DOC-006 formaliza registros e guardas;
- testes T-PER-001 a T-PER-006 comprovam o contrato.

## Condição de revisão

Revisar se o armazenamento escolhido não puder oferecer a fronteira transacional. Nesse caso, a stack deve ser rejeitada ou um protocolo equivalente deve ser comprovado antes da mudança.

## Documentos relacionados

- POD-DOC-002;
- POD-DOC-005;
- POD-DOC-006;
- POD-DOC-010.
