# POD — REGISTRO VIVO DE IDEIAS E MEMÓRIA

**Status:** WORKING / NON-NORMATIVE
**Finalidade:** capturar ideias, princípios, capacidades, riscos, correções e memórias durante a fase de concepção do POD sem alterar automaticamente a arquitetura oficial.

## Regra central

`MEMÓRIA REGISTRADA != REGRA ARQUITETURAL ATIVA`

Nenhuma entrada deste arquivo modifica por si só baseline, contrato, arquitetura, ADR ou implementação.

A arquitetura final será montada posteriormente por revisão integral deste registro, resolução de conflitos, deduplicação e consolidação.

## Tipos de registro

- IDEA
- PRINCIPLE
- CAPABILITY
- RULE_CANDIDATE
- CONSTRAINT
- LESSON_LEARNED
- RISK
- QUESTION
- ARCHITECTURAL_INSIGHT

## Estados

- CAPTURED
- UNDER_REVIEW
- CANDIDATE
- REJECTED
- MERGED
- CONSOLIDATED

## Estrutura de cada memória

```text
ID:
DATA:
TIPO:
STATUS:
NORMATIVO: NÃO

TEXTO ORIGINAL:

INTERPRETAÇÃO TÉCNICA:

MOTIVAÇÃO:

IMPACTO POSSÍVEL:

DEPENDÊNCIAS:

CONFLITOS POSSÍVEIS:

RELAÇÕES COM OUTRAS MEMÓRIAS:

DECISÃO FINAL:

INCORPORADO EM:
```

## Processo de consolidação futura

`CAPTURAR → AGRUPAR → COMPARAR → DETECTAR DUPLICIDADES → DETECTAR CONTRADIÇÕES → RESOLVER → SELECIONAR REGRAS FINAIS → MONTAR ARQUITETURA → VALIDAR PONTA A PONTA → BASELINE`

## Política durante a fase de concepção

1. Registrar cada nova ideia aqui.
2. Preservar o texto original separadamente da interpretação técnica.
3. Não criar novo ADR para cada ideia.
4. Não alterar baseline por memória isolada.
5. Permitir coexistência temporária de ideias conflitantes.
6. Resolver conflitos somente na consolidação do bloco ou da arquitetura final.
7. Preservar histórico de ideias rejeitadas, fundidas ou superadas.
8. Criar ADR somente quando uma decisão estrutural realmente precisar ser formalizada após consolidação.

---

# MEMÓRIAS

## MEM-POD-20260902-001

**DATA:** 02/09/2026  
**TIPO:** PRINCIPLE / CAPABILITY  
**STATUS:** CAPTURED  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL

> O que tem de bom em LMCP e WMCP será integralmente incorporado.

### INTERPRETAÇÃO TÉCNICA

Na consolidação final do POD, todas as capacidades, mecanismos, comportamentos, soluções, contratos, estratégias de recuperação, persistência, supervisão, execução, segurança, testes, ferramentas, evidências e lições tecnicamente boas e comprovadas existentes nos projetos doadores devem ser inventariadas e absorvidas pelo POD.

A incorporação integral significa preservar o valor técnico e funcional comprovado, não copiar cegamente defeitos, acoplamentos, nomenclaturas, caminhos, dependências ou decisões superadas.

O resultado deve ser capacidade nativa do POD, com identidade, contratos, testes e arquitetura próprios.

### MOTIVAÇÃO

Evitar perda do investimento técnico, das soluções já comprovadas e das lições aprendidas nos projetos doadores durante a construção do POD.

### IMPACTO POSSÍVEL

- inventário completo de capacidades dos projetos doadores;
- matriz de equivalência entre capacidades existentes e módulos futuros do POD;
- preservação de comportamentos comprovados por testes de regressão;
- fusão de implementações equivalentes;
- aperfeiçoamento de mecanismos existentes antes da incorporação;
- absorção em Cérebro, Coração, Memória, Federação, motores, segurança, recovery, observabilidade e ferramentas do POD conforme pertinência;
- criação futura de gates que provem que nenhuma capacidade útil foi perdida na migração.

### DEPENDÊNCIAS

- acesso ao código, documentação, testes e evidências dos projetos doadores;
- inventário técnico completo;
- definição da arquitetura final do POD;
- critérios objetivos para classificar uma capacidade como boa, comprovada, redundante, defeituosa ou superada.

### CONFLITOS POSSÍVEIS

Pode conflitar com a regra ZERO DONOR COUPLING se "incorporação integral" for interpretada como dependência direta ou cópia estrutural do projeto doador. A interpretação correta é absorção integral do valor técnico, mantendo zero dependência de runtime, build, configuração, nomenclatura, caminho ou serviço doador no POD final.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Relaciona-se com o princípio de preservação, comparação, fusão, aperfeiçoamento, teste, regressão, migração e comprovação antes de aposentar qualquer capacidade existente.

### DECISÃO FINAL

PENDENTE DE CONSOLIDAÇÃO DA ARQUITETURA FINAL.

### INCORPORADO EM

Ainda não incorporado em arquitetura normativa.

---

## MEM-POD-20260902-002

**DATA:** 02/09/2026  
**TIPO:** ARCHITECTURAL_INSIGHT / CAPABILITY  
**STATUS:** CAPTURED  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL

> Componentes de POD: Memoria, Governador, Cerebro, Tunel Core, sistema imunologico.

### INTERPRETAÇÃO TÉCNICA

A composição conceitual atual do POD considera cinco componentes principais candidatos à arquitetura final:

1. **Memória** — responsável por preservar conhecimento, estado, histórico, evidências, checkpoints, documentos e informações necessárias à continuidade do trabalho.
2. **Governador** — responsável pelo controle operacional, recursos, prioridades, concorrência, supervisão, recuperação e aplicação das regras operacionais, sem ser a origem da autonomia ou autoridade técnica do POD.
3. **Cérebro** — responsável por compreensão, raciocínio, decisão técnica, planejamento, diagnóstico, seleção de conhecimento e condução intelectual da missão.
4. **Túnel Core** — componente candidato responsável pela conectividade durável, segura e reconciliável entre POD, nós, canais externos e capacidades distribuídas, preservando a regra de que conexão não é execução.
5. **Sistema Imunológico** — componente candidato responsável por detectar, classificar, conter, recuperar e aprender com ameaças, anomalias, corrupção, comportamentos indevidos, falhas recorrentes e degradação operacional, sem competir com a autoridade do Cérebro ou do Governador.

Essa lista representa a visão conceitual atual e poderá ser ampliada, fundida ou reorganizada durante a consolidação final.

### MOTIVAÇÃO

Definir os grandes órgãos funcionais do POD antes de detalhar serviços, módulos e contratos, reduzindo fragmentação prematura da arquitetura.

### IMPACTO POSSÍVEL

- organização da futura arquitetura por grandes componentes soberanos;
- redefinição dos limites entre Cérebro, Governador e Sistema Imunológico;
- consolidação de conectividade e federação sob o conceito de Túnel Core;
- redistribuição de funções hoje espalhadas entre recovery, segurança, observabilidade, watchdog, supervisor e conectividade;
- definição posterior de contratos explícitos entre os cinco componentes.

### DEPENDÊNCIAS

- definição detalhada do papel de cada componente;
- comparação com capacidades existentes nos projetos doadores;
- análise de sobreposição entre Governador, Sistema Imunológico, Recovery, Supervisor e Segurança;
- definição do que pertence ao núcleo soberano e do que deve permanecer como serviço auxiliar.

### CONFLITOS POSSÍVEIS

Pode haver sobreposição entre Governador e Sistema Imunológico, e entre Túnel Core e conceitos anteriores de Federação, Gateway, MCP, Action e Relay. Esses conflitos não serão resolvidos agora; serão analisados na consolidação da arquitetura final.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Relaciona-se com MEM-POD-20260902-001, pois capacidades úteis existentes nos projetos doadores poderão ser absorvidas e distribuídas entre esses componentes após inventário e comparação.

### DECISÃO FINAL

PENDENTE DE CONSOLIDAÇÃO DA ARQUITETURA FINAL.

### INCORPORADO EM

Ainda não incorporado em arquitetura normativa.

---

## MEM-POD-20260902-003

**DATA:** 02/09/2026  
**TIPO:** ARCHITECTURAL_INSIGHT / RULE_CANDIDATE / CAPABILITY  
**STATUS:** CAPTURED  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL

> O que podemos implementar diretamente no codigo fonte de POD?

Decisão de trabalho associada: iniciar somente por uma fundação neutra, formada por invariantes, contratos, primitivas, portas, testes e gates de baixo arrependimento, evitando congelar prematuramente a topologia dos grandes componentes.

### INTERPRETAÇÃO TÉCNICA

Durante a fase de concepção, o código-fonte do POD pode receber componentes cujo valor permaneça válido independentemente da arquitetura final. A implementação inicial deve se concentrar no DNA técnico transversal e evitar decisões prematuras sobre a distribuição definitiva de responsabilidades entre os grandes componentes.

Candidatos de baixo arrependimento para implementação direta:

1. Identidades soberanas: `mission_id`, `project_id`, `command_id`, `event_id`, `attempt_id`, `worker_id`, `checkpoint_id`, `evidence_id`, `incident_id`, `node_id` e `correlation_id`.
2. Separação de entidades e ciclos de vida: missão, tentativa, Worker, processo, sessão e conexão são entidades diferentes.
3. Contratos genéricos de comando, evento, resultado, evidência e checkpoint.
4. Idempotência e deduplicação por chave lógica.
5. Invariante de persistir antes de confirmar.
6. Portas/interfaces de persistência: Mission Repository, Event Store, State Store, Checkpoint Store, Evidence Store, Idempotency Store, Inbox e Outbox.
7. Lease, generation e fencing token para rejeitar mutação obsoleta.
8. Health funcional multidimensional: LIVENESS, READINESS e PROGRESS.
9. Taxonomia de falhas que separa falha de tentativa, ferramenta, Worker, teste, serviço e estratégia de conclusão terminal da missão.
10. Checkpoints versionados, verificáveis, persistentes e reconciliáveis.
11. Modelo canônico de evidências com hash e proveniência.
12. Motor genérico de prova de conclusão, culminando em `MISSION_PROVEN` somente quando todos os gates obrigatórios forem satisfeitos.
13. Primitivas de segurança para segredo, referência de segredo e redaction centralizada.
14. Abstração de relógio com UTC para auditoria e monotônico para duração, lease, timeout, heartbeat e backoff.
15. Primitivas reutilizáveis de retry, backoff, circuit breaker e restart budget.
16. Contratos de recursos e capacidade, incluindo snapshots e decisões ADMIT/DEFER/THROTTLE, sem implementar ainda o Governador completo.
17. Gates arquiteturais de desacoplamento para impedir dependência indevida de projetos doadores.
18. Estrutura inicial de testes unitários, de contrato, arquitetura, resiliência, recovery e segurança.

