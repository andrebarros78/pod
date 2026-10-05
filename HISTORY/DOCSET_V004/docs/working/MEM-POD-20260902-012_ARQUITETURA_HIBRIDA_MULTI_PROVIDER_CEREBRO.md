# MEM-POD-20260902-012 — ARQUITETURA HÍBRIDA E MULTI-PROVIDER DO CÉREBRO POD

**DATA:** 02/09/2026  
**TIPO:** ARCHITECTURAL_INSIGHT / CAPABILITY / RULE_CANDIDATE  
**STATUS:** CANDIDATE  
**NORMATIVO:** NÃO

## TEXTO ORIGINAL

> arquitetura Vai ser hibrida, com compatibilidade com todos os provedores de IA A Api fica no cerebro do sistema.

Decisão posterior do proprietário:

> Provado: oito pontos para essa arquitetura híbrida, POD será híbrido e multi-provider por definição

## DECISÃO CONCEITUAL

O POD será concebido como arquitetura híbrida e multi-provider por definição. Provedores e modelos de IA são recursos cognitivos substituíveis consumidos pelo Cérebro; nenhum provedor ou modelo é o Cérebro do POD e nenhum deles adquire autoridade soberana.

```text
POD = HÍBRIDO + MULTI-PROVIDER

PROVIDER != POD BRAIN
MODEL != OPERATIONAL AUTHORITY
```

A propriedade lógica da integração com provedores de IA pertence ao Cérebro por meio de uma API/camada neutra de capacidades cognitivas.

```text
AI_PROVIDER_API_OWNER = POD_BRAIN
PROVIDER_LOCK_IN = FALSE
MODEL_AGNOSTIC = TRUE
CONTEXT_OWNED_BY_POD = TRUE
```

Credenciais não pertencem ao Cérebro: são resolvidas por referência segura via Vault/Secret Broker no momento de uso.

## POSIÇÃO CONCEITUAL

```text
POD BRAIN
├── Cognitive Orchestrator
├── Context Engine
├── Knowledge Retrieval
├── Policy Gate
├── AI Capability Router
├── Provider Capability Registry
├── Provider-neutral API
├── Provider Adapters
├── Quality Evaluator
├── Cost / Latency Router
├── Cognitive Evidence
└── Cognitive Degradation / Failover
```

O restante do POD solicita capacidade cognitiva ao Cérebro e não integra diretamente SDKs/protocolos específicos de fornecedores como dependência arquitetural.

## OITO PONTOS APROVADOS

### 1. Provider Capability Registry

Cada provedor/modelo deve possuir perfil observável de capacidades e limitações, por exemplo:

```text
provider
model
model/version quando disponível
reasoning
code
vision
tool use
structured output
embeddings/reranking quando aplicável
context limits
latency
cost
rate limits
data/privacy policy
availability
known quality profile
```

O roteamento ocorre por capacidade e requisitos, não por nome comercial.

### 2. Normalização de contratos

Respostas e requisições específicas de fornecedor devem ser convertidas por adapters para contratos cognitivos internos POD.

```text
PROVIDER-SPECIFIC REQUEST/RESPONSE
→ ADAPTER/NORMALIZER
→ POD COGNITIVE CONTRACT
```

Trocar provedor não pode exigir reescrever domínio, missão, Memória, Engenharia de Construção ou Engines.

### 3. Context Portability

Contexto pertence ao POD. Cada provedor recebe somente uma projeção necessária e autorizada do contexto soberano.

```text
CONTEXT_OWNED_BY_POD = TRUE
PROVIDER_CONTEXT = AUTHORIZED_PROJECTION
```

A troca de modelo/provedor deve preservar missão, decisões, checkpoints, conhecimento, evidências e histórico pertencentes ao POD.

### 4. Policy Router antes do Provider Router

Antes de otimizar qualidade, latência ou custo, o Cérebro deve verificar se o dado/ação pode ser enviado ao provedor.

Ordem conceitual:

```text
POLICY / DATA CLASSIFICATION / AUTHORITY
→ REQUIRED CAPABILITY
→ QUALITY
→ PRIVACY
→ LATENCY
→ COST
→ HEALTH
→ PROVIDER/MODEL
```

Dados sensíveis, segredos e materiais restritos não podem ser enviados a provedor incompatível com a política aplicável.

### 5. Health funcional de modelos e provedores

HTTP disponível não equivale a capacidade funcional adequada.

Dimensões candidatas:

```text
AVAILABLE
AUTH_VALID
RATE_LIMIT_OK
LATENCY_OK
CAPABILITY_OK
TOOL_USE_OK
STRUCTURED_OUTPUT_OK
QUALITY_OK
```

