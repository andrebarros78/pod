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
    Document(1, "POD-DOC-001", "docs/POD_INDICE_MESTRE_V003.md", "3.0.0", "ACTIVE", "A1", "MASTER_DOCUMENT_INDEX"),
    Document(2, "POD-DOC-002", "docs/baselines/POD_BASELINE_V003_2026-09-02.md", "3.0.0", "ACTIVE", "A1", "ARCHITECTURE_BASELINE"),
    Document(3, "POD-DOC-003", "docs/architecture/POD_DNA_OPERACIONAL_V002.md", "2.0.0", "ACTIVE", "A1", "OPERATIONAL_DNA"),
    Document(4, "POD-DOC-004", "docs/specifications/POD_PROJETO_CONCEITUAL_V002.md", "2.0.0", "ACTIVE", "A2", "CONCEPTUAL_PROJECT"),
    Document(5, "POD-DOC-005", "docs/architecture/POD_ARQUITETURA_TECNICA_V002.md", "2.0.0", "ACTIVE", "A2", "TECHNICAL_ARCHITECTURE"),
    Document(6, "POD-DOC-006", "docs/specifications/POD_CONTRATOS_DADOS_ESTADOS_V002.md", "2.0.0", "ACTIVE", "A2", "CONTRACT_DATA_STATE_SPECIFICATION"),
    Document(7, "POD-DOC-007", "docs/specifications/POD_SEGURANCA_AUTORIZACOES_V002.md", "2.0.0", "ACTIVE", "A1", "SECURITY_AUTHORIZATION_SPECIFICATION"),
    Document(8, "POD-DOC-008", "docs/specifications/POD_REQUISITOS_RASTREABILIDADE_V002.md", "2.0.0", "ACTIVE", "A3", "TRACEABILITY_MATRIX"),
    Document(9, "POD-DOC-009", "docs/specifications/POD_PLANO_MESTRE_CONSTRUCAO_V002.md", "2.0.0", "ACTIVE", "A3", "MASTER_BUILD_PLAN"),
    Document(10, "POD-DOC-010", "docs/specifications/POD_PLANO_TESTES_ACEITE_V002.md", "2.0.0", "ACTIVE", "A3", "MASTER_TEST_PLAN"),
    Document(11, "POD-DOC-011", "docs/governance/POD_GOVERNANCA_DOCUMENTAL_V003.md", "3.0.0", "ACTIVE", "A2", "GOVERNANCE_SPECIFICATION"),
    Document(12, "POD-DOC-012", "docs/adr/README.md", "1.0.0", "ACTIVE", "A2", "ADR_INDEX"),
    Document(13, "POD-ADR-003", "docs/adr/ADR-003-AUTORIDADE-DE-PROVA-E-TRANSICAO-DE-MISSAO.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
    Document(14, "POD-ADR-004", "docs/adr/ADR-004-PERSISTENCIA-ATOMICA-JOURNAL-E-OUTBOX.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
    Document(15, "POD-ADR-005", "docs/adr/ADR-005-PORTOES-HUMANOS-E-DEPENDENCIAS-EXTERNAS.md", "1.0.0", "ACCEPTED", "A1", "ARCHITECTURE_DECISION"),
    Document(16, "POD-ADR-006", "docs/adr/ADR-006-LEASE-FENCING-TEMPO-E-DELEGACAO-OFFLINE.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
    Document(17, "POD-ADR-007", "docs/adr/ADR-007-NUCLEO-DE-SEGURANCA-DESDE-A-FUNDACAO.md", "1.0.0", "ACCEPTED", "A1", "ARCHITECTURE_DECISION"),
    Document(18, "POD-ADR-008", "docs/adr/ADR-008-MULTIPROJETO-FEDERACAO-E-SUPERSESSAO-DA-TOPOLOGIA-ANTERIOR.md", "1.0.0", "ACCEPTED", "A2", "ARCHITECTURE_DECISION"),
)


ADR_REQUIRED_SECTIONS = (
    "Contexto",
    "Problema",
    "Decisão",
    "Alternativas consideradas",
    "Consequências",
    "Migração",
    "Rollback",
    "Segurança",
    "Compatibilidade",
    "Evidência",
    "Condição de revisão",
    "Documentos relacionados",
)

ACTIVE_CONTRACT_PATHS = (
    "docs/baselines/POD_BASELINE_V003_2026-09-02.md",
    "docs/architecture/POD_DNA_OPERACIONAL_V002.md",
    "docs/architecture/POD_ARQUITETURA_TECNICA_V002.md",
    "docs/specifications/POD_CONTRATOS_DADOS_ESTADOS_V002.md",
    "docs/specifications/POD_SEGURANCA_AUTORIZACOES_V002.md",
    "docs/specifications/POD_PLANO_MESTRE_CONSTRUCAO_V002.md",
)

FORBIDDEN_ACTIVE_PATTERNS = {
    r"PERSISTIR\s*→\s*COMMIT\s*→\s*(?:REGISTRAR\s+)?EVENTO": "sequência de dual write substituída",
    r"expires_monotonic_ref": "referência monotônica persistida",
    r"A barreira de decisão humana obrigatória é gasto financeiro novo": "portão humano financeiro exclusivo",
    r"1 POD MAQ\s*=\s*1 instalação\s*=\s*1 projeto": "invariante single-project substituído",
}

SECRET_PATTERNS = {
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----": "private key",
    r"\bghp_[A-Za-z0-9]{30,}\b": "GitHub personal token",
    r"\bgithub_pat_[A-Za-z0-9_]{30,}\b": "GitHub fine-grained token",
    r"\bsk-[A-Za-z0-9_-]{24,}\b": "API secret token",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def document_record(document: Document) -> dict[str, object]:
    path = ROOT / document.path
    data = path.read_bytes()
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


def canonical_set_payload(records: list[dict[str, object]]) -> bytes:
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
        "supersedes": ["POD-DOCSET-V002", "POD-2026-09-02"],
        "canonical_document_count": len(records),
        "set_hash_algorithm": {
            "name": "SHA-256",
            "encoding": "UTF-8",
            "line_format": "<order>\\t<document_id>\\t<path>\\t<size_bytes>\\t<sha256_hex>\\n",
            "ordering": "order ascending",
            "manifest_included": False,
        },
        "set_hash": f"sha256:{sha256_bytes(canonical_set_payload(records))}",
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


def metadata_value(text: str, label: str) -> str | None:
    match = re.search(rf"^\*\*{re.escape(label)}:\*\*\s*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def validate_manifest(errors: list[str]) -> None:
    if not MANIFEST_PATH.is_file():
        errors.append(f"manifest ausente: {MANIFEST_PATH.relative_to(ROOT)}")
        return

    try:
        actual = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"manifest JSON inválido: {exc}")
        return

    expected = build_manifest()
    for key in (
        "schema_version",
        "document_set_id",
        "status",
        "supersedes",
        "canonical_document_count",
        "set_hash_algorithm",
        "set_hash",
        "implementation_status_claimed",
        "documents",
    ):
        if actual.get(key) != expected.get(key):
            errors.append(f"manifest divergente no campo {key}")


def validate_metadata(errors: list[str]) -> None:
    ids: set[str] = set()
    for document in CANONICAL:
        path = ROOT / document.path
        if not path.is_file():
            errors.append(f"documento canônico ausente: {document.path}")
            continue
        text = path.read_text(encoding="utf-8")
        values = {
            "Identificador": metadata_value(text, "Identificador"),
            "Versão": metadata_value(text, "Versão"),
            "Status": metadata_value(text, "Status"),
            "Data": metadata_value(text, "Data"),
        }
        if values["Identificador"] != document.document_id:
            errors.append(f"{document.path}: Identificador esperado {document.document_id}")
        if values["Versão"] != document.version:
            errors.append(f"{document.path}: Versão esperada {document.version}")
        if values["Status"] != document.status:
            errors.append(f"{document.path}: Status esperado {document.status}")
        if not values["Data"]:
            errors.append(f"{document.path}: Data ausente")
        if document.document_id in ids:
            errors.append(f"Identificador duplicado: {document.document_id}")
        ids.add(document.document_id)


def iter_markdown_links(text: str) -> list[str]:
    return re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text)


def validate_links(errors: list[str]) -> None:
    for path in (ROOT / "docs").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw_target in iter_markdown_links(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or re.match(r"^(?:https?://|mailto:|sandbox:)", target):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapa do repositório: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: link quebrado: {target}")


def validate_markdown_structure(errors: list[str]) -> None:
    """Reject truncated canonical Markdown before it can enter the manifest."""
    for document in CANONICAL:
        if not document.path.endswith(".md"):
            continue
        path = ROOT / document.path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if len(re.findall(r"^~~~(?:[A-Za-z0-9_-]+)?\s*$", text, re.MULTILINE)) % 2:
            errors.append(f"{document.path}: bloco Markdown ~~~ não fechado")


def validate_adrs(errors: list[str]) -> None:
    for document in CANONICAL:
        if document.document_type != "ARCHITECTURE_DECISION":
            continue
        text = (ROOT / document.path).read_text(encoding="utf-8")
        for section in ADR_REQUIRED_SECTIONS:
            if not re.search(rf"^##\s+{re.escape(section)}\s*$", text, re.MULTILINE):
                errors.append(f"{document.path}: seção ADR ausente: {section}")


def validate_active_invariants(errors: list[str]) -> None:
    combined = "\n".join((ROOT / path).read_text(encoding="utf-8") for path in ACTIVE_CONTRACT_PATHS)
    for pattern, description in FORBIDDEN_ACTIVE_PATTERNS.items():
        if re.search(pattern, combined, re.IGNORECASE):
            errors.append(f"contrato ativo contém {description}")

    required_tokens = (
        "MISSION_CORE_IS_SOLE_MISSION_STATE_WRITER = TRUE",
        "PROOF_ENGINE_EMITS_VERDICT_ONLY = TRUE",
        "ATOMIC_STATE_EVENT_OUTBOX = TRUE",
        "WAITING_FINANCIAL_AUTHORIZATION",
        "WAITING_OWNER_APPROVAL",
        "WAITING_EXTERNAL",
        "issued_at_utc",
        "expires_at_utc",
        "authority_epoch",
        "fencing_token",
        "ownership_scope",
        "confidentiality",
        "training_eligibility",
        "execution_effect",
    )
    contracts = (ROOT / "docs/specifications/POD_CONTRATOS_DADOS_ESTADOS_V002.md").read_text(encoding="utf-8")
    for token in required_tokens:
        if token not in contracts:
            errors.append(f"contrato canônico não contém token obrigatório: {token}")


def validate_traceability(errors: list[str]) -> None:
    requirements_path = ROOT / "docs/specifications/POD_REQUISITOS_RASTREABILIDADE_V002.md"
    tests_path = ROOT / "docs/specifications/POD_PLANO_TESTES_ACEITE_V002.md"
    requirements_text = requirements_path.read_text(encoding="utf-8")
    tests_text = tests_path.read_text(encoding="utf-8")

    requirement_lines = re.findall(r"^\|\s*REQ-[A-Z]+-\d{3}\s*\|.*$", requirements_text, re.MULTILINE)
    requirement_ids = [
        re.match(r"^\|\s*(REQ-[A-Z]+-\d{3})\s*\|", line).group(1)
        for line in requirement_lines
    ]
    if len(requirement_ids) != len(set(requirement_ids)):
        errors.append("matriz contém requirement_id duplicado")
    if len(requirement_ids) < 80:
        errors.append(f"matriz possui somente {len(requirement_ids)} requisitos; mínimo esperado 80")

    defined_test_list = re.findall(r"^\|\s*(T-[A-Z]+-\d{3})\s*\|", tests_text, re.MULTILINE)
    defined_tests = set(defined_test_list)
    if len(defined_test_list) != len(defined_tests):
        errors.append("plano de testes contém test_id duplicado")
    if len(defined_tests) < 100:
        errors.append(f"plano possui somente {len(defined_tests)} testes; mínimo esperado 100")

    referenced_tests = set(re.findall(r"\bT-[A-Z]+-\d{3}\b", requirements_text))
    missing = sorted(referenced_tests - defined_tests)
    if missing:
        errors.append(f"testes referenciados e não definidos: {', '.join(missing)}")

    allowed_states = {
        "DEFINED_NOT_IMPLEMENTED",
        "IMPLEMENTING",
        "IMPLEMENTED_NOT_TESTED",
        "TESTED_NOT_EVIDENCED",
        "EVIDENCED_NOT_ACCEPTED",
        "ACCEPTED",
        "BLOCKED",
        "DEFERRED",
        "NON_COMPLIANT",
        "NOT_APPLICABLE",
    }
    status_counts: dict[str, int] = {}
    for line in requirement_lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 7:
            errors.append(f"linha de requisito com {len(cells)} colunas: {cells[0]}")
            continue
        requirement_id, _, _, _, tests_cell, _, status = cells
        if status not in allowed_states:
            errors.append(f"{requirement_id}: estado inválido {status}")
        status_counts[status] = status_counts.get(status, 0) + 1
        if not re.search(r"\bT-[A-Z]+-\d{3}\b", tests_cell):
            errors.append(f"{requirement_id}: nenhum teste associado")
        if not requirement_id.startswith("REQ-DOC-") and status != "DEFINED_NOT_IMPLEMENTED":
            errors.append(
                f"{requirement_id}: implementação ainda não existe, estado deve ser DEFINED_NOT_IMPLEMENTED"
            )

    summary_counts = {
        state: int(count)
        for state, count in re.findall(
            r"^\|\s*([A-Z_]+)\s*\|\s*(\d+)\s*\|$",
            requirements_text,
            re.MULTILINE,
        )
        if state in allowed_states
    }
    if summary_counts != status_counts:
        errors.append(
            f"resumo de estados divergente: declarado={summary_counts}, real={status_counts}"
        )

    active_doc_ids = {document.document_id for document in CANONICAL}
    referenced_doc_ids = set(re.findall(r"\bPOD-DOC-\d{3}\b", requirements_text))
    missing_docs = sorted(referenced_doc_ids - active_doc_ids)
    if missing_docs:
        errors.append(f"documentos referenciados e não ativos: {', '.join(missing_docs)}")

    active_adr_ids = {
        document.document_id.replace("POD-", "")
        for document in CANONICAL
        if document.document_type == "ARCHITECTURE_DECISION"
    }
    referenced_adr_ids = set(re.findall(r"\bADR-\d{3}\b", requirements_text))
    missing_adrs = sorted(referenced_adr_ids - active_adr_ids)
    if missing_adrs:
        errors.append(f"ADRs referenciados e não ativos: {', '.join(missing_adrs)}")


def validate_single_active_set(errors: list[str]) -> None:
    active_paths = {document.path for document in CANONICAL if document.status == "ACTIVE"}
    for path in (ROOT / "docs").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if metadata_value(text, "Status") == "ACTIVE":
            relative = path.relative_to(ROOT).as_posix()
            if relative not in active_paths:
                errors.append(f"documento ACTIVE fora do manifesto: {relative}")


def validate_secrets(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".json", ".py", ".yml", ".yaml", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern, description in SECRET_PATTERNS.items():
            if re.search(pattern, text):
                errors.append(f"{path.relative_to(ROOT)}: possível {description}")


def validate() -> list[str]:
    errors: list[str] = []
    validate_manifest(errors)
    validate_metadata(errors)
    validate_links(errors)
    validate_markdown_structure(errors)
    validate_adrs(errors)
    validate_active_invariants(errors)
    validate_traceability(errors)
    validate_single_active_set(errors)
    validate_secrets(errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-manifest",
        action="store_true",
        help="gera o manifesto antes de validar",
    )
    args = parser.parse_args()

    if args.write_manifest:
        write_manifest()

    errors = validate()
    if errors:
        print("POD_DOCSET_INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    requirements_text = (
        ROOT / "docs/specifications/POD_REQUISITOS_RASTREABILIDADE_V002.md"
    ).read_text(encoding="utf-8")
    requirement_count = len(
        re.findall(r"^\|\s*REQ-[A-Z]+-\d{3}\s*\|", requirements_text, re.MULTILINE)
    )
    print("POD_DOCSET_VALID")
    print(f"document_set_id={manifest['document_set_id']}")
    print(f"documents={manifest['canonical_document_count']}")
    print(f"requirements={requirement_count}")
    print(f"set_hash={manifest['set_hash']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