Estrutura física candidata, ainda não normativa:

```text
src/pod/
├── domain/
│   ├── ids.py
│   ├── mission.py
│   ├── command.py
│   ├── event.py
│   ├── attempt.py
│   ├── checkpoint.py
│   ├── evidence.py
│   ├── health.py
│   ├── lease.py
│   ├── fencing.py
│   ├── errors.py
│   └── proof.py
├── ports/
│   ├── persistence.py
│   ├── execution.py
│   ├── privileged_execution.py
│   ├── clock.py
│   ├── storage.py
│   └── telemetry.py
└── primitives/
    ├── retry.py
    ├── backoff.py
    ├── circuit_breaker.py
    ├── redaction.py
    └── hashing.py
```

Testes candidatos:

```text
tests/
├── unit/
├── contract/
├── architecture/
├── resilience/
├── recovery/
└── security/
```

### MOTIVAÇÃO

Permitir que a construção do POD avance enquanto a arquitetura final continua em evolução, reduzindo retrabalho e evitando que decisões prematuras sobre componentes, processos, banco de dados, conectividade ou topologia obriguem futuras reescritas extensas.

### IMPACTO POSSÍVEL

- criação futura de uma Fase 0 de Fundação Neutra;
- estabelecimento precoce de contratos estáveis e invariantes de domínio;
- possibilidade de testar durabilidade, idempotência, fencing, health, evidência e prova antes da topologia definitiva;
- redução do custo de mudanças arquiteturais posteriores;
- base comum para absorção das capacidades tecnicamente comprovadas dos projetos doadores.

### NÃO IMPLEMENTAR AINDA COMO TOPOLOGIA FINAL

Enquanto a arquitetura estiver em concepção, evitar congelar diretamente no código:

- Governador completo;
- Cérebro completo;
- Memória física definitiva;
- Túnel Core definitivo;
- Sistema Imunológico definitivo;
- Federação definitiva;
- Gateway definitivo;
- topologia e quantidade final de processos/serviços;
- banco de dados concreto como dependência de domínio;
- Scheduler completo;
- topologia final de Workers;
- Learning & Training Tool definitiva;
- Provider Manager definitivo;
- Painel definitivo.

Esses elementos podem receber interfaces e contratos neutros quando necessário, mas sua composição final deve aguardar a consolidação arquitetural.

### DEPENDÊNCIAS

- continuação da concepção arquitetural;
- inventário e deduplicação das capacidades candidatas provenientes dos documentos técnicos analisados;
- definição posterior dos limites dos grandes componentes do POD;
- testes objetivos para validar cada invariante implementado.

### CONFLITOS POSSÍVEIS

A implementação precoce de contratos excessivamente específicos pode, mesmo dentro da Fundação Neutra, cristalizar decisões ainda não consolidadas. Portanto, qualquer código iniciado nesta fase deve minimizar dependência de infraestrutura concreta e separar domínio, portas e adaptadores.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Relaciona-se com MEM-POD-20260902-001, pois fornece uma superfície neutra para absorção de capacidades úteis, e com MEM-POD-20260902-002, pois evita decidir prematuramente como essas capacidades serão distribuídas entre Memória, Governador, Cérebro, Túnel Core e Sistema Imunológico.

### DECISÃO FINAL

PENDENTE DE CONSOLIDAÇÃO DA ARQUITETURA FINAL.

### INCORPORADO EM

Ainda não incorporado em arquitetura normativa nem autorizado como arquitetura final.

---

## MEM-POD-20260902-004

**DATA:** 02/09/2026  
**TIPO:** PRINCIPLE / RULE_CANDIDATE / SOURCE_CODE_REQUIREMENT  
**STATUS:** MERGED  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL

> Registra, estes 10 pontos tem que fazer parte do codigo fonte de POD.

### INTERPRETAÇÃO TÉCNICA

Foram registrados dez requisitos obrigatórios de comportamento do código-fonte: missão aceita como obrigação de buscar `MISSION_PROVEN`; usuário não convertido em operador técnico; raciocínio e decisão de engenharia; não perda de estado essencial; autodiagnóstico/contenção/autorrecuperação; conhecimento técnico utilizável; interface simples; verdade operacional; soberania com segurança; absorção de valor técnico comprovado sem acoplamento doador.

O detalhamento integral permanece preservado no anexo:

`docs/working/MEM-POD-20260902-004_DEZ_REQUISITOS_OBRIGATORIOS_DO_CODIGO_FONTE.md`

### MOTIVAÇÃO

Garantir que propriedades centrais do POD sejam materializadas em código, contratos, testes, evidências e gates, e não permaneçam apenas como documentação.

### IMPACTO POSSÍVEL

Criação de rastreabilidade requisito → contrato → implementação → teste → evidência → gate.

### DEPENDÊNCIAS

Consolidação da arquitetura final e matriz de rastreabilidade.

