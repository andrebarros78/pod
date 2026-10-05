# ADR-011 — CAPABILITY ENGINE, AQUISIÇÃO PROGRESSIVA E EVOLUÇÃO GOVERNADA

**Identificador:** POD-ADR-011
**Versão:** 1.0.0
**Status:** ACCEPTED
**Data:** 2026-10-05
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A2 — decisão arquitetural

## Contexto

O POD precisa reutilizar conhecimento operacional de skills, catálogos e projetos externos sem transformar qualquer fornecedor, catálogo, prompt ou repositório doador em dependência do produto. O desenho ativo já possui Knowledge Store, Capability, Policy, Brain, Construction Engineering, Proof Engine e Learning/Training, mas faltava o contrato explícito de aquisição, seleção, avaliação, promoção e evolução das capacidades reutilizáveis.

## Problema

Instalar skills externas diretamente no runtime criaria acoplamento, autoridade implícita, risco de prompt injection, incompatibilidade de licença, contexto excessivo e ausência de prova de que a skill melhora o resultado. Também permitiria que uma autoevolução defeituosa alterasse a versão ativa sem rollback.

## Decisão

O POD terá um **Capability Engine nativo**, integrado ao Control Plane e ao Knowledge Store. Fontes externas entram somente por um pipeline de aquisição controlada:

~~~text
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
~~~

Invariantes:

~~~text
CAPABILITY_ENGINE_IS_POD_NATIVE = TRUE
EXTERNAL_SKILL_IS_REFERENCE_INPUT_ONLY = TRUE
PROGRESSIVE_CAPABILITY_LOADING = TRUE
CAPABILITY_PROMOTION_REQUIRES_EVAL = TRUE
CAPABILITY_CANNOT_EXPAND_AUTHORITY = TRUE
DONOR_RUNTIME_COUPLING = ZERO
SELF_EVOLUTION_WRITES_CANDIDATE_ONLY = TRUE
UNLICENSED_SOURCE_CONTENT_NOT_COPIED = TRUE
~~~

### Registry mínimo

Cada versão registra capability_id/version, domínio, trigger_rules, entradas/saídas, required_context, tools/recursos, authority ceiling, effect classes, risk_class, proveniência/licença, test/eval suite, benchmark, métricas, last_validation, status e rollback_ref.

### Carregamento progressivo

~~~text
L1 METADATA = id + descrição + trigger + risco + custo aproximado
L2 SPEC = procedimento + contratos + invariantes + exemplos
L3 RESOURCES = scripts + referências + fixtures + assets sob demanda
~~~

O Brain/Construction Engineering não recebe todo o catálogo no contexto. O Capability Router seleciona candidatos por objetivo, domínio, policy, ferramentas, risco e evidência histórica.

### Promoção

Uma capability candidata somente fica `PROMOTED` após testes funcionais, eval de trigger/seleção, regressão, segurança, verificação de autoridade, custo/recursos quando aplicáveis, comparação contra baseline, donor decoupling e proveniência/licença registradas.

### Evolução

Autoaprendizado ou capability evolution cria **nova versão candidata em sandbox**. Nunca altera a versão ativa in-place. Promoção é atômica; falha preserva a versão anterior e permite rollback.

## Alternativas consideradas

1. Instalar diretamente plugins/skills de terceiros no runtime — rejeitado por acoplamento e autoridade implícita.
2. Copiar todos os SKILL.md para o contexto — rejeitado por custo, poluição de contexto e governança fraca.
3. Manter apenas documentação humana — rejeitado porque não produz seleção, eval ou ciclo de melhoria executável.
4. Capability Engine nativo com fontes externas apenas como insumo — escolhido.

## Consequências

O POD pode adquirir novas capacidades sem inflar permanentemente o contexto; capabilities tornam-se versionadas, testáveis e reversíveis; catálogos tornam-se fontes substituíveis; eval/benchmark impedem promoção subjetiva. O custo é implementar Registry, Router, Eval Harness, Promotion Gate e proveniência.

## Migração

1. registrar fontes e hashes em `docs/working/capability-acquisition/`;
2. criar requisitos `REQ-CAP-*` e testes `T-CAP-*`;
3. incorporar Capability Engine em F6 e evolução governada em F11;
4. manter capacidades como `DEFINED_NOT_IMPLEMENTED` até o runtime existir.

## Rollback

Antes da implementação, revogar este ADR e remover requisitos derivados restaura o desenho anterior. Após implementação, rollback seleciona a versão anterior `PROMOTED`, invalida candidata e preserva evidência/histórico/proveniência.

## Segurança

Fonte externa inicia `QUARANTINED`; instrução externa nunca altera Policy, Capability, Human Gate ou SecretRef; capability recebe somente contexto/ferramentas permitidos; nenhum segredo é incorporado; conteúdo sem licença explícita não é copiado verbatim; hash/proveniência são verificados; capability suspeita pode ser suspensa/revogada sem apagar histórico.

## Compatibilidade

Complementa Knowledge Store, Learning/Training, Brain, Construction Engineering, Proof Engine e Security Plane. Não altera autoridade do Mission Core nem do Proof Engine e não torna IA externa obrigatória.

## Evidência

- `docs/working/POD_CAPABILITY_ACQUISITION_V001.md`;
- `docs/working/capability-acquisition/POD_CAPABILITY_SOURCE_MANIFEST_V001.json`;
- `docs/working/capability-acquisition/POD_CAPABILITY_CATALOG_V001.md`.

## Condição de revisão

Revisar se testes mostrarem necessidade de processo físico separado, versão major do contrato ou mecanismo mais simples com as mesmas garantias de proveniência, eval, segurança, progressive loading e rollback.

## Documentos relacionados

- POD-DOC-003 — DNA Operacional V002;
- POD-DOC-004 — Projeto Conceitual V002;
- POD-DOC-005 — Arquitetura Técnica V002;
- POD-DOC-006 — Contratos, Dados e Estados V002;
- POD-DOC-007 — Segurança e Autorizações V002;
- POD-DOC-008 — Requisitos e Rastreabilidade V002;
- POD-DOC-009 — Plano Mestre de Construção V002;
- POD-DOC-010 — Plano de Testes e Aceite V002;
- ADR-009 — Independência do ChatGPT, IA híbrida e Terminal Soberano.
