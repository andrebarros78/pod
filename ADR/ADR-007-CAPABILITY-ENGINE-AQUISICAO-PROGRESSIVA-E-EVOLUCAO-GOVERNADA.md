# ADR-007 — Capability Engine, aquisição progressiva e evolução governada

**Status:** ACCEPTED  
**Data:** 2026-10-05  
**Autoridade:** reconciliação da alteração concorrente `2d4ccddff3c59c257424f365af38b376d24b4687` com a raiz canônica F1  
**Origem histórica:** ADR-011 do DOCSET V004 anterior

## Contexto

Durante a reconciliação F1, `main` recebeu em paralelo uma aquisição controlada de 19 referências de capability e uma decisão de Capability Engine. Essa alteração é útil, mas foi construída sobre o DOCSET V004 antigo enquanto a linha F1 de 03/10 já havia migrado V004 para `HISTORY/` e estabelecido uma raiz canônica nova.

A solução correta é preservar o commit concorrente como ancestral Git e absorver sua capacidade útil no namespace e governança atuais, sem reativar o DOCSET V004 como autoridade concorrente.

## Decisão

O POD terá um **Capability Engine nativo**, subordinado ao Governador/Policy e integrado ao conhecimento e à Engenharia de Construção.

Pipeline:

```text
DISCOVER
→ FETCH/PIN
→ HASH
→ LICENSE/PROVENANCE
→ QUARANTINE
→ NORMALIZE BEHAVIOR
→ DEFINE POD CAPABILITY CONTRACT
→ EVAL
→ SECURITY/REGRESSION
→ BENCHMARK
→ PROMOTION GATE
→ CAPABILITY REGISTRY
→ PROGRESSIVE LOAD
```

Invariantes:

```text
CAPABILITY_ENGINE_IS_POD_NATIVE = TRUE
EXTERNAL_SKILL_IS_REFERENCE_INPUT_ONLY = TRUE
PROGRESSIVE_CAPABILITY_LOADING = TRUE
CAPABILITY_PROMOTION_REQUIRES_EVAL = TRUE
CAPABILITY_CANNOT_EXPAND_AUTHORITY = TRUE
DONOR_RUNTIME_COUPLING = ZERO
SELF_EVOLUTION_WRITES_CANDIDATE_ONLY = TRUE
UNLICENSED_SOURCE_CONTENT_NOT_COPIED = TRUE
```

A versão candidata nunca substitui a versão promovida in-place. Promoção é versionada, auditável e reversível.

## Aquisição V001 reconciliada

A alteração concorrente registrou 19 fontes: 14 GitHub pinadas por commit/hash e 5 pacotes LobeHub pinados por hash. O manifesto e o catálogo foram preservados em `EVIDENCE/capability-acquisition/` sem copiar conteúdo doador para o runtime.

O registro histórico afirma que as fontes externas foram verificadas fisicamente no ambiente de aquisição. Nesta reconciliação remota, esse diretório externo não está disponível; portanto:

```text
SOURCE_MANIFEST_PRESENT = VERIFIED
SOURCE_MANIFEST_STRUCTURE = REVALIDATED_BY_CI
DONOR_RUNTIME_COUPLING = REVALIDATED_BY_CI
EXTERNAL_SOURCE_BYTES = HISTORICALLY_VERIFIED_NOT_REFETCHED
```

Isso não altera a regra da Baseline que mantém aquisição/integração de **componentes runtime** como `NOT_EXECUTED`. Trata-se de aquisição de referências/comportamentos para desenho de capabilities, não integração de Mem0, Temporal, OpenHands ou qualquer outro componente runtime.

## Contrato F1

`SCHEMAS/v1/pod_capability.proto` e `SCHEMAS/v1/capability_version.schema.json` definem Registry, avaliação e promoção sem alegar runtime implementado.

## Alternativas consideradas

- reativar o DOCSET V004 modificado: rejeitado por criar duas raízes normativas;
- descartar o commit concorrente: rejeitado por perda de trabalho/evidência;
- incorporar seletivamente na raiz atual e preservar o commit como ancestral: escolhido.

## Consequências

A raiz canônica mantém uma única arquitetura e não perde a aquisição já realizada. O futuro runtime poderá usar as referências como insumo sem acoplamento operacional.

## Migração

1. preservar manifesto, catálogo e prova histórica;
2. normalizar ADR para a série canônica raiz;
3. adicionar contratos F1 do Capability Engine;
4. validar por CI;
5. manter runtime como `NOT_IMPLEMENTED` até fase própria.

## Rollback

Revogar o ADR e os contratos de Capability Engine sem apagar a evidência histórica. Nenhuma fonte externa é necessária para o POD continuar operando.

## Segurança

Toda fonte externa nasce não confiável/quarentenada. Conteúdo sem licença explícita não é copiado. Capability não pode ampliar autoridade, policy, secrets, privacy ou human gates.

## Compatibilidade

Aditiva. Não altera `pod.proto` nem as mensagens F1 existentes.

## Evidência

- commit concorrente `2d4ccddff3c59c257424f365af38b376d24b4687`;
- `EVIDENCE/capability-acquisition/POD_CAPABILITY_SOURCE_MANIFEST_V001.json`;
- `EVIDENCE/capability-acquisition/POD_CAPABILITY_CATALOG_V001.md`;
- `HISTORY/CAPABILITY_ACQUISITION_V001_LEGACY_PROOF.md`.

## Condição de revisão

Revisar ao implementar Capability Registry/Router/Eval/Promotion em runtime.