### CONFLITOS POSSÍVEIS

A posição física dos comportamentos pode mudar; os comportamentos aprovados não devem ser eliminados.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Fundido conceitualmente em MEM-POD-20260902-005, que consolida quatorze requisitos.

### DECISÃO FINAL

APROVADO PELO PROPRIETÁRIO COMO REQUISITO DE MATERIALIZAÇÃO FUTURA NO CÓDIGO.

### INCORPORADO EM

Registro Vivo mestre; detalhamento preservado no anexo citado. Ainda não normativo nem implementado.

---

## MEM-POD-20260902-005

**DATA:** 02/09/2026  
**TIPO:** PRINCIPLE / CAPABILITY / RULE_CANDIDATE / ARCHITECTURAL_INSIGHT  
**STATUS:** CANDIDATE  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL

> registre em Registro Vivo

### INTERPRETAÇÃO TÉCNICA

Consolida quatorze requisitos fundamentais do POD: os dez requisitos de MEM-004 mais autossustentação operacional, governança adaptativa de recursos, rastreabilidade/reprodutibilidade total e degradação inteligente com continuidade parcial.

Regra superior:

`POD NÃO TRANSFERE COMPLEXIDADE TÉCNICA PARA O USUÁRIO.`

Regra de progresso:

`ATIVIDADE != PROGRESSO`

O detalhamento integral permanece preservado no anexo:

`docs/working/MEM-POD-20260902-005_QUATORZE_REQUISITOS_FUNDAMENTAIS.md`

### MOTIVAÇÃO

Definir propriedades de raiz que tornem o POD um construtor soberano confiável e operacionalmente sustentável.

### IMPACTO POSSÍVEL

Afeta missão, Cérebro, Engenharia de Construção, Memória, Governador, Sistema Imunológico, recursos, recovery, interfaces, evidências e autossustentação.

### DEPENDÊNCIAS

Contratos finais, arquitetura consolidada, rastreabilidade e gates objetivos.

### CONFLITOS POSSÍVEIS

Sobreposições de responsabilidade entre Governador, Sistema Imunológico, recovery e runtime serão resolvidas na consolidação.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Complementa e incorpora MEM-004.

### DECISÃO FINAL

APROVADO PELO PROPRIETÁRIO COMO CONJUNTO FUNDAMENTAL CANDIDATO À CONSOLIDAÇÃO FINAL.

### INCORPORADO EM

Registro Vivo mestre; detalhamento preservado no anexo citado. Ainda não baseline nem implementação comprovada.

---

## MEM-POD-20260902-006

**DATA:** 02/09/2026  
**TIPO:** ARCHITECTURAL_INSIGHT / RULE_CANDIDATE / SECURITY  
**STATUS:** CANDIDATE  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL

> Ele trata da contrução de um produto pelo POD ou da contrução de POD?

### INTERPRETAÇÃO TÉCNICA

Separação obrigatória entre dois domínios conceituais:

```text
SEGURANÇA_DO_POD
→ protege o construtor

SEGURANÇA_DO_PRODUTO
→ protege o produto construído pelo POD
```

`SECURITY_MAX` é fonte doadora principalmente para a segurança, hardening e prova do próprio POD. Técnicas podem ser reaproveitadas na segurança do produto, mas os domínios não devem ser confundidos.

Detalhamento:

`docs/working/MEM-POD-20260902-006_SEGURANCA_DO_POD_VS_SEGURANCA_DO_PRODUTO.md`

### MOTIVAÇÃO

Evitar mistura entre proteção do construtor soberano e engenharia de segurança aplicada a cada produto construído.

### IMPACTO POSSÍVEL

Gates distintos, isolamento, responsabilidades distintas e reutilização controlada de capacidades de segurança.

### DEPENDÊNCIAS

Consolidação de Segurança transversal, Sistema Imunológico e Engenharia de Construção.

### CONFLITOS POSSÍVEIS

Sobreposição entre Segurança transversal, Governador, Sistema Imunológico, recovery e execução privilegiada.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Relaciona-se diretamente com MEM-007.

### DECISÃO FINAL

APROVADO COMO DISTINÇÃO CONCEITUAL PARA CONSOLIDAÇÃO.

### INCORPORADO EM

Registro Vivo mestre; detalhamento preservado no anexo citado.

---

## MEM-POD-20260902-007

**DATA:** 02/09/2026  
**TIPO:** CAPABILITY / RULE_CANDIDATE / ARCHITECTURAL_INSIGHT  
**STATUS:** CANDIDATE  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL

> Agora vamos tratar SEGURANCA_DO_PRODUTO do produto construido por POD

### INTERPRETAÇÃO TÉCNICA

`SEGURANÇA_DO_PRODUTO` é capacidade candidata nativa da Engenharia de Construção do POD. Deve abranger, conforme risco e aplicabilidade: classificação de risco, threat modeling, Security by Design, Secure Coding, identidade/autorização, proteção de dados e segredos, supply chain, API Security, AI Security, infraestrutura, banco, logging seguro, testes adversariais, regressão e evidência.

Princípio:

```text
PRODUTO FUNCIONANDO != PRODUTO SEGURO
```

Candidato de conclusão:

```text
FUNCTIONAL_PROVEN
+ QUALITY_PROVEN
+ SECURITY_PROVEN
+ RECOVERY_PROVEN
+ EVIDENCE_PROVEN
= PRODUCT_MISSION_PROVEN
```

