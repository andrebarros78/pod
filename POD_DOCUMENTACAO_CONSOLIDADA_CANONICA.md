# POD — DOCUMENTAÇÃO CONSOLIDADA CANÔNICA

**Versão:** 4.0.0-DRAFT-CANONICAL  
**Data-base:** 03/10/2026  
**Status:** DOCUMENTAÇÃO CONSOLIDADA PARA BASELINE  
**Estado de implementação:** conceitual/executivo; não presume implementação, instalação ou integração realizada.  
**Produto:** POD — Plataforma Orquestradora Durável

---

# 0. AUTORIDADE E PRECEDÊNCIA

Este documento reconcilia e consolida o estado arquitetural atual do POD a partir de:

1. `POD_PROJETO_CONSOLIDADO_v3.md`;
2. `POD_RECONCILIACAO_CONVERSA_GOVERNADOR_EXECUTION_FABRIC_ADE.md`;
3. `POD_BASELINE_CANONICA_AQUISICAO_EVOLUCAO_HIGIENE_v1.0.md`;
4. `PROJECT_EXECUTION_STANDARD.md`;
5. `ANTI_HALLUCINATION_STANDARD.md`;
6. `NORMA_TRANSVERSAL_DE_ENGENHARIA_DE_SEGURANCA`.

A v3 permanece a principal síntese anterior, mas é atualizada por duas decisões posteriores:

- o ADE passa a existir explicitamente como Executor Autônomo de Desenvolvimento e Correção;
- a estratégia de construção passa a adotar `REUSE FIRST`, com aquisição, sanitização, normalização, qualificação, contextualização, validação, contratualização e integração antes de construir novamente capacidades maduras.

As três normas transversais permanecem obrigatórias como documentos especializados enquanto não forem integralmente absorvidas por revisão formal sem perda de requisitos.

Material anterior incompatível é histórico e não orienta nova implementação.

---

# PARTE I — IDENTIDADE E OBJETIVO

## 1. O QUE É O POD

POD é uma **Plataforma Orquestradora Durável**, soberana e multiprojeto, destinada a transformar objetivos humanos em produtos e resultados técnicos efetivamente construídos, adquiridos quando vantajoso, integrados, testados, recuperáveis, documentados e comprovados.

O POD não é:

- chat;
- prompt;
- painel;
- MCP;
- wrapper de IA;
- conjunto de scripts;
- executor remoto simples;
- coding agent isolado;
- federação de governos concorrentes;
- sistema dependente de ChatGPT ou de um único provedor;
- sistema que trata atividade como conclusão.

O usuário define principalmente:

- objetivo;
- resultado esperado;
- regras de negócio;
- restrições;
- orçamento;
- prazo quando aplicável;
- portões humanos indispensáveis.

O POD assume o caminho técnico.

## 2. RESULTADO HUMANO DESEJADO

```text
OBJETIVO HUMANO
→ POD COMPREENDE
→ POD DECIDE
→ POD PESQUISA O QUE JÁ EXISTE
→ POD ADQUIRE OU CONSTRÓI
→ POD EXECUTA
→ POD OBSERVA
→ POD TESTA
→ POD DIAGNOSTICA
→ POD CORRIGE
→ POD RECUPERA
→ POD INTEGRA
→ POD REGRESSIONA
→ POD PRODUZ EVIDÊNCIA
→ POD CRIA CHECKPOINT
→ POD PROVA
→ MISSION_PROVEN
```

Falha recuperável é trabalho do POD, não do usuário.

---

# PARTE II — INVARIANTES SOBERANOS

## 3. UMA SOBERANIA LÓGICA

```text
ONE BRAIN
ONE GOVERNOR
ONE PROJECT REGISTRY
ONE MISSION REGISTRY
ONE OPERATIONAL MEMORY LOGIC
ONE GLOBAL LOGICAL QUEUE
ONE AUTHORIZATION MODEL
ONE GIT POLICY
ONE EVIDENCE / LEDGER MODEL
ONE CONTROL PLANE

N EXECUTION NODES
N OPERATING SYSTEMS
N PROVIDERS
N CAPABILITIES
N THIRD-PARTY COMPONENTS
```

