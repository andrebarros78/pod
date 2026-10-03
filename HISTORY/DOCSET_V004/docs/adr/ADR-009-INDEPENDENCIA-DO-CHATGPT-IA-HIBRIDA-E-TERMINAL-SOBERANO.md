# ADR-009 — Independência do ChatGPT, IA híbrida e Terminal Soberano

**Identificador:** POD-ADR-009
**Versão:** 1.0.0
**Status:** ACCEPTED
**Data:** 2026-09-03
**Conjunto:** POD-DOCSET-V003
**Decisão de produto:** André Barros
**Autoridade técnica:** Pipo
**Impacto:** arquitetura, runtime, interfaces, IA, segurança, operação e aceite

## Resumo executivo

O POD será um produto próprio, persistente e operável sem ChatGPT. Ele utilizará
inteligência artificial por APIs e, quando disponível, por modelos locais, através
de uma arquitetura híbrida e multiprovedor. ChatGPT, MCP, painéis e outros canais
serão adaptadores opcionais; nenhum deles será fonte de verdade ou requisito para
o funcionamento do núcleo.

O POD terá um executável próprio chamado `pod` e um Terminal Soberano para receber
missões, consultar estado, conceder autorizações, acompanhar execução e verificar
provas. Fechar o terminal não encerrará o serviço nem apagará a missão.

## Contexto

O POD nasceu para receber uma missão, preservar o compromisso assumido, planejar,
executar, recuperar falhas e concluir somente mediante prova. Um chat de terceiros
não oferece as garantias necessárias para exercer esse papel porque sessões,
contexto, ferramentas, conectores, políticas da plataforma e disponibilidade
podem mudar fora do controle do POD.

Ao mesmo tempo, modelos de IA externos oferecem capacidade importante de
raciocínio, geração, análise e revisão. Rejeitar APIs externas reduziria a qualidade
e elevaria o custo de criar modelos próprios. A solução correta é aproveitar essas
capacidades sem entregar a elas autoridade, memória soberana ou continuidade.

André definiu três requisitos de produto inseparáveis:

1. usar APIs de IA em arquitetura híbrida;
2. não depender da estrutura do ChatGPT;
3. possuir terminal próprio quando o produto estiver concluído.

## Problema

Sem uma decisão explícita, a implementação poderia:

- confundir ChatGPT com o POD;
- exigir uma conversa aberta para continuar missões;
- armazenar regras soberanas apenas em prompts;
- acoplar o runtime a um servidor MCP voltado ao ChatGPT;
- tratar GPT ou qualquer outro provedor como cérebro permanente;
- interromper o sistema quando um provedor ficar indisponível;
- fazer do terminal apenas um invólucro de uma sessão externa;
- permitir que saída de modelo altere política, autoridade ou estado diretamente;
- criar dependência comercial e operacional de um único fornecedor;
- declarar sucesso por texto, sem estado persistente e evidência independente.

Isso violaria soberania, continuidade, auditabilidade, recuperação e independência
de fornecedor.

## Decisão

### 1. Invariantes não negociáveis

~~~text
POD_IS_STANDALONE_PRODUCT = TRUE
CHATGPT_IS_NOT_RUNTIME_DEPENDENCY = TRUE
CHAT_SESSION_IS_NOT_STATE = TRUE
MCP_IS_OPTIONAL_ADAPTER = TRUE
MCP_OUTAGE_CANNOT_STOP_CORE = TRUE
AI_PROVIDER_IS_REPLACEABLE = TRUE
AI_OUTPUT_HAS_NO_SOVEREIGN_AUTHORITY = TRUE
POLICY_IS_ENFORCED_BY_CODE = TRUE
PROMPT_IS_NOT_POLICY = TRUE
TERMINAL_IS_NATIVE_POD_INTERFACE = TRUE
TERMINAL_PROCESS_IS_NOT_POD_RUNTIME = TRUE
MISSION_CONTINUES_WITH_INTERFACES_CLOSED = TRUE
CORE_OPERATES_WITHOUT_EXTERNAL_AI = TRUE
PROOF_DOES_NOT_DEPEND_ON_CHAT_TEXT = TRUE
~~~

