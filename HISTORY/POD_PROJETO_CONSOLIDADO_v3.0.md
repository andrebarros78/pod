# POD — Projeto Consolidado (v3.0)

**Estado:** conceitual e executivo. Nada implementado.
**Autoria:** projeto e especificação. **Construção:** responsabilidade de terceiro (construtor).
**Substitui:** Especificação Soberana Reconciliada, Project Execution Standard e a v2.0 higienizada. Os originais vão para `HISTORY/` (NORMATIVE=false).

---

# PARTE A — PROJETO CONCEITUAL

## A1. O que é o POD
Plataforma Orquestradora Durável: recebe um objetivo humano e assume a responsabilidade de entregá-lo construído, testado, recuperável e comprovado. Gera sistemas para web, Windows, Apple e Android.

Não é: chat, prompt, painel, MCP, wrapper de IA, nem conjunto de scripts.

## A2. Princípios
1. **Uma soberania lógica.** Um Governador decide; executores só executam.
2. **Inteligência ≠ autoridade.** O Cérebro propõe; o Governador valida e autoriza.
3. **Núcleo blindado e fixo** (A3). Regra mais importante.
4. **Tudo que é produzido fica fora do núcleo.**
5. **Sem autorização explícita = negado.** Falha fecha (fail closed).
6. **Sem prova não há conclusão.** Quem executa não aprova o próprio resultado.
7. **Falha recuperável é trabalho do POD**, não do usuário.
8. **Multiprojeto:** uma instalação, N projetos isolados por `project_id`.
9. **Zero dependência dos sistemas doadores** (WMCP/LMCP) no produto final.
10. **Zero dependência de ChatGPT** ou de qualquer provedor único de IA.

## A3. Núcleo blindado (regra de não-inchaço)
O núcleo guarda **o que está acontecendo**, nunca **o que foi produzido**.

**Pode ficar:** IDs de projeto/missão/tarefa, estados e transições, leases, fencing tokens, autorizações, registros de nós e capacidades, ledger com hash e ponteiro, referências a segredos.

**Nunca entra:** código gerado, builds, logs, saídas de comando, evidências em si, respostas de IA (só resumo estruturado + hash), conhecimento de longo prazo, cache, temporários.

**Regras testáveis:**
```text
CORE_STORES_CONTENT=false
CORE_EXECUTES_GENERATED_CODE=false
CORE_RUNS_PRIVILEGED=false
CORE_UNSAFE_CODE=0
CORE_DIRECT_ENTRYPOINTS=1  (só Command API autenticada)
CORE_MAX_RECORD_SIZE=<definir>
CORE_MAX_DB_SIZE=<definir>
```
**Contra inchaço:** compactação em checkpoints, arquivamento fora, retenção por prazo, rejeição (nunca truncamento) de registro acima do limite, teste de estabilidade de tamanho sob carga prolongada.

**Blindagem:** núcleo pequeno, Rust sem `unsafe`, dependências mínimas e fixadas, sem shell/painel/Cérebro escrevendo direto, processos separados por função sensível, ledger só de acréscimo encadeado por hash, premissa de *assume breach*.

## A4. Arquitetura
```text
HUMANO → Terminal / Painel → COMMAND API
                                 ↓
                           GOVERNADOR (núcleo)
        Cérebro ──propõe──▶ ↑   ↓ despacha
                          EXECUTION FABRIC
                     Executor Linux | Executor Windows | futuros
                                 ↓
                          Recursos reais / Sandboxes
   Transversais: Segurança · Evidência · Recovery/Imunológico
   Fora do núcleo: Workspaces/Git · Object store · Conhecimento · Cofre
```

| Componente | Função | Dentro do núcleo? |
|---|---|---|
| Governador | registries, máquina de estados, scheduler, recursos, autorização, leases/fencing, ledger, política de Git | Sim |
| Cérebro | entende, planeja, diagnostica, replaneja; sem poder administrativo | Não |
| Execution Fabric | nós, capacidades, despacho, ACK, heartbeat, reconexão | Não |
| Executores | autonomia local limitada; sem soberania | Não |
| Engenharia de Construção | módulo → teste → prova → integração | Não |
| Recovery/Imunológico | detecção, contenção, recuperação (mecanismo único) | Não |
| Memória/Conhecimento | memória operacional e biblioteca governada | Não |
| Provider Manager | provedores de IA intercambiáveis | Não |
| Terminal e Painel | clientes da mesma Command API; painel não é fonte de verdade | Não |

## A5. Regras de projeto e missão
- **Projeto** registra: id, objetivo, escopo, fora de escopo, workspace, repositório, risco, perfil de segurança, contrato de aceite.
- **Missão** é obrigação persistente até `MISSION_PROVEN`, cancelamento soberano, impossibilidade externa comprovada ou bloqueio humano registrado.
- **Nova ordem** é correlacionada antes de virar missão: continuação, atualização, subtarefa, trabalho paralelo seguro, ordem substituta, conflito real ou missão nova.
- **Portão humano** só para: gasto novo, conta externa, credencial/MFA/CAPTCHA, ação irreversível, aprovação jurídica ou comercial. Bloqueia só o ramo dependente.
- **Execução desconectada:** tarefa já autorizada pode continuar; objetivo novo não é inventado; resultado persiste localmente e reconcilia ao reconectar.
- **Git:** política única e soberana (repositório, branches, worktrees, tags, rollback); executores não decidem.