Detalhamento:

`docs/working/MEM-POD-20260902-007_SEGURANCA_DO_PRODUTO.md`

### MOTIVAÇÃO

Impedir que o POD considere um produto pronto apenas porque funciona.

### IMPACTO POSSÍVEL

Product Security Engineering nativa, gates `PROD-SEC-GATE-*`, testes adversariais e bloqueio de conclusão diante de falhas críticas aplicáveis.

### DEPENDÊNCIAS

Engenharia de Construção, catálogo de riscos/controles/testes e critérios de `SECURITY_PROVEN`.

### CONFLITOS POSSÍVEIS

Não confundir com Segurança do próprio POD nem aplicar controles desproporcionais ao risco do produto.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Relaciona-se com MEM-006 e com os 14 requisitos fundamentais.

### DECISÃO FINAL

APROVADO COMO CAPACIDADE CANDIDATA PARA CONSOLIDAÇÃO FINAL.

### INCORPORADO EM

Registro Vivo mestre; detalhamento preservado no anexo citado.

---

## MEM-POD-20260902-008

**DATA:** 02/09/2026  
**TIPO:** ARCHITECTURAL_INSIGHT / CAPABILITY / RULE_CANDIDATE  
**STATUS:** CANDIDATE  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL / INTENÇÃO DO USUÁRIO

> A Rede Federada pode ter hoje 4 nós, amanhã 10, depois 20, depois 3, 9 ou apenas 1. Ela deve ser adaptável, rápida e de fácil conexão. Ao colocar um PC na rede, ele deve entrar automaticamente, descobrir e liberar suas ferramentas para uso conforme as políticas do POD. O operador deve poder ordenar de forma simples: “execute missão no PC 1”, “use PC 3 para esta tarefa”, “use PC X”, sem precisar lidar com IP, porta, SSH, PID ou configuração técnica.

### INTERPRETAÇÃO TÉCNICA

A Rede Federada do POD deve ser uma malha elástica de nós dinâmicos, autoformável e orientada por capacidades, na qual a quantidade de nós é estado operacional e não parte fixa da arquitetura.

```text
FEDERATION_SIZE = N
N pode variar dinamicamente: 1 → 4 → 10 → 20 → 3 → 9 → 1
```

Adicionar ou remover nós não deve exigir alteração arquitetural, recompilação de topologia, reconfiguração manual de rotas ou recadastro manual de ferramentas.

Princípio central:

```text
ADICIONOU UM NÓ = ADICIONOU CAPACIDADE AO POD
REMOVEU UM NÓ != PERDEU A MISSÃO
```

O detalhamento integral permanece preservado no anexo:

`docs/working/MEM-POD-20260902-008_REDE_FEDERADA_ELASTICA_FAST_PATH_E_FLUIDEZ.md`

### MOTIVAÇÃO

Permitir expansão e redução dinâmica da frota sem aumentar a complexidade operacional para o usuário e sem sacrificar persistência, velocidade ou recuperação.

### IMPACTO POSSÍVEL

Federação, Túnel Core, Node Engine, roteamento, recursos, estado distribuído, segurança, painel e testes de desempenho/falha.

### DEPENDÊNCIAS

Contratos de identidade, autoridade distribuída, persistência/reconciliação, segurança e compatibilidade de nós.

### CONFLITOS POSSÍVEIS

Limites entre Túnel Core, Federação, Governador, Node Agent e Micro-Scheduler ainda precisam ser fechados.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Relaciona-se aos requisitos de persistência, degradação inteligente, recursos e verdade operacional.

### DECISÃO FINAL

APROVADO PELO PROPRIETÁRIO COMO DIREÇÃO CONCEITUAL PARA CONSOLIDAÇÃO.

### INCORPORADO EM

Registro Vivo mestre; detalhamento preservado no anexo citado.

---

## MEM-POD-20260902-009

**DATA:** 02/09/2026  
**TIPO:** CAPABILITY / RULE_CANDIDATE / ARCHITECTURAL_INSIGHT  
**STATUS:** CANDIDATE  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL

> **Learning & Training Tool nativa do POD**. aprovado

### INTERPRETAÇÃO TÉCNICA

Fica aprovada para consolidação arquitetural a **Learning & Training Tool nativa do POD**, absorvendo o valor técnico do projeto doador analisado sem manter identidade, caminhos, contratos ou dependências WMCP.

Posição conceitual aprovada:

```text
PART_OF_POD_SYSTEM = TRUE
PART_OF_CORE = FALSE
INVOKED_ON_DEMAND = TRUE
PERMANENTLY_LOADED = FALSE
```

A ferramenta possui dois modos distintos:

```text
LEARNING → o POD adquire, valida, pratica, prova e mantém competência para si
TRAINING → o POD transfere, especializa, testa e comprova competência em alvo externo autorizado
```

Definição de aprendizado:

```text
APRENDER != LER E ARMAZENAR
APRENDER = COMPREENDER + VALIDAR + EXPERIMENTAR + OPERAR + REPETIR + FALHAR + RECUPERAR + EXPLICAR + DOCUMENTAR + MEMORIZAR + MANTER ATUALIZADO + PROVAR
```