### 2. Fronteira do produto

Pertencem ao POD:

- Mission Core e máquina de estados;
- Constitution/Policy e mecanismo determinístico de autorização;
- banco de estado, journal, outbox, idempotência e auditoria;
- scheduler, filas, workers, supervisor e recuperação;
- Brain híbrido, contexto operacional e memória autorizada;
- Proof Engine e Evidence Store;
- Provider Router e Provider Adapters;
- Tool Gateway e adapters de ferramentas;
- API própria;
- Terminal Soberano;
- painel próprio, quando implementado;
- configuração, segredos por referência, observabilidade e atualização.

Não pertencem ao núcleo do POD:

- produto ChatGPT;
- histórico de conversa do ChatGPT;
- memória da conta ChatGPT;
- instruções personalizadas da conta;
- disponibilidade de plugin ou connector;
- servidor MCP criado exclusivamente para uma interface externa;
- modelo específico de qualquer fornecedor;
- texto final emitido por um modelo.

### 3. Arquitetura lógica aprovada

~~~text
INTERFACES
  Terminal Soberano | API POD | Painel POD | ChatGPT opcional | outros clientes
                             ↓
COMMAND INGRESS + IDENTITY + POLICY ENFORCEMENT
                             ↓
MISSION CORE + SCHEDULER + SUPERVISOR + PROOF ENGINE
                             ↓
STATE STORE + EVENT JOURNAL + OUTBOX + EVIDENCE STORE
                             ↓
       BRAIN HÍBRIDO                TOOL GATEWAY
             ↓                           ↓
 POLICY ROUTER → PROVIDER ROUTER    adapters nativos/MCP
             ↓
 APIs externas | modelos locais | motores determinísticos
~~~

A seta indica dependência permitida. Nenhuma seta retorna de ChatGPT, MCP ou
Provider Adapter para autoridade soberana.

### 4. Núcleo persistente e interfaces descartáveis

O runtime do POD será um serviço durável supervisionado pelo sistema operacional.
Terminal, painel, ChatGPT e API clients conectam-se ao serviço; não o hospedam.

Consequências obrigatórias:

- fechar o terminal não encerra missão;
- fechar o painel não encerra missão;
- perder a conversa não perde estado;
- reiniciar o serviço recupera missões não terminais;
- troca de interface não cria uma nova missão;
- toda resposta exibida deriva do estado soberano;
- nenhuma interface fabrica `MISSION_PROVEN`.

### 5. Inteligência híbrida

O Brain combinará quatro classes de capacidade:

| Classe | Uso | Autoridade |
|---|---|---|
| regras determinísticas | política, validação, cálculo e gates | limitada ao contrato versionado |
| modelos locais | tarefas compatíveis com recursos e privacidade locais | consultiva |
| APIs de IA externas | raciocínio, geração, análise e revisão | consultiva |
| ferramentas especializadas | compiladores, testes, scanners e automações | efeito limitado por capability |

O Brain escolhe estratégia; não altera diretamente estado soberano, política ou
prova. Toda proposta de ação passa pelo Mission Core e pelo Policy Enforcement.

### 6. Multiprovedor e portabilidade

O Provider Router selecionará provedores por capacidade, saúde, custo, latência,
privacidade, região, limite e política. Cada Provider Adapter traduz o contrato
interno para a API específica.

Provedores possíveis incluem OpenAI API, Anthropic API, Google Gemini API,
DeepSeek API, GLM API e modelos locais. Essa lista não cria obrigatoriedade nem
preferência permanente.

Regras:

- GPT via API é capacidade opcional, não fundação;
- nenhum `provider_id` é codificado no domínio;
- entrada e saída usam envelopes canônicos do POD;
- contexto portátil não depende do formato de conversa do fornecedor;
- resposta registra provedor, modelo, versão, custo, uso e hashes;
- failover preserva classificação, orçamento, autoridade e política;
- dado incompatível com a política de um provedor não é enviado;
- troca de provedor não muda critério de aceite;
- indisponibilidade total de IA externa não corrompe nem encerra missão.

### 7. Modos de funcionamento

