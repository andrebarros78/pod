# POD — CONTRATOS CONCEITUAIS ENTRE COMPONENTES — V001

**Data:** 02/09/2026  
**Status:** WORKING / NON-NORMATIVE  
**Base:** `POD_PROJETO_CONCEITUAL_RECONSOLIDADO_V001_20260902.md`  
**Escopo:** contratos conceituais, autoridade, entradas, saídas e limites entre os grandes componentes do POD  

---

# 0. REGRA CENTRAL

Este documento não escolhe banco, framework, protocolo físico, linguagem, quantidade de processos nem tecnologia de mensageria.

Ele responde somente:

```text
QUEM CHAMA QUEM
O QUE ENTRA
O QUE SAI
QUEM DECIDE
QUEM PODE VETAR
QUEM PERSISTE
QUEM EXECUTA
QUEM PROVA
QUEM RECUPERA
```

Princípio:

```text
NO_COMPETING_SOVEREIGN_AUTHORITIES = TRUE
```

---

# 1. MATRIZ SOBERANA DE AUTORIDADE

| Domínio | Autoridade principal | Pode vetar/limitar | Persistência soberana | Execução física | Prova |
|---|---|---|---|---|---|
| limites e permissões | Constituição / Policy | Segurança crítica | Memória | não executa | auditoria de policy |
| objetivo/estratégia técnica | Cérebro | Policy / Segurança | Memória | não executa | Proof Engine valida resultado |
| procedimento de construção | Engenharia de Construção | Policy / Cérebro / Segurança | Memória | via Engines | testes/evidência |
| prioridade/recursos/concorrência | Governador | Policy | Memória | coordena | health/progresso |
| estado soberano | Memória | regras de consistência | própria Memória | não executa | integridade/replay |
| roteamento federado | Federação | Policy / Governador | Memória + journal distribuído | não executa produto | reconciliação |
| execução local | Engine | Policy / envelope / fencing | journal/checkpoint | Engine | evidência de execução |
| segurança ativa | Sistema Imunológico | Policy | incidentes/evidências | contenção autorizada | security evidence |
| conclusão | Proof Engine | Policy / gates obrigatórios | verdict/evidência | não constrói | MISSION_PROVEN |

Nenhum componente pode ampliar silenciosamente seu escopo.

---

# 2. CONTRATO DE MISSÃO

Entrada mínima conceitual:

```text
mission_id
project_id
objective
constraints
acceptance_criteria
policy_version
priority
budget_policy
requested_target/node quando explícito
```

Fluxo:

```text
INGRESS
→ POLICY/VALIDAÇÃO
→ MISSION_ACCEPTED
→ CÉREBRO
→ PLANO/DECOMPOSIÇÃO
→ EXECUÇÃO
→ PROVA
→ MISSION_PROVEN
```

Saídas possíveis:

```text
MISSION_PROVEN
CANCELLED_BY_OWNER
SUPERSEDED
TERMINATED_BY_POLICY
IMPOSSIBLE_PROVEN
```

Estados intermediários não encerram obrigação:

```text
RUNNING
REPLANNING
RECOVERING
PAUSED
WAITING_EXTERNAL
WAITING_FINANCIAL_AUTHORIZATION
PROVING
```

---

# 3. CÉREBRO ↔ ENGENHARIA DE CONSTRUÇÃO

## Cérebro fornece

```text
objetivo técnico
contexto autorizado
critérios
restrições
prioridades
dependências conhecidas
risco
estratégia atual
```

## Engenharia devolve

```text
procedimento técnico
work units
pré-condições
capabilities necessárias
artefatos esperados
testes necessários
riscos técnicos
rollback/compensação quando aplicável
estimativa técnica de recursos
```

## Limites

```text
CÉREBRO decide O QUE e POR QUÊ
ENGENHARIA decide COMO construir dentro da estratégia
```

Engenharia pode propor replanejamento, mas não altera objetivo, Policy, orçamento financeiro ou critério soberano sozinha.

---

# 4. CÉREBRO ↔ MEMÓRIA

Cérebro lê projeções autorizadas de:

```text
missão
projeto
estado atual
histórico relevante
checkpoints
evidências
conhecimento
competências
incidentes
custos
```

Cérebro não escreve estado soberano diretamente. Ele emite decisões/comandos/fatos candidatos que passam pelo caminho oficial de persistência.

