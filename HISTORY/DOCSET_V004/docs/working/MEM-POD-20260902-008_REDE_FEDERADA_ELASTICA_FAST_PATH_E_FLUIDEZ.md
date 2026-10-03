# MEM-POD-20260902-008 — REDE FEDERADA ELÁSTICA, FAST PATH E FLUIDEZ

**DATA:** 02/09/2026  
**TIPO:** ARCHITECTURAL_INSIGHT / CAPABILITY / RULE_CANDIDATE  
**STATUS:** CAPTURED  
**NORMATIVO:** NÃO

## TEXTO ORIGINAL / INTENÇÃO DO USUÁRIO

> A Rede Federada pode ter hoje 4 nós, amanhã 10, depois 20, depois 3, 9 ou apenas 1. Ela deve ser adaptável, rápida e de fácil conexão. Ao colocar um PC na rede, ele deve entrar automaticamente, descobrir e liberar suas ferramentas para uso conforme as políticas do POD. O operador deve poder ordenar de forma simples: “execute missão no PC 1”, “use PC 3 para esta tarefa”, “use PC X”, sem precisar lidar com IP, porta, SSH, PID ou configuração técnica.

Também foi consolidado que cada nó federado deve incorporar a configuração operacional derivada do estudo anterior de Fast Path: agente permanente, identidade estável, conexão outbound persistente, inbox durável, ACK separado de RESULT, health funcional, bridges quentes, eventos sem polling, autorrecuperação, reconciliação, boot determinístico, métricas de latência e retirada de SSH do caminho crítico normal.

## INTERPRETAÇÃO TÉCNICA

A Rede Federada do POD deve ser uma malha elástica de nós dinâmicos, autoformável e orientada por capacidades, na qual a quantidade de nós é estado operacional e não parte fixa da arquitetura.

```text
FEDERATION_SIZE = N

N pode variar dinamicamente:
1 → 4 → 10 → 20 → 3 → 9 → 1
```

Adicionar ou remover nós não deve exigir alteração arquitetural, recompilação de topologia, reconfiguração manual de rotas ou recadastro manual de ferramentas.

Princípio central:

```text
ADICIONOU UM NÓ
=
ADICIONOU CAPACIDADE AO POD

REMOVEU UM NÓ
!=
PERDEU A MISSÃO
```

## PLUG-AND-FEDERATE

Capacidade candidata denominada `PLUG-AND-FEDERATE`:

```text
INSTALAR / ATIVAR POD NODE ENGINE
→ gerar ou recuperar node_id
→ autenticar
→ abrir transporte outbound persistente
→ iniciar Node Agent
→ criar Node Inbox durável
→ descobrir ferramentas e recursos
→ registrar capabilities
→ iniciar bridges aplicáveis
→ publicar health funcional
→ reconciliar estado
→ READY
```

O operador não deve cadastrar manualmente ferramentas, IPs, portas, PIDs ou caminhos técnicos para o uso normal do nó.

## PERFIL OBRIGATÓRIO CANDIDATO DO NÓ FEDERADO

Cada nó deve possuir, conceitualmente:

```text
POD FEDERATED NODE
├── Stable Identity
├── Node Agent permanente
├── Persistent Outbound Transport
├── Durable Node Inbox
├── ACK / RESULT Separation
├── Functional Health
├── Capability Registry
├── Local Executors
├── Fast Path
├── Governed Path
├── Event Push
├── Local Journal
├── Checkpoints
├── Idempotency
├── Lease / Generation / Fencing
├── Reconciliation
├── Auto-Recovery
├── Performance Telemetry
└── Capability Bridges
    ├── Browser
    ├── Git
    ├── Python
    ├── PowerShell
    ├── Database
    └── outras ferramentas descobertas
```

## IDENTIDADE DO NÓ

Campos candidatos:

```text
node_id
boot_id
instance_id
engine_version
os
aliases
```

- `node_id`: identidade soberana estável do equipamento/nó.
- `boot_id`: muda a cada boot.
- `instance_id`: identifica a execução corrente do Node Agent.
- aliases humanos permitem comandos como `PC 1`, `PC 3`, `PC Vendas`, `B2` etc.

IP, hostname, porta e PID não devem ser identidade soberana.

## NODE AGENT PERMANENTE

Cada nó deve possuir um `POD Node Agent` permanente que:

- inicia automaticamente com o sistema;
- preserva identidade;
- mantém transporte;
- recebe comandos;
- mantém Node Inbox, journal e checkpoints;
- despacha executores e bridges;
- publica health, recursos e capabilities;
- publica eventos e resultados;
- executa reconciliação e autorrecuperação.