Execução pode ser distribuída. Soberania operacional não.

Alta disponibilidade, replicação e failover não autorizam duas autoridades concorrentes sobre a mesma verdade.

## 4. INTELIGÊNCIA ≠ AUTORIDADE

O Cérebro pensa e propõe.

O Governador valida política, estado, autorização e compromisso operacional.

Executores executam.

Nenhum componente pode assumir silenciosamente responsabilidade de outro.

## 5. MULTIPROJETO

```text
1 INSTALAÇÃO POD
→ N PROJETOS
```

Cada projeto possui `project_id` persistente e isolamento de:

- objetivo;
- escopo;
- missões;
- tarefas;
- workspace;
- branches/worktrees;
- checkpoints;
- evidências;
- artefatos;
- autorizações contextuais;
- recursos;
- incidentes;
- histórico.

Serviços soberanos comuns não são duplicados por projeto.

## 6. ZERO DONOR COUPLING NORMALIZADO

WMCP, LMCP e outros sistemas históricos não participam do runtime final do POD.

São permitidos como fontes de:

- algoritmos;
- contratos;
- padrões;
- testes;
- experiência;
- recovery;
- memória;
- governança;
- falhas aprendidas.

É proibido no produto final:

```text
DONOR_RUNTIME_DEPENDENCIES > 0
DONOR_LEGACY_PATH_REFERENCES > 0
DONOR_LEGACY_CONFIG_REFERENCES > 0
DONOR_LEGACY_SERVICE_DEPENDENCIES > 0
DONOR_SOVEREIGN_AUTHORITY > 0
```

A regra não proíbe bibliotecas e componentes OSS maduros. Componentes de terceiros são permitidos sob contratos POD, sanitização, qualificação e substituibilidade.

---

# PARTE III — NÚCLEO BLINDADO

## 7. REGRA DE NÃO-INCHAÇO

O núcleo guarda **o que está acontecendo**, não **o que foi produzido**.

Pode conter:

- IDs de projeto, missão e tarefa;
- estados e transições;
- leases;
- fencing tokens;
- autorizações;
- registros de nós/capacidades;
- ledger com hash e ponteiro;
- referências a segredos;
- metadados mínimos necessários à soberania.

Nunca contém:

- código gerado;
- builds;
- logs completos;
- outputs de comando;
- evidências em conteúdo bruto;
- respostas completas de IA;
- conhecimento de longo prazo;
- cache;
- temporários;
- artefatos descartáveis.

Regras:

```text
CORE_STORES_CONTENT=false
CORE_EXECUTES_GENERATED_CODE=false
CORE_RUNS_PRIVILEGED=false
CORE_UNSAFE_CODE=0
CORE_DIRECT_ENTRYPOINTS=1
CORE_MAX_RECORD_SIZE=<definir por medição>
CORE_MAX_DB_SIZE=<definir por medição>
```

O núcleo deve permanecer pequeno, auditável, estável sob carga prolongada e resistente a inchaço.

---

# PARTE IV — ARQUITETURA CONSOLIDADA

## 8. VISÃO GERAL

```text
HUMANO
  │
  ├── Terminal
  └── Painel
        │
        ▼
   COMMAND API
        │
        ├───────────────┐
        │               │
        ▼               │
     CÉREBRO             │
        │ propõe         │
        ▼               │
    GOVERNADOR ◀─────────┘
        │
        ├── Project Registry
        ├── Mission Registry
        ├── Task Graph
        ├── Scheduler Global
        ├── Resource Governor
        ├── Authorization
        ├── Git Policy
        ├── Recovery Coordination
        ├── Checkpoints
        └── Evidence/Ledger
        │
        ▼
ENGENHARIA DE CONSTRUÇÃO
        │
        ▼
       ADE
        │
        ▼
 EXECUTION FABRIC
    ├── Executor Linux
    ├── Executor Windows
    └── futuros nós
        │
        ▼
 Recursos reais / Sandboxes

Transversais:
Segurança · Verdade/Evidência · Recovery/Imunológico · Observabilidade

Fora do núcleo:
Workspaces/Git · Object Store · Conhecimento · Cofre · Providers · componentes especializados
```

