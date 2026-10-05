# POD — ARQUITETURA TÉCNICA DERIVADA — V001

**Data:** 02/09/2026  
**Status:** WORKING / NON-NORMATIVE  
**Base:** Projeto Conceitual Reconsolidado + Contratos Conceituais + Modelo Canônico de Dados/Estados/Eventos  
**Objetivo:** transformar a concepção em arquitetura técnica lógica sem congelar tecnologia física prematuramente.

---

# 0. PRINCÍPIOS DE DERIVAÇÃO

```text
DOMÍNIO NÃO DEPENDE DE INFRAESTRUTURA
POLICY PRECEDE AÇÃO MATERIAL
ESTADO SOBERANO NÃO VIVE EM PROCESSO
CONEXÃO != EXECUÇÃO
PROVIDER != CÉREBRO
PAINEL != FONTE DA VERDADE
FALHA LOCAL != PARADA GLOBAL
```

Não são invariantes desta versão:

```text
quantidade fixa de serviços
banco específico
mensageria específica
framework web específico
Windows-only
single-project
limite fixo de providers/credenciais
```

---

# 1. CAMADAS LÓGICAS

```text
+-------------------------------------------------------------+
| CAMADA 1 — DOMÍNIO / CONSTITUIÇÃO                          |
| IDs, Mission, Project, Policy, estados, eventos, prova,     |
| lease/fencing, segurança sem dependência de infraestrutura   |
+-------------------------------------------------------------+
| CAMADA 2 — APLICAÇÃO / ORQUESTRAÇÃO                         |
| Cérebro, Construction, Governor, Scheduler, Proof, Recovery, |
| Learning orchestration, Product Delivery                     |
+-------------------------------------------------------------+
| CAMADA 3 — PORTAS / CONTRATOS                               |
| Memory, Event/State, Execution, Federation, Provider, Vault, |
| Clock, Evidence, Storage, Privileged Execution, Telemetry     |
+-------------------------------------------------------------+
| CAMADA 4 — ADAPTADORES / INFRAESTRUTURA                     |
| Engines, bancos, filas, filesystem, MCP/Action, web,         |
| providers, OS, browser, Git, terminal, bridges               |
+-------------------------------------------------------------+
```

Dependência arquitetural aponta para dentro.

---

# 2. GRANDES PLANOS DO RUNTIME

A topologia física pode variar, mas logicamente o POD possui:

```text
CONTROL PLANE
→ missão, Policy, Cérebro, Construction, Governor, Scheduler, Proof

MEMORY PLANE
→ estado soberano, eventos, checkpoints, evidências, conhecimento

FEDERATION PLANE
→ membership, routing, transport, Node Inbox, reconciliation

EXECUTION PLANE
→ POD Engines e capabilities locais

SECURITY PLANE
→ identidade, Policy enforcement, Vault, Immune, privileged execution

INTERFACE PLANE
→ Panel, Terminal, external ingress, Notes
```

Esses planos não implicam seis processos obrigatórios.

---

# 3. CONTROL PLANE

## 3.1 Mission Core

Responsabilidades:

```text
aceitação da missão
lifecycle
command handling
policy binding
state transitions
replanning triggers
proof orchestration
```

Não executa ferramentas pesadas diretamente.

## 3.2 Cérebro

Subcapacidades lógicas:

```text
Cognitive Orchestrator
Context Engine
Knowledge Retrieval
AI Capability Router
Provider Capability Registry
Provider Adapters boundary
Quality Evaluator
Cost/Latency Router
Cognitive Evidence
```

Toda integração de IA pertence logicamente ao Cérebro.

## 3.3 Construction Engine

```text
objective decomposition
technical procedure synthesis
repository/workspace understanding
change planning
build/integration strategy
test strategy request
failure diagnosis
correction/retest loop
```

Ferramentas de terceiros são capabilities substituíveis.

## 3.4 Governor

```text
admission control
resource budgets
fairness multiprojeto
priorities
concurrency
preemption
health/progress governance
recovery budgets
```

## 3.5 Scheduler

```text
DAG-ready selection
ordering
critical-path awareness
aging
priority lanes
```

## 3.6 Proof Engine

```text
gate evaluation
independent verification
MISSION_PROVEN verdict
PRODUCT_MISSION_PROVEN verdict
```

---

# 4. MEMORY PLANE