## TRANSPORTE PERSISTENTE

O transporte normal deve ser iniciado pelo nó e permanecer quente.

```text
NÓ
=========================>
conexão outbound persistente
=========================>
FEDERAÇÃO POD
```

SSH pode existir apenas como mecanismo administrativo de recuperação, fora do caminho crítico normal.

Não criar conexão física nova por comando.

Invariante candidato:

```text
NO_PER_COMMAND_CONNECTION = TRUE
```

## NODE INBOX DURÁVEL

Cada nó deve possuir fila lógica própria, por exemplo:

```text
node:<node_id>:inbox
```

Fluxo obrigatório candidato:

```text
COMMAND
→ VALIDAR
→ PERSISTIR
→ DEDUPLICAR
→ COMMAND_ACCEPTED
→ EXECUTAR
```

O comando aceito deve sobreviver a restart do Agent, reinício do POD e reboot do sistema operacional.

## ACK SEPARADO DE RESULT

Invariante:

```text
ACK != RESULT
```

Estados/eventos candidatos:

```text
COMMAND_ACCEPTED
COMMAND_STARTED
COMMAND_PROGRESS
COMMAND_COMPLETED
COMMAND_FAILED
```

`COMMAND_ACCEPTED` significa: identidade/capability validadas, comando persistido e responsabilidade assumida pelo nó. A execução continua depois.

Meta inicial candidata:

```text
ACK p95 <= 500 ms em LAN/Tailscale saudável
ACK normal < 1 s
```

Valores finais dependem de prova real.

## HEALTH FUNCIONAL DO NÓ

O nó deve publicar separadamente, conforme aplicável:

```text
NODE_ONLINE
TRANSPORT_READY
AGENT_READY
EXECUTOR_READY
SESSION_READY
BROWSER_READY
```

Além de:

```text
CPU
RAM
DISK
QUEUE_DEPTH
ACTIVE_COMMAND
LATENCY
ENGINE_VERSION
CAPABILITIES
LAST_CHECKPOINT
```

A federação deve conhecer indisponibilidade antes de enviar trabalho sempre que possível.

## CAPABILITY DISCOVERY AUTOMÁTICO

Ferramentas e recursos devem ser descobertos automaticamente.

Regra candidata:

```text
FERRAMENTA DESCOBERTA
+
PERMITIDA PELA POLÍTICA DO NÓ
=
CAPACIDADE DISPONÍVEL AO POD
```

Exemplos:

```text
Python encontrado → capability disponível
Git encontrado → capability disponível
PowerShell encontrado → capability disponível
Docker encontrado → capability disponível
Browser Bridge disponível → browser capability disponível
Privileged Executor autorizado → operações administrativas disponíveis
```

O operador não cadastra capability uma a uma.

## ROTEAMENTO MANUAL E AUTOMÁTICO

A Rede Federada deve suportar ambos:

### Afinidade explícita do operador

```text
"execute no PC 3"
→ target_node = PC 3
→ validar capability/health
→ executar no PC 3
```

Se o nó explicitamente solicitado não puder cumprir a tarefa, o POD deve informar o impedimento em vez de trocar silenciosamente de nó.

### Escolha automática

```text
MISSÃO/TAREFA
→ requisitos
→ capability match
→ health
→ recursos
→ afinidade
→ latência
→ fila
→ melhor nó
```

A mesma missão pode distribuir subtarefas entre múltiplos nós mantendo `mission_id` e `project_id` comuns.

## FAST PATH E GOVERNED PATH

A federação deve possuir roteamento automático entre dois caminhos conceituais:

```text
FAST PATH
→ ações simples
→ previamente autorizadas
→ reversíveis
→ capability válida
→ baixa latência
```

```text
GOVERNED PATH
→ administrativas
→ privilegiadas
→ destrutivas
→ financeiras
→ fora de capability
→ maior necessidade de política/prova
```

O operador não escolhe o caminho técnico; o POD decide.

## BROWSER BRIDGE QUENTE

Nós com navegador compatível podem expor operações governadas, como:

```text
browser.health
browser.open
browser.focus
browser.read
browser.click
browser.type
browser.back
```

O Bridge deve manter contexto reutilizável de sessão, PID, janela/target, URL e título, evitando redescoberta global a cada comando.

## ZERO POLLING NO HOT PATH

Invariante candidato:

```text
NO_HOT_PATH_POLLING = TRUE
```

Fluxo normal usa push/eventos. Polling permanece apenas como fallback de reconciliação/recovery.

## RECONCILIAÇÃO PÓS-FALHA

Após perda de conexão, nó e federação devem comparar:

```text
command_id
sequence
ACKs
RESULTs
generation
checkpoints
journal pendente
```

Um comando já concluído nunca deve ser reexecutado apenas porque o `RESULT` não chegou ao coordenador antes da queda.

Regra:

```text
RESULT PERDIDO
!=
COMANDO NÃO EXECUTADO
```

## AUTORECOVERY

O nó deve recuperar, com backoff e limites, falhas de:

- Node Agent;
- transporte;
- bridge;
- navegador;
- sessão interativa;
- rede/Tailscale quando aplicável;
- reinício do coordenador;
- reboot do próprio nó.

Falha local não deve derrubar trabalhos independentes da federação.

## MICRO-SCHEDULER LOCAL

Para reduzir idas e voltas, cada nó pode possuir um Micro-Scheduler Local autorizado para sequências de baixa latência dentro de uma capability válida.

Objetivo:

```text
POD CENTRAL
→ autoriza / envia trabalho

NODE AGENT
→ executa localmente pequenas decisões operacionais permitidas
→ usa executor/bridge quente
```

Não cria nova soberania e não altera objetivo, política, gasto ou `MISSION_PROVEN`.

## CONNECTION MULTIPLEXING

Uma conexão persistente deve transportar fluxos lógicos independentes de:

- controle;
- comandos;
- ACK;
- eventos;
- resultados;
- health;
- telemetria;
- reconciliação.

Invariante:

```text
1 TRANSPORTE QUENTE
→ N FLUXOS LÓGICOS
```

## HOT CAPABILITY CACHE

O POD não deve redescobrir a cada comando versões, capabilities, health e sessão quando nada mudou.

Cache quente deve ser invalidado/reconstruído quando ocorrer mudança real.

## NODE AFFINITY

Subtarefas relacionadas devem preferir permanecer no nó quando isso evita:

- transferência de dados;
- reconstrução de ambiente;
- cache frio;
- nova sessão;
- reabertura de navegador;
- reinstalação/reindexação desnecessária.

## PREWARMING

Capacidades provavelmente necessárias podem ser preparadas antecipadamente, por exemplo:

- ambiente Python;
- Browser Bridge;
- executor de testes;
- estado Git;
- caches/índices.

## DELTA SYNC

Sincronizações entre nós devem transferir somente diferenças quando possível.

```text
manifest
→ hashes
→ comparar
→ transferir DELTA
```

Aplicável a código, artefatos, contexto, checkpoints, índices e outros dados compatíveis.

Invariante:

```text
DATA_MOVEMENT_MINIMIZED = TRUE
```

## COMMAND BATCHING

Operações pequenas, relacionadas e seguras podem ser agrupadas em um lote governado quando a semântica permitir, preservando resultado individual, segurança, cancelamento e auditoria.

## PRIORITY LANES

Classes candidatas de tráfego:

```text
CONTROL
FAST_COMMAND
RESULT
MISSION_WORK
ARTIFACT_TRANSFER
TELEMETRY
BACKGROUND_SYNC
```

Fluxos de controle e Fast Path não devem ficar bloqueados atrás de transferências volumosas.

## LATENCY-AWARE ROUTING

O roteamento automático deve considerar, além de capability e recursos:

```text
latência atual
ACK médio
execução média
cache quente
afinidade
queue_age
```

A pergunta deixa de ser apenas “quem pode fazer?” e passa a incluir “quem pode fazer mais rapidamente agora?”.

## LOCAL RESULT CACHE

Resultados determinísticos e seguros podem ser cacheados quando o estado de origem não mudou, por exemplo versão de runtime, capability, hash ou commit atual.

Não aplicar indiscriminadamente a ações mutáveis.

## ACK EM DUAS CAMADAS

Distinguir conceitualmente:

```text
TRANSPORT_ACK
= bytes/mensagem recebidos pelo transporte

COMMAND_ACCEPTED
= comando validado, persistido e assumido pelo nó
```

Somente `COMMAND_ACCEPTED` representa aceite operacional real.

## LATENCY BUDGET POR ESTÁGIO

A federação deve medir, no mínimo:

```text
route
node_selection
transport
inbox_persist
command_accept
local_dispatch
bridge/executor
result_publish
```