## 9. CÉREBRO SOBERANO

Responsabilidades:

- compreender intenção;
- decompor objetivo;
- planejar;
- comparar alternativas;
- decidir arquitetura;
- selecionar estratégia;
- pesquisar quando necessário;
- avaliar conhecimento;
- diagnosticar;
- replanejar;
- interpretar evidências;
- coordenar engenharia.

Não pode:

- conceder autorização a si próprio;
- executar irrestritamente como root/Administrator;
- escrever diretamente no banco soberano;
- alterar evidência passada;
- declarar sucesso sem critério verificável;
- ser a única fonte da própria certificação.

## 10. GOVERNADOR SOBERANO

É a autoridade operacional única.

Possui e coordena:

- Project Registry;
- Mission Registry;
- Task Graph;
- Scheduler Global;
- Resource Governor;
- Conflict Resolver;
- Authorization;
- Git Policy;
- Recovery Coordination;
- Node Registry;
- Capability Registry;
- Checkpoint Registry;
- Incident Registry;
- Evidence/Ledger;
- estado e transições;
- leases;
- fencing;
- prioridades.

Motores externos de workflow podem fornecer durabilidade, timers, retries e entrega de atividades, mas não se tornam Governador.

## 11. MEMÓRIA SOBERANA

A memória lógica do POD é persistente e independente de chat.

```text
POD MEMORY
├── OPERACIONAL
├── DOCUMENTAL
├── CONHECIMENTO
├── APRENDIZADO
├── EVIDÊNCIAS
├── CHECKPOINTS
└── HISTÓRICO
```

Queda de navegador, ChatGPT, conexão, worker, processo ou máquina não pode apagar obrigação assumida.

Memória não é prova atual.

## 12. ENGENHARIA DE CONSTRUÇÃO

Define como construir corretamente:

- contratos;
- módulos;
- responsabilidades;
- critérios de aceite;
- gates;
- integração;
- testes;
- segurança;
- evidência;
- fechamento;
- versionamento.

## 13. ADE — EXECUTOR AUTÔNOMO DE DESENVOLVIMENTO E CORREÇÃO

O ADE trabalha autonomamente no software.

Deve:

- inspecionar repositórios;
- compreender código;
- desenvolver;
- modificar;
- refatorar;
- corrigir bugs;
- administrar dependências autorizadas;
- compilar;
- executar;
- testar;
- diagnosticar;
- corrigir;
- retestar;
- integrar;
- regressionar;
- produzir evidência.

Loop:

```text
INSPECIONAR
→ COMPREENDER
→ PLANEJAR ALTERAÇÃO
→ IMPLEMENTAR
→ EXECUTAR
→ OBSERVAR
→ TESTAR
   ├─ FAIL → DIAGNOSTICAR → ISOLAR CAUSA → MUDAR TENTATIVA → CORRIGIR → RETESTAR
   └─ PASS → INTEGRAR → REGRESSIONAR → EVIDÊNCIA → CHECKPOINT → PROVAR
```

```text
FAIL != STOP
ERROR != STOP
TEST_FAILED != STOP
REGRESSION != STOP
```

Coding agents externos podem ser utilizados como providers do ADE.

## 14. EXECUTION FABRIC

Fornece:

- Node Registry;
- Capability Discovery;
- routing;
- durable inbox quando aplicável;
- dispatch;
- ACK;
- leases;
- fencing;
- heartbeat;
- health;
- eventos/resultados;
- reconnect;
- reconciliation.

O Governador solicita capacidades. O Fabric seleciona nó adequado conforme capacidade, autorização, saúde, recursos e conflitos.

