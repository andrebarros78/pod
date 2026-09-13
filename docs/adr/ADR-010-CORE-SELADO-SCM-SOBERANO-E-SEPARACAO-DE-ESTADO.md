# ADR-010 — CORE SELADO, SCM SOBERANO E SEPARAÇÃO DE ESTADO

**Identificador:** POD-ADR-010
**Versão:** 1.0.0
**Status:** ACCEPTED
**Data:** 2026-09-13
**Conjunto alvo:** POD-DOCSET-V004
**Autoridade:** A1/A2
**Decisão:** separar estruturalmente Core, execução, cognição, dados e integrações; impedir acúmulo operacional no Core; instituir SCM soberano com admissão governada.

## 1. Contexto

O DOCSET V003 já estabelece POD multiprojeto, soberania do Mission Core, execução governada, memória persistente, evidência por hash, IA multi-provider e independência estrutural do ChatGPT.

A reconciliação V004 fecha lacunas ainda abertas:

- o termo Memory abrangia estado operacional, evidência, checkpoint, conhecimento e projeções sem classificação física suficiente;
- a fronteira entre Core e estado mutável não estava expressa como invariante de armazenamento;
- Knowledge Store existia, porém sem ciclo normativo completo de admissão, contradição, revalidação, supersessão e revogação;
- RAG, índices, vetores, grafo e cache não estavam explicitamente classificados como projeções reconstruíveis;
- integrações externas não estavam consolidadas em um plano lógico próprio;
- a atualização do Core não exigia imutabilidade de release e promoção atômica;
- missão não possuía um Execution Envelope único reunindo escopo, capacidades, recursos, retenção, rollback, evidência e política de conhecimento.

## 2. Decisão

O POD adota as seguintes fronteiras lógicas:

~~~text
CORE
CONTROL PLANE
COGNITION PLANE
EXECUTION PLANE
DATA PLANE
INTEGRATION PLANE
EXPERIENCE SURFACES
FEDERATION CAPABILITIES
SECURITY AS CROSS-CUTTING CONTROL
~~~

Planos são responsabilidades lógicas; não obrigam microserviços.

### 2.1 Core

O Core contém somente:

- bootstrap;
- identidade do POD;
- contratos fundamentais;
- composição mínima;
- kernel de governança necessário para iniciar e validar a plataforma.

O Core não contém dados de projeto, missão, evidência, checkpoint, cache, contexto temporário, índice, embedding, workspace ou histórico bruto de execução.

### 2.2 Releases

~~~text
CORE_RELEASE = IMMUTABLE
ACTIVE_RELEASE_POINTER = ATOMICALLY_MUTABLE
RUNTIME_CONFIGURATION = EXTERNAL
RUNTIME_STATE = EXTERNAL
SECRETS = EXTERNAL
FEATURE_FLAGS = EXTERNAL_AND_GOVERNED
~~~

Upgrade é preparado fora da release ativa, verificado e promovido atomicamente. Rollback troca a release ativa para uma versão previamente validada e executa reconciliação/health gate.

### 2.3 Classes de estado

Todo dado persistido deve ser classificado como:

~~~text
DURABLE
RECONSTRUCTIBLE
EPHEMERAL
~~~

DURABLE inclui estado soberano, conhecimento canônico, decisões, evidência obrigatória e checkpoints ainda necessários.

RECONSTRUCTIBLE inclui embeddings, índices lexicais, projeções de grafo, read models, materializações e caches derivados.

EPHEMERAL inclui temporários, downloads intermediários, staging e workspaces transitórios que não representam verdade durável.

Nada persiste sem classificação.

### 2.4 SCM

SCM significa **Sovereign Cognitive Memory** e é o subsistema cognitivo governado do POD.

SCM não é sinônimo de banco vetorial, RAG, log, histórico bruto ou checkpoint.

Composição lógica:

~~~text
SCM
├── Knowledge Admission
├── Canonical Knowledge
├── Knowledge Ledger
├── Distillation
├── Contradiction Resolution
├── Revalidation
└── Retrieval Interface
~~~

O conhecimento canônico é fonte durável. Vetores, índices lexicais, projeções de Knowledge Graph e cache são projeções reconstruíveis.

### 2.5 Admission Gate

Memory Distiller não grava diretamente conhecimento canônico.

~~~text
EXECUTION
→ KNOWLEDGE_CANDIDATE
→ PROVENANCE_CHECK
→ EVIDENCE_CHECK
→ SECRET_AND_SENSITIVE_FILTER
→ DEDUPLICATION
→ CONTRADICTION_CHECK
→ SCOPE_VALIDATION
→ CONFIDENCE_ASSIGNMENT
→ KNOWLEDGE_ADMISSION_GATE
→ CANONICAL_KNOWLEDGE
~~~

Falha em qualquer gate preserva o candidato no estado adequado, sem promoção silenciosa.

### 2.6 Ledger e estados cognitivos

Conhecimento é append-only no ledger. Alteração de entendimento gera evento de evolução, não sobrescrita destrutiva.

Estados mínimos:

~~~text
CANDIDATE
ACTIVE
DISPUTED
SUSPENDED
SUPERSEDED
REVOKED
QUARANTINED
DEPRECATED
~~~

Eventos mínimos:

~~~text
knowledge.candidate_created
knowledge.admitted
knowledge.rejected
knowledge.reinforced
knowledge.disputed
knowledge.superseded
knowledge.suspended
knowledge.revoked
knowledge.revalidation_requested
knowledge.revalidated
knowledge.distillation_requested
~~~

Conhecimento REVOKED, SUSPENDED, QUARANTINED ou SUPERSEDED não participa de retrieval ativo, salvo consulta explícita de auditoria.

### 2.7 Scope obrigatório

Conhecimento promovido declara explicitamente seu escopo aplicável. O contrato suporta, no mínimo:

~~~text
global
platform
project_id
environment
operating_system
component
version_range
valid_from
valid_until
~~~

Ausência de escopo suficiente impede admissão.

### 2.8 Confidence e freshness

~~~text
confidence = qualidade da sustentação/evidência
freshness = atualidade da validação
~~~

Tempo não reduz arbitrariamente confidence. Conhecimento pode manter alta confidence e possuir freshness expirada, exigindo revalidação antes de uso de alto risco.

### 2.9 Revalidação

Revalidação pode ser acionada por:

- tempo;
- mudança de versão;
- mudança de API;
- mudança de sistema operacional;
- mudança de dependência;
- mudança de configuração;
- contradição;
- criticidade da missão;
- uso de conhecimento com freshness inadequada.

~~~text
REVALIDATE_BY_TIME
+ REVALIDATE_BY_EVENT
+ REVALIDATE_BY_RISK
~~~

### 2.10 Destilação não é barreira global

Conclusão de execução não depende globalmente da promoção cognitiva.

A missão persiste resultado/checkpoint e pode prosseguir, emitindo `KNOWLEDGE_DISTILLATION_REQUESTED`. Somente um próximo passo que dependa especificamente do conhecimento ainda não admitido pode esperar por esse resultado.

### 2.11 Evidence Store por conteúdo

Artefatos e evidências grandes devem suportar endereçamento por conteúdo:

~~~text
sha256:<digest>
~~~

A mesma carga física pode ser referenciada por várias missões sem duplicação de bytes, preservando classificação, proveniência, ownership e retenção por referência.

### 2.12 Execution Envelope

Toda missão aceita possui envelope efetivo contendo, direta ou referencialmente:

~~~text
mission_id
project_id
objective
constraints
allowed_capabilities
security_scope
resource_budget
workspace_policy
retention_policy
timeout_policy
rollback_policy
evidence_policy
knowledge_policy
integration_policy
~~~

Executor não amplia esse envelope.

