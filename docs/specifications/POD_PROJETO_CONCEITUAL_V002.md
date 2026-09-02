# POD — PROJETO CONCEITUAL — V002

**Identificador:** POD-DOC-004
**Versão:** 2.0.0
**Status:** ACTIVE
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A2 — definição de produto
**Substitui:** projeto conceitual reconsolidado V001 e conceitos do DOCSET V002

## 1. Problema

Construção de software assistida por IA costuma depender de sessões frágeis, contexto parcial, fornecedores específicos e confirmação textual de sucesso. Quando a sessão cai, o executor falha ou o modelo muda, estado e responsabilidade podem ser perdidos.

O POD existe para transformar um objetivo em uma missão durável, governada e comprovável.

## 2. Usuário

O usuário principal é o Owner do produto ou projeto. Ele define:

- objetivo;
- prioridade;
- restrições de negócio;
- orçamento;
- prazo quando existir;
- critérios de aceite de negócio;
- decisões soberanas e portões humanos.

O usuário não deve operar processos, filas, retries, reconciliação, ferramentas ou detalhes técnicos rotineiros.

## 3. Objetivo

Construir e operar uma plataforma local-first capaz de:

1. receber uma missão;
2. verificar se o contrato permite aceitá-la;
3. persistir o compromisso;
4. compreender e decompor o trabalho;
5. escolher capacidades apropriadas;
6. executar de forma controlada;
7. testar e corrigir;
8. sobreviver a falhas recuperáveis;
9. produzir evidência verificável;
10. entregar o resultado;
11. concluir somente após prova.

## 4. Valor

- menos dependência de operação manual;
- continuidade entre sessões e falhas;
- verdade operacional;
- redução de retrabalho;
- independência de fornecedor;
- uso controlado de custo e recursos;
- capacidade de auditar por que uma missão concluiu ou não;
- reaproveitamento seguro de conhecimento entre projetos.

## 5. Escopo

O POD inclui conceitualmente:

- Mission Core;
- Brain;
- Construction Engineering;
- Governor;
- Scheduler;
- Memory;
- Proof Engine;
- Engine/Worker Runtime;
- Federation e Node Agent;
- Policy e Security;
- Immune System;
- Provider Capability Registry e Provider Adapters;
- Knowledge Library;
- Learning & Training;
- Product Testing e Product Security;
- Artifact e Delivery;
- Panel, Launcher, Terminal e APIs;
- Backup, Recovery e Self Update.

## 6. Fora do escopo conceitual imediato

Não são decisões desta versão:

- linguagem de programação;
- framework;
- banco físico;
- barramento físico;
- provedor de IA padrão;
- nuvem obrigatória;
- quantidade fixa de serviços;
- topologia final de processos;
- interface visual definitiva;
- marketplace de extensões;
- treino próprio de modelo na primeira entrega.

## 7. Princípios

### 7.1 Local-first

Missão aceita e persistida deve continuar sem depender da permanência do painel, ChatGPT ou canal externo. Dependência indispensável pode suspender o ramo, não apagar a missão.

### 7.2 Soberania por contrato

Soberania não é acesso irrestrito. Cada ação exige identidade, escopo, policy, capability e gate.

### 7.3 Autoridade separada

Quem planeja não executa diretamente. Quem executa não certifica sozinho. Quem avalia prova não altera estado. Quem mostra estado não o fabrica.

### 7.4 Progresso verificável

Atividade, log, heartbeat e consumo não representam progresso. Progresso deriva de requisito satisfeito, falha eliminada, dependência fechada, artefato promovido ou gate de prova avançado.

### 7.5 Simplicidade crescente

O domínio suporta multiprojeto, vários provedores e federação desde o início. A implantação começa com um nó e uma fatia vertical, adicionando distribuição apenas após prova.

### 7.6 Zero donor coupling

Projetos existentes são fontes de aprendizado, não dependências estruturais.

## 8. Componentes

### Mission Core

Controla a máquina de estados, aplica guardas e é o único escritor do estado soberano da missão.

### Brain

Compreende intenção, consulta conhecimento, formula estratégia, planeja e replaneja. Não possui acesso físico implícito nem poder de conclusão.

### Construction Engineering

Transforma estratégia em WorkUnits, alterações, testes, artefatos e planos de recuperação.

### Governor

Aplica prioridade, limites de CPU, RAM, disco, concorrência, tempo e custo autorizado.

### Scheduler

Escolhe quando e onde despachar WorkUnits já autorizadas. Não cria objetivo ou privilégio.

### Memory

Preserva estado transacional, eventos, outbox, checkpoints, evidências, artefatos, decisões, conhecimento e proveniência.

### Proof Engine

Avalia critérios e evidências por regras versionadas e produz ProofVerdict.