Falha de provider não é falha da missão:

```text
PROVIDER_FAILED != MISSION_FAILED
```

### 6. Versionamento e regressão de modelos

Mudanças materiais de modelo, versão, contrato, template ou comportamento devem ser rastreáveis. Competências/fluxos críticos podem exigir regressão antes de aceitar o novo comportamento como equivalente.

```text
MODEL_CHANGE_REQUIRES_REGRESSION_WHEN_CRITICAL = TRUE
```

### 7. Shadow / Challenger Evaluation

Decisões de maior risco podem usar um segundo modelo/provedor como challenger ou revisor independente quando o benefício justificar custo e latência.

Isso não é votação por maioria. A decisão permanece do Cérebro e deve considerar evidência objetiva, testes e critérios da missão.

### 8. Degradação cognitiva controlada

Indisponibilidade de IA externa não deve produzir parada global quando existirem caminhos locais ou determinísticos seguros.

```text
EXTERNAL_AI_OFFLINE
→ usar conhecimento POD comprovado quando suficiente
→ usar lógica determinística
→ usar modelo local compatível quando disponível
→ continuar testes/recovery/ramos independentes
→ aguardar somente o que realmente depender de IA externa
```

```text
PROVIDER_FAILURE_IS_NOT_MISSION_FAILURE = TRUE
```

## ARBITRAGEM COGNITIVA

Quando múltiplos modelos/recursos apresentam respostas divergentes, o Cérebro não decide por maioria cega.

Fluxo conceitual:

```text
PROPOSTAS
→ verificar requisitos e proveniência
→ comparar evidências
→ avaliar desempenho histórico relevante
→ executar experimento/teste quando possível
→ eliminar opções incompatíveis
→ decidir tecnicamente
→ preservar justificativa/evidência material
```

Para decisões materiais:

```text
COGNITIVE_RESULT_REQUIRES_VALIDATION_WHEN_MATERIAL = TRUE
```

Evidência determinística ou teste real prevalece sobre consenso textual de modelos quando houver conflito.

## INTEGRAÇÃO COM LEARNING & TRAINING

Aprendizado e competência pertencem ao POD, não ao modelo usado durante aquisição, síntese ou avaliação.

```text
TROCAR MODELO != PERDER APRENDIZADO
```

A Learning & Training Tool pode consumir provedores pelo Cérebro e adapters oficiais, mantendo currículo, conhecimento, trajetórias, evidências e competence proof na Memória POD.

## SEGURANÇA E SEGREDOS

```text
CÉREBRO → solicita capacidade/provider
VAULT/SECRET BROKER → resolve SecretRef autorizado
RUNTIME → injeta somente no escopo necessário
```

É proibido transformar chave de API em estado cognitivo, conhecimento, log ou evidência comum.

## INVARIANTES CONSOLIDADOS

```text
PROVIDER_LOCK_IN = FALSE
MODEL_AGNOSTIC = TRUE
AI_PROVIDER_API_OWNER = POD_BRAIN
CONTEXT_OWNED_BY_POD = TRUE
PROVIDER_IS_REPLACEABLE = TRUE
MODEL_IS_NOT_AUTHORITY = TRUE
PROVIDER_FAILURE_IS_NOT_MISSION_FAILURE = TRUE
SENSITIVE_DATA_ROUTING_IS_POLICY_GOVERNED = TRUE
MODEL_CHANGE_REQUIRES_REGRESSION_WHEN_CRITICAL = TRUE
COGNITIVE_RESULT_REQUIRES_VALIDATION_WHEN_MATERIAL = TRUE
```

## MOTIVAÇÃO

Permitir que o POD use recursos cognitivos externos e locais de forma soberana, resiliente, econômica e substituível, sem criar lock-in e sem delegar a um modelo externo a identidade ou autoridade do Cérebro POD.

## RELAÇÕES COM OUTRAS MEMÓRIAS

Relaciona-se com MEM-005 (14 requisitos), MEM-007 (Segurança do Produto), MEM-009 (Learning & Training), MEM-010 (economia de execução) e com a auditoria conceitual registrada posteriormente.

## DECISÃO FINAL

**APROVADO PELO PROPRIETÁRIO: POD SERÁ HÍBRIDO E MULTI-PROVIDER POR DEFINIÇÃO; A INTEGRAÇÃO/API DE IA PERTENCE AO CÉREBRO E OS OITO MECANISMOS ACIMA SÃO PARTE DA DIREÇÃO CONCEITUAL.**

Aprovação conceitual não equivale a implementação, teste, prova ou baseline.

## INCORPORADO EM

Registro de trabalho para consolidação arquitetural posterior.