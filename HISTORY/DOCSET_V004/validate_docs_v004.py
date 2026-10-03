#!/usr/bin/env python3
"""Validate POD-DOCSET-V004 without mutating the historical V003 validator."""

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
MANIFEST_PATH = ROOT / "docs/POD_DOCUMENT_MANIFEST_V004.json"
DOCSET_ID = "POD-DOCSET-V004"

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
    Document(1, "POD-DOC-001", "docs/POD_INDICE_MESTRE_V004.md", "4.0.0", "ACTIVE", "A1", "MASTER_DOCUMENT_INDEX"),
    Document(2, "POD-DOC-002", "docs/baselines/POD_BASELINE_V003_2026-09-02.md", "3.0.0", "ACTIVE", "A1", "ARCHITECTURE_BASELINE"),
    Document(3, "POD-DOC-003", "docs/architecture/POD_DNA_OPERACIONAL_V002.md", "2.0.0", "ACTIVE", "A1", "OPERATIONAL_DNA"),
    Document(4, "POD-DOC-004", "docs/specifications/POD_PROJETO_CONCEITUAL_V002.md", "2.0.0", "ACTIVE", "A2", "CONCEPTUAL_PROJECT"),
    Document(5, "POD-DOC-005", "docs/architecture/POD_ARQUITETURA_TECNICA_V003.md", "3.0.0", "ACTIVE", "A2", "TECHNICAL_ARCHITECTURE"),
    Document(6, "POD-DOC-006", "docs/specifications/POD_CONTRATOS_DADOS_ESTADOS_V002.md", "2.0.0", "ACTIVE", "A2", "CONTRACT_DATA_STATE_SPECIFICATION"),
    Document(7, "POD-DOC-007", "docs/specifications/POD_SEGURANCA_AUTORIZACOES_V002.md", "2.0.0", "ACTIVE", "A1", "SECURITY_AUTHORIZATION_SPECIFICATION"),
    Document(8, "POD-DOC-008", "docs/specifications/POD_REQUISITOS_RASTREABILIDADE_V002.md", "2.1.0", "ACTIVE", "A3", "TRACEABILITY_MATRIX"),
    Document(9, "POD-DOC-009", "docs/specifications/POD_PLANO_MESTRE_CONSTRUCAO_V002.md", "2.1.0", "ACTIVE", "A3", "MASTER_BUILD_PLAN"),
    Document(10, "POD-DOC-010", "docs/specifications/POD_PLANO_TESTES_ACEITE_V002.md", "2.1.0", "ACTIVE", "A3", "MASTER_TEST_PLAN"),
    Document(11, "POD-DOC-011", "docs/governance/POD_GOVERNANCA_DOCUMENTAL_V003.md", "3.1.0", "ACTIVE", "A2", "GOVERNANCE_SPECIFICATION"),
    Document(12, "POD-DOC-012", "docs/adr/README_V004.md", "1.2.0", "ACTIVE", "A2", "ADR_INDEX"),
    Document(13, "POD-ADR-003", "docs/adr/ADR-003-AUTORIDADE-DE-PROVA-E-TRANSICAO-DE-MISSAO.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
    Document(14, "POD-ADR-004", "docs/adr/ADR-004-PERSISTENCIA-ATOMICA-JOURNAL-E-OUTBOX.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
    Document(15, "POD-ADR-005", "docs/adr/ADR-005-PORTOES-HUMANOS-E-DEPENDENCIAS-EXTERNAS.md", "1.0.0", "ACCEPTED", "A1", "ARCHITECTURE_DECISION"),
    Document(16, "POD-ADR-006", "docs/adr/ADR-006-LEASE-FENCING-TEMPO-E-DELEGACAO-OFFLINE.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
    Document(17, "POD-ADR-007", "docs/adr/ADR-007-NUCLEO-DE-SEGURANCA-DESDE-A-FUNDACAO.md", "1.0.0", "ACCEPTED", "A1", "ARCHITECTURE_DECISION"),
    Document(18, "POD-ADR-008", "docs/adr/ADR-008-MULTIPROJETO-FEDERACAO-E-SUPERSESSAO-DA-TOPOLOGIA-ANTERIOR.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
    Document(19, "POD-ADR-009", "docs/adr/ADR-009-INDEPENDENCIA-DO-CHATGPT-IA-HIBRIDA-E-TERMINAL-SOBERANO.md", "1.0.0", "ACCEPTED", "A1", "ARCHITECTURE_DECISION"),
    Document(20, "POD-ADR-010", "docs/adr/ADR-010-CORE-SELADO-SCM-SOBERANO-E-SEPARACAO-DE-ESTADO.md", "1.0.0", "ACCEPTED", "A1/A2", "ARCHITECTURE_DECISION"),
    Document(21, "POD-DOC-013", "docs/specifications/POD_CORE_SCM_ARMAZENAMENTO_EXECUTION_ENVELOPE_V001.md", "1.0.0", "ACTIVE", "A2", "CORE_SCM_STORAGE_EXECUTION_ENVELOPE_SPECIFICATION"),
)

ADR_REQUIRED_SECTIONS = (
    "Contexto", "Problema", "Decisão", "Alternativas consideradas", "Consequências",
    "Migração", "Rollback", "Segurança", "Compatibilidade", "Evidência",
    "Condição de revisão", "Documentos relacionados",
)

REQUIRED_V004_TOKENS = (
    "CORE_RELEASE = IMMUTABLE",
    "NOTHING_EXECUTES_WITHOUT_SCOPE = TRUE",
    "NOTHING_PERSISTS_WITHOUT_CLASSIFICATION = TRUE",
    "NOTHING_BECOMES_KNOWLEDGE_WITHOUT_EVIDENCE = TRUE",
    "NOTHING_EXTERNAL_BECOMES_STRUCTURAL_DEPENDENCY = TRUE",
    "CORE_CONTAMINATION = 0",
    "REGENERABLE_DATA_IN_CORE = 0",
    "UNTRACEABLE_KNOWLEDGE = 0",
    "UNSCOPED_KNOWLEDGE = 0",
    "UNREVERSIBLE_KNOWLEDGE = 0",
    "Sovereign Cognitive Memory",
    "DURABLE",
    "RECONSTRUCTIBLE",
    "EPHEMERAL",
    "KnowledgeAdmissionDecision",
    "ExecutionEnvelope",
    "content_ref = sha256:<digest>",
)

SECRET_PATTERNS = {
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----": "private key",
    r"\bghp_[A-Za-z0-9]{30,}\b": "GitHub personal token",
    r"\bgithub_pat_[A-Za-z0-9_]{30,}\b": "GitHub fine-grained token",
    r"\bsk-[A-Za-z0-9_-]{24,}\b": "API secret token",
}

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def metadata_value(text: str, label: str) -> str | None:
    match = re.search(rf"^\*\*{re.escape(label)}:\*\*\s*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None

def document_record(document: Document) -> dict[str, object]:
    data = (ROOT / document.path).read_bytes()
    return {
        "order": document.order,
        "document_id": document.document_id,
        "path": document.path,
        "document_type": document.document_type,
        "authority_level": document.authority,
        "version": document.version,
        "status": document.status,
        "size_bytes": len(data),
        "sha256": f"sha256:{sha256_bytes(data)}",
    }

def set_payload(records: list[dict[str, object]]) -> bytes:
    lines = []
    for item in sorted(records, key=lambda value: int(value["order"])):
        digest = str(item["sha256"]).removeprefix("sha256:")
        lines.append(
            f'{item["order"]}\t{item["document_id"]}\t{item["path"]}\t'
            f'{item["size_bytes"]}\t{digest}\n'
        )
    return "".join(lines).encode("utf-8")

def build_manifest() -> dict[str, object]:
    records = [document_record(document) for document in CANONICAL]
    return {
        "schema_version": "2.0",
        "document_set_id": DOCSET_ID,
        "status": "ACTIVE",
        "generated_at": datetime.now(ZoneInfo("America/Sao_Paulo")).isoformat(timespec="seconds"),
        "supersedes": ["POD-DOCSET-V003"],
        "canonical_document_count": len(records),
        "set_hash_algorithm": {
            "name": "SHA-256",
            "encoding": "UTF-8",
            "line_format": "<order>\\t<document_id>\\t<path>\\t<size_bytes>\\t<sha256_hex>\\n",
            "ordering": "order ascending",
            "manifest_included": False,
        },
        "set_hash": f"sha256:{sha256_bytes(set_payload(records))}",
        "implementation_status_claimed": False,
        "documents": records,
    }

def write_manifest() -> None:
    manifest = build_manifest()
    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

def validate(errors: list[str]) -> None:
    ids: set[str] = set()
    for document in CANONICAL:
        path = ROOT / document.path
        if not path.is_file():
            errors.append(f"documento canônico ausente: {document.path}")
            continue
        text = path.read_text(encoding="utf-8")
        expected = {
            "Identificador": document.document_id,
            "Versão": document.version,
            "Status": document.status,
        }
        for label, value in expected.items():
            if metadata_value(text, label) != value:
                errors.append(f"{document.path}: {label} esperado {value}")
        if not metadata_value(text, "Data"):
            errors.append(f"{document.path}: Data ausente")
        if document.document_id in ids:
            errors.append(f"Identificador duplicado: {document.document_id}")
        ids.add(document.document_id)
        if document.path.endswith(".md") and len(re.findall(r"^~~~(?:[A-Za-z0-9_-]+)?\s*$", text, re.MULTILINE)) % 2:
            errors.append(f"{document.path}: bloco Markdown ~~~ não fechado")
        for pattern, description in SECRET_PATTERNS.items():
            if re.search(pattern, text):
                errors.append(f"{document.path}: possível segredo detectado: {description}")

    for document in CANONICAL:
        if document.document_type != "ARCHITECTURE_DECISION":
            continue
        text = (ROOT / document.path).read_text(encoding="utf-8")
        for section in ADR_REQUIRED_SECTIONS:
            if not re.search(rf"^##\s+{re.escape(section)}\s*$", text, re.MULTILINE):
                errors.append(f"{document.path}: seção ADR ausente: {section}")

    combined = "\n".join(
        (ROOT / p).read_text(encoding="utf-8")
        for p in (
            "docs/POD_INDICE_MESTRE_V004.md",
            "docs/architecture/POD_ARQUITETURA_TECNICA_V003.md",
            "docs/adr/ADR-010-CORE-SELADO-SCM-SOBERANO-E-SEPARACAO-DE-ESTADO.md",
            "docs/specifications/POD_CORE_SCM_ARMAZENAMENTO_EXECUTION_ENVELOPE_V001.md",
        )
    )
    for token in REQUIRED_V004_TOKENS:
        if token not in combined:
            errors.append(f"reconciliação V004 não contém token obrigatório: {token}")

    if MANIFEST_PATH.is_file():
        try:
            actual = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"manifest JSON inválido: {exc}")
        else:
            expected = build_manifest()
            for key in (
                "schema_version", "document_set_id", "status", "supersedes",
                "canonical_document_count", "set_hash_algorithm", "set_hash",
                "implementation_status_claimed", "documents",
            ):
                if actual.get(key) != expected.get(key):
                    errors.append(f"manifest V004 divergente no campo {key}")
    else:
        errors.append("manifest V004 ausente")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-manifest", action="store_true")
    args = parser.parse_args()
    if args.write_manifest:
        write_manifest()
    errors: list[str] = []
    validate(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("POD_DOCSET_V004_VALID")
    return 0

if __name__ == "__main__":
    sys.exit(main())