---

# PARTE B — PROJETO EXECUTIVO

## B1. Linguagens e tecnologias (decisão)

| Parte | Tecnologia | Motivo |
|---|---|---|
| Núcleo / Governador | **Rust** | segurança de memória, sem coletor de lixo, estável |
| Execution Fabric | **Rust** | mesmo runtime do núcleo, uma só linguagem |
| Executores Linux e Windows | **Rust** (+ shell restrito / PowerShell controlado) | compilados, pequenos, isoláveis |
| Estado do núcleo | **SQLite** → **PostgreSQL** | simples no MVP, robusto depois |
| Contratos | **Protobuf + JSON Schema** | fonte única; tipos gerados em Rust |
| Cérebro | Orquestração em **Rust**; **Python** só em contêiner isolado | Python não toca o núcleo |
| Terminal | **Rust** | cliente da Command API |
| Painel | **TypeScript + HTML/CSS** | interface web |
| Modelagem formal | **TLA+** | provar leases, fencing e estados antes de codificar |
| Segurança crítica (opcional) | **Ada/SPARK** | só se algum módulo exigir prova formal |
| Código gerado (saída) | Kotlin (Android), Swift (Apple), C# (Windows), TypeScript/HTML (web), Python e outras | sempre em sandbox |

Compilar para Apple exige Mac com Xcode e conta de desenvolvedor; publicar em lojas exige contas e aprovação humana.

## B2. Escada única de provas
```text
MODULE_PROVEN → INTEGRATION_PROVEN → MISSION_PROVEN → PRODUCT_PROVEN → SEALED
```
- **MODULE_PROVEN:** contrato verificado, testes, segurança, recovery, evidência, zero falha crítica aberta.
- **INTEGRATION_PROVEN:** módulos provados, comunicação real, reconciliação, sem múltiplas fontes de verdade.
- **MISSION_PROVEN:** resultado + teste real + critério de aceite + evidência + regressão + checkpoint.
- **PRODUCT_PROVEN:** provas de plataforma (multiprojeto, cross-platform, resiliência, segurança, endurance, ciclo de vida, desacoplamento).
- **SEALED:** auditoria independente assumindo que a prova anterior pode estar errada; se falhar, a prova é revogada.

Não contam como prova: código escrito, build passou, processo rodando, endpoint responde, commit criado, painel verde.

**Estados de verdade:** VERIFIED, INFERRED, HYPOTHESIS, NOT_VERIFIED, UNKNOWN. Nunca promover estado fraco a VERIFIED em silêncio.
**Não autocertificação:** o mesmo ator não define o critério, executa, cria a evidência e aprova o PASS.

## B3. Roadmap e ordens de construção

Cada fase é uma **ordem de construção** entregue ao construtor, com critério de aceite e saída verificável.

| Fase | Entrega | Critério de aceite | Saída |
|---|---|---|---|
| 0 | Baseline: inventário, ADRs mínimos, congelar novas soberanias | documentos concorrentes = 0 | BASELINE_RECONCILED |
| 1 | Contratos + modelo TLA+ do núcleo | schemas versionados; modelo sem violação de invariantes | CORE_CONTRACTS_DEFINED |
| 2 | **MVP:** ordem entra → Governador (SQLite) → 1 executor Linux → teste → evidência no object store → MISSION_PROVEN | núcleo não armazena conteúdo; tamanho estável; reboot retoma | MVP_PROVEN |
| 3 | Núcleo completo: registries, scheduler, recursos, leases, fencing, recovery | testes de lease, fencing, writer obsoleto | GOVERNOR_PROVEN |
| 4 | Cérebro + Provider Manager | replanejamento; falha de provedor não derruba missão | BRAIN_PROVEN |
| 5 | Executor Windows + prova cross-platform | uma missão com tarefas Linux e Windows | CROSS_PLATFORM_PROVEN |
| 6 | Engenharia de Construção, memória/conhecimento, imunológico | pipeline módulo→prova→integração funcionando | CONSTRUCTION_PROVEN |
| 7 | Terminal e Painel | POD operável sem chat externo | TERMINAL_PROVEN |
| 8 | Provas de plataforma: multiprojeto, falhas injetadas, segurança, endurance, ciclo de vida, desacoplamento | todos os gates PASS | PRODUCT_PROVEN |
| 9 | Missão real de referência e selagem | auditoria independente aprovada | SEALED |

**Regra para o construtor:** cada módulo é construído, provado e selado isoladamente antes de integrar; módulo falho não entra na integração final.

## B4. Contratos mínimos (conteúdo, sem código)
Project, Mission, Task, TaskGraph, Command, Event, StateTransition, ExecutionRequest, ExecutionLease, ExecutionEvent, ExecutionResult, CapabilityDescriptor, NodeIdentity, NodeHeartbeat, ResourceClaim, AuthorizationGrant/Denial, Checkpoint, EvidenceRecord, Incident, RecoveryAction, GitIntent, ArtifactManifest, KnowledgeRecord, ProviderDescriptor.

