from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DocsValidatorIntegrationTests(unittest.TestCase):
    maxDiff = None

    def run_validator(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "scripts/validate_docs.py"],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )

    def with_copy(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory(prefix="pod-docset-test-")
        target = Path(temporary.name) / "repo"
        shutil.copytree(
            ROOT,
            target,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
        )
        return temporary, target

    def test_current_docset_passes(self) -> None:
        result = self.run_validator(ROOT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("POD_DOCSET_VALID", result.stdout)

    def test_tampered_canonical_document_fails_hash(self) -> None:
        temporary, target = self.with_copy()
        self.addCleanup(temporary.cleanup)
        path = target / "docs/architecture/POD_DNA_OPERACIONAL_V002.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nadulterado\n", encoding="utf-8")

        result = self.run_validator(target)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("manifest divergente", result.stdout)

    def test_missing_adr_section_is_rejected(self) -> None:
        temporary, target = self.with_copy()
        self.addCleanup(temporary.cleanup)
        path = target / "docs/adr/ADR-003-AUTORIDADE-DE-PROVA-E-TRANSICAO-DE-MISSAO.md"
        text = path.read_text(encoding="utf-8").replace("## Rollback", "## Retorno")
        path.write_text(text, encoding="utf-8")

        result = self.run_validator(target)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("seção ADR ausente: Rollback", result.stdout)

    def test_obsolete_dual_write_sequence_is_rejected(self) -> None:
        temporary, target = self.with_copy()
        self.addCleanup(temporary.cleanup)
        path = target / "docs/architecture/POD_DNA_OPERACIONAL_V002.md"
        text = path.read_text(encoding="utf-8")
        text += "\nPERSISTIR → COMMIT → EVENTO\n"
        path.write_text(text, encoding="utf-8")

        result = self.run_validator(target)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("sequência de dual write substituída", result.stdout)

    def test_unknown_active_document_is_rejected(self) -> None:
        temporary, target = self.with_copy()
        self.addCleanup(temporary.cleanup)
        path = target / "docs/UNREGISTERED.md"
        path.write_text(
            "# Não registrado\n\n"
            "**Identificador:** POD-DOC-999\n"
            "**Versão:** 1.0.0\n"
            "**Status:** ACTIVE\n"
            "**Data:** 2026-09-02\n",
            encoding="utf-8",
        )

        result = self.run_validator(target)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("documento ACTIVE fora do manifesto", result.stdout)

    def test_missing_test_reference_is_rejected(self) -> None:
        temporary, target = self.with_copy()
        self.addCleanup(temporary.cleanup)
        path = target / "docs/specifications/POD_REQUISITOS_RASTREABILIDADE_V002.md"
        text = path.read_text(encoding="utf-8").replace(
            "T-MSN-001,T-MSN-002",
            "T-MSN-001,T-XXX-999",
            1,
        )
        path.write_text(text, encoding="utf-8")

        result = self.run_validator(target)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("testes referenciados e não definidos: T-XXX-999", result.stdout)

    def test_unclosed_markdown_fence_is_rejected(self) -> None:
        temporary, target = self.with_copy()
        self.addCleanup(temporary.cleanup)
        path = target / "docs/architecture/POD_DNA_OPERACIONAL_V002.md"
        text = path.read_text(encoding="utf-8") + "\n~~~text\ntruncado\n"
        path.write_text(text, encoding="utf-8")

        result = self.run_validator(target)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("bloco Markdown ~~~ não fechado", result.stdout)

    def test_missing_sovereignty_invariant_is_rejected(self) -> None:
        temporary, target = self.with_copy()
        self.addCleanup(temporary.cleanup)
        path = target / "docs/adr/ADR-009-INDEPENDENCIA-DO-CHATGPT-IA-HIBRIDA-E-TERMINAL-SOBERANO.md"
        text = path.read_text(encoding="utf-8").replace(
            "CHATGPT_IS_NOT_RUNTIME_DEPENDENCY = TRUE",
            "CHATGPT_DEPENDENCY_UNSPECIFIED = TRUE",
        )
        path.write_text(text, encoding="utf-8")

        result = self.run_validator(target)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ADR-009 não contém invariante obrigatório", result.stdout)


if __name__ == "__main__":
    unittest.main()