Uma missão pode atravessar Linux e Windows mantendo o mesmo `mission_id`.

---

# PARTE V — REUSE FIRST E AQUISIÇÃO

## 15. REGRA REUSE FIRST

Antes de construir capacidade nova:

```text
PESQUISAR
→ ANALISAR
→ COMPARAR
→ SELECIONAR
→ ADQUIRIR
→ SANITIZAR
→ NORMALIZAR E QUALIFICAR
→ APERFEIÇOAR
→ CONTEXTUALIZAR
→ VALIDAR
→ CONTRATUALIZAR
→ INTEGRAR
→ PROVAR
```

Construir do zero somente quando:

- não existir solução adequada;
- solução existente violar invariantes;
- custo/risco/lock-in forem maiores;
- integração segura for inviável;
- diferencial soberano exigir implementação própria.

## 16. PIPELINE DE AQUISIÇÃO

### AQUISIÇÃO
Obter componente oficial e registrar proveniência, versão, licença, dependências, custo e motivo.

### SANITIZAÇÃO
Revisar supply chain, vulnerabilidades, segredos, telemetria, permissões, privilégios, conexões, instalação e defaults.

### NORMALIZAÇÃO E QUALIFICAÇÃO
Encapsular atrás de contrato POD, impedir vazamento de tipos, medir vantagem, ownership e sobreposição.

### CONTEXTUALIZAÇÃO
Definir onde pertence, responsabilidade, autoridade permitida/proibida, fronteira de segurança e recovery.

### VALIDAÇÃO
Executar testes reais de função, erro, restart, persistência, recovery, concorrência, segurança e regressão.

### CONTRATUALIZAÇÃO
Congelar interface, schema, erros, versão, dados, autorização, limites, atualização, rollback, substituição e remoção.

### INTEGRAÇÃO
Conectar ao fluxo real e provar resultado de ponta a ponta.

## 17. SELEÇÃO INICIAL PARA QUALIFICAÇÃO

| Domínio | Candidato selecionado | Papel permitido |
|---|---|---|
| Memória longa | Mem0 | implementação de memória, não prova/soberania |
| Memória relacional/temporal | Graphiti | camada opcional, após teste |
| Cérebro/orquestração | LangGraph | runtime de orquestração atrás de contrato POD |
| ADE | OpenHands | provider especializado, não soberania |
| Durable execution | Temporal | motor durável do Governador, não Governador |
| Policy engine | Cedar | avaliação de autorização sob modelo POD |
| Vetores | PostgreSQL + pgvector | persistência vetorial junto ao PostgreSQL |
| Tools externas | MCP | protocolo de borda/adapters |
| Observabilidade | OpenTelemetry | telemetria padronizada |
| Cofre | OpenBao | candidato a qualificação |
| Sandbox alto risco | Firecracker | candidato a qualificação |
| Mensageria adicional | NATS JetStream | somente se necessidade não coberta for provada |

Status de todos os itens: seleção documental; aquisição/integração não presumidas.

---

# PARTE VI — PROJETOS, MISSÕES E ESTADO

## 18. PROJECT REGISTRY

Cada projeto registra no mínimo:

```text
project_id
name
objective
scope
out_of_scope
status
workspace
repository
default_branch
risk_class
resource_policy
security_profile
acceptance_contract
created_at
updated_at
```

## 19. MISSION REGISTRY

Cada missão registra:

```text
mission_id
project_id
objective
scope
acceptance_criteria
status
priority
authorization_context
task_graph
resource_claims
evidence_requirements
checkpoint
failure_state
recovery_state
created_at
updated_at
```

Missão iniciada permanece obrigação até:

- `MISSION_PROVEN`;
- cancelamento soberano explícito;
- impossibilidade externa comprovada;
- bloqueio humano real registrado.

## 20. CORRELAÇÃO DE NOVAS ORDENS

Antes de criar missão:

