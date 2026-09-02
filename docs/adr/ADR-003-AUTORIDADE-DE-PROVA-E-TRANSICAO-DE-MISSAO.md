# ADR-003 — Autoridade de prova e transição de missão

**Identificador:** POD-ADR-003
**Versão:** 1.0.0
**Status:** ACCEPTED
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Decisão de produto:** André Barros
**Autoridade técnica:** Pipo
**Substitui:** trechos conflitantes do ADR-002 e da baseline POD-2026-09-02

## Contexto

A baseline anterior dizia que o Cérebro determinava prova suficiente. Os contratos posteriores atribuíam o verdict ao Proof Engine, enquanto o Mission Core controlava o ciclo de vida. Isso criava três candidatos à mesma autoridade.

## Problema

O componente que constrói ou planeja não pode certificar sozinho o próprio resultado. O componente que avalia evidência também não deve alterar estado operacional sem revalidar concorrência e policy.

## Decisão

As responsabilidades ficam separadas:

1. Brain propõe estratégia, plano e replanejamento.
2. Engine produz fatos, artefatos e evidências.
3. Proof Engine avalia a versão exata dos critérios e emite ProofVerdict imutável.
4. Mission Core é o único escritor do estado soberano da missão.
5. Mission Core transiciona para MISSION_PROVEN somente após revalidar verdict, mission_version, policy_version, guardas, generation e falhas críticas.

ProofVerdict mínimo:

~~~text
proof_verdict_id
mission_id
mission_version
acceptance_criteria_version
policy_version
evidence_manifest_hash
gate_results
verdict = PASSED | FAILED | INCONCLUSIVE
reason_codes
created_at_utc
producer_version
~~~

Verdict não é comando e não é estado. Alteração da missão ou dos critérios invalida verdict anterior.

## Alternativas consideradas

### Brain decide e transiciona

Rejeitada: mistura planejamento, interesse no resultado e certificação.

### Proof Engine decide e transiciona

Rejeitada: mistura avaliação com propriedade do aggregate e aumenta risco de corrida.

### Mission Core executa toda avaliação

Rejeitada: acopla regras de prova ao lifecycle e dificulta teste independente.

## Consequências

- elimina autoridades concorrentes;
- permite testes independentes do Proof Engine;
- exige consumo idempotente de verdict;
- exige versionamento de critérios;
- adiciona uma etapa explícita entre prova e conclusão.

## Migração

- substituir referências a Cérebro como autoridade final;
- tratar resultados anteriores como candidatos;
- introduzir ProofVerdict;
- concentrar transições no Mission Core;
- criar testes T-AUT-001, T-PRF-001, T-PRF-002 e T-MSN-004.

## Rollback

Rollback documental restaura o DOCSET anterior, mas não é permitido após existir estado persistido no novo contrato sem migração explícita. Antes da implementação, o rollback é apenas de documentação Git.

## Segurança

Proof Engine não recebe capability de escrita de Mission. Mission Core rejeita verdict adulterado, obsoleto ou de produtor não autorizado.

## Compatibilidade

Quebra semanticamente qualquer implementação que permita Brain, Worker ou Proof Engine escrever MISSION_PROVEN diretamente. Não existe implementação oficial, portanto não há migração de runtime nesta data.

## Evidência

- conflito reproduzido entre baseline anterior e contratos V001;
- matriz de autoridade consolidada em POD-DOC-002, POD-DOC-003 e POD-DOC-006;
- validação automatizada exige a separação.

## Condição de revisão

Revisar apenas se evidência operacional demonstrar que a separação impede consistência ou recuperação. Conveniência de implementação não é motivo suficiente.

## Documentos relacionados

- POD-DOC-002;
- POD-DOC-003;
- POD-DOC-005;
- POD-DOC-006;
- POD-DOC-010.
