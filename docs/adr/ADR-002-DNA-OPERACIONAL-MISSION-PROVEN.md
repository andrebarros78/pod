# ADR-002 — DNA OPERACIONAL, AUTONOMIA RAIZ E COMPROMISSO MISSION_PROVEN

**Status:** ACCEPTED
**Data:** 2026-09-02
**Decisão:** ativa e vinculante para nova implementação
**Documento normativo associado:** `docs/architecture/POD_DNA_OPERACIONAL_V001.md`

---

## Contexto

A arquitetura anterior concentrava parte relevante da autonomia, autoridade técnica, elevação administrativa, acesso a ferramentas e continuidade operacional dentro do conceito de Governor.

Essa organização cria um problema de identidade e de limites de módulo: o POD passa a parecer um sistema que recebe permissão de seu Governador para trabalhar, quando sua finalidade essencial é ser o próprio construtor responsável pela missão.

Também havia excesso de situações tratadas como portões humanos, inclusive dificuldades técnicas que devem ser resolvidas pela própria Engenharia de Construção e pelo Loop Engineering.

---

## Decisão

Fica decidido que autonomia, autoridade técnica, conhecimento técnico, autoridade de execução, autorização administrativa estrutural, persistência, constância e compromisso de conclusão pertencem ao DNA do POD e não ao Governor.

A regra soberana passa a ser:

`MISSION_GIVEN → MISSION_ACCEPTED → WORK → PROOF → MISSION_PROVEN`

Uma missão aceita deve continuar sendo trabalhada até MISSION_PROVEN enquanto existir caminho técnico autorizado e recurso disponível.

Falhas técnicas são trabalho do POD e não constituem portão humano.

O Governor passa a ter responsabilidade de controle operacional: recursos, prioridades, concorrência, fairness, Scheduler, Workers, leases, fencing, retries, backoff, circuit breakers, health, reconciliação, recovery e incidentes.

---

## Barreira humana soberana

Gasto financeiro novo não previamente autorizado exige aprovação humana.

Antes de abrir esse portão, o POD deve procurar alternativa gratuita ou já autorizada tecnicamente adequada, quando existir.

O bloqueio financeiro afeta apenas o ramo dependente.

---

## Dependências externas

Condições que não representam decisão técnica — como falta física de energia, hardware indisponível, MFA/CAPTCHA, credencial indispensável inexistente, serviço externo obrigatório indisponível ou conexão externa indispensável sem alternativa — são classificadas como dependências externas.

Elas devem colocar somente o ramo afetado em `WAITING_EXTERNAL`, preservando estado e permitindo continuidade dos demais ramos.

`WAITING_EXTERNAL != FAILED`

A simples queda de ChatGPT, MCP, Action ou painel não interrompe uma missão local já aceita e persistida.

---

## Elevação administrativa

O POD possui autorização administrativa estrutural para realizar operações necessárias à missão dentro das políticas soberanas.

O Core não deve permanecer permanentemente elevado. A elevação é materializada pelo POD Privileged Executor, por porta autenticada e auditável, apenas quando necessária.

A autonomia do POD não autoriza desabilitar, burlar ou contornar proteções obrigatórias do sistema operacional, políticas soberanas, controles de segurança, licenças ou limites legais.

---

## Consequências

1. O domínio raiz deve representar compromisso de missão e autoridade técnica fora de `pod.governor`.
2. O Governor deve ser reduzido a governança operacional e de recursos.
3. Barreiras técnicas devem entrar no Loop Engineering automaticamente.
4. Estados de falha de tentativa, Worker, ferramenta ou estratégia não encerram a missão.
5. MISSION_PROVEN é a conclusão positiva soberana.
6. Gasto novo não autorizado é o principal portão humano de decisão.
7. Dependências externas suspendem apenas o ramo afetado e não são classificadas como falha técnica terminal.
8. Terminal, leitura, escrita, execução e operações administrativas devem ser modelados como capacidades nativas do POD, mediadas por contratos e componentes seguros.
9. A Biblioteca de Conhecimento e mecanismos de aquisição/validação de conhecimento passam a sustentar diretamente a autonomia de construção.
10. Documentos anteriores que atribuam ao Governor a origem da autonomia ou que tratem barreira técnica resolvível como necessidade de aprovação devem ser interpretados como superseded neste ponto específico.

---

## Precedência

Este ADR não apaga documentos históricos.

Ele substitui, apenas onde houver conflito, regras anteriores sobre:

- origem da autonomia;
- origem da autoridade técnica;
- papel do Governor;
- classificação de barreiras técnicas;
- classificação de dependências externas;
- critério de continuidade da missão.

Os demais requisitos de segurança, persistência, evidência, rastreabilidade, isolamento e ZERO DONOR COUPLING permanecem vigentes.

---

## Critério de implementação

A decisão somente será considerada implementada quando testes provarem, no mínimo:

1. erro técnico recuperável não leva a encerramento da missão;
2. falha de Worker gera recuperação/replanejamento e não abandono;
3. falha de teste gera correção/reteste;
4. ausência de ferramenta provoca descoberta/alternativa/instalação autorizada antes de pedir intervenção;
5. operação administrativa autorizada é executada via Privileged Executor sem elevar permanentemente o Core;
6. queda de canal externo não interrompe trabalho local persistido;
7. WAITING_EXTERNAL bloqueia apenas dependências reais e retoma após reconciliação;
8. gasto novo não autorizado bloqueia somente o ramo financeiro;
9. Governor pode ser testado separadamente de autonomia e decisão técnica;
10. MISSION_PROVEN somente ocorre com prova objetiva.