```text
CONTINUATION
OBJECTIVE_UPDATE
COMPATIBLE_SUBTASK
SAFE_PARALLEL_WORK
SUPERSEDING_ORDER
REAL_CONFLICT
NEW_MISSION
```

Somente `NEW_MISSION` cria missão independente.

## 21. ESTADOS DE MISSÃO

```text
CREATED
CORRELATED
PLANNING
READY
RUNNING
WAITING_DEPENDENCY
WAITING_HUMAN_GATE
RECOVERING
VALIDATING
REGRESSION
FINALIZING
MISSION_PROVEN
BLOCKED_EXTERNAL
CANCELLED
FAILED_UNRECOVERABLE
```

Transições devem ser explícitas, persistidas e auditáveis.

---

# PARTE VII — SEGURANÇA

## 22. PRINCÍPIOS OBRIGATÓRIOS

- Security by Design;
- Security by Default;
- Security by Verification;
- Security by Containment;
- Least Privilege;
- Deny by Default;
- Fail Closed;
- Minimize Attack Surface;
- Defense in Depth;
- Assume Breach;
- Evidence by Construction;
- Non-Bypassable Gates.

Regra:

```text
SEM_AUTORIZACAO_EXPLICITA=NEGADO
```

Código gerado nunca roda no núcleo.

Operação privilegiada somente por executor dedicado, identificado, autorizado, limitado e auditado.

Componente de terceiro não recebe confiança automática.

## 23. PORTÕES HUMANOS

Portão humano somente quando necessário, incluindo:

- gasto novo;
- conta externa;
- credencial pessoal;
- MFA/CAPTCHA;
- ação irreversível;
- aprovação jurídica/comercial;
- produção quando exigida;
- publicação externa sensível.

O portão bloqueia somente o ramo dependente.

---

# PARTE VIII — VERDADE, EVIDÊNCIA E PROVA

## 24. ESTADOS DE CONHECIMENTO

```text
VERIFIED
INFERRED
HYPOTHESIS
NOT_VERIFIED
UNKNOWN
```

Memória, documentação, probabilidade ou confiança não promovem estado para `VERIFIED`.

## 25. ESCADA ÚNICA DE PROVA

```text
MODULE_PROVEN
→ INTEGRATION_PROVEN
→ MISSION_PROVEN
→ PRODUCT_PROVEN
→ SEALED
```

Não contam como prova final:

- código escrito;
- build aprovado;
- processo ativo;
- endpoint respondendo;
- commit criado;
- painel verde;
- componente instalado;
- agente registrado;
- aquisição concluída sem validação.

## 26. PROVAS MÍNIMAS

```text
INTEGRAÇÃO:
PRODUTOR → CONTRATO → TRANSPORTE → CONSUMIDOR → RESULTADO

PERSISTÊNCIA:
WRITE → RESTART → READ → STATE_MATCH

RECOVERY:
FAIL/STOP → DETECT → RECOVER → RECONNECT → RESTORE → RESUME → RESULT

CORREÇÃO:
REPRODUZIR FALHA → CORRIGIR → RETESTAR → FALHA NÃO OCORRE → REGRESSÃO
```

## 27. MISSION_PROVEN

```text
RESULTADO
+ TESTE REAL
+ CRITÉRIO DE ACEITE
+ EVIDÊNCIA
+ REGRESSÃO
+ CHECKPOINT FINAL
= MISSION_PROVEN
```

---

# PARTE IX — CICLO DE CONSTRUÇÃO E INTEGRAÇÃO

## 28. MÓDULO

Cada módulo possui:

- objetivo;
- responsabilidade;
- inputs;
- outputs;
- dependências;
- consumidores;
- interfaces;
- estado;
- persistência;
- erro;
- segurança;
- recovery;
- critérios de aceite;
- fora de escopo.

Fluxo:

```text
MODULE_ORDERED
→ INSPECIONAR
→ DEFINIR BASELINE
→ ADQUIRIR OU IMPLEMENTAR
→ EXECUTAR
→ OBSERVAR
→ TESTAR
→ DIAGNOSTICAR
→ CORRIGIR
→ RETESTAR
→ ENDURECER
→ REGRESSÃO
→ COMPROVAR
→ MODULE_PROVEN
→ FECHAR
→ VERSIONAR
→ MODULE_SEALED
```

