# POD — SEGURANÇA, AMEAÇAS E AUTORIZAÇÕES — V002

**Identificador:** POD-DOC-007
**Versão:** 2.0.0
**Status:** ACTIVE
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A1 — política técnica de segurança
**Substitui:** modelo de segurança e manifesto de autorizações do DOCSET V002
**Implementação comprovada:** NÃO

## 1. Objetivo

Permitir autonomia técnica sem transformar acesso local, identidade válida ou modelo de IA em autoridade irrestrita.

~~~text
AUTONOMY
+ IDENTITY
+ SCOPE
+ POLICY
+ CAPABILITY
+ HUMAN GATES
+ ISOLATION
+ AUDIT
+ RECOVERY
= CONTROLLED EXECUTION
~~~

## 2. Princípios

1. deny by default;
2. menor privilégio;
3. identidade não implica autoridade;
4. autorização é específica para ação e escopo;
5. segredo não entra em documento, log, evento, evidência ou prompt;
6. projeto é fronteira de isolamento;
7. efeito define o rigor do gate;
8. conteúdo externo não altera policy;
9. segurança pode bloquear, não fabricar sucesso;
10. toda negação material é auditável;
11. falha segura preserva estado;
12. proteção cresce junto com cada capacidade.

## 3. Ativos protegidos

- host e sistema operacional;
- identidade do POD, nós e atores;
- Constitution/Policy;
- missões e critérios;
- estado transacional e journal;
- segredos;
- código e artefatos;
- evidências e ProofVerdicts;
- conhecimento;
- orçamento e uso de provedores;
- canais e sessões;
- backups e pacotes de atualização;
- produtos construídos.

## 4. Ameaças principais

| ID | Ameaça | Controle obrigatório |
|---|---|---|
| THR-001 | prompt injection em conteúdo | isolamento de instrução, proveniência e policy fora do contexto |
| THR-002 | modelo tenta ampliar ferramenta | capability e allowlist por ação |
| THR-003 | vazamento de segredo | SecretRef, redaction e bloqueio de egress |
| THR-004 | Worker antigo grava resultado | generation e fencing no commit |
| THR-005 | comando duplicado | idempotência e inbox |
| THR-006 | projeto lê outro projeto | ownership_scope e testes negativos |
| THR-007 | nó falso ou revogado | enrollment, identidade e revogação |
| THR-008 | pacote adulterado | hash, assinatura quando disponível e provenance |
| THR-009 | painel contorna Core | Command API única e nenhuma escrita direta |
| THR-010 | falsa conclusão | Proof Engine separado e Mission Core |
| THR-011 | ação externa repetida após timeout | EffectIntent e reconciliação |
| THR-012 | gasto não autorizado | budget envelope e gate financeiro |
| THR-013 | publicação/produção sem consentimento | gate soberano do Owner |
| THR-014 | operação offline excessiva | TTL finito e effect classes |
| THR-015 | evento contém segredo | schema/redaction gate |
| THR-016 | update compromete missões | pacote verificado, side-by-side e rollback |
| THR-017 | conhecimento envenenado | confiança, validade e promoção |
| THR-018 | supply chain comprometida | lock, SBOM, verificação e scanner |

## 5. Identidades

Tipos:

~~~text
OWNER
HUMAN_OPERATOR
POD_SERVICE
NODE
WORKER
PROVIDER_ADAPTER
EXTERNAL_CLIENT
~~~

Identidade registra:

- actor_id;
- tipo;
- emissor;
- credencial ou identity_ref;
- status;
- validade;
- projetos permitidos;
- capabilities;
- última rotação ou verificação.

Processo local também precisa de identidade lógica.

## 6. Autenticação

Cada fronteira autenticável deve:

- validar origem;
- rejeitar credencial expirada ou revogada;
- impedir replay quando aplicável;
- proteger canal conforme risco;
- registrar somente referência segura;
- falhar fechada.

O mecanismo físico será definido pela stack. O contrato não permite autenticação por confiança implícita em localhost.

## 7. Autorização

Decisão mínima:

~~~text
actor
action
target
ownership_scope
mission_id
policy_version
capability
execution_effect
environment
approval_ref optional
decision
reason_code
~~~

Decisões: ALLOW, DENY, REQUIRE_FINANCIAL_APPROVAL, REQUIRE_OWNER_APPROVAL, WAIT_EXTERNAL.

## 8. Capabilities

Capability é específica, finita e não transferível por padrão.

Campos:

- capability_id;
- actor_id;
- actions;
- resources;
- ownership_scope;
- effect_classes;
- not_before;
- expires_at;
- delegation_allowed;
- max_delegation_depth;
- constraints;
- issuer;
- status.

Wildcard global é proibido em produção sem exceção documentada e temporária.

## 9. Portões humanos

### Financeiro

Protege gasto ou obrigação nova. Approval deve declarar limite, moeda, alvo, ação, validade e payload_hash.

### Owner soberano

Protege produção, exposição pública, ação externa irreversível, destruição, elevação material, alteração de objetivo, decisão jurídica/comercial e aceitação de risco alto.

### Participação externa

Credencial, MFA, CAPTCHA, ação física ou serviço indispensável não são aprovação técnica. O POD aguarda em WAITING_EXTERNAL e não tenta contornar.

## 10. Elevação administrativa

Elevação:

- é ação separada;
- exige motivo e escopo;
- usa executor privilegiado isolado quando a stack exigir;
- não concede shell administrativo geral ao Brain;
- possui timeout;
- registra comando normalizado e resultado;
- nunca contorna UAC;
- é negada para payload não validado.

## 11. Segredos