| Condição | Comportamento obrigatório |
|---|---|
| ChatGPT indisponível | nenhuma degradação do núcleo |
| MCP externo indisponível | somente capacidades daquele adapter ficam indisponíveis |
| provedor principal indisponível | failover autorizado |
| todas as APIs de IA indisponíveis | execução determinística/local ou `WAITING_EXTERNAL` apenas no ramo dependente |
| internet indisponível | continuidade local dentro das delegações válidas |
| terminal fechado | runtime e missões continuam |
| painel fechado | runtime e missões continuam |
| runtime reiniciado | supervisor restaura e reconcilia |
| modelo produz instrução proibida | Policy nega e audita |

### 8. Papel do MCP

MCP é um protocolo de adaptação de ferramentas e contexto. Pode ser utilizado:

- entre Tool Gateway e uma ferramenta compatível;
- para expor capacidades limitadas do POD a clientes externos;
- para integrar temporariamente ChatGPT, IDE ou agente autorizado;
- para encapsular ferramenta legada quando for economicamente melhor.

MCP não será:

- barramento soberano obrigatório;
- banco de estado;
- supervisor do runtime;
- mecanismo exclusivo de execução;
- portador implícito de autoridade;
- dependência do Terminal Soberano;
- requisito para o Mission Core iniciar ou recuperar.

Ferramenta indispensável pode usar MCP internamente, desde que possua adapter,
health, timeout, retry, circuit breaker e rota de degradação explícita. A queda
dessa ferramenta suspende apenas o trabalho que realmente depende dela.

### 9. Terminal Soberano

O produto instalará um executável próprio `pod`. Ele será cliente nativo da API
local do POD e funcionará sem ChatGPT e sem MCP externo.

Interfaces mínimas:

~~~text
pod start
pod stop
pod restart
pod status
pod doctor
pod terminal
pod mission create
pod mission list
pod mission inspect <mission_id>
pod mission pause <mission_id>
pod mission resume <mission_id>
pod mission cancel <mission_id>
pod approve <authorization_id>
pod deny <authorization_id>
pod providers status
pod providers test <provider_id>
pod tools status
pod logs
pod events
pod evidence <mission_id>
pod proof <mission_id>
pod config validate
pod version
~~~

`pod terminal` abrirá uma sessão interativa própria. Linguagem natural poderá ser
usada quando houver provedor adequado, mas comandos críticos terão representação
estruturada e confirmação vinculada a um `authorization_id`.

### 10. Contrato do terminal

O Terminal Soberano deverá:

- operar em português por padrão;
- oferecer modo humano legível e modo `--json` estável;
- retornar códigos de saída documentados;
- autenticar identidade local e remota;
- respeitar RBAC, scopes, capabilities e portões;
- exibir claramente ambiente, projeto e missão;
- separar comando aceito de resultado concluído;
- acompanhar comandos assíncronos por `command_id`;
- permitir reconexão sem duplicar efeito;
- transmitir logs e eventos sem tratá-los como fonte de verdade;
- ocultar segredos e dados classificados;
- registrar comando, ator, policy decision e resultado;
- oferecer ajuda local sem depender da internet;
- funcionar em terminal Windows e Linux suportados;
- recusar versão incompatível com a API do runtime;
- nunca executar shell arbitrário apenas porque uma IA solicitou.

`pod stop`, `pod restart` e `pod mission cancel` exigirão policy e autorização
compatíveis com o efeito. Parada controlada deverá drenar ou checkpointar trabalho;
jamais converter missão ativa em conclusão ou cancelamento silencioso.

### 11. Separação entre terminal e runtime

~~~text
pod terminal encerrou ≠ POD encerrou
conexão caiu ≠ missão cancelada
ACK recebido ≠ trabalho concluído
texto de sucesso ≠ ProofVerdict PASS
processo de IA encerrou ≠ missão encerrou
~~~

O daemon ou serviço continuará sob supervisor externo ao terminal. O terminal
poderá ser atualizado, reiniciado ou substituído sem perder estado de missão.

### 12. Regras soberanas por código

As regras de André serão representadas em Constitution/Policy versionada,
validada e aplicada pelo núcleo. Prompt pode explicar ou contextualizar regra, mas
não é a regra executável.