## 29. INTEGRAÇÃO

Somente módulos/capacidades comprovados entram na integração final.

```text
DISCOVER_CONTRACTS
→ VALIDATE_CONTRACTS
→ INTEGRATE
→ OBSERVE_REAL_FLOW
→ RECONCILE
→ TEST
→ CORRECT
→ RETEST
```

Reconciliação procura:

- múltiplas fontes de verdade;
- dados duplicados;
- contratos divergentes;
- versões incompatíveis;
- race conditions;
- dependências circulares;
- eventos perdidos;
- filas órfãs;
- producers/consumers ausentes;
- configuração contraditória;
- inconsistência após restart;
- responsabilidades duplicadas;
- implementações concorrentes.

---

# PARTE X — STACK E DECISÕES TECNOLÓGICAS

## 30. CAMADAS SOBERANAS

Mantém-se como direção arquitetural:

| Parte | Direção |
|---|---|
| Núcleo / Governador | Rust |
| Execution Fabric | Rust |
| Executores Linux/Windows | Rust + shell/PowerShell restritos |
| Estado soberano | SQLite inicialmente → PostgreSQL |
| Contratos | Protobuf + JSON Schema |
| Terminal | Rust |
| Painel | TypeScript + HTML/CSS |
| Modelagem formal | TLA+ para estados/leases/fencing |
| Código produzido | linguagem adequada ao produto, sempre fora do núcleo |

### Revisão necessária — Cérebro

A antiga regra de orquestração exclusivamente em Rust passa a ser **aberta por ADR** para permitir runtime especializado de agente em processo isolado, desde que:

- não toque diretamente o núcleo;
- opere atrás de contratos POD;
- seja substituível;
- não se torne autoridade;
- não seja fonte única de prova.

Essa abertura é necessária para compatibilizar a nova política `REUSE FIRST` com componentes maduros de orquestração.

---

# PARTE XI — TESTES MÍNIMOS DA PLATAFORMA

## 31. MATRIZ MÍNIMA

```text
INSTALL
START
RESTART
REBOOT
PROJECT_CREATE
MULTIPROJECT_ISOLATION
MISSION_CORRELATION
DUPLICATE_COMMAND
IDEMPOTENCY
CONFLICT_DETECTION
LEASE
FENCING
STALE_WORKER
LINUX_EXECUTION
WINDOWS_EXECUTION
CROSS_PLATFORM_MISSION
NETWORK_PARTITION
STATE_RECONCILIATION
RECOVERY
GIT_POLICY
SECRET_HANDLING
AUTHORIZATION_DENIAL
FAIL_CLOSED
PROVIDER_FAILURE
BRAIN_REPLAN
EVIDENCE_CHAIN
REGRESSION
DONOR_DECOUPLING
THIRD_PARTY_COMPONENT_FAILURE
COMPONENT_REPLACEMENT
ENDURANCE
UPDATE
ROLLBACK
CORE_SIZE_STABLE
REFERENCE_MISSION
```

---

# PARTE XII — GOVERNANÇA DOCUMENTAL

## 32. ESTRUTURA CANÔNICA

```text
POD_DOCUMENTACAO_CONSOLIDADA_CANONICA.md  ← fonte arquitetural consolidada
POD_BASELINE_CANONICA_AQUISICAO_EVOLUCAO_HIGIENE.md
ADR/                                      ← mudanças arquiteturais
SCHEMAS/                                  ← contratos formais
CONTRACTS/                                ← contratos de projeto/módulo/componente
RUNBOOKS/                                 ← operação
EVIDENCE/                                 ← provas
RELEASES/                                 ← manifestos
HISTORY/                                  ← material histórico, NORMATIVE=false
```

Normas transversais especializadas permanecem obrigatórias e complementares:

