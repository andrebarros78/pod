# MEM-POD-20260902-007 — SEGURANÇA_DO_PRODUTO

**DATA:** 02/09/2026  
**TIPO:** CAPABILITY / RULE_CANDIDATE / ARCHITECTURAL_INSIGHT  
**STATUS:** CAPTURED  
**NORMATIVO:** NÃO

## TEXTO ORIGINAL

> Agora vamos tratar SEGURANCA_DO_PRODUTO do produto construido por POD

Decisão associada: `SEGURANÇA_DO_PRODUTO` deve ser tratada como capacidade nativa da Engenharia de Construção do POD, distinta da segurança que protege o próprio POD.

## INTERPRETAÇÃO TÉCNICA

A segurança do produto construído pelo POD deve fazer parte do ciclo de engenharia desde a compreensão do objetivo até o aceite final. O POD não deve apenas executar scanners ou adicionar controles ao final; deve identificar riscos, modelar ameaças, projetar arquitetura segura, implementar controles, testar funcionalmente e adversarialmente, corrigir vulnerabilidades, executar regressão e preservar evidências.

Regra central:

```text
PRODUTO FUNCIONANDO
!=
PRODUTO SEGURO

PRODUTO SEGURO
=
REQUISITOS DE SEGURANÇA
+ ARQUITETURA SEGURA
+ IMPLEMENTAÇÃO SEGURA
+ TESTES
+ TESTES ADVERSARIAIS
+ CORREÇÃO
+ REGRESSÃO
+ EVIDÊNCIAS
```

## ESCOPO CANDIDATO DA CAPACIDADE

### 1. Classificação de risco do produto

O POD deverá avaliar, conforme aplicável:

- tipo de produto;
- exposição à Internet;
- usuários e papéis;
- autenticação e autorização;
- dados tratados;
- segredos;
- integrações externas;
- APIs;
- bancos;
- infraestrutura;
- pagamentos;
- dados pessoais ou sensíveis;
- ações privilegiadas;
- impacto de comprometimento.

### 2. Threat Modeling

Fluxo candidato:

```text
OBJETIVO
→ ARQUITETURA DO PRODUTO
→ ATIVOS
→ FRONTEIRAS DE CONFIANÇA
→ AMEAÇAS
→ CONTROLES
→ TESTES
```

### 3. Security by Design

Princípios candidatos:

- menor privilégio;
- negação por padrão;
- separação de funções;
- isolamento;
- validação de entrada;
- proteção de saída;
- gestão de segredos;
- limites explícitos de confiança;
- criptografia quando aplicável;
- integridade;
- auditoria;
- recuperação;
- redução da superfície de ataque.

### 4. Secure Coding

A Engenharia de Construção do POD deverá conhecer e aplicar padrões seguros de acordo com linguagem, framework e tipo de produto, incluindo prevenção e correção, quando aplicável, de:

- SQL Injection;
- Command Injection;
- Path Traversal;
- XSS;
- CSRF;
- SSRF;
- XXE;
- deserialização insegura;
- controle de acesso quebrado;
- validação insuficiente;
- uso inseguro de criptografia;
- segredos hardcoded;
- permissões excessivas;
- race conditions / TOCTOU;
- execução arbitrária;
- mass assignment;
- upload inseguro de arquivos.

### 5. Identidade, autenticação e autorização

Regra:

```text
IDENTIDADE != AUTORIZAÇÃO
```

O POD deverá projetar e testar, conforme necessário:

- autenticação;
- sessões;
- expiração;
- revogação;
- papéis;
- permissões;
- escopos;
- proteção contra brute force;
- recuperação de conta;
- MFA quando proporcional ao risco;
- testes negativos de autorização.

### 6. Segurança de dados

