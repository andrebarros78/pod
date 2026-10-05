# POD — PLANO MESTRE DE CONSTRUÇÃO — V001

**Data:** 02/09/2026  
**Status:** WORKING / NON-NORMATIVE  
**Base:** Projeto Conceitual Reconsolidado + Contratos Conceituais + Modelo Canônico + Arquitetura Técnica Derivada  
**Objetivo:** ordenar a construção do POD por incrementos prováveis, testáveis e reversíveis, evitando topologia fixa prematura.

---

# 0. REGRA DE EXECUÇÃO

Cada fase deve produzir:

```text
IMPLEMENTAÇÃO
+ TESTE
+ EVIDÊNCIA
+ REGRESSÃO
+ CHECKPOINT
```

Nenhuma fase avança apenas por presença de código.

```text
DEFINED
→ IMPLEMENTED
→ TESTED
→ EVIDENCED
→ ACCEPTED
```

Falha de teste retorna ao Loop Engineering; não encerra a missão de construção.

---

# 1. ORDEM MESTRA

```text
FASE 0  FUNDAÇÃO NEUTRA
FASE 1  MEMÓRIA SOBERANA MÍNIMA + MISSION CORE
FASE 2  POLICY + CICLO DE MISSÃO + PROOF MÍNIMO
FASE 3  PAINEL OPERACIONAL FUNCIONAL MÍNIMO
FASE 4  ENGINE LOCAL INICIAL + EXECUÇÃO SEGURA
FASE 5  CONSTRUCTION ENGINE NATIVA
FASE 6  GOVERNOR + SCHEDULER + PROGRESSO REAL
FASE 7  CÉREBRO HÍBRIDO MULTI-PROVIDER
FASE 8  FEDERAÇÃO + NODE AGENT + TÚNEL CORE
FASE 9  POD ENGINES MULTIPLATAFORMA
FASE 10 SEGURANÇA TRANSVERSAL + SISTEMA IMUNOLÓGICO
FASE 11 LEARNING & TRAINING
FASE 12 PRODUCT TESTING + DELIVERY CONTRACT
FASE 13 AUTOSSUSTENTAÇÃO / UPDATE / BACKUP / DR
FASE 14 PERFORMANCE / FAULT / LOAD / FEDERATION PROOF
FASE 15 E2E FINAL DO PRÓPRIO POD
```

A sequência pode ter paralelismo controlado depois que dependências mínimas forem provadas.

---

# 2. FASE 0 — FUNDAÇÃO NEUTRA

Construir somente elementos de baixo arrependimento:

```text
IDs soberanos
entidades de domínio
Clock abstraction
hashing
redaction
errors/failure taxonomy
retry/backoff/circuit breaker
lease/generation/fencing primitives
ports/interfaces
architecture tests
ZERO DONOR COUPLING gate
```

Critério de saída:

```text
DOMÍNIO NÃO IMPORTA INFRAESTRUTURA
IDs imutáveis
fencing testado
clock monotonic/UTC separado
primitivas unitariamente testadas
```

---

# 3. FASE 1 — MEMÓRIA SOBERANA MÍNIMA + MISSION CORE

Implementar:

```text
Project/Mission Repository
Event Store port
State Store port
Command Inbox
Idempotency Store
Checkpoint Store
Evidence Store mínimo
Mission Core mínimo
```

Invariante obrigatório:

```text
VALIDAR → PERSISTIR → COMMIT → EVENTO → CONFIRMAR
```

Testes mínimos:

```text
restart sem perder missão
comando duplicado não duplica efeito
state rebuild/replay básico
checkpoint persistente
```

---

# 4. FASE 2 — POLICY + CICLO DE MISSÃO + PROOF MÍNIMO

Implementar:

```text
Policy abstraction/version
Mission state machine
Pause/Resume/Cancel
WAITING_EXTERNAL
WAITING_FINANCIAL_AUTHORIZATION
Recovery/Replanning transitions
Proof Gate framework
```

Provar:

```text
MISSION_ACCEPTED cria obrigação persistente
estado terminal só ocorre por regra válida
falha de tentativa não encerra missão
MISSION_PROVEN exige gate real
```

---

# 5. FASE 3 — PAINEL OPERACIONAL FUNCIONAL MÍNIMO

Esta fase é precoce por decisão conceitual.

Entregar Painel real, mesmo visualmente simples:

```text
SYSTEM health/version
MISSIONS status/progress/current stage/blockers
EVIDENCE checkpoints/tests/proofs
CONTROL pause/resume/recovery
```

Arquitetura:

```text
READ MODELS / QUERY API
COMMAND API
REAL EVENT STREAM
```