- `NORMA_TRANSVERSAL_DE_ENGENHARIA_DE_SEGURANCA`;
- `ANTI_HALLUCINATION_STANDARD`;
- `PROJECT_EXECUTION_STANDARD`.

A futura absorção dessas normas pela fonte única exige reconciliação formal linha a linha ou matriz de rastreabilidade que prove ausência de perda normativa.

## 33. PRECEDÊNCIA

Quando houver conflito:

```text
DECISÃO FORMAL MAIS NOVA E COMPATÍVEL
>
REGRA HISTÓRICA
```

Mas nenhuma decisão ordinária pode reduzir requisitos obrigatórios de segurança, verdade/evidência ou gates sem ADR e exceção formal válida quando aplicável.

---

# PARTE XIII — ROADMAP RECONCILIADO

## 34. FASE 0 — BASELINE E HIGIENE

- consolidar fonte canônica;
- eliminar soberanias/documentos concorrentes;
- registrar ADRs necessários;
- instituir pipeline de aquisição;
- inventariar capacidades já existentes no mercado;
- congelar construção prematura de capacidades maduras.

Saída: `BASELINE_RECONCILED`.

## 35. FASE 1 — CONTRATOS E MODELO FORMAL

- Project/Mission/Task;
- estados;
- leases/fencing;
- autorização;
- EvidenceRecord;
- contratos de componente;
- TLA+ para invariantes críticos.

Saída: `CORE_CONTRACTS_DEFINED`.

## 36. FASE 2 — FATIA VERTICAL MÍNIMA

Uma ordem entra → Governador → executor → teste → evidência → checkpoint → conclusão simples.

Ao mesmo tempo, provar substituibilidade de pelo menos um componente adquirido.

Saída: `MVP_PROVEN`.

## 37. FASES POSTERIORES

- Governador completo;
- Cérebro + Provider Manager;
- Windows + cross-platform;
- ADE + Engenharia de Construção;
- Memória/Conhecimento;
- Recovery/Imunológico;
- Terminal/Painel;
- provas de plataforma;
- missão real de referência;
- selagem independente.

Nenhuma fase avança por aparência de funcionamento.

---

# PARTE XIV — GATES DE AQUISIÇÃO E INTEGRAÇÃO

## 38. COMPONENT ACQUISITION GATE

```text
SOURCE_VERIFIED
LICENSE_VERIFIED
SUPPLY_CHAIN_CHECK
SECURITY_SANITIZATION
DEPENDENCY_REVIEW
PRIVILEGE_REVIEW
NETWORK_REVIEW
TELEMETRY_REVIEW
ROLLBACK_DEFINED
REMOVAL_DEFINED
```

## 39. COMPONENT QUALIFICATION GATE

```text
RESPONSIBILITY_DEFINED
POD_INTERFACE_DEFINED
NO_TYPE_LEAKAGE
DATA_OWNERSHIP_DEFINED
AUTHORITY_BOUNDARY_DEFINED
FAILURE_CONTRACT_DEFINED
RECOVERY_DEFINED
OBSERVABILITY_DEFINED
BENEFIT_MEASURED
OVERLAP_RESOLVED
```

## 40. COMPONENT INTEGRATION GATE

```text
REAL_FLOW_PASS
SECURITY_PASS
PERSISTENCE_PASS_OR_NA
RECOVERY_PASS_OR_NA
REGRESSION_PASS
NO_SOVEREIGNTY_LEAK
NO_LEGACY_DONOR_COUPLING
REMOVAL_TESTED_WHEN_CRITICAL
```

Gate ausente = `NOT_PROVEN`.

---

# PARTE XV — PRINCÍPIOS TERMINAIS

## 41. FÓRMULA POD