Classificação candidata:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
SECRET
RESTRICTED
```

A classificação deve orientar armazenamento, acesso, criptografia, logs, backup, egress, retenção e descarte.

### 7. Segredos

O produto não deverá depender de segredos incorporados em código, Git, frontend, imagem, logs ou artefatos públicos.

Modelo candidato:

```text
SecretRef
→ Secret Store
→ injeção em runtime
→ uso mínimo
→ rotação / revogação
```

### 8. Supply Chain Security

A segurança do produto deverá abranger:

- lockfiles;
- versões controladas;
- análise de dependências diretas e transitivas;
- vulnerabilidades conhecidas;
- SBOM quando aplicável;
- proveniência;
- hashes/assinaturas quando aplicável;
- build reproduzível quando possível;
- controle de introdução de novas dependências.

Regra candidata:

```text
DEPENDÊNCIA NOVA
→ ANALISAR
→ ACEITAR
→ FIXAR
→ MONITORAR
```

### 9. API Security

Quando houver APIs, testar, conforme aplicável:

- autenticação;
- autorização por objeto;
- autorização por função;
- rate limiting;
- schema validation;
- payload limits;
- mass assignment;
- injection;
- replay;
- CORS;
- tratamento de erros;
- exposição excessiva de dados;
- abuso de recursos.

### 10. Segurança de produtos com IA

Regra candidata:

```text
PROMPT != AUTORIDADE
```

Ameaças a considerar:

- prompt injection;
- indirect prompt injection;
- data poisoning;
- tool abuse;
- exfiltração;
- RAG poisoning;
- segredos em contexto;
- execução induzida;
- cross-user data leakage;
- memory poisoning;
- output inseguro.

Separação candidata:

```text
LLM → PROPÕE
POLICY → VALIDA
EXECUTOR → EXECUTA
```

### 11. Segurança de infraestrutura

Avaliar, conforme aplicável:

- portas;
- firewall;
- TLS;
- DNS;
- containers;
- serviços;
- usuários;
- ACL;
- filesystem;
- processos;
- cloud;
- bancos;
- backups;
- rede.

### 12. Segurança de banco de dados

Provar, conforme aplicável:

- menor privilégio;
- queries parametrizadas;
- controle de acesso;
- migrações seguras;
- backup e restore;
- integridade;
- proteção de dados sensíveis;
- isolamento entre ambientes.

### 13. Logging seguro

```text
LOG DEVE CONTER
→ evento
→ contexto
→ IDs
→ erro
→ autoria
→ timestamp

LOG NÃO DEVE CONTER
→ senha
→ token
→ chave
→ segredo
→ dado sensível desnecessário
```

### 14. Testes adversariais

O POD deverá perguntar não apenas `FUNCIONA?`, mas também:

```text
COMO POSSO QUEBRAR?
COMO POSSO BURLAR?
COMO POSSO ESCALAR?
COMO POSSO VAZAR?
COMO POSSO DUPLICAR?
COMO POSSO FORÇAR ESTADO INVÁLIDO?
```

Fluxo candidato:

```text
IMPLEMENTAR
→ TESTAR FUNCIONALMENTE
→ ATACAR A PRÓPRIA IMPLEMENTAÇÃO
→ ENCONTRAR FRAQUEZA
→ CORRIGIR
→ RETESTAR
→ REGRESSÃO
```

### 15. Security Regression / Impact Analysis

Mudanças relevantes devem acionar análise de superfície afetada e seleção de testes de segurança correspondentes.

### 16. Perfis de segurança por risco

Perfis candidatos, ainda não normativos:

```text
PROD-SEC-1 — STANDARD
PROD-SEC-2 — SENSITIVE
PROD-SEC-3 — CRITICAL
PROD-SEC-4 — HIGH-IMPACT / SOVEREIGN
```

Quanto maior o risco, maior a profundidade de controles, isolamento, testes adversariais e evidência.

### 17. Security Gates do produto

Criar futuramente família própria, separada dos gates de segurança do POD:

```text
PROD-SEC-GATE-xxx
```

Exemplos candidatos:

- Threat Model válido;
- segredos protegidos;
- autenticação comprovada;
- autorização negativa comprovada;
- testes de injection aprovados;
- dependências auditadas;
- SBOM gerada quando aplicável;
- logs sanitizados;
- backup/restore provado quando aplicável;
- nenhum achado crítico aberto após teste adversarial.

### 18. Integração com a conclusão da missão

Para produtos em que segurança for aplicável:

```text
FUNCTIONAL_PROVEN
+ QUALITY_PROVEN
+ SECURITY_PROVEN
+ RECOVERY_PROVEN
+ EVIDENCE_PROVEN
=
PRODUCT_MISSION_PROVEN
```

Regra candidata:

```text
CRITICAL_SECURITY_FAILURE > 0
→ MISSION_PROVEN BLOQUEADO
```

## CAPACIDADE CANDIDATA DA ENGENHARIA DE CONSTRUÇÃO

```text
POD CONSTRUCTION ENGINEERING
└── PRODUCT SECURITY ENGINEERING
    ├── Risk Classification
    ├── Threat Modeling
    ├── Secure Architecture
    ├── Secure Coding
    ├── Dependency Security
    ├── Data Security
    ├── Identity & Access
    ├── API Security
    ├── AI Security
    ├── Infrastructure Security
    ├── Adversarial Testing
    ├── Security Regression
    └── Security Evidence