**Cada contrato de módulo declara:** nome, objetivo, responsabilidade, entradas, saídas, dependências, consumidores, interfaces, estado, persistência, contrato de erro, fronteira de segurança, comportamento de recovery, critérios de aceite, fora de escopo.

**Estados de missão:** CREATED, CORRELATED, PLANNING, READY, RUNNING, WAITING_DEPENDENCY, WAITING_HUMAN_GATE, RECOVERING, VALIDATING, REGRESSION, FINALIZING, MISSION_PROVEN, BLOCKED_EXTERNAL, CANCELLED, FAILED_UNRECOVERABLE. Transições explícitas, persistidas e auditáveis.

## B5. Segurança
Security by design/default/verification/containment, menor privilégio, deny by default, fail closed, defesa em profundidade.
- Segredos fora do núcleo, logs e evidências; só referências.
- Operação privilegiada somente em executor dedicado (identidade, política, escopo, ACL, task_id, auditoria, rollback).
- Código gerado nunca roda no núcleo; sempre em sandbox.
- **Gate de segurança:** segredos expostos = 0, credenciais padrão = 0, portas públicas injustificadas = 0, vulnerabilidades críticas aplicáveis = 0.
- **Software sensível (ex.: bancário):** o POD gera e testa, mas a aprovação para produção é humana, com auditoria externa e conformidade normativa (ex.: PCI-DSS).

## B6. Testes mínimos da plataforma
INSTALL, START, RESTART, REBOOT, PROJECT_CREATE, MULTIPROJECT_ISOLATION, MISSION_CORRELATION, DUPLICATE_COMMAND, IDEMPOTENCY, CONFLICT_DETECTION, LEASE, FENCING, STALE_WORKER, LINUX_EXECUTION, WINDOWS_EXECUTION, CROSS_PLATFORM_MISSION, NETWORK_PARTITION, STATE_RECONCILIATION, RECOVERY, GIT_POLICY, SECRET_HANDLING, AUTHORIZATION_DENIAL, FAIL_CLOSED, PROVIDER_FAILURE, BRAIN_REPLAN, EVIDENCE_CHAIN, REGRESSION, DONOR_DECOUPLING, ENDURANCE, UPDATE, ROLLBACK, **CORE_SIZE_STABLE**, REFERENCE_MISSION.

## B7. Riscos e decisões em aberto

| Item | Recomendação |
|---|---|
| Limites do núcleo (registro, banco) | definir no MVP com medição real |
| Object store | começar com armazenamento local por hash; migrar depois |
| Sandbox | contêiner no MVP; microVM para código de risco alto |
| Custo de chamadas de IA | orçamento por missão, controlado pelo Governador |
| Alta disponibilidade sem duas autoridades | um líder por lease; réplica passiva; validar no TLA+ |
| Cérebro erra (modelo probabilístico) | nunca é fonte única de prova; verificação determinística |
| Escopo excessivo | seguir o MVP; não iniciar fase seguinte sem a anterior provada |

## B8. Governança documental
```text
POD_PROJETO_CONSOLIDADO.md  ← fonte normativa única
ADR/        decisões arquiteturais posteriores
SCHEMAS/    contratos formais
RUNBOOKS/   operação
EVIDENCE/   provas geradas
RELEASES/   manifestos de versão
HISTORY/    material histórico (NORMATIVE=false)
```
Mudança que afete soberania, segurança, persistência, execução, prova ou contratos exige ADR. Adaptador de transição exige dono, propósito, origem, alvo de substituição, critério de remoção e testes.

**Estado operacional da missão:** arquivo `MISSION_STATE.json` separado (fase, módulo ativo, status dos módulos, fatos verificados, falhas abertas, bloqueios externos, próxima ação, evidências). A memória de conversa não substitui estado persistido.

## B9. Papéis
- **Projetista (este documento):** especificação, arquitetura, decisões, ordens e critérios de aceite.
- **Construtor:** escreve código, schemas finais e testes; roda, mede e prova.
- **Humano responsável:** aprova portões humanos, gastos, lojas e produção.

---

# ANEXO — Rastreabilidade
| Origem | Incorporado em |
|---|---|
| Soberania única, multiprojeto, zero donor | A2, A4 |
| Cérebro, Governador, Memória, Fabric, Executores | A4 |
| Segurança transversal, cofre, executor privilegiado, portão humano | A5, B5 |
| Persistência, filas, leases, fencing, idempotência | A3, B3, B6 |
| Imunológico e Recovery | A4 (unificados) |
| Verdade, evidência, não autocertificação | B2 |
| Marco Zero à finalização (fases 0–20) | B3 (condensadas em 10 fases) |
| Standard de execução (módulo, integração, seal, estado) | B2, B3, B4, B8 |
| Novo nesta versão | Núcleo blindado e fixo (A3), stack decidida (B1), MVP (B3) |