```text
POD
=
CÉREBRO SOBERANO
+ GOVERNADOR SOBERANO
+ MEMÓRIA SOBERANA
+ PROJECT REGISTRY
+ MISSION REGISTRY
+ ENGENHARIA DE CONSTRUÇÃO
+ ADE
+ EXECUTION FABRIC
+ EXECUTORES NATIVOS
+ SISTEMA IMUNOLÓGICO / RECOVERY
+ RESOURCE GOVERNOR
+ SCHEDULER GLOBAL
+ SEGURANÇA / AUTORIZAÇÃO
+ GIT SOBERANO
+ BIBLIOTECA DE CONHECIMENTO
+ PROVIDERS DE IA
+ COMPONENTES OSS QUALIFICADOS
+ EVIDÊNCIA / LEDGER
+ TERMINAL
+ PAINEL
```

## 42. REGRAS FINAIS

```text
UMA SOBERANIA LÓGICA.
MÚLTIPLOS PROJETOS.
MÚLTIPLAS MISSÕES COORDENADAS.
MÚLTIPLOS NÓS.
MÚLTIPLOS SISTEMAS OPERACIONAIS.
MÚLTIPLOS PROVEDORES.
MÚLTIPLOS COMPONENTES ESPECIALIZADOS.
UM GOVERNADOR.
UMA VERDADE OPERACIONAL.
LINUX E WINDOWS SÃO EXECUTORES.
ADE É O EXECUTOR AUTÔNOMO DE ENGENHARIA.
FALHA RECUPERÁVEL NÃO ENCERRA MISSÃO.
MEMÓRIA NÃO É PROVA.
ATIVIDADE NÃO É PROGRESSO.
MISSION_PROVEN EXIGE PROVA.
ZERO LEGACY DONOR COUPLING NO PRODUTO FINAL.
REUSE FIRST.
CONSTRUIR SOMENTE O QUE FALTA.
```

## 43. REGRA TERMINAL DE HIGIENE

```text
PESQUISAR O QUE JÁ EXISTE
→ ADQUIRIR O QUE É EXCELENTE OU BOM
→ SANITIZAR
→ APERFEIÇOAR
→ NORMALIZAR PARA POD
→ CONTEXTUALIZAR
→ VALIDAR
→ CONTRATUALIZAR
→ INTEGRAR
→ PROVAR
→ CONSTRUIR SOMENTE O DIFERENCIAL AUSENTE
```

**O POD não é definido pelas tecnologias que carrega. É definido pela capacidade de assumir um objetivo e concluí-lo com verdade, segurança, recuperação e prova.**

---

# ANEXO A — ESTADO DOCUMENTAL ATUAL

```text
DOCUMENTATION_CONSOLIDATED=VERIFIED
BASELINE_ACQUISITION_POLICY=DOCUMENTED
ADE_EXPLICITLY_IN_ARCHITECTURE=DOCUMENTED
REUSE_FIRST=DOCUMENTED
ZERO_DONOR_COUPLING_NORMALIZED=DOCUMENTED

RUNTIME_IMPLEMENTATION=NOT_VERIFIED
THIRD_PARTY_ACQUISITION=NOT_EXECUTED
SANITIZATION=NOT_EXECUTED
QUALIFICATION=NOT_EXECUTED
INTEGRATION=NOT_EXECUTED
PRODUCT_PROVEN=NO
```

# ANEXO B — FONTES PRESERVADAS

Os seguintes arquivos devem ser preservados para rastreabilidade e reconciliação:

- `POD_PROJETO_CONSOLIDADO_v3.md`;
- `POD_RECONCILIACAO_CONVERSA_GOVERNADOR_EXECUTION_FABRIC_ADE.md`;
- `POD_ESPECIFICACAO_SOBERANA_RECONCILIADA_PONTA_A_PONTA.md`;
- `POD — Especificação Higienizada v2.0.md`;
- `PROJECT_EXECUTION_STANDARD.md`;
- `ANTI_HALLUCINATION_STANDARD.md`;
- `NORMA_TRANSVERSAL_DE_ENGENHARIA_DE_SEGURANCA`.

Documentos superados não devem ser apagados; devem permanecer em `HISTORY/` com `NORMATIVE=false` quando a migração documental for executada no repositório.
