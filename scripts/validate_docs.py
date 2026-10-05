#!/usr/bin/env python3
"""Generate and validate the active POD documentary set."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "docs/POD_DOCUMENT_MANIFEST_V003.json"
DOCSET_ID = "POD-DOCSET-V003"

@dataclass(frozen=True)
class Document:
    order: int
    document_id: str
    path: str
    version: str
    status: str
    authority: str
    document_type: str

CANONICAL = (
    Document(1, "POD-DOC-001", "docs/POD_INDICE_MESTRE_V003.md", "3.3.0", "ACTIVE", "A1", "MASTER_DOCUMENT_INDEX"),
    Document(2, "POD-DOC-002", "docs/baselines/POD_BASELINE_V003_2026-09-02.md", "3.0.0", "ACTIVE", "A1", "ARCHITECTURE_BASELINE"),
    Document(3, "POD-DOC-003", "docs/architecture/POD_DNA_OPERACIONAL_V002.md", "2.0.0", "ACTIVE", "A1", "OPERATIONAL_DNA"),
    Document(4, "POD-DOC-004", "docs/specifications/POD_PROJETO_CONCEITUAL_V002.md", "2.0.0", "ACTIVE", "A2", "CONCEPTUAL_PROJECT"),
    Document(5, "POD-DOC-005", "docs/architecture/POD_ARQUITETURA_TECNICA_V002.md", "2.1.0", "ACTIVE", "A2", "TECHNICAL_ARCHITECTURE"),
    Document(6, "POD-DOC-006", "docs/specifications/POD_CONTRATOS_DADOS_ESTADOS_V002.md", "2.0.0", "ACTIVE", "A2", "CONTRACT_DATA_STATE_SPECIFICATION"),
    Document(7, "POD-DOC-007", "docs/specifications/POD_SEGURANCA_AUTORIZACOES_V002.md", "2.0.0", "ACTIVE", "A1", "SECURITY_AUTHORIZATION_SPECIFICATION"),
    Document(8, "POD-DOC-008", "docs/specifications/POD_REQUISITOS_RASTREABILIDADE_V002.md", "2.2.0", "ACTIVE", "A3", "TRACEABILITY_MATRIX"),
    Document(9, "POD-DOC-009", "docs/specifications/POD_PLANO_MESTRE_CONSTRUCAO_V002.md", "2.2.0", "ACTIVE", "A3", "MASTER_BUILD_PLAN"),
    Document(10, "POD-DOC-010", "docs/specifications/POD_PLANO_TESTES_ACEITE_V002.md", "2.2.0", "ACTIVE", "A3", "MASTER_TEST_PLAN"),
    Document(11, "POD-DOC-011", "docs/governance/POD_GOVERNANCA_DOCUMENTAL_V003.md", "3.1.0", "ACTIVE", "A2", "GOVERNANCE_SPECIFICATION"),
    Document(12, "POD-DOC-012", "docs/adr/README.md", "1.3.0", "ACTIVE", "A2", "ADR_INDEX"),
    Document(13, "POD-ADR-003", "docs/adr/ADR-003-AUTORIDADE-DE-PROVA-E-TRANSICAO-DE-MISSAO.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
    Document(14, "POD-ADR-004", "docs/adr/ADR-004-PERSISTENCIA-ATOMICA-JOURNAL-E-OUTBOX.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
    Document(15, "POD-ADR-005", "docs/adr/ADR-005-PORTOES-HUMANOS-E-DEPENDENCIAS-EXTERNAS.md", "1.0.0", "ACCEPTED", "A1", "ARCHITECTURE_DECISION"),
    Document(16, "POD-ADR-006", "docs/adr/ADR-006-LEASE-FENCING-TEMPO-E-DELEGACAO-OFFLINE.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
    Document(17, "POD-ADR-007", "docs/adr/ADR-007-NUCLEO-DE-SEGURANCA-DESDE-A-FUNDACAO.md", "1.0.0", "ACCEPTED", "A1", "ARCHITECTURE_DECISION"),
    Document(18, "POD-ADR-008", "docs/adr/ADR-008-MULTIPROJETO-FEDERACAO-E-SUPERSESSAO-DA-TOPOLOGIA-ANTERIOR.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
    Document(19, "POD-ADR-009", "docs/adr/ADR-009-INDEPENDENCIA-DO-CHATGPT-IA-HIBRIDA-E-TERMINAL-SOBERANO.md", "1.0.0", "ACCEPTED", "A1", "ARCHITECTURE_DECISION"),
    Document(20, "POD-ADR-011", "docs/adr/ADR-011-CAPABILITY-ENGINE-AQUISICAO-PROGRESSIVA-E-EVOLUCAO-GOVERNADA.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
)

ADR_REQUIRED_SECTIONS = ("Contexto","Problema","Decisão","Alternativas consideradas","Consequências","Migração","Rollback","Segurança","Compatibilidade","Evidência","Condição de revisão","Documentos relacionados")
ACTIVE_CONTRACT_PATHS = (
    "docs/baselines/POD_BASELINE_V003_2026-09-02.md",
    "docs/architecture/POD_DNA_OPERACIONAL_V002.md",
    "docs/architecture/POD_ARQUITETURA_TECNICA_V002.md",
    "docs/specifications/POD_CONTRATOS_DADOS_ESTADOS_V002.md",
    "docs/specifications/POD_SEGURANCA_AUTORIZACOES_V002.md",
    "docs/specifications/POD_PLANO_MESTRE_CONSTRUCAO_V002.md",
    "docs/adr/ADR-009-INDEPENDENCIA-DO-CHATGPT-IA-HIBRIDA-E-TERMINAL-SOBERANO.md",
    "docs/adr/ADR-011-CAPABILITY-ENGINE-AQUISICAO-PROGRESSIVA-E-EVOLUCAO-GOVERNADA.md",
)
FORBIDDEN_ACTIVE_PATTERNS = {r"PERSISTIR\s*→\s*COMMIT\s*→\s*(?:REGISTRAR\s+)?EVENTO":"sequência de dual write substituída",r"expires_monotonic_ref":"referência monotônica persistida",r"A barreira de decisão humana obrigatória é gasto financeiro novo":"portão humano financeiro exclusivo",r"1 POD MAQ\s*=\s*1 instalação\s*=\s*1 projeto":"invariante single-project substituído"}
SECRET_PATTERNS = {r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----":"private key",r"\bghp_[A-Za-z0-9]{30,}\b":"GitHub personal token",r"\bgithub_pat_[A-Za-z0-9_]{30,}\b":"GitHub fine-grained token",r"\bsk-[A-Za-z0-9_-]{24,}\b":"API secret token"}

def sha256_bytes(data: bytes) -> str: return hashlib.sha256(data).hexdigest()
def document_record(document: Document) -> dict[str, object]:
    data=(ROOT/document.path).read_bytes(); return {"order":document.order,"document_id":document.document_id,"path":document.path,"document_type":document.document_type,"authority_level":document.authority,"version":document.version,"status":document.status,"size_bytes":len(data),"sha256":f"sha256:{sha256_bytes(data)}"}
def canonical_set_payload(records:list[dict[str,object]])->bytes:
    return "".join(f'{i["order"]}\t{i["document_id"]}\t{i["path"]}\t{i["size_bytes"]}\t{str(i["sha256"]).removeprefix("sha256:")}\n' for i in sorted(records,key=lambda v:int(v["order"]))).encode("utf-8")
def build_manifest()->dict[str,object]:
    records=[document_record(d) for d in CANONICAL]; return {"schema_version":"2.0","document_set_id":DOCSET_ID,"status":"ACTIVE","generated_at":datetime.now(ZoneInfo("America/Sao_Paulo")).isoformat(timespec="seconds"),"supersedes":["POD-DOCSET-V002","POD-2026-09-02"],"canonical_document_count":len(records),"set_hash_algorithm":{"name":"SHA-256","encoding":"UTF-8","line_format":"<order>\\t<document_id>\\t<path>\\t<size_bytes>\\t<sha256_hex>\\n","ordering":"order ascending","manifest_included":False},"set_hash":f"sha256:{sha256_bytes(canonical_set_payload(records))}","implementation_status_claimed":False,"documents":records}
def write_manifest()->None: MANIFEST_PATH.write_text(json.dumps(build_manifest(),ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
def metadata_value(text:str,label:str)->str|None:
    m=re.search(rf"^\*\*{re.escape(label)}:\*\*\s*(.+?)\s*$",text,re.MULTILINE); return m.group(1).strip() if m else None

def validate(errors:list[str])->None:
    actual=json.loads(MANIFEST_PATH.read_text(encoding="utf-8")); expected=build_manifest()
    for key in ("schema_version","document_set_id","status","supersedes","canonical_document_count","set_hash_algorithm","set_hash","implementation_status_claimed","documents"):
        if actual.get(key)!=expected.get(key): errors.append(f"manifest divergente no campo {key}")
    ids=set()
    for d in CANONICAL:
        p=ROOT/d.path
        if not p.is_file(): errors.append(f"documento canônico ausente: {d.path}"); continue
        t=p.read_text(encoding="utf-8")
        for label,value in (("Identificador",d.document_id),("Versão",d.version),("Status",d.status)):
            if metadata_value(t,label)!=value: errors.append(f"{d.path}: {label} esperado {value}")
        if not metadata_value(t,"Data"): errors.append(f"{d.path}: Data ausente")
        if d.document_id in ids: errors.append(f"Identificador duplicado: {d.document_id}")
        ids.add(d.document_id)
        if d.path.endswith('.md') and len(re.findall(r"^~~~(?:[A-Za-z0-9_-]+)?\s*$",t,re.MULTILINE))%2: errors.append(f"{d.path}: bloco Markdown ~~~ não fechado")
        if d.document_type=="ARCHITECTURE_DECISION":
            for section in ADR_REQUIRED_SECTIONS:
                if not re.search(rf"^##\s+{re.escape(section)}\s*$",t,re.MULTILINE): errors.append(f"{d.path}: seção ADR ausente: {section}")
    combined="\n".join((ROOT/p).read_text(encoding="utf-8") for p in ACTIVE_CONTRACT_PATHS)
    for pattern,desc in FORBIDDEN_ACTIVE_PATTERNS.items():
        if re.search(pattern,combined,re.IGNORECASE): errors.append(f"contrato ativo contém {desc}")
    for token in ("MISSION_CORE_IS_SOLE_MISSION_STATE_WRITER = TRUE","PROOF_ENGINE_EMITS_VERDICT_ONLY = TRUE","ATOMIC_STATE_EVENT_OUTBOX = TRUE","WAITING_FINANCIAL_AUTHORIZATION","WAITING_OWNER_APPROVAL","WAITING_EXTERNAL","issued_at_utc","expires_at_utc","authority_epoch","fencing_token","ownership_scope","confidentiality","training_eligibility","execution_effect"):
        if token not in (ROOT/"docs/specifications/POD_CONTRATOS_DADOS_ESTADOS_V002.md").read_text(encoding="utf-8"): errors.append(f"contrato canônico não contém token obrigatório: {token}")
    sov=(ROOT/"docs/adr/ADR-009-INDEPENDENCIA-DO-CHATGPT-IA-HIBRIDA-E-TERMINAL-SOBERANO.md").read_text(encoding="utf-8")
    for token in ("POD_IS_STANDALONE_PRODUCT = TRUE","CHATGPT_IS_NOT_RUNTIME_DEPENDENCY = TRUE","MCP_IS_OPTIONAL_ADAPTER = TRUE","POLICY_IS_ENFORCED_BY_CODE = TRUE","PROMPT_IS_NOT_POLICY = TRUE","TERMINAL_IS_NATIVE_POD_INTERFACE = TRUE","TERMINAL_PROCESS_IS_NOT_POD_RUNTIME = TRUE","MISSION_CONTINUES_WITH_INTERFACES_CLOSED = TRUE","CORE_OPERATES_WITHOUT_EXTERNAL_AI = TRUE"):
        if token not in sov: errors.append(f"ADR-009 não contém invariante obrigatório: {token}")
    cap=(ROOT/"docs/adr/ADR-011-CAPABILITY-ENGINE-AQUISICAO-PROGRESSIVA-E-EVOLUCAO-GOVERNADA.md").read_text(encoding="utf-8")
    for token in ("CAPABILITY_ENGINE_IS_POD_NATIVE = TRUE","EXTERNAL_SKILL_IS_REFERENCE_INPUT_ONLY = TRUE","PROGRESSIVE_CAPABILITY_LOADING = TRUE","CAPABILITY_PROMOTION_REQUIRES_EVAL = TRUE","CAPABILITY_CANNOT_EXPAND_AUTHORITY = TRUE","DONOR_RUNTIME_COUPLING = ZERO","SELF_EVOLUTION_WRITES_CANDIDATE_ONLY = TRUE","UNLICENSED_SOURCE_CONTENT_NOT_COPIED = TRUE"):
        if token not in cap: errors.append(f"ADR-011 missing required invariant: {token}")
    req=(ROOT/"docs/specifications/POD_REQUISITOS_RASTREABILIDADE_V002.md").read_text(encoding="utf-8"); tests=(ROOT/"docs/specifications/POD_PLANO_TESTES_ACEITE_V002.md").read_text(encoding="utf-8")
    lines=re.findall(r"^\|\s*REQ-[A-Z]+-\d{3}\s*\|.*$",req,re.MULTILINE); defined=set(re.findall(r"^\|\s*(T-[A-Z]+-\d{3})\s*\|",tests,re.MULTILINE)); referenced=set(re.findall(r"\bT-[A-Z]+-\d{3}\b",req)); missing=sorted(referenced-defined)
    if missing: errors.append(f"testes referenciados e não definidos: {', '.join(missing)}")
    allowed={"DEFINED_NOT_IMPLEMENTED","IMPLEMENTING","IMPLEMENTED_NOT_TESTED","TESTED_NOT_EVIDENCED","EVIDENCED_NOT_ACCEPTED","ACCEPTED","BLOCKED","DEFERRED","NON_COMPLIANT","NOT_APPLICABLE"}; counts={}
    for line in lines:
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells)!=7: continue
        rid,_,_,_,tests_cell,_,status=cells; counts[status]=counts.get(status,0)+1
        if status not in allowed: errors.append(f"{rid}: estado inválido {status}")
        if not re.search(r"\bT-[A-Z]+-\d{3}\b",tests_cell): errors.append(f"{rid}: nenhum teste associado")
        if not rid.startswith("REQ-DOC-") and status!="DEFINED_NOT_IMPLEMENTED": errors.append(f"{rid}: implementação ainda não existe, estado deve ser DEFINED_NOT_IMPLEMENTED")
    summary={state:int(count) for state,count in re.findall(r"^\|\s*([A-Z_]+)\s*\|\s*(\d+)\s*\|$",req,re.MULTILINE) if state in allowed}
    if summary!=counts: errors.append(f"resumo de estados divergente: declarado={summary}, real={counts}")
    for p in ROOT.rglob('*'):
        if p.is_file() and '.git' not in p.parts and p.suffix.lower() in {'.md','.json','.py','.yml','.yaml','.txt'}:
            t=p.read_text(encoding='utf-8',errors='ignore')
            for pattern,desc in SECRET_PATTERNS.items():
                if re.search(pattern,t): errors.append(f"{p.relative_to(ROOT)}: possível {desc}")

def main()->int:
    parser=argparse.ArgumentParser(); parser.add_argument('--write-manifest',action='store_true'); args=parser.parse_args()
    if args.write_manifest: write_manifest()
    errors=[]
    try: validate(errors)
    except (FileNotFoundError,json.JSONDecodeError) as exc: errors.append(str(exc))
    if errors:
        print('POD_DOCSET_INVALID'); [print(f'- {e}') for e in errors]; return 1
    manifest=json.loads(MANIFEST_PATH.read_text(encoding='utf-8')); req=(ROOT/'docs/specifications/POD_REQUISITOS_RASTREABILIDADE_V002.md').read_text(encoding='utf-8'); count=len(re.findall(r'^\|\s*REQ-[A-Z]+-\d{3}\s*\|',req,re.MULTILINE))
    print('POD_DOCSET_VALID'); print(f"document_set_id={manifest['document_set_id']}"); print(f"documents={manifest['canonical_document_count']}"); print(f"requirements={count}"); print(f"set_hash={manifest['set_hash']}"); return 0

if __name__=='__main__': sys.exit(main())