Capacidades aprovadas para absorção nativa, sujeitas a contrato e prova: Curriculum Manager; Knowledge Plane; Epistemic Integrity; Source Dependency Graph; Experience Plane; Action→Effect; State Graph/State Novelty; trajetórias; Procedure Synthesis; Deterministic Replay; Failure & Recovery Learning; Permanent Operational Memory; Change Monitor; Local Relearning; Competence Proof; Training Eligibility; Training Plane; escolha automática do método de especialização; provider/model agnostic; evidência e verificação independente.

A arquitetura interna candidata será tratada em quatro planos conceituais:

```text
1. KNOWLEDGE PLANE
2. EXPERIENCE PLANE
3. COMPETENCE PLANE
4. TRAINING PLANE
```

Conhecimento adquirido não cria autorização:

`KNOWLEDGE != AUTHORITY`

### MOTIVAÇÃO

Transformar aprendizado do POD em competência operacional comprovada, persistente e atualizável, e permitir treinamento controlado de produtos, agentes, skills, módulos e modelos quando aplicável.

### IMPACTO POSSÍVEL

Integração com Cérebro, Memória, Engenharia de Construção, Rede Federada, Segurança, Evidências e recursos.

### DEPENDÊNCIAS

Contratos neutros POD, Memória soberana, ferramentas/adapters autorizados, políticas de segurança/dados, gates de competência/evidência e Rede Federada quando aplicável.

### CONFLITOS POSSÍVEIS

Não incorporar identidade de projeto doador, não permitir que conteúdo aprendido vire política/autoridade, não confundir LEARNING com TRAINING e não declarar competência sem replay/evidência/gates.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Relaciona-se com MEM-001, MEM-003, MEM-005 e MEM-008.

### DECISÃO FINAL

APROVADO PELO PROPRIETÁRIO PARA FAZER PARTE DA ARQUITETURA A SER CONSOLIDADA DO POD.

### INCORPORADO EM

Registro Vivo mestre. A incorporação normativa ocorrerá somente na consolidação arquitetural correspondente.

---

## MEM-POD-20260902-010

**DATA:** 02/09/2026  
**TIPO:** ARCHITECTURAL_INSIGHT / CONSTRAINT / RULE_CANDIDATE  
**STATUS:** CANDIDATE  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL

> **seis lacunas**: aprovado, registre

### INTERPRETAÇÃO TÉCNICA

Ficam aprovadas para fechamento durante a consolidação arquitetural seis lacunas: soberania durante partição da Rede Federada; mobilidade de workspace/dados/artefatos entre nós; ciclo de vida da frota federada; Product Delivery Contract; economia de execução/orçamento técnico; consolidação formal de Learning & Training.

O detalhamento e a resolução conceitual posterior estão preservados em MEM-POD-20260902-013.

### MOTIVAÇÃO

Fechar ambiguidades que poderiam produzir split-brain, inconsistência distribuída, artefatos conflitantes, incompatibilidade de nós, entrega incompleta, desperdício de recursos ou aprendizado sem contrato claro.

### IMPACTO POSSÍVEL

Federação, Memória, Túnel Core, Governador, Engines, Engenharia de Construção, Learning & Training, segurança e testes.

### DEPENDÊNCIAS

MEM-008, MEM-009, 14 requisitos fundamentais, Segurança do POD/Produto e contratos futuros de identidade, lease/fencing, evidência e MISSION_PROVEN.

### CONFLITOS POSSÍVEIS

Fechar sem congelar tecnologia específica e sem reintroduzir acoplamento de projetos doadores.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Relaciona-se especialmente com MEM-003, MEM-005, MEM-007, MEM-008, MEM-009 e MEM-013.

### DECISÃO FINAL

APROVADO PELO PROPRIETÁRIO COMO CONJUNTO DE LACUNAS OBRIGATÓRIAS; FECHAMENTO CONCEITUAL REGISTRADO EM MEM-013.

### INCORPORADO EM

Registro Vivo mestre; problema histórico preservado e resolução conceitual referenciada.

---

## MEM-POD-20260902-011

**DATA:** 02/09/2026  
**TIPO:** CAPABILITY / RULE_CANDIDATE / DELIVERY_REQUIREMENT / ARCHITECTURAL_INSIGHT  
**STATUS:** CANDIDATE  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL

> o painel não é enfeite ele precisa ser funcional

### INTERPRETAÇÃO TÉCNICA

O Painel do POD deve ser tratado como **console operacional visual funcional**, e não como dashboard decorativo ou camada de apresentação criada apenas ao final da construção.

Regra central:

```text
PAINEL POD = OBSERVAR + COMANDAR + DIAGNOSTICAR + INTERVIR + COMPROVAR
PAINEL POD != ENFEITE
```

O Painel deve ser uma das primeiras entregas incrementais funcionais, construída depois da fundação persistente e do Core operacional mínimo, e deve evoluir junto com o restante do POD.

Sequência candidata:

```text
1. FUNDAÇÃO PERSISTENTE MÍNIMA
2. CORE OPERACIONAL MÍNIMO
3. PAINEL OPERACIONAL FUNCIONAL
4. EVOLUÇÃO DOS DEMAIS COMPONENTES
5. PAINEL EVOLUI JUNTO COM CADA CAPACIDADE
```

A primeira versão do Painel não deve ser mock visual. Mesmo simples, deve consumir estado real e comandar o runtime real por contratos oficiais.

