#!/usr/bin/env python3
from pathlib import Path
import hashlib
import os
import subprocess
import sys
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
VERSION = "v1.7.4"
URL = f"https://github.com/tlaplus/tlaplus/releases/download/{VERSION}/tla2tools.jar"
EXPECTED_SHA256 = "936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88"
JAR = Path(os.environ.get("TLA2TOOLS_JAR", f"/tmp/pod-tla2tools-{VERSION}.jar"))

if not JAR.exists():
    urllib.request.urlretrieve(URL, JAR)

actual = hashlib.sha256(JAR.read_bytes()).hexdigest()
if actual != EXPECTED_SHA256:
    print(f"POD_FORMAL_INVALID\n- tla2tools sha256 mismatch: {actual}")
    sys.exit(1)

with tempfile.TemporaryDirectory(prefix="pod-tlc-") as metadir:
    cmd = [
        "java", "-XX:+UseParallelGC", "-cp", str(JAR), "tlc2.TLC",
        "-metadir", metadir,
        "-config", str(ROOT / "formal" / "PODCore.cfg"),
        str(ROOT / "formal" / "PODCore.tla"),
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
print(p.stdout, end="")
if p.stderr:
    print(p.stderr, file=sys.stderr, end="")
if p.returncode != 0:
    print("POD_FORMAL_INVALID")
    sys.exit(p.returncode)
print("POD_FORMAL_VALID")