Uma memória lógica soberana com stores especializados por responsabilidade.

Portas conceituais:

```text
MissionRepository
ProjectRepository
EventStore
StateStore
CommandInbox
Outbox
IdempotencyStore
CheckpointStore
EvidenceStore
ArtifactStore
IncidentStore
ApprovalStore
KnowledgeStore
CompetenceStore
NoteStore
```

Implementação física pode combinar ou separar esses stores.

Read Models e índices são derivados/reconstruíveis.

---

# 5. FEDERATION PLANE

Componentes lógicos:

```text
Federation Registry
Membership/Enrollment
Trust/Identity Manager
Capability Registry
Routing Engine
Transport Multiplexer
Node Inbox Contract
ACK/Result Coordinator
Lease/Generation/Fencing
Reconciliation Engine
Fleet Lifecycle Manager
Latency/Health Telemetry
```

Túnel Core pertence aqui como substrato de transporte/conectividade durável.

Regras:

```text
NO_PER_COMMAND_CONNECTION = TRUE
NO_HOT_PATH_POLLING = TRUE
ACK != RESULT
```

Transporte normal é persistente, autenticado e bidirecional quando disponível.

---

# 6. EXECUTION PLANE

Cada POD Engine possui:

```text
Stable Node Identity
Node Agent
Capability Discovery
Local Durable Inbox
Local Journal
Local Checkpoints
Execution Dispatcher
Micro-Scheduler
Fast Path
Governed Path
Capability Bridges
Health/Telemetry
Recovery/Reconnect
```

Tipos iniciais conceituais:

```text
POD Windows Engine
POD Linux Engine
```

A arquitetura admite Engines futuras sem alterar semântica de missão.

---

# 7. CAPABILITY BRIDGES

Capabilities são descobertas e registradas; não viram autoridade.

Exemplos:

```text
filesystem
shell
PowerShell
Bash
Python
Git
browser
database
build tools
containers
local AI
network tooling
testing tools
```

Contrato:

```text
DISCOVERED
→ VERIFIED
→ POLICY-ALLOWED
→ AVAILABLE
```

Ferramenta instalada não significa permissão automática para qualquer efeito.

---

# 8. PRIVILEGED EXECUTION

O Core/Cérebro não permanece elevado.

```text
POD
→ Privileged Execution Port
→ POD Privileged Executor
→ OS
```

Valida:

```text
identity
mission/project
policy
scope
operation class
resource
generation/expiry
audit
rollback/compensation metadata
```

Nunca contorna UAC, antivírus ou segurança do sistema.

---

# 9. SECURITY PLANE

Segurança é transversal.

Subcapacidades:

```text
Policy Enforcement
Identity/AuthN/AuthZ
Data Classification
Vault/Secret Broker
Audit/Redaction
Supply-chain controls
Runtime integrity
Immune detection/containment
Incident response
Quarantine/Revocation
```

Sistema Imunológico é mecanismo ativo da Segurança, não Policy concorrente.

---

# 10. INTERFACE PLANE

## Painel

```text
Query API / Read Models
Command API
Real event stream
```

Entrega cedo após fundação persistente e Core mínimo.

## Terminal

Cliente administrativo nativo que usa os mesmos contratos do Core.

## Bloco de Notas

Capacidade da Memória para captura rápida de pendências.

## Ingress externo

MCP, Action/HTTPS e futuros canais são adapters. Todos convergem para o mesmo Command Ingress durável.

---

# 11. FLUXO DE MISSÃO PONTA A PONTA

```text
USER / EXTERNAL AI / TERMINAL / PANEL
            |
            v
       INGRESS ADAPTER
            |
            v
     COMMAND INBOX DURÁVEL
            |
            v
     POLICY + MISSION CORE
            |
            v
          CÉREBRO
            |
            v
   CONSTRUCTION ENGINE
            |
            v
        GOVERNOR
            |
            v
        SCHEDULER
            |
            v
       FEDERATION
            |
            v
        POD ENGINE
            |
            v
  RESULT + EVIDENCE + CHECKPOINT
            |
            v
         MEMORY
            |
            v
      TEST / PROOF ENGINE
            |
      +-----+-----+
      |           |
   FALHOU      PROVOU
      |           |
   REPLAN     MISSION_PROVEN
```

---

# 12. FLUXO MULTI-PROVIDER