Gates:

```text
PANEL_REAL_STATE_GATE
PANEL_COMMAND_PATH_GATE
PANEL_NO_DIRECT_DB_MUTATION_GATE
PANEL_CLOSE_CONTINUITY_GATE
```

---

# 6. FASE 4 — ENGINE LOCAL INICIAL + EXECUÇÃO SEGURA

Construir primeiro um Engine local real, sem assumir que será único.

Capacidades mínimas:

```text
Stable Identity
local inbox/journal
capability discovery
filesystem
shell
Git/Python ou equivalentes disponíveis
process execution
checkpoint/result/evidence
health
```

Separar execução privilegiada por porta própria.

Provar:

```text
Core não precisa ficar elevado
reboot/restart preserva comando aceito
command_id/idempotency funcionam
execução deixa evidência
```

---

# 7. FASE 5 — CONSTRUCTION ENGINE NATIVA

Implementar capacidades próprias:

```text
inspect repository/environment
understand change scope
decompose objective
plan smallest useful action
execute through ports
observe effect
diagnose failure
correct/retest
integrate
```

Não depender estruturalmente de Codex/Claude/OpenCode.

Testes:

```text
construção simples end-to-end
correção de teste falho
mudança multi-arquivo
regressão
rollback de mudança inadequada
```

---

# 8. FASE 6 — GOVERNOR + SCHEDULER + PROGRESSO REAL

Implementar:

```text
DAG/ready queue
priorities
resource snapshots
admission control
concurrency
fairness multiprojeto
aging/starvation prevention
preemption
restart budgets
stagnation detection
```

Provar:

```text
atividade sem avanço não aumenta progresso
projeto não monopoliza indefinidamente
falta de recurso gera defer/throttle
falha local não para ramos independentes
```

---

# 9. FASE 7 — CÉREBRO HÍBRIDO MULTI-PROVIDER

Implementar sob ownership do Cérebro:

```text
Context Engine
Knowledge Retrieval
AI Capability Router
Provider Registry
Provider-neutral contracts
Adapters
Health
Cost/Latency routing
Validation
Failover
Challenger path
```

Oito mecanismos aprovados são gates da fase.

Provar:

```text
troca de provider não altera missão
contexto permanece do POD
provider down não derruba missão
Policy bloqueia envio de dado incompatível
modelo não executa ação diretamente
```

---

# 10. FASE 8 — FEDERAÇÃO + NODE AGENT + TÚNEL CORE

Implementar:

```text
Node Agent permanente
persistent outbound transport
multiplexing
Node Inbox durável
TRANSPORT_ACK + COMMAND_ACCEPTED
result/event push
heartbeat funcional
capability registry
lease/generation/fencing
reconciliation
fleet lifecycle
trust enrollment/revocation
```

Gates:

```text
NO_PER_COMMAND_CONNECTION
NO_HOT_PATH_POLLING
ACK != RESULT
STALE_GENERATION_CANNOT_COMMIT
```

Fault tests:

```text
network cut
agent kill
result delivery lost
node reboot
old generation returns
duplicate command
```

---

# 11. FASE 9 — POD ENGINES MULTIPLATAFORMA

Generalizar contrato de Engine e provar ao menos:

```text
POD Windows Engine
POD Linux Engine
```

Objetivo:

```text
MISSION SEMANTICS INDEPENDENT OF OS
```

Capability discovery e privileged execution respeitam particularidades do sistema operacional sem contaminar o domínio.

---

# 12. FASE 10 — SEGURANÇA TRANSVERSAL + SISTEMA IMUNOLÓGICO

Materializar:

```text
identity/authentication
authorization/policy enforcement
Vault/SecretRef
redaction
data classification
audit
runtime integrity
supply-chain checks
quarantine/revocation
incident lifecycle
immune detection/containment/recovery
```

Provar que Segurança contém sem assumir autoridade cognitiva ou alterar Policy silenciosamente.

---

# 13. FASE 11 — LEARNING & TRAINING

Implementar como capability sob demanda, fora do Core permanente:

```text
Knowledge Plane
Experience Plane
Competence Plane
Training Plane
Epistemic Integrity
Source Dependency Graph
Action→Effect
Deterministic Replay
Failure/Recovery Learning
Change/Staleness
Competence Proof
Training Eligibility
```

Provar:

```text
KNOWLEDGE_ACQUIRED != COMPETENCE_PROVEN
KNOWLEDGE != AUTHORITY
Learning não modifica Policy diretamente
Training não é automaticamente fine-tuning
```

---

