# POD — DNA OPERACIONAL SOBERANO — V002

**Identificador:** POD-DOC-003
**Versão:** 2.0.0
**Status:** ACTIVE
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A1 — invariantes raiz
**Substitui:** POD_DNA_OPERACIONAL_V001

## 1. Definição raiz

POD é o construtor soberano.

~~~text
MISSION_GIVEN
→ ADMISSION
→ MISSION_ACCEPTED
→ WORK
→ PROOF
→ MISSION_PROVEN
~~~

Aceitar uma missão cria compromisso durável. Não cria permissão ilimitada, orçamento ilimitado ou direito de ultrapassar política.

## 2. Autonomia

Autonomia é nativa, mas sempre limitada por:

- objetivo e restrições da missão;
- Constitution/Policy;
- capability;
- escopo;
- orçamento autorizado;
- portões humanos;
- segurança;
- recursos físicos;
- lei e licença.

Governor controla recursos e prioridade. Ele não concede autonomia, não altera objetivo e não certifica conclusão.

## 3. Persistência e constância

~~~text
FAIL            != STOP
ERROR           != STOP
TEST_FAILED     != STOP
WORKER_FAILED   != STOP
SERVICE_FAILED  != STOP
~~~

Uma falha recuperável segue:

~~~text
DETECT
→ CONTAIN
→ PRESERVE
→ DIAGNOSE
→ REPLAN_OR_RECOVER
→ TEST
→ RECONCILE
→ RESUME
~~~

Repetição cega é proibida. Cada ciclo deve produzir nova evidência, estratégia, correção ou critério satisfeito.

## 4. Convergência obrigatória

Toda missão aceita define limites contra loop improdutivo:

- tentativas iguais limitadas;
- estagnação detectável;
- replanejamento governado;
- consumo observado;
- deadline_policy explícita;
- impossibility_proof_policy explícita.

Esgotamento de uma estratégia não encerra a missão. Esgotamento comprovado de todos os caminhos autorizados pode produzir IMPOSSIBLE_PROVEN.

## 5. Autoridades não concorrentes

~~~text
BRAIN          = planeja e replaneja
GOVERNOR       = limita recursos e prioridade
SCHEDULER      = despacha trabalho autorizado
ENGINE         = executa e produz fatos
PROOF_ENGINE   = avalia evidências e emite verdict
MISSION_CORE   = altera o estado soberano da missão
SECURITY       = nega, contém e quarentena
MEMORY         = preserva estado, história e evidência
~~~

Nenhum componente acumula silenciosamente duas autoridades incompatíveis.

## 6. Conclusão

Proof Engine não declara estado. Ele emite ProofVerdict vinculado a:

- mission_id;
- mission_version;
- acceptance_criteria_version;
- policy_version;
- evidence_manifest_hash;
- gate_results;
- verdict;
- reason_codes;
- created_at.

Mission Core realiza MISSION_PROVEN somente quando o verdict é PASSED, atual, íntegro e todos os guardas da transição estão satisfeitos.

## 7. Portões humanos

Existem três classes distintas:

1. **WAITING_FINANCIAL_AUTHORIZATION** — novo gasto ou obrigação financeira;
2. **WAITING_OWNER_APPROVAL** — produção, exposição pública, efeito externo irreversível, mudança destrutiva, elevação de privilégio ou decisão jurídica/comercial;
3. **WAITING_EXTERNAL** — credencial, MFA, CAPTCHA, ação física, hardware, conexão ou serviço indispensável indisponível.

Esses estados suspendem somente o ramo dependente. O POD preserva contexto, continua trabalho independente e retoma quando o guardião competente liberar a condição.

## 8. Segurança

Segurança não é fase opcional nem poder absoluto.

~~~text
IDENTITY
→ SCOPE
→ POLICY
→ CAPABILITY
→ GATE
→ EXECUTION
→ AUDIT
~~~

Segurança pode impedir ação. Não pode redefinir o objetivo, fabricar prova ou mudar Policy por conta própria.

## 9. Multiprojeto

Uma instalação pode operar vários projetos. Isolamento é obrigatório em estado, segredo, artefato, custo, conhecimento e execução.

PROJECT é fronteira de propriedade. MISSION é fronteira de compromisso. NODE é local de execução. Nenhum desses conceitos se substitui.

## 10. Federação

Federação distribui capacidade. Não distribui soberania sem delegação explícita.

Operação offline:

- exige capability pré-emitida;
- possui validade finita;
- não renova a própria autoridade;
- não executa efeito externo irreversível;
- preserva resultados compartilhados como candidatos até reconciliação;
- não permite commit com generation obsoleta.

## 11. IA e fornecedores

Modelo de IA é recurso cognitivo substituível.

~~~text
PROVIDER != BRAIN
MODEL_OUTPUT != POLICY
MODEL_OUTPUT != AUTHORIZATION
MODEL_OUTPUT != PROOF
~~~

O POD possui contexto, memória, políticas, roteamento e prova.

## 12. Regra soberana resumida

> Missão aceita é compromisso durável de buscar resultado comprovado dentro das restrições autorizadas. Falha técnica recuperável exige diagnóstico, correção e continuidade. O Brain planeja, o Engine executa, o Proof Engine avalia, e somente o Mission Core altera a missão. Política, segurança e portões humanos limitam a ação; nenhum deles fabrica conclusão. O sistema impede repetição cega, preserva estado e termina positivamente somente em MISSION_PROVEN.
