# POD — BLOCO DE NOTAS

**Status:** WORKING / OPERATIONAL NOTES
**Finalidade:** capturar rapidamente pendências, observações e marcações durante a implementação e operação do POD sem interromper a missão em andamento.

## Regra de entrada

Quando o operador usar comandos naturais como `registre`, `anota`, `anote`, `marca`, `marque`, `guarda`, `guarde isso`, `lembra disso` ou equivalentes, sem indicar outro destino explícito, o conteúdo deve ser registrado neste Bloco de Notas.

```text
ANOTAR != PAUSAR MISSÃO
```

## Regra de estado

Toda nova anotação nasce obrigatoriamente como:

```text
STATUS = PENDÊNCIA
```

## Formato obrigatório de identificação

Cada anotação deve conter:

```text
ID: b6c5cd691f7d52707dd64275a2498e7d97xxxxxx
DATA: AAAA-MM-DD
NOME: identificação curta e objetiva do assunto
PROJETO / PARTE: projeto, módulo, componente ou área relacionada
STATUS: PENDÊNCIA
TEXTO ORIGINAL: conteúdo preservado da anotação
```

O prefixo fixo do identificador é:

```text
b6c5cd691f7d52707dd64275a2498e7d97
```

Os seis últimos caracteres são hexadecimais e devem ser únicos dentro do Bloco de Notas.

O identificador é um `note_id` operacional e não deve ser interpretado como hash criptográfico do conteúdo.

## Precedência de destino

```text
"registre" / "anota" / "marca" sem destino explícito
→ BLOCO DE NOTAS POD

"registre no Registro Vivo"
→ Registro Vivo

"registre na documentação do projeto"
→ documentação indicada

"registre como decisão arquitetural"
→ fluxo de consolidação arquitetural correspondente
```

---

# PENDÊNCIAS

## b6c5cd691f7d52707dd64275a2498e7d97c14a2f

**DATA:** 2026-09-02  
**NOME:** Regra nativa do Bloco de Notas POD  
**PROJETO / PARTE:** POD / Memória / Bloco de Notas  
**STATUS:** PENDÊNCIA

### TEXTO ORIGINAL

> Toda anotação vai para Bloco de Notas como Pendencia com b6c5cd691f7d52707dd64275a2498e7d97xxxxxx e data e Um nome para identificação do que se trata ou de qual parte do projeto.

### CONTEXTO

O Bloco de Notas POD deve ser nativo, persistente e usado durante implementação/operação para registrar rapidamente observações e pendências sem interromper a missão. Comandos naturais de anotação sem destino explícito devem cair neste local.