### CAPACIDADES MÍNIMAS DA PRIMEIRA ENTREGA FUNCIONAL

```text
SYSTEM → health funcional real, versão, serviços/componentes essenciais
MISSIONS → mission_id, estado, progresso real, etapa, bloqueios, MISSION_PROVEN
EVIDENCE → checkpoints, testes, evidências/provas
FEDERATION → nós, ONLINE/READY/DEGRADED, capabilities, recursos
CONTROL → pause, resume, recovery e comandos autorizados existentes
```

### REGRAS DE AUTORIDADE DO PAINEL

```text
PAINEL LÊ → Read Models / estado soberano
PAINEL COMANDA → Command API → Core → política → persistência → execução
PAINEL RECEBE → eventos reais
```

É proibido o Painel editar banco soberano diretamente, matar processos diretamente, escrever configuração soberana diretamente ou inventar status sem prova.

```text
FECHAR O PAINEL != PARAR O POD
```

### GATES CANDIDATOS DO PAINEL

```text
PANEL_REAL_STATE_GATE
PANEL_COMMAND_PATH_GATE
PANEL_NO_DIRECT_DB_MUTATION_GATE
PANEL_CLOSE_CONTINUITY_GATE
PANEL_OPERATIONAL_COVERAGE_GATE
```

### MOTIVAÇÃO

Dar ao operador visão verdadeira e capacidade real de controle desde as primeiras fases e impedir que a interface seja adicionada tardiamente como decoração desacoplada do runtime.

### IMPACTO POSSÍVEL

Prioridade de entrega precoce, Read Models, Query API, Command API, stream de eventos e testes E2E contra estado real.

### DEPENDÊNCIAS

Fundação persistente/Core mínimo, contratos de comando/evento/estado/health/evidência, Read Models e segurança/autorização.

### CONFLITOS POSSÍVEIS

Não contraria MEM-003: o Painel definitivo não precisa ser congelado cedo; a decisão é construir um Painel Operacional Mínimo funcional cedo e evoluí-lo.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Relaciona-se com MEM-003, MEM-005, MEM-008 e MEM-010.

### DECISÃO FINAL

APROVADO PELO PROPRIETÁRIO: O PAINEL É UMA DAS PRIMEIRAS ENTREGAS FUNCIONAIS DO POD E DEVE OPERAR SOBRE O RUNTIME REAL, NÃO SER UM ENFEITE.

### INCORPORADO EM

Registro Vivo mestre. Deve entrar na consolidação arquitetural, plano de construção e matriz de testes/rastreabilidade.

---

## MEM-POD-20260902-012

**DATA:** 02/09/2026  
**TIPO:** ARCHITECTURAL_INSIGHT / CAPABILITY / RULE_CANDIDATE  
**STATUS:** CANDIDATE  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL

> arquitetura Vai ser hibrida, com compatibilidade com todos os provedores de IA A Api fica no cerebro do sistema.

Decisão posterior:

> Provado: oito pontos para essa arquitetura híbrida, POD será híbrido e multi-provider por definição

### INTERPRETAÇÃO TÉCNICA

O POD será **híbrido e multi-provider por definição**. Provedores e modelos de IA são recursos cognitivos substituíveis consumidos pelo Cérebro; nenhum provedor/modelo é o Cérebro nem adquire autoridade soberana.

```text
AI_PROVIDER_API_OWNER = POD_BRAIN
PROVIDER_LOCK_IN = FALSE
MODEL_AGNOSTIC = TRUE
CONTEXT_OWNED_BY_POD = TRUE
PROVIDER != POD BRAIN
MODEL != OPERATIONAL AUTHORITY
```

Os oito mecanismos aprovados são:

1. Provider Capability Registry;
2. normalização de contratos;
3. Context Portability;
4. Policy Router antes do Provider Router;
5. health funcional de modelos/provedores;
6. versionamento e regressão de modelos;
7. Shadow/Challenger Evaluation orientado por risco;
8. degradação cognitiva controlada.

Arbitragem de respostas divergentes pertence ao Cérebro e deve usar requisitos, evidência, testabilidade, histórico relevante e experimentos/testes quando possível, nunca votação cega.

Credenciais permanecem no Vault/Secret Broker por `SecretRef`, não no estado cognitivo.

Detalhamento integral:

`docs/working/MEM-POD-20260902-012_ARQUITETURA_HIBRIDA_MULTI_PROVIDER_CEREBRO.md`

### MOTIVAÇÃO

Garantir soberania cognitiva, substituição de fornecedores, failover, privacidade, controle de custo/latência e evolução futura sem reescrever o POD.

### IMPACTO POSSÍVEL

Cérebro, contexto, providers, Vault, Learning & Training, segurança, economia de execução e evidência cognitiva.

### DEPENDÊNCIAS

Policy, classificação de dados, Vault, Context Engine, Provider Adapters e métricas de qualidade/latência/custo.

### CONFLITOS POSSÍVEIS

Nenhum provider pode assumir autoridade do Cérebro; resultado de modelo não é política nem autorização.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Relaciona-se com MEM-005, MEM-007, MEM-009, MEM-010 e MEM-013.

### DECISÃO FINAL

APROVADO PELO PROPRIETÁRIO COMO DIREÇÃO CONCEITUAL PARA CONSOLIDAÇÃO.