Toda decisão de política material produzirá:

~~~text
policy_decision_id
policy_version
actor_id
project_id
mission_id optional
requested_effect
decision ALLOW | DENY | REQUIRE_GATE
reason_codes
matched_rules
input_hash
decided_at_utc
~~~

Somente fluxo de governança autorizado altera Constitution/Policy. Conteúdo de
chat, documento externo, memória aprendida, saída de modelo ou ferramenta não pode
promover a si próprio a regra soberana.

### 13. Autorização e efeitos

O terminal não concede acesso total por estar na máquina do Owner. Toda ação usa:

- identidade autenticada;
- escopo de projeto;
- classe de efeito;
- capability com menor privilégio;
- regra de política;
- orçamento e limite;
- portão humano quando aplicável;
- auditoria e idempotência.

Gasto novo, publicação de alto impacto, destruição irreversível, segredo pessoal e
decisão reservada ao Owner continuam bloqueados até autorização válida.

### 14. Dados, memória e contexto

Estado de missão, memória, evidência e histórico pertencem ao POD. O contexto
enviado a uma API é uma projeção mínima, classificada e temporária.

É proibido depender de:

- histórico de conversa do provedor;
- memória proprietária de uma conta externa;
- identificador de thread externo como ID soberano;
- retenção do provedor para recuperação;
- resposta anterior não registrada no POD.

Quando permitido, o POD persiste resumo, proveniência e hashes necessários para
reproduzir a decisão, sem registrar segredo ou conteúdo proibido.

### 15. API própria

Terminal, painel e integrações usarão a API versionada do POD. Essa API será
independente das APIs de IA e separará:

- comandos;
- consultas;
- eventos;
- autorizações;
- evidências;
- administração;
- saúde funcional.

API externa de IA nunca será exposta como se fosse API soberana do POD.

### 16. Atualização e substituição

Provider Adapter, modelo, terminal, painel e adapter MCP podem ser substituídos
independentemente quando preservarem contrato e compatibilidade. Migração de
contexto não altera IDs soberanos nem reescreve eventos históricos.

### 17. Requisitos consolidados

| ID | Requisito | Criticidade |
|---|---|---|
| REQ-SOV-001 | POD inicia, opera e recupera sem ChatGPT | CRITICAL |
| REQ-SOV-002 | núcleo inicia e recupera sem MCP externo | CRITICAL |
| REQ-SOV-003 | regras soberanas são aplicadas por código versionado | CRITICAL |
| REQ-SOV-004 | saída de IA não altera autoridade diretamente | CRITICAL |
| REQ-SOV-005 | APIs de IA são acessadas somente por Provider Adapters | CRITICAL |
| REQ-SOV-006 | nenhum provedor é dependência fixa do domínio | CRITICAL |
| REQ-SOV-007 | failover preserva política, privacidade e orçamento | CRITICAL |
| REQ-SOV-008 | modo sem IA externa preserva núcleo e estado | CRITICAL |
| REQ-SOV-009 | executável `pod` oferece terminal próprio | CRITICAL |
| REQ-SOV-010 | encerrar terminal ou painel não encerra missão | CRITICAL |
| REQ-SOV-011 | terminal possui saída humana e JSON estável | HIGH |
| REQ-SOV-012 | comandos e efeitos do terminal são auditados | CRITICAL |
| REQ-SOV-013 | estado e contexto soberanos pertencem ao POD | CRITICAL |
| REQ-SOV-014 | prova não depende de texto ou sessão externa | CRITICAL |
| REQ-SOV-015 | API própria separa POD de APIs de fornecedores | CRITICAL |

### 18. Testes de aceite obrigatórios