# 14. FASE 12 — PRODUCT TESTING + DELIVERY CONTRACT

Construir o sistema que valida o produto criado pelo POD.

Capacidades:

```text
Test Strategy
isolated environments
fixtures/test data
unit/contract/integration/E2E
security tests
fault/recovery tests
performance tests
regression
independent verifier
artifact promotion
final evidence pack
```

Delivery bundle conforme aplicabilidade:

```text
artifact/version/hash
install/run instructions
config schema
migration
backup/rollback
SBOM
security proof
recovery proof
test report
known limitations
final manifest
```

---

# 15. FASE 13 — AUTOSSUSTENTAÇÃO / UPDATE / BACKUP / DR

Implementar:

```text
install/bootstrap
self-health
backup/restore
side-by-side update
candidate/known-good
migration check
canary activation
rollback
disaster recovery
```

Provar atualização sem perda de missão e restore em ambiente limpo/recuperado.

---

# 16. FASE 14 — PERFORMANCE / FAULT / LOAD

Medir por estágio:

```text
p50
p95
p99
```

Testar:

```text
1/4/8/16/32 concorrências quando o ambiente suportar
CPU/RAM/disk pressure
queue growth
provider degradation
multi-node dispatch
node churn
network partition
checkpoint/reconciliation
```

Objetivo é estabilidade e custo total, não maximizar paralelismo.

---

# 17. FASE 15 — E2E FINAL DO PRÓPRIO POD

Missão de prova:

```text
receber projeto real controlado
→ compreender
→ planejar
→ construir
→ distribuir
→ falhar intencionalmente em alguns pontos
→ recuperar
→ testar
→ auditar
→ entregar
→ provar
```

Deve incluir interrupções reais:

```text
fechar painel
cortar canal externo
reiniciar processo
reiniciar nó
provider indisponível
reboot quando seguro
```

O resultado final é:

```text
POD CONSTRÓI UM PRODUTO
+ SOBREVIVE ÀS FALHAS PREVISTAS
+ ENTREGA O PRODUTO
+ PRODUZ EVIDENCE PACK
+ DECLARA MISSION_PROVEN SOMENTE APÓS PROVA
```

---

# 18. PAINEL EVOLUTIVO POR FASE

O Painel não espera o fim.

```text
F3  missão/health/control
F4  Engine/execution/evidence
F6  Governor/resources/queues
F7  providers/cognitive health/cost
F8  federation/nodes
F10 security/incidents
F11 learning/training
F12 testing/delivery
F13 backups/updates
```

---

# 19. RASTREABILIDADE OBRIGATÓRIA

Cada requisito futuro deve ligar:

```text
REQUIREMENT
→ CONCEPT
→ CONTRACT
→ COMPONENT
→ BUILD PHASE
→ TEST
→ EVIDENCE
→ ACCEPTANCE
```

Estados de conformidade podem seguir a cadeia já validada historicamente:

```text
DEFINED_NOT_IMPLEMENTED
→ IMPLEMENTING
→ IMPLEMENTED_NOT_TESTED
→ TESTED_NOT_EVIDENCED
→ EVIDENCED_NOT_ACCEPTED
→ ACCEPTED
```

---

# 20. REGRA DE NÃO BLOQUEIO

Uma fase pode iniciar trabalho preparatório paralelo quando:

```text
dependências conceituais estão fechadas
interfaces necessárias já estão estáveis
trabalho é isolável
rollback é possível
não cria lock-in precoce
```

Mas nenhum ramo é declarado aceito sem seus gates.

---

# 21. ZERO DONOR COUPLING DURANTE A CONSTRUÇÃO

Em todas as fases:

```text
absorver comportamento/prova útil
normalizar para POD
não importar runtime doador
não usar paths/names/services doadores
regressão de comportamento
```

O gate deve rodar continuamente desde F0.

---

# 22. DEFINIÇÃO DE PRONTO POR FASE

Uma fase está pronta quando:

```text
todos os requisitos CRITICAL aplicáveis = ACCEPTED
nenhuma lacuna de autoridade aberta
contratos utilizados estão versionados
regressão verde
falhas injetadas obrigatórias passam
artifacts/evidence preservados
checkpoint criado
```

---

# 23. PRÓXIMO PASSO APÓS ESTE PLANO

A próxima transição deixa de ser conceitual e passa a ser preparação de implementação:

```text
1. montar matriz de requisitos da nova arquitetura
2. escolher stack física por ADR/benchmark
3. criar skeleton do repositório
4. implementar FASE 0
5. executar gates
```

A escolha de stack deve ser feita somente contra requisitos e provas, não por herança dos documentos antigos.