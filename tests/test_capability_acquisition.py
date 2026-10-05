from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/validate_capability_acquisition.py"
MANIFEST = ROOT / "docs/working/capability-acquisition/POD_CAPABILITY_SOURCE_MANIFEST_V001.json"

spec = importlib.util.spec_from_file_location("validate_capability_acquisition", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

class CapabilityAcquisitionTests(unittest.TestCase):
    def test_current_manifest_passes(self) -> None:
        result = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("POD_CAPABILITY_ACQUISITION_VALID", result.stdout)
        self.assertIn("sources=19", result.stdout)
        self.assertIn("donor_runtime_coupling=0", result.stdout)

    def test_duplicate_capability_is_rejected(self) -> None:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        data["sources"].append(dict(data["sources"][0])); data["source_count"] = len(data["sources"])
        errors = module.validate_structure(data)
        self.assertTrue(any("duplicate capability_id" in error for error in errors))

    def test_runtime_coupling_scan_detects_donor_reference(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); runtime = root / "src"; runtime.mkdir()
            (runtime / "bad.py").write_text('SOURCE = "obra/superpowers"\n', encoding="utf-8")
            hits = module.scan_runtime_coupling(root)
            self.assertEqual(len(hits), 1); self.assertIn("obra/superpowers", hits[0])

if __name__ == "__main__":
    unittest.main()