| ID | Cenário | Resultado esperado |
|---|---|---|
| T-SOV-001 | iniciar sem credencial ChatGPT | núcleo READY |
| T-SOV-002 | iniciar sem servidor MCP externo | núcleo READY; adapter DEGRADED |
| T-SOV-003 | fechar terminal durante missão | missão continua |
| T-SOV-004 | fechar painel durante missão | missão continua |
| T-SOV-005 | reiniciar runtime com missão ativa | missão recuperada e reconciliada |
| T-SOV-006 | derrubar provedor principal | failover conforme policy |
| T-SOV-007 | derrubar todos os provedores externos | núcleo saudável; ramo dependente aguarda |
| T-SOV-008 | trocar GPT por outro provedor | contrato interno e critérios preservados |
| T-SOV-009 | modelo solicitar ação proibida | DENY auditado |
| T-SOV-010 | prompt contradizer Constitution | Constitution prevalece |
| T-SOV-011 | executar comandos em modo `--json` | schema e exit codes válidos |
| T-SOV-012 | perder conexão do terminal e reconectar | nenhum efeito duplicado |
| T-SOV-013 | consultar prova sem ChatGPT | Evidence Pack reproduzível |
| T-SOV-014 | usar modelo local autorizado | missão não depende de API externa |
| T-SOV-015 | atualizar terminal separadamente | runtime e missões preservados |
| T-SOV-016 | injetar thread externa como ID soberano | entrada recusada ou mapeada |
| T-SOV-017 | vazar segredo por saída/log | conteúdo sanitizado e incidente registrado |
| T-SOV-018 | tentar elevar regra via memória aprendida | promoção bloqueada |

### 19. Critério de conclusão

Esta decisão somente estará implementada quando todos os requisitos SOV estiverem
ligados a código, testes, evidências e aceite. Demonstração em ChatGPT, terminal
simulado, mock isolado ou documento não comprova implementação.

Prova mínima integrada:

1. iniciar o POD sem ChatGPT e sem MCP externo;
2. criar missão pelo executável `pod`;
3. iniciar execução com uma API de IA;
4. interromper o provedor e comprovar failover;
5. fechar e reabrir o terminal;
6. reiniciar o runtime;
7. concluir a missão;
8. consultar o Evidence Pack pelo terminal;
9. verificar journal, policy decisions, custo e hashes;
10. repetir cenário sem nenhuma IA externa e provar degradação segura.

### 20. Sequência de implementação

1. contratos de Constitution/Policy e Provider Envelope;
2. serviço persistente do POD e API própria;
3. armazenamento transacional e recuperação;
4. CLI `pod` com status, doctor, mission e saída JSON;
5. Terminal Soberano interativo;
6. Provider Router e primeiro adapter de API;
7. segundo adapter independente para provar portabilidade;
8. adapter local/determinístico e modo sem IA externa;
9. Tool Gateway com adapter nativo;
10. MCP opcional e isolado;
11. testes de desconexão, failover, reinício e segurança;
12. Evidence Pack e aceite integrado.

### 21. Proibições arquiteturais

É proibido aprovar implementação em que:

- o comando `pod` apenas abra ou controle ChatGPT;
- o Mission Core esteja dentro de plugin, GPT personalizado ou sessão de chat;
- MCP seja o único caminho entre terminal e runtime;
- regras soberanas existam somente em prompt;
- uma resposta do modelo altere banco sem caso de uso autorizado;
- perder uma thread externa faça perder missão;
- um único fornecedor esteja codificado no domínio;
- a conclusão dependa de mensagem produzida pela própria IA executora;
- fechar a interface encerre o supervisor;
- offline signifique acesso irrestrito;
- fallback envie dados a provedor incompatível;
- o terminal ignore identidade, escopo, policy ou gate.

## Alternativas consideradas

### Manter ChatGPT como interface e runtime principal

Rejeitada. Não oferece soberania de estado, continuidade independente nem controle
suficiente sobre políticas da plataforma.

### Depender de um MCP central ligado ao ChatGPT

Rejeitada. Transforma um protocolo e uma interface externa em ponto único de falha.

### Usar somente uma API de IA

Rejeitada. Cria aprisionamento, risco de indisponibilidade e fragilidade comercial.

### Usar somente modelos locais

Rejeitada como regra geral. Eleva custo operacional e pode reduzir capacidade. O
modelo local permanece opção por privacidade, resiliência ou economia.

### Criar terminal que hospeda todo o runtime

Rejeitada. Fechar a janela encerraria missões e impediria operação persistente.

### Arquitetura aprovada