### Engine e Worker

Executam ações limitadas por envelope, capability, geração, timeout e política. Produzem fatos e candidatos.

### Security e Immune System

Security decide autorização. Immune System detecta, contém, quarentena e inicia recuperação dentro da policy.

### Federation

Mantém identidade de nós, compatibilidade, roteamento, lease, delegação e reconciliação.

### Provider Layer

Normaliza provedores, modelos, capacidades, custo, saúde, privacidade e portabilidade de contexto.

### Interfaces

Painel, Launcher, Terminal e APIs projetam verdade operacional e enviam comandos pelo ingress comum.

## 9. Fluxo principal

~~~text
OWNER
→ COMMAND INGRESS
→ ADMISSION
→ MISSION CORE
→ BRAIN
→ CONSTRUCTION ENGINEERING
→ POLICY / GOVERNOR
→ SCHEDULER
→ ENGINE
→ EVIDENCE
→ PROOF ENGINE
→ MISSION CORE
→ DELIVERY / MISSION_PROVEN
~~~

Memory sustenta todas as transições. Security pode negar ou conter. Panel observa e comanda sem contornar o fluxo.

## 10. Missão e WorkUnit

MISSION representa compromisso com um objetivo.

WORK_UNIT é a única unidade durável de trabalho. O termo Task pode aparecer na interface, mas não cria entidade separada.

Uma WorkUnit possui:

- entradas e saídas;
- dependências;
- critérios;
- effect_class;
- capability;
- timeout;
- retry_policy;
- generation;
- estado;
- evidências.

## 11. Multiprojeto

Uma instalação opera zero ou mais projetos.

Cada projeto tem:

- identidade;
- workspace;
- políticas;
- classificação;
- orçamento;
- segredos;
- conhecimento;
- artefatos;
- missões;
- retenção.

Compartilhamento exige regra explícita e proveniência. Não há herança silenciosa.

## 12. Cérebro híbrido e multi-provider

O Brain pode usar modelos locais e externos. A escolha ocorre por:

~~~text
POLICY ROUTER
→ CAPABILITY MATCH
→ PRIVACY
→ HEALTH
→ COST/LATENCY
→ PROVIDER ROUTER
~~~

O primeiro incremento pode utilizar um único adapter, desde que a porta seja neutra e o contexto permaneça sob controle do POD.

## 13. Conhecimento e aprendizagem

Conhecimento possui:

- origem;
- escopo;
- classificação;
- confiança;
- validade;
- versão;
- evidência;
- permissões de uso;
- elegibilidade de treino separada.

Aprendizado pode propor promoção. Não altera policy, arquitetura ou memória canônica silenciosamente.

## 14. Segurança do POD e do produto

São domínios relacionados, mas distintos:

- segurança do POD protege construtor, host, credenciais, políticas e execução;
- segurança do produto aplica requisitos ao artefato construído.

O POD não pode declarar produto seguro apenas porque sua própria infraestrutura está protegida.

## 15. Entrega

Entrega exige Artifact Manifest com:

- identidade e versão;
- conteúdo e hashes;
- proveniência;
- requisitos atendidos;
- testes;
- evidências;
- limitações;
- instruções operacionais;
- rollback quando aplicável.

## 16. Falha e recuperação

Falha recuperável preserva:

- missão;
- versão;
- WorkUnits;
- tentativas;
- evidências;
- idempotência;
- leases;
- checkpoints;
- outbox.

Reinício não cria nova missão e não reinicia a lógica desde zero.

## 17. Limites

O POD não pode:

- gastar sem envelope ou aprovação;
- contornar MFA, CAPTCHA, UAC ou policy;
- executar ação externa irreversível sem gate;
- enviar segredo a modelo sem autorização;
- usar last-write-wins para estado crítico;
- aceitar resultado de geração obsoleta;
- confundir disponibilidade do processo com saúde funcional;
- entrar em repetição infinita;
- fabricar MISSION_PROVEN.

## 18. Critérios de sucesso do projeto

O projeto POD estará funcional quando, em ambiente controlado:

1. aceitar missão válida e rejeitar missão inválida;
2. persistir toda mutação material atomicamente;
3. executar uma construção real;
4. sobreviver a reinício e queda do canal;
5. impedir duplicidade;
6. respeitar portões;
7. provar isolamento de projeto;
8. recuperar falha injetada;
9. produzir Evidence Pack;
10. promover artefato;
11. emitir ProofVerdict válido;
12. transicionar por Mission Core;
13. entregar resultado reproduzível;
14. atingir MISSION_PROVEN sem falha crítica aberta.

## 19. Posição

O conceito está aprovado. A implementação ainda não existe e deve seguir a matriz, os ADRs e o plano ativo do DOCSET V003.