```text
CÉREBRO
→ Policy/Data Classification
→ AI Capability Router
→ Registry/Health
→ Provider Adapter
→ Provider/Local Model
→ Normalize
→ Validate/Challenge when required
→ Cognitive Result
→ CÉREBRO
```

Provider-specific SDK não entra no domínio.

---

# 13. FLUXO DE PERSISTÊNCIA

```text
COMMAND/DECISION/RESULT
→ VALIDATE
→ SOVEREIGN WRITE PORT
→ COMMIT
→ EVENT
→ ACK/CONFIRM
→ PROJECT READ MODELS ASYNC
```

Large evidence/artifacts podem usar content-addressed storage ou equivalente; o conceito obrigatório é hash + provenance + referência soberana.

---

# 14. FLUXO DE RECOVERY

```text
FAILURE/STALL
→ DETECT
→ CLASSIFY
→ CONTAIN
→ CHECK SOVEREIGN STATE
→ RECONCILE
→ REPLAN/RESTART/REASSIGN
→ TEST
→ RESUME
```

Restart sem diagnóstico é limitado por budget/backoff/circuit breaker.

---

# 15. MULTIPROJETO

Uma instalação POD atende múltiplos projetos.

Compartilhado:

```text
Core capabilities
Memory infrastructure
Governor
Federation
Engines
Panel/Terminal
Vault infrastructure
Privileged Executor
```

Isolado logicamente:

```text
project state
mission state
workspace
data/artifacts
authorizations
budgets
credentials scope
evidence
```

Governador aplica quotas, guaranteed share, controlled burst e starvation prevention.

---

# 16. SELF-UPDATE

Atualização usa caminho side-by-side/conceitualmente separável:

```text
CURRENT KNOWN-GOOD
→ CANDIDATE
→ VERIFY
→ MIGRATION CHECK
→ CANARY/ACTIVATE
→ HEALTH/REGRESSION
→ COMMIT OR ROLLBACK
```

Uma atualização nunca apaga missão persistida.

---

# 17. OBSERVABILIDADE

Health não é um booleano único.

Dimensões:

```text
LIVENESS
READINESS
PROGRESS
INTEGRITY
CAPACITY
CONNECTIVITY
RECOVERY_STATE
```

Métricas de performance por estágio devem permitir p50/p95/p99 quando aplicável.

---

# 18. FAST PATH / GOVERNED PATH

Fast Path aplica-se somente a operações:

```text
já autorizadas
reversíveis/limitadas
escopo conhecido
capability pronta
baixo risco
```

Governed Path aplica-se a:

```text
privileged
destructive
financial
production-sensitive
scope-changing
security-sensitive
unknown capability/effect
```

Seleção é do POD por Policy e classe de efeito; usuário não precisa escolher caminho técnico.

---

# 19. ZERO DONOR COUPLING

Arquitetura física e código final devem satisfazer:

```text
DONOR_RUNTIME_DEPENDENCIES = 0
DONOR_CODE_IMPORTS = 0
DONOR_PATH_REFERENCES = 0
DONOR_CONFIG_REFERENCES = 0
DONOR_SERVICE_DEPENDENCIES = 0
```

Conhecimento histórico pode existir em arquivo/auditoria, fora de build/runtime.

---

# 20. DECISÕES AINDA DELIBERADAMENTE ABERTAS

Serão escolhidas na consolidação técnica/implementação com prova:

```text
linguagem principal
banco físico
message bus
process topology
framework web
packaging/installer
transporte federado concreto
storage de artefatos
formato físico de Event Store
mecanismo de service supervision por SO
```

A escolha deve preservar os contratos já consolidados.

---

# 21. GATES ARQUITETURAIS

```text
LAYER_DEPENDENCY_GATE
NO_DIRECT_DB_MUTATION_GATE
POLICY_ENFORCEMENT_GATE
MULTIPROJECT_ISOLATION_GATE
FEDERATION_FENCING_GATE
ENGINE_ENVELOPE_GATE
PROVIDER_DECOUPLING_GATE
PRIVILEGED_EXECUTION_GATE
PANEL_COMMAND_PATH_GATE
ZERO_DONOR_COUPLING_GATE
PROOF_INDEPENDENCE_GATE
```

---

# 22. PRÓXIMO ARTEFATO

`POD_PLANO_MESTRE_DE_CONSTRUCAO_V001_20260902.md`