```

Essa capacidade não implica necessariamente um processo ou serviço separado; pode ser uma propriedade e competência nativa da Engenharia de Construção.

## DISTINÇÃO SOBERANA

```text
SEGURANÇA_DO_POD
→ protege o construtor

SEGURANÇA_DO_PRODUTO
→ protege o produto construído pelo construtor
```

Os contratos, gates, evidências e responsabilidades não devem ser confundidos entre esses dois domínios.

## MOTIVAÇÃO

Evitar que o POD considere um produto pronto apenas porque funciona. A entrega deve possuir segurança proporcional ao risco e comprovada como parte da missão, reduzindo vulnerabilidades introduzidas por arquitetura, código, dependências, dados, APIs, infraestrutura ou IA.

## IMPACTO POSSÍVEL

- criação futura de `Product Security Engineering` nativa do POD;
- integração de segurança ao planejamento e ao Loop Engineering;
- geração automática de threat models e requisitos de segurança;
- seleção de controles por risco;
- testes adversariais e regressão de segurança;
- gates específicos do produto;
- bloqueio de `MISSION_PROVEN` diante de vulnerabilidade crítica aplicável;
- evidência de segurança como parte da entrega.

## DEPENDÊNCIAS

- consolidação da Engenharia de Construção do POD;
- definição final dos perfis de risco;
- catálogo de controles e testes por tecnologia e tipo de produto;
- integração futura com Biblioteca de Conhecimento, ferramentas de análise, testes e evidências;
- critérios objetivos para `SECURITY_PROVEN`.

## CONFLITOS POSSÍVEIS

- não confundir segurança do próprio POD com segurança do produto construído;
- evitar controles excessivos para produtos de baixo risco;
- evitar tratar ferramentas de scanner como prova suficiente;
- não congelar produtos/ferramentas específicas como requisito arquitetural quando a capacidade puder ser implementada por alternativas equivalentes;
- segurança deve bloquear conclusão quando houver falha crítica aplicável, mas não deve impedir trabalho independente desnecessariamente.

## RELAÇÕES COM OUTRAS MEMÓRIAS

- `MEM-POD-20260902-003` — Fundação Neutra e invariantes de baixo arrependimento;
- `MEM-POD-20260902-005` — 14 requisitos fundamentais do POD;
- `MEM-POD-20260902-006` — distinção Segurança do POD × Segurança do Produto;
- princípio de absorção das melhores capacidades técnicas sem acoplamento a projetos doadores.

## DECISÃO FINAL

PENDENTE DE CONSOLIDAÇÃO DA ARQUITETURA FINAL.

## INCORPORADO EM

Ainda não incorporado em arquitetura normativa nem autorizado como topologia final. Registrado como capacidade candidata obrigatória para avaliação na consolidação final do POD.