### INCORPORADO EM

Registro Vivo mestre; detalhamento preservado no anexo citado.

---

## MEM-POD-20260902-013

**DATA:** 02/09/2026  
**TIPO:** ARCHITECTURAL_INSIGHT / RULE_CANDIDATE / CONSTRAINT / CONSOLIDATION_INPUT  
**STATUS:** CANDIDATE  
**NORMATIVO:** NÃO

### TEXTO ORIGINAL

> Correto, faça a correção, feche as lacunas e registre

### INTERPRETAÇÃO TÉCNICA

A auditoria conceitual ponta a ponta identificou lacunas e sobreposições antes da consolidação dos contratos e da documentação normativa. O proprietário aprovou sua correção e fechamento conceitual.

Não serão criados novos grandes órgãos apenas para resolvê-las. As sobreposições ficam normalizadas:

```text
CORAÇÃO = agrupamento/metáfora da governança operacional; não segundo Governador
TÚNEL CORE = substrato de transporte/conectividade da Rede Federada
SISTEMA IMUNOLÓGICO = mecanismo ativo de Segurança; não segunda Policy
POLICY/CONSTITUIÇÃO = autoridade transversal de limites; não conhecimento nem modelo de IA
```

Foram fechadas conceitualmente 24 áreas:

1. matriz soberana de autoridade;
2. Constituição/Policy;
3. precedência decisão × segurança × recursos;
4. ciclo de vida completo da missão;
5. pause/drain/cancel/preempt/rollback/compensate;
6. planejamento × engenharia × scheduling × roteamento;
7. modelo de consistência por classe de estado;
8. ordenação/event delivery com at-least-once + idempotência + dedup + reconciliação;
9. tempo distribuído com UTC + monotonic + sequence/generation;
10. soberania durante partição/fencing;
11. mobilidade de workspace/dados/artefatos por manifesto/hash/Writer Lease/promotion;
12. ciclo de vida da frota JOIN→ENROLL→TRUST/COMPAT→READY→DRAIN→LEAVE→REVOKE;
13. trust bootstrap, rotação e revogação de identidade de nó;
14. envelope restrito de delegação do Micro-Scheduler;
15. fairness multiprojeto, quotas, burst e starvation prevention;
16. escopos explícitos de compartilhamento entre projetos;
17. arquitetura híbrida/multi-provider;
18. arbitragem cognitiva por evidência/teste, não maioria;
19. integração Learning & Training sem promoção direta para Policy/Authority;
20. Product Delivery Contract com gates aplicáveis;
21. self-update side-by-side com known-good/rollback;
22. prova independente separada de quem construiu;
23. definição objetiva de progresso real;
24. economia de execução por custo total da missão, não paralelismo máximo.

Invariantes resultantes:

```text
NO_COMPETING_SOVEREIGN_AUTHORITIES = TRUE
POLICY_PRECEDES_TECHNICAL_ACTION = TRUE
ONE_AUTHORITATIVE_GENERATION_PER_MUTABLE_SCOPE = TRUE
STALE_GENERATION_CANNOT_COMMIT = TRUE
CACHE_IS_NOT_SOURCE_OF_TRUTH = TRUE
DISCOVERY_IS_NOT_TRUST = TRUE
PROJECT_SCOPE_IS_EXPLICIT = TRUE
PROVIDER_IS_NOT_BRAIN = TRUE
KNOWLEDGE_IS_NOT_POLICY = TRUE
BUILDER_IS_NOT_SOLE_VERIFIER = TRUE
ACTIVITY_IS_NOT_PROGRESS = TRUE
MORE_PARALLELISM_IS_NOT_ALWAYS_MORE_EFFICIENT = TRUE
```

O detalhamento integral das decisões e limites de cada uma das 24 áreas está preservado em:

`docs/working/MEM-POD-20260902-013_FECHAMENTO_DAS_LACUNAS_DA_AUDITORIA_CONCEITUAL.md`

### MOTIVAÇÃO

Eliminar ambiguidades conceituais antes de transformar o projeto em contratos, ADRs, schemas, implementação e testes.

### IMPACTO POSSÍVEL

Toda a arquitetura: missão, Cérebro, Engenharia, Governador, Memória, Federação, Engines, Segurança, Learning & Training, multi-provider, multiprojeto, entrega, self-update e prova.

### DEPENDÊNCIAS

Consolidação posterior em contratos e documentação normativa.

### CONFLITOS POSSÍVEIS

As decisões são conceituais; detalhes físicos/tecnológicos ainda não estão congelados e devem preservar ZERO DONOR COUPLING.

### RELAÇÕES COM OUTRAS MEMÓRIAS

Fecha conceitualmente MEM-010 e se relaciona com MEM-005, MEM-007, MEM-008, MEM-009, MEM-011 e MEM-012.

### DECISÃO FINAL

APROVADO PELO PROPRIETÁRIO PARA CORRIGIR E FECHAR AS LACUNAS DO PROJETO CONCEITUAL ANTES DA CONSOLIDAÇÃO DOS CONTRATOS E DA DOCUMENTAÇÃO NORMATIVA.

Fechamento conceitual não equivale a contrato implementado, teste, prova ou baseline.

### INCORPORADO EM

Registro Vivo mestre; detalhamento preservado no anexo citado.
