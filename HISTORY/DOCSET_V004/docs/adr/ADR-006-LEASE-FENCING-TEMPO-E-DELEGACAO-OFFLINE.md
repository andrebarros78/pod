# ADR-006 — Lease, fencing, tempo e delegação offline

**Identificador:** POD-ADR-006
**Versão:** 1.0.0
**Status:** ACCEPTED
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Decisão de produto:** André Barros
**Autoridade técnica:** Pipo
**Substitui:** expires_monotonic_ref persistido e delegação offline indefinida

## Contexto

O modelo V001 persistia expires_monotonic_ref. Relógios monotônicos só são comparáveis dentro do mesmo processo vivo; reinício ou outro nó perde a referência. A federação também não limitava formalmente a autoridade offline.

## Problema

Um lease poderia permanecer aparentemente válido após reinício, ser comparado entre relógios incompatíveis ou permitir que um nó isolado mantivesse autoridade além do limite seguro.

## Decisão

Lease persistido contém:

~~~text
lease_id
resource_scope
issuer_node_id
owner_id
authority_epoch
generation
fencing_token
issued_at_utc
expires_at_utc
clock_uncertainty_ms
capability_ref
effect_classes
status
~~~

Relógio monotônico é usado apenas para medir timeout e duração no mesmo processo. Nunca é persistido como instante global.

Commit compartilhado exige authority_epoch, generation e fencing_token atuais. Expiração UTC considera clock_uncertainty e validação da autoridade.

## Delegação offline

- TTL é finito e definido por policy;
- não existe renovação autônoma offline;
- READ_ONLY pode prosseguir;
- REVERSIBLE_LOCAL pode prosseguir;
- SHARED_MUTATION fica como candidato até reconciliação;
- EXTERNAL_IRREVERSIBLE é proibido;
- Policy, Approval e Secret rotation não podem ser alterados offline;
- evidence e artifact candidatos preservam node_id, generation e timestamps.

## Alternativas consideradas

### Somente timestamp UTC

Rejeitada isoladamente: clock skew pode aceitar lease vencido.

### Somente relógio monotônico

Rejeitada: não sobrevive a reinício nem pode ser comparada entre nós.

### Coordenador permanentemente online

Rejeitada como requisito absoluto porque elimina autonomia local durante partição.

### CRDT para qualquer estado

Rejeitada: nem todo estado é combinável e efeitos irreversíveis não admitem merge.

## Consequências

- autoridade precisa manter epoch e último fencing token aceito;
- configuração define incerteza e TTL por classe;
- nó offline trabalha com poderes menores;
- reconciliação pode rejeitar resultado sem apagar evidência;
- last-write-wins permanece proibido para estado crítico.

## Migração

- remover expires_monotonic_ref de contrato persistido;
- introduzir os campos desta decisão;
- criar testes de reinício, skew, partition, stale generation e reconciliação;
- invalidar lease de versão anterior durante migração.

## Rollback

Rollback de runtime exige expirar todos os leases e drenar nós. Antes da implementação, basta reverter o commit documental.

## Segurança

Fencing é aplicado no ponto de commit, não apenas no dispatch. Capability offline é de menor privilégio e não contém segredo bruto.

## Compatibilidade

Incompatível com agentes que enviem apenas expires_monotonic_ref. A negociação federada deve recusar protocolo anterior.

## Evidência

- falha semântica reproduzida no modelo canônico V001;
- contrato consolidado em POD-DOC-005 e POD-DOC-006;
- testes T-DST-001 a T-DST-007.

## Condição de revisão

Revisar se testes com a stack escolhida demonstrarem modelo mais simples com as mesmas garantias de reinício, partição e fencing.

## Documentos relacionados

- POD-DOC-005;
- POD-DOC-006;
- POD-DOC-007;
- POD-DOC-010.