### 2.13 Integration Plane

Toda dependência externa entra por porta/adaptador controlado.

~~~text
POD INTERNAL CONTRACT
→ INTEGRATION ADAPTER
→ EXTERNAL PROVIDER
~~~

É proibido tornar protocolo, API ou produto externo uma dependência estrutural do domínio ou do Core.

## 3. Invariantes

~~~text
NOTHING_EXECUTES_WITHOUT_SCOPE = TRUE
NOTHING_PERSISTS_WITHOUT_CLASSIFICATION = TRUE
NOTHING_BECOMES_KNOWLEDGE_WITHOUT_EVIDENCE = TRUE
NOTHING_EXTERNAL_BECOMES_STRUCTURAL_DEPENDENCY = TRUE

CORE_CONTAMINATION = 0
PROJECT_DATA_IN_CORE = 0
MISSION_DATA_IN_CORE = 0
TEMP_DATA_IN_CORE = 0
REGENERABLE_DATA_IN_CORE = 0
UNTRACEABLE_KNOWLEDGE = 0
UNSCOPED_KNOWLEDGE = 0
UNREVERSIBLE_KNOWLEDGE = 0
~~~

## 4. Governança física de memória

SCM deve publicar métricas, no mínimo:

~~~text
SCM_TOTAL_SIZE
SCM_OBJECT_COUNT
SCM_GROWTH_RATE
DUPLICATION_RATIO
STALE_KNOWLEDGE_RATIO
UNVALIDATED_CANDIDATES
REVALIDATION_BACKLOG
~~~

A política pode impor limites por `project_id`, tipo, origem, idade, confidence e freshness.

Regra:

~~~text
KNOWLEDGE_GROWTH = ALLOWED + MEASURED + JUSTIFIED + COMPACTABLE
~~~

Repetições equivalentes reforçam objeto existente quando semanticamente correto, em vez de criar cópia integral.

## 5. Consequências

### Positivas

- Core permanece pequeno, estável e auditável;
- projetos e missões crescem sem contaminar a plataforma;
- conhecimento permanente possui prova, escopo e reversibilidade;
- projeções cognitivas podem ser descartadas e reconstruídas;
- fornecedor externo permanece substituível;
- rollback de Core e rollback cognitivo tornam-se explícitos;
- retenção e higiene física ficam testáveis.

### Custos

- mais contratos de classificação;
- ledger cognitivo e revalidação precisam ser implementados;
- armazenamento por conteúdo exige gestão de referências e garbage collection seguro;
- promoção de release exige pipeline de saúde e rollback.

## 6. Compatibilidade

Esta decisão preserva:

- multiprojeto do ADR-008;
- independência do ChatGPT e IA híbrida do ADR-009;
- autoridade de missão do ADR-003;
- persistência atômica do ADR-004;
- segurança desde F0 do ADR-007;
- federação e delegação governadas.

Onde o DOCSET V003 utilizar `Memory` como termo amplo, V004 deve distinguir Operational State, Evidence, Checkpoint e SCM conforme esta decisão.

## 7. Critérios de aceite

A implementação somente pode afirmar esta arquitetura como PROVEN quando houver evidência de:

- Core imutável por release;
- configuração, segredo e estado fora da release;
- projetos e missões fisicamente fora do Core;
- classificação DURABLE/RECONSTRUCTIBLE/EPHEMERAL aplicada;
- Admission Gate testado;
- conhecimento sem proveniência rejeitado;
- conhecimento sem escopo rejeitado;
- contradicão não sobrescrita silenciosamente;
- revogação removendo conhecimento do retrieval ativo;
- projeções destruídas e reconstruídas sem perda canônica;
- Evidence Store verificando hash;
- deduplicação física por conteúdo;
- métricas de crescimento do SCM;
- rollback de release;
- `CORE_CONTAMINATION=0` e `UNEXPECTED_RESIDUE=0` após missão de teste.
