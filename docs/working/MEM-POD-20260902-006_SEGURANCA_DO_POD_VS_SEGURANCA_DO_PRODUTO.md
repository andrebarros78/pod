# MEM-POD-20260902-006 — SEGURANÇA DO POD VS SEGURANÇA DO PRODUTO

**DATA:** 02/09/2026  
**TIPO:** ARCHITECTURAL_INSIGHT / RULE_CANDIDATE / SECURITY  
**STATUS:** CAPTURED  
**NORMATIVO:** NÃO

## TEXTO ORIGINAL

> Ele trata da contrução de um produto pelo POD ou da contrução de POD?

Decisão associada: registrar a distinção entre a segurança que protege o próprio POD e a segurança que o POD aplica aos produtos que constrói.

## INTERPRETAÇÃO TÉCNICA

O documento `SECURITY_MAX_V1_0_20260902.md` deve ser tratado predominantemente como fonte de engenharia para a **construção, proteção, hardening, operação segura e prova de segurança do próprio POD**, e não como especificação principal de segurança dos produtos construídos pelo POD.

A arquitetura futura deve separar explicitamente dois domínios:

### 1. SEGURANÇA DO PRÓPRIO POD

Protege o construtor soberano e sua infraestrutura, incluindo, conforme a arquitetura final:

- Cérebro;
- Memória;
- Governador;
- Sistema Imunológico;
- Túnel Core;
- Engines Windows/Linux;
- Workers;
- Vault e Secret Broker;
- Executor Privilegiado;
- identidade e capabilities;
- políticas;
- comunicação e federação;
- banco, eventos, evidências e auditoria;
- supply chain, releases e atualizações do próprio POD;
- recuperação, backup e continuidade do próprio POD.

Princípio:

```text
SEGURANÇA DO POD
=
PROTEGER O CONSTRUTOR
```

### 2. SEGURANÇA APLICADA PELO POD AO PRODUTO CONSTRUÍDO

É capacidade da Engenharia de Construção POD para projetar, implementar, testar e provar a segurança do software que estiver sendo construído em uma missão.

Pode abranger, conforme o produto:

- threat modeling do produto;
- arquitetura segura;
- autenticação e autorização;
- gestão de segredos;
- segurança de APIs;
- proteção de dados;
- hardening;
- dependências e supply chain do produto;
- análise estática e dinâmica;
- testes adversariais;
- isolamento;
- segurança de banco e infraestrutura;
- auditoria;
- recovery;
- evidências de segurança;
- gates de aceite do produto.

Princípio:

```text
SEGURANÇA APLICADA PELO POD
=
PROTEGER O PRODUTO QUE O CONSTRUTOR ENTREGA
```

## REGRA DE SEPARAÇÃO

```text
SEGURANÇA QUE PROTEGE O CONSTRUTOR
!=
SEGURANÇA QUE O CONSTRUTOR IMPLEMENTA NO PRODUTO
```

Os dois domínios compartilham princípios e mecanismos, mas possuem alvos, autoridade, ciclo de vida, risco e critérios de prova diferentes.

Uma vulnerabilidade no produto em construção não deve automaticamente comprometer o POD. Da mesma forma, os controles internos de soberania do POD não devem ser confundidos com requisitos funcionais do produto.

## PAPEL DO SECURITY_MAX

`SECURITY_MAX` é classificado, para fins de concepção do POD, como fonte doadora de alto valor para o primeiro domínio:

```text
SECURITY_MAX
→ SEGURANÇA DO PRÓPRIO POD
```

Suas capacidades úteis podem também alimentar a Engenharia de Segurança aplicada aos produtos, mas isso é uma segunda utilização e não altera seu enquadramento principal.

A absorção futura deve preservar capacidades e invariantes úteis, removendo nomenclatura, precedência, caminhos, serviços ou dependências específicas dos projetos doadores, em conformidade com ZERO DONOR COUPLING.

## MOTIVAÇÃO

Evitar misturar duas responsabilidades distintas durante a consolidação arquitetural e impedir que requisitos de proteção do núcleo soberano sejam confundidos com requisitos de segurança de cada produto construído.

A separação também permite que o POD possua uma base de segurança própria obrigatória enquanto adapte a segurança aplicada a cada produto conforme contexto, criticidade, dados, exposição e critérios de aceite da missão.

## IMPACTO POSSÍVEL

- criação futura de um domínio transversal de Segurança do POD;
- definição mais precisa do Sistema Imunológico;
- definição de capacidades de Security Engineering dentro da Engenharia de Construção POD;
- gates independentes para `POD_SECURITY_PROVEN` e para a segurança do produto de cada missão;
- isolamento obrigatório entre ambiente do POD e workspaces/produtos em construção;
- políticas diferenciadas para proteger o construtor e proteger o artefato construído;
- reutilização controlada de conhecimento e mecanismos de `SECURITY_MAX` sem acoplamento doador.

## DEPENDÊNCIAS

- consolidação da arquitetura final do POD;
- definição final dos limites entre Governador, Sistema Imunológico, Cérebro, Engines e Segurança transversal;
- definição futura da Engenharia de Segurança aplicada aos produtos;
- inventário e normalização das capacidades úteis do `SECURITY_MAX`.

## CONFLITOS POSSÍVEIS

Pode haver sobreposição entre Segurança transversal, Sistema Imunológico, Recovery, Governador, Privileged Executor e Engenharia de Construção. Essa sobreposição deve ser resolvida na consolidação final por responsabilidade, autoridade, contrato e gate, sem transformar toda segurança em um único módulo.

Também deve ser evitada a interpretação de que todo produto construído precisa reproduzir integralmente a arquitetura `SECURITY_MAX`; os controles do produto devem ser proporcionais ao risco e ao objetivo da missão.

## RELAÇÕES COM OUTRAS MEMÓRIAS

- `MEM-POD-20260902-001` — absorção integral do valor técnico comprovado dos projetos doadores;
- `MEM-POD-20260902-002` — componentes conceituais, incluindo Sistema Imunológico;
- `MEM-POD-20260902-003` — Fundação Neutra e invariantes implementáveis sem congelar topologia;
- `MEM-POD-20260902-004` — dez requisitos obrigatórios do comportamento do código-fonte;
- `MEM-POD-20260902-005` — quatorze requisitos fundamentais do POD.

## DECISÃO FINAL

PENDENTE DE CONSOLIDAÇÃO DA ARQUITETURA FINAL.

## INCORPORADO EM

Ainda não incorporado em arquitetura normativa, baseline ou ADR.
