# POD — CATÁLOGO NATIVO DE CAPACIDADES ADQUIRIDAS — V001

**Identificador:** POD-WORK-CAP-001
**Versão:** 1.0.0
**Status:** REFERENCE_ONLY
**Data:** 2026-09-03
**Finalidade:** normalizar capacidades externas úteis em contratos nativos do POD, sem dependência de runtime dos doadores.

## Regras de uso

1. Fonte externa é evidência de descoberta, não autoridade operacional.
2. Nenhuma capability amplia Policy, Capability ou Human Gate.
3. Nenhum source repo, pacote LobeHub ou catálogo participa de build/runtime do POD.
4. Implementação será POD-native e precisa passar eval, regressão, segurança e benchmark antes de promoção.
5. Carregamento é progressivo: metadata → spec → recursos sob demanda.

## Capacidades

### CAP-AUTH-001 — Capability Authoring & Evaluation

- **Origem de descoberta:** SkillsMP / `skill-creator`.
- **Comportamento absorvido:** criar, testar, comparar baseline, medir e versionar capacidades.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-DBG-001 — Systematic Root-Cause Debugging

- **Origem de descoberta:** SkillsMP / `systematic-debugging`.
- **Comportamento absorvido:** investigar causa-raiz antes de corrigir e usar falha como evidência.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-PROOF-001 — Fresh Verification Before Completion

- **Origem de descoberta:** SkillsMP / `verification-before-completion`.
- **Comportamento absorvido:** executar prova fresca antes de qualquer declaração de conclusão.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-WRK-001 — Durable Worker Ledger

- **Origem de descoberta:** SkillsMP / `subagent-driven-development`.
- **Comportamento absorvido:** orquestrar workers por plano persistente e retomar sem repetir trabalho concluído.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-QA-001 — Independent Code Review

- **Origem de descoberta:** SkillsMP / `requesting-code-review`.
- **Comportamento absorvido:** revisão separada antes da integração.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-TDD-001 — Test-Driven Development

- **Origem de descoberta:** SkillsMP / `test-driven-development`.
- **Comportamento absorvido:** RED-GREEN-REFACTOR e testes antes da implementação material.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-GIT-001 — Isolated Worktree Execution

- **Origem de descoberta:** SkillsMP / `using-git-worktrees`.
- **Comportamento absorvido:** isolamento de trabalho mutável e baseline testado.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-MEM-001 — Hybrid Memory Retrieval

- **Origem de descoberta:** SkillsMP / `memory`.
- **Comportamento absorvido:** combinar busca exata, textual, semântica, metadados e recência.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-AUT-001 — Autonomous Continuation

- **Origem de descoberta:** SkillsMP / `autonomy`.
- **Comportamento absorvido:** selecionar próxima ação após conclusão sem exigir comando humano rotineiro.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-WF-001 — Quality-Gated Process

- **Origem de descoberta:** SkillsMP / `process`.
- **Comportamento absorvido:** workflow com gates, checkpoints e continuidade.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-PAR-001 — Governed Parallel Execution

- **Origem de descoberta:** SkillsMP / `parallel-execution`.
- **Comportamento absorvido:** executar itens independentes em paralelo respeitando dependências.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-BRW-001 — Browser DevTools Verification

- **Origem de descoberta:** SkillsMP / `browser-testing-with-devtools`.
- **Comportamento absorvido:** validar DOM, console, rede, performance e acessibilidade em navegador real.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-BRW-002 — Browser Automation

- **Origem de descoberta:** SkillsMP / `browser-use`.
- **Comportamento absorvido:** navegação e interação controlada via navegador real.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-PAR-002 — Independent-Domain Dispatch

- **Origem de descoberta:** SkillsMP / `dispatching-parallel-agents`.
- **Comportamento absorvido:** despachar um worker por domínio independente com contexto mínimo necessário.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-PERF-001 — Performance Validation

- **Origem de descoberta:** LobeHub / `testing-performance`.
- **Comportamento absorvido:** carga, stress, percentis p50/p95/p99 e thresholds reproduzíveis.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-EXEC-001 — Checkpointed Project Execution

- **Origem de descoberta:** LobeHub / `project-execution`.
- **Comportamento absorvido:** execução por plano com dependências, checkpoints, Definition of Done e gates.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-OBS-001 — Log & Trace Analysis

- **Origem de descoberta:** LobeHub / `log-analysis`.
- **Comportamento absorvido:** correlação por eventos/trace, incidentes, performance e auditoria.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-EVOL-001 — Governed Capability Evolution

- **Origem de descoberta:** LobeHub / `capability-evolver`.
- **Comportamento absorvido:** analisar histórico, gerar candidato de melhoria, avaliar e promover somente com governança.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

### CAP-SEC-001 — Self Security Audit

- **Origem de descoberta:** LobeHub / `clawdbot-self-security-audit`.
- **Comportamento absorvido:** auditar postura, detectar riscos e transformar achados em evidência/remediação.
- **Entrada POD:** objetivo/subtarefa, contexto mínimo, policy_version, capability envelope, recursos disponíveis.
- **Saída POD:** decisão/ação candidata + evidência estruturada + versão da capability usada.
- **Gate:** não pode alterar autoridade; deve registrar versão, origem e resultado; falha exige diagnóstico ou fallback governado.

## Carregamento progressivo

~~~text
L1 METADATA     = id, nome, descrição, trigger, custo/risco
L2 SPEC         = procedimento, entradas, saídas, invariantes e exemplos
L3 RESOURCES    = referências, scripts, fixtures e assets somente quando necessários
~~~

## Lifecycle

~~~text
DISCOVERED → ACQUIRED → QUARANTINED → NORMALIZED → EVALUATING
→ QUALIFIED → PROMOTED → SUSPENDED/REVOKED → ARCHIVED
~~~

Self-evolution nunca edita a versão ativa. Gera nova versão candidata em sandbox, avalia, compara, promove atomicamente ou descarta.