Regra:

~~~text
SECRET VALUE
→ VAULT
→ SHORT-LIVED ACCESS
→ AUTHORIZED CONSUMER
→ MEMORY CLEAR WHEN POSSIBLE
~~~

Documentos, eventos e prompts usam SecretRef.

É proibido:

- segredo em Git;
- segredo em argumento de processo quando evitável;
- segredo em log;
- segredo em Evidence Pack;
- segredo em dataset;
- segredo em Read Model;
- envio automático a provedor.

## 12. IA e conteúdo não confiável

Todo texto de arquivo, site, issue, log ou modelo é dado, não policy.

Brain:

- não executa instrução encontrada em conteúdo sem validar intenção;
- não recebe ferramenta além da capability;
- não amplia próprio orçamento;
- não lê todos os segredos;
- não certifica próprio resultado;
- registra provider/model e hashes;
- aplica classificação antes de egress.

## 13. Isolamento multiprojeto

Default:

- segredo: PROJECT;
- workspace: PROJECT;
- missão: PROJECT;
- evidência: PROJECT;
- artefato: PROJECT;
- custo: PROJECT;
- conhecimento: PROJECT salvo promoção explícita.

Toda consulta possui project_id derivado da identidade ou do contexto autorizado. project_id somente informado pelo cliente não é suficiente.

## 14. Federação

Nó entra por:

~~~text
DISCOVER
→ ENROLL
→ IDENTITY PROOF
→ VERSION NEGOTIATION
→ CAPABILITY ATTESTATION
→ POLICY ASSIGNMENT
→ READY
~~~

Revogação impede novos leases. Commit ainda valida fencing. Nó quarentenado pode enviar evidência de diagnóstico por canal limitado.

## 15. Segurança do produto construído

O Product Security Contract deriva da missão e pode exigir:

- threat model;
- autenticação;
- autorização;
- validação;
- proteção de segredos;
- dependências;
- SAST/DAST conforme aplicável;
- SBOM;
- licenças;
- hardening;
- backup;
- teste de recuperação;
- segurança de entrega.

NOT_APPLICABLE exige justificativa. Segurança do POD não substitui esses gates.

## 16. Supply chain

Antes de promover artefato:

- dependências identificadas e fixadas;
- origem verificada;
- licença registrada;
- hashes preservados;
- scanner executado conforme risco;
- resultado ligado ao Artifact Manifest;
- vulnerabilidade crítica incompatível bloqueia promoção.

## 17. Auditoria

AuditRecord material pertence à mesma transação da ação.

Contém:

- actor;
- action;
- target;
- decision;
- reason_code;
- policy_version;
- approval_ref;
- correlation_id;
- timestamp;
- outcome_ref;
- redaction_status.

Log não substitui AuditRecord.

## 18. Sistema Imunológico

Pode:

- detectar;
- conter;
- bloquear capability;
- quarentenar nó, Worker ou artefato;
- iniciar recuperação;
- abrir incidente;
- recomendar revogação.

Não pode:

- alterar objetivo;
- alterar Policy;
- aprovar gasto;
- fabricar evidência;
- declarar MISSION_PROVEN;
- apagar histórico.

## 19. Incidentes

Fluxo:

~~~text
DETECT
→ CONTAIN
→ PRESERVE
→ CLASSIFY
→ DIAGNOSE
→ RECOVER
→ VERIFY
→ PREVENT RECURRENCE
→ CLOSE
~~~

Incidente crítico pode pausar apenas o escopo afetado ou o sistema quando a integridade global estiver em risco.

## 20. Backup e recuperação

- backup criptografado quando contém dado protegido;
- acesso separado;
- restore testado;
- retenção definida;
- chave não armazenada junto do backup;
- recuperação não reduz generation/fencing;
- evidência de restore vinculada ao release.

## 21. Atualização

Update exige:

- provenance;
- hash;
- assinatura quando suportada;
- compatibilidade;
- backup;
- health gate;
- rollout controlado;
- rollback;
- preservação de missão;
- audit record.

## 22. Segurança por fase

| Fase | Gate mínimo |
|---|---|
| F0 | tipos Identity/Scope/Capability/Effect, redaction, SecretRef, threat baseline |
| F1 | audit atômico, isolamento de store, idempotência, fencing |
| F2 | Policy evaluator e portões |
| F3 | auth de UI/API e proibição de escrita direta |
| F4 | sandbox, allowlist, timeout e effect intent |
| F5 | segurança de alteração e testes |
| F6 | quotas e proteção contra starvation/abuso |
| F7 | privacy/cost/egress para IA |
| F8 | enrollment, revogação e protocolo federado |
| F9 | hardening por sistema operacional |
| F10 | Immune System e incidentes avançados |
| F11 | poisoning e Training Eligibility |
| F12 | Product Security |
| F13 | update, backup e DR |
| F14–F15 | ataque, falha e aceite sistêmico |

## 23. Exceções

Exceção de segurança contém:

- ID;
- requisito;
- escopo;
- motivo;
- risco;
- compensação;
- Owner quando necessário;
- responsável técnico;
- expiração;
- teste;
- evidência.

Exceção vencida é DENY.

## 24. Critérios de aceite

- testes negativos de autorização passam;
- project isolation passa;
- segredo não aparece em scan de repo/log/event/evidence;
- stale generation falha;
- approval não pode ser reutilizado fora do payload;
- ação externa irreversível sem gate falha;
- prompt injection não altera policy;
- nó revogado não recebe lease;
- pacote adulterado falha;
- restore preserva integridade;
- nenhuma vulnerabilidade crítica aberta é compatível com release.