Serviço próprio persistente, API própria, Terminal Soberano, regras determinísticas,
IA híbrida multiprovedor e MCP opcional por adapter.

## Consequências

### Positivas

- independência real do ChatGPT;
- continuidade entre sessões e interfaces;
- portabilidade entre provedores;
- controle de custo e privacidade;
- terminal próprio simples para o Owner;
- regras aplicadas de forma reproduzível;
- recuperação e auditoria verificáveis;
- capacidade de operar de forma degradada.

### Custos e responsabilidades

- o POD precisa manter seu próprio serviço, banco, API e atualização;
- adapters exigem testes contratuais por provedor;
- modo offline/local possui capacidade menor e deve ser declarado;
- terminal e runtime precisam de compatibilidade versionada;
- observabilidade, segurança e supervisor não podem ser terceirizados ao chat.

## Migração

Como o runtime ainda não foi implementado, esta decisão entra antes da escolha da
stack e não exige migração de dados. O plano de construção deverá incorporar os
requisitos SOV desde F0.

Qualquer protótipo futuro criado dentro de ChatGPT, plugin ou MCP deve ser tratado
como interface descartável. Estado relevante será exportado para contratos próprios
antes de promoção.

## Rollback

Antes de existir implementação dependente, rollback consiste em reverter o commit
normativo e retirar o ADR do índice e do manifesto. Depois de existir runtime,
revogar essa decisão exigirá novo ADR, migração explícita, análise de aprisionamento,
backup, compatibilidade e autorização do Owner.

Não é permitido rollback silencioso para dependência do ChatGPT.

## Segurança

- chaves de APIs permanecem no Vault por SecretRef;
- terminal nunca imprime segredo;
- prompts e respostas são dados não confiáveis;
- Tool Gateway valida capability antes de qualquer efeito;
- Provider Router aplica privacidade e orçamento antes do envio;
- fallback não reduz classificação ou proteção;
- ChatGPT e MCP externos recebem menor privilégio;
- comando remoto exige autenticação forte e canal protegido;
- logs, eventos e evidências passam por sanitização;
- modo local não remove controles de autorização;
- atualização de adapter usa proveniência e verificação.

## Compatibilidade

A decisão é compatível com POD-DOCSET-V003 e torna explícitos princípios já
presentes de local-first, adapters, multiprovedor, autoridade separada e prova
independente. Ela adiciona o contrato do Terminal Soberano e critérios objetivos de
independência do ChatGPT e MCP.

## Evidência

Nesta revisão, a evidência comprova apenas a decisão documental:

- ADR presente e estruturalmente válido;
- invariantes explícitos;
- requisitos e cenários de aceite consolidados;
- registro no índice e manifesto;
- validação automatizada do DOCSET.

O runtime ainda não existe. Portanto, todos os requisitos SOV de produto permanecem
`DEFINED_NOT_IMPLEMENTED` até testes reais produzirem evidência.

## Condição de revisão

Revisar esta decisão se:

- o POD considerar depender de produto de chat externo;
- MCP deixar de ser opcional;
- uma API de IA passar a deter estado soberano;
- o terminal deixar de ser cliente independente;
- surgir requisito de operação totalmente desconectada com modelo local obrigatório;
- mudança de plataforma exigir novo contrato de identidade ou supervisor;
- prova demonstrar que algum invariante é fisicamente inviável.

## Documentos relacionados

- POD-DOC-001 — Índice Mestre V003;
- POD-DOC-002 — Baseline V003;
- POD-DOC-003 — DNA Operacional V002;
- POD-DOC-004 — Projeto Conceitual V002;
- POD-DOC-005 — Arquitetura Técnica V002;
- POD-DOC-006 — Contratos, Dados e Estados V002;
- POD-DOC-007 — Segurança e Autorizações V002;
- POD-DOC-008 — Matriz de Requisitos V002;
- POD-DOC-009 — Plano Mestre de Construção V002;
- POD-DOC-010 — Plano de Testes e Aceite V002;
- ADR-003 — Autoridade de prova e transição;
- ADR-005 — Portões humanos e dependências externas;
- ADR-007 — Núcleo de segurança desde a fundação;
- ADR-008 — Multiprojeto e federação.