Registrar p50/p95/p99 para localizar o gargalo real.

Metas iniciais candidatas derivadas do estudo anterior:

```text
heartbeat <= 2 s
perda de conexão detectada <= 5 s
ACK p95 <= 500 ms
local dispatch após ACK <= 100 ms
comando simples com Browser quente p95 <= 1,5 s
(excluindo carregamento externo da página)
```

Valores são objetivos de engenharia e exigem testes reais antes de serem considerados comprovados.

## INVARIANTES CANDIDATOS CONSOLIDADOS

```text
NODES_DYNAMIC = TRUE
NODE_JOIN_REQUIRES_NO_ARCHITECTURE_CHANGE = TRUE
NODE_LEAVE_DOES_NOT_DESTROY_MISSION = TRUE
TOOL_DISCOVERY_AUTOMATIC = TRUE
HUMAN_ALIAS_SUPPORTED = TRUE
EXPLICIT_NODE_ROUTING_SUPPORTED = TRUE
AUTOMATIC_BEST_NODE_ROUTING_SUPPORTED = TRUE
NO_PER_COMMAND_CONNECTION = TRUE
NO_HOT_PATH_POLLING = TRUE
CACHE_WARM_WHEN_POSSIBLE = TRUE
DATA_MOVEMENT_MINIMIZED = TRUE
FEDERATION_SIZE_MUST_NOT_CHANGE_MISSION_SEMANTICS = TRUE
```

## PRINCÍPIO DE FLUIDEZ

```text
REDE FEDERADA RÁPIDA
=
MENOS IDAS E VOLTAS
+ MENOS DESCOBERTA REPETIDA
+ MENOS TRANSFERÊNCIA
+ MAIS CONTEXTO QUENTE
+ MAIS EXECUÇÃO LOCAL AUTORIZADA
```

## RELAÇÃO COM MISSION_PROVEN

A quantidade de nós não altera a semântica da missão.

```text
1 NÓ ou 20 NÓS
→ mesmo objetivo
→ mesmo contrato
→ mesmos critérios de aceite aplicáveis
→ mesma exigência de evidência
→ MISSION_PROVEN somente após prova
```

A federação aumenta capacidade e velocidade; não reduz os requisitos de conclusão.

## MOTIVAÇÃO

Permitir que o POD use uma quantidade variável de computadores de forma simples, rápida, automática, resiliente e transparente para o operador, sem transformar expansão da capacidade em aumento proporcional de complexidade operacional.

## IMPACTO POSSÍVEL

- definição futura da Federação POD e do Túnel Core;
- POD Node Engine Windows/Linux;
- registro soberano de nós e aliases;
- Capability Registry distribuído/reconciliável;
- Node Inbox e journal local;
- transporte persistente multiplexado;
- Fast Path/Governed Path;
- bridges quentes por capability;
- roteamento por capacidade, afinidade, recursos e latência;
- execução distribuída multiprojeto;
- testes de concorrência, failover, reconciliação e desempenho.

## CONFLITOS / PONTOS PENDENTES

- definir posteriormente a fronteira final entre Rede Federada e Túnel Core;
- definir tecnologia concreta de transporte sem congelar prematuramente WebSocket/HTTP2/QUIC/etc.;
- definir modelo físico do Capability Registry e Node Inbox;
- definir políticas de ingresso/revogação de nós;
- definir limites de autonomia do Micro-Scheduler Local;
- definir como artefatos e workspaces são distribuídos sem criar conflito de escrita;
- integrar a Rede Federada à Segurança do POD sem transformar a adesão de um nó em confiança automática.

## RELAÇÕES COM OUTRAS MEMÓRIAS

Relaciona-se com:

- MEM-POD-20260902-002 — componentes conceituais, especialmente Túnel Core e Governador;
- MEM-POD-20260902-003 — Fundação Neutra, IDs, leases, fencing, health, persistência, idempotência e evidências;
- MEM-POD-20260902-004/005 — requisitos fundamentais do código-fonte, autonomia, recuperação, recursos, rastreabilidade e continuidade parcial;
- MEM-POD-20260902-006 — separação entre segurança do POD e segurança do produto;
- princípio ZERO DONOR COUPLING — toda capacidade derivada de estudos anteriores deve entrar com identidade POD nativa.

## DECISÃO FINAL

PENDENTE DE CONSOLIDAÇÃO DA ARQUITETURA FINAL.

## INCORPORADO EM

Ainda não incorporado em arquitetura normativa, baseline ou ADR.