```text
MEMORY != AUTHORITY
KNOWLEDGE != POLICY
```

---

# 5. CÉREBRO ↔ IA MULTI-PROVIDER

O Cérebro é o dono lógico da API/camada cognitiva.

```text
AI_PROVIDER_API_OWNER = POD_BRAIN
PROVIDER != POD_BRAIN
MODEL != OPERATIONAL_AUTHORITY
```

Contrato de capacidade:

```text
capability_required
context_projection
data_classification
quality_target
latency_target
cost_policy
provider_constraints
validation_requirement
```

Fluxo:

```text
POLICY
→ CAPABILITY ROUTER
→ PROVIDER REGISTRY
→ ADAPTER
→ PROVIDER/MODEL
→ NORMALIZER
→ QUALITY/VALIDATION
→ CÉREBRO
```

Credenciais são resolvidas por `SecretRef`; nunca pertencem ao estado cognitivo.

---

# 6. ENGENHARIA ↔ GOVERNADOR

Engenharia pede capacidade de execução:

```text
work_unit
required_capabilities
resource_envelope
priority
dependencies
data locality
safety class
```

Governador responde:

```text
ADMIT
DEFER
THROTTLE
PREEMPT
REJECT_BY_POLICY
```

Governador não muda o objetivo técnico; ele controla quando e com quais recursos o trabalho pode ocorrer.

---

# 7. GOVERNADOR ↔ SCHEDULER

Scheduler recebe unidades `READY` e ordena execução respeitando:

```text
DAG
prioridade
critical path
dependências
fairness
aging
quotas
resource availability
```

Governador define limites, quotas, concorrência, preempção e fairness.

```text
SCHEDULER = ORDEM
GOVERNADOR = ADMISSÃO + RECURSOS + CONTINUIDADE
```

---

# 8. GOVERNADOR ↔ FEDERAÇÃO

Governador fornece envelope de execução e restrições.

Federação seleciona destino por:

```text
capability
health
resources
latency
affinity
data locality
warm state
transfer cost
security classification
```

Se o operador exigir um nó específico, a Federação respeita a escolha quando o nó for compatível e autorizado; não desloca silenciosamente.

---

# 9. FEDERAÇÃO ↔ ENGINE

Contrato de despacho inclui, conforme aplicável:

```text
mission_id
project_id
work_unit_id
attempt_id
command_id
node_id
generation
fencing_token
allowed_capabilities
data_scope
resource_budget
policy_version
expiry
idempotency_key
```

Fluxo mínimo:

```text
RECEBER
→ VALIDAR
→ PERSISTIR NODE INBOX
→ DEDUP
→ ACK/ACCEPTED
→ EXECUTAR
→ EVENTOS/PROGRESS
→ RESULT
→ EVIDENCE
→ RECONCILIAR
```

```text
ACK != RESULT
RESULT DELIVERY LOST != COMMAND NOT EXECUTED
```

---

# 10. ENGINE ↔ EVIDÊNCIA / CHECKPOINT

Engine produz fatos, não verdicts soberanos.

Saídas:

```text
stdout/stderr referenciado
exit status
file/artifact hashes
observed effects
metrics
checkpoint candidate
result candidate
failure fingerprint
```

A evidência deve possuir proveniência suficiente para vincular:

```text
mission → work_unit → attempt → command → node → generation → artifact/result
```

---

# 11. MEMÓRIA ↔ EVENT/STATE

Regra de mutação:

```text
VALIDAR
→ PERSISTIR
→ COMMIT
→ REGISTRAR EVENTO
→ CONFIRMAR
```

Separações:

```text
COMMAND != EVENT
EVENT != CURRENT STATE
ATTEMPT != MISSION
PROCESS != WORKER
CONNECTION != EXECUTION
READ MODEL != SOURCE OF TRUTH
```

Read Models, índices e caches são reconstruíveis.

---

# 12. SEGURANÇA ↔ TODOS

Toda ação material conceitualmente passa por:

```text
IDENTIDADE
→ PROJECT/MISSION SCOPE
→ POLICY
→ CAPABILITY
→ AUTHORIZATION/GATE
→ EXECUTION
```

Sistema Imunológico pode:

```text
DETECT
CONTAIN
QUARANTINE
REVOKE/ISOLATE dentro da autoridade concedida
TRIGGER RECOVERY
```

Não pode alterar Policy por conta própria.

Precedência:

```text
POLICY
> SEGURANÇA CRÍTICA / INTEGRIDADE
> AUTORIZAÇÃO SOBERANA
> OBJETIVO
> DECISÃO TÉCNICA
> GOVERNANÇA DE RECURSOS
> EXECUÇÃO LOCAL
```

---

# 13. LEARNING & TRAINING ↔ CÉREBRO / MEMÓRIA

Learning pode propor promoção de:

```text
FACT
PROCEDURE
COMPETENCE
EVIDENCE
```

Não pode promover diretamente:

```text
POLICY
AUTHORITY
PERMISSION
SECRET ACCESS
FINANCIAL AUTHORIZATION
```

Training atua somente em alvo externo autorizado e dados elegíveis.

---

# 14. PAINEL / TERMINAL ↔ CORE

```text
PAINEL/TERMINAL LÊ
→ Query API / Read Models

PAINEL/TERMINAL COMANDA
→ Command API
→ Policy
→ Core
→ persistência
→ execução
```

Proibido:

```text
mutação direta do banco
execução privilegiada direta
alteração direta de Policy
status inventado
```

Fechar interface não interrompe missão.

---

# 15. BLOCO DE NOTAS ↔ MEMÓRIA

Comandos naturais sem destino explícito:

```text
registre
anota
marca
guarda
```

criam uma nota persistente:

```text
STATUS = PENDÊNCIA
```

Nota não vira automaticamente task, Policy ou decisão arquitetural.

Promoção é explícita e preserva proveniência.

---

# 16. PROOF ENGINE ↔ MISSÃO

Proof Engine recebe:

```text
acceptance criteria
applied gates
artifacts
results
test reports
security evidence
recovery evidence
regression evidence
final checkpoint
known limitations
```

Decide apenas o verdict de prova.

```text
BUILDER_IS_NOT_SOLE_VERIFIER = TRUE
```

Para produto, conforme aplicabilidade:

```text
FUNCTIONAL_PROVEN
+ QUALITY_PROVEN
+ SECURITY_PROVEN
+ RECOVERY_PROVEN
+ EVIDENCE_PROVEN
= PRODUCT_MISSION_PROVEN
```

`NOT_APPLICABLE` exige justificativa registrada.

---

# 17. RECOVERY CONTRACT

Qualquer falha recuperável segue:

```text
DETECT
→ CONTAIN
→ PRESERVE STATE
→ DIAGNOSE
→ REPLAN/RECOVER
→ TEST
→ RECONCILE
→ RESUME
```

Recovery não apaga evidência, não mascara tentativa falha e não reexecuta cegamente comando cujo resultado possa já existir.

---

# 18. CONTRATO DE ECONOMIA DE EXECUÇÃO

Toda estratégia material pode considerar:

```text
financial cost
compute
elapsed time
API/token cost
network transfer
disk
energy/availability
data locality
warm cache
```

Regra:

```text
MORE_PARALLELISM != ALWAYS_MORE_EFFICIENT
```

Gasto financeiro novo nunca é inferido como autorizado.

---

# 19. INVARIANTES DE ACEITE DESTES CONTRATOS

```text
NO_COMPETING_SOVEREIGN_AUTHORITIES = TRUE
POLICY_PRECEDES_TECHNICAL_ACTION = TRUE
PERSIST_BEFORE_CONFIRM = TRUE
ACK_IS_NOT_RESULT = TRUE
CACHE_IS_NOT_SOURCE_OF_TRUTH = TRUE
PROVIDER_IS_NOT_BRAIN = TRUE
KNOWLEDGE_IS_NOT_POLICY = TRUE
STALE_GENERATION_CANNOT_COMMIT = TRUE
BUILDER_IS_NOT_SOLE_VERIFIER = TRUE
CONNECTION_IS_NOT_EXECUTION = TRUE
ACTIVITY_IS_NOT_PROGRESS = TRUE
```

---

# 20. PRÓXIMO ARTEFATO DERIVADO

Este documento alimenta diretamente:

`POD_MODELO_CANONICO_DE_DADOS_ESTADOS_E_EVENTOS_V001_20260902.md`

Sem ainda escolher implementação física.