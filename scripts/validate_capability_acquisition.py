#!/usr/bin/env python3
"""Validate the reconciled POD capability reference acquisition."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "EVIDENCE/capability-acquisition/POD_CAPABILITY_SOURCE_MANIFEST_V001.json"
TEXT_SUFFIXES = {".py", ".toml", ".yml", ".yaml", ".json", ".ps1", ".bat", ".cmd", ".rs", ".go", ".cs", ".java", ".kt", ".swift"}
RUNTIME_ROOT_NAMES = ("src", "app", "runtime", "pod")
DONOR_TOKENS = (
    "anthropics/skills",
    "obra/superpowers",
    "intelligentcode-ai/skills",
    "addyosmani/agent-skills",
    "browser-use/browser-use",
    "fcarucci/daneel",
    "market.lobehub.com/api/v1/skills",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_manifest(path: Path = MANIFEST) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_structure(data: dict[str, object]) -> list[str]:
    errors: list[str] = []
    sources = data.get("sources")
    if data.get("acquisition_id") != "POD-CAPABILITY-ACQUISITION-V001":
        errors.append("acquisition_id invalid")
    if data.get("runtime_dependency_on_sources") is not False:
        errors.append("runtime_dependency_on_sources must be false")
    if data.get("donor_runtime_coupling") != 0:
        errors.append("donor_runtime_coupling must be zero")
    if not isinstance(sources, list):
        return errors + ["sources must be a list"]
    if data.get("source_count") != len(sources):
        errors.append("source_count mismatch")
    if len(sources) != 19:
        errors.append(f"expected 19 sources, got {len(sources)}")
    ids = [item.get("capability_id") for item in sources if isinstance(item, dict)]
    if len(ids) != len(set(ids)):
        errors.append("duplicate capability_id")
    for item in sources:
        if not isinstance(item, dict):
            errors.append("source item must be object")
            continue
        cid = str(item.get("capability_id", "unknown"))
        if item.get("verbatim_copied_into_pod") is not False:
            errors.append(f"{cid}: verbatim_copied_into_pod must be false")
        source_hash = str(item.get("source_sha256", ""))
        if not source_hash.startswith("sha256:") or len(source_hash) != 71:
            errors.append(f"{cid}: invalid source_sha256")
        source_type = item.get("source_type")
        if source_type == "GITHUB_PINNED":
            if not item.get("source_commit") or not item.get("license_sha256"):
                errors.append(f"{cid}: pinned GitHub source lacks commit/license hash")
        elif source_type == "MARKETPLACE_PACKAGE_PINNED_BY_HASH":
            if item.get("license") != "NOT_INCLUDED_IN_DOWNLOADED_PACKAGE":
                errors.append(f"{cid}: marketplace license state is not explicit")
            if item.get("acquisition_mode") != "BEHAVIOR_ONLY_UNTIL_LICENSE_IS_EXPLICIT":
                errors.append(f"{cid}: marketplace acquisition mode is unsafe")
            if not item.get("package_sha256"):
                errors.append(f"{cid}: marketplace package hash missing")
        else:
            errors.append(f"{cid}: unsupported source_type {source_type}")
    return errors


def git_head(repo: Path) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def validate_external_sources(data: dict[str, object], source_root: Path) -> list[str]:
    errors: list[str] = []
    repos_by_commit: dict[str, Path] = {}
    for child in source_root.iterdir():
        if child.is_dir() and child.name != "lobehub":
            head = git_head(child)
            if head:
                repos_by_commit[head] = child
    for item in data["sources"]:
        cid = item["capability_id"]
        if item["source_type"] == "GITHUB_PINNED":
            repo = repos_by_commit.get(item["source_commit"])
            if repo is None:
                errors.append(f"{cid}: pinned repository not found locally")
                continue
            source = repo / item["source_path"]
            license_path = repo / item["license_path"]
            if not source.is_file() or "sha256:" + sha256(source) != item["source_sha256"]:
                errors.append(f"{cid}: source hash mismatch")
            if not license_path.is_file() or "sha256:" + sha256(license_path) != item["license_sha256"]:
                errors.append(f"{cid}: license hash mismatch")
        else:
            slug = Path(urlparse(item["download_url"]).path).parts[-2]
            package = source_root / "lobehub" / f"{slug}.zip"
            extracted = source_root / "lobehub" / slug / item["source_path"]
            if not package.is_file() or "sha256:" + sha256(package) != item["package_sha256"]:
                errors.append(f"{cid}: package hash mismatch")
            if not extracted.is_file() or "sha256:" + sha256(extracted) != item["source_sha256"]:
                errors.append(f"{cid}: extracted source hash mismatch")
    return errors


def scan_runtime_coupling(root: Path = ROOT) -> list[str]:
    hits: list[str] = []
    for name in RUNTIME_ROOT_NAMES:
        base = root / name
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
            for token in DONOR_TOKENS:
                if token.lower() in text:
                    hits.append(f"{path.relative_to(root).as_posix()}::{token}")
    return hits


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path)
    args = parser.parse_args()
    data = load_manifest()
    errors = validate_structure(data)
    coupling = scan_runtime_coupling()
    if coupling:
        errors.extend(f"runtime donor coupling: {item}" for item in coupling)
    if args.source_root:
        errors.extend(validate_external_sources(data, args.source_root))
    if errors:
        print("POD_CAPABILITY_ACQUISITION_INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    github_count = sum(1 for x in data["sources"] if x["source_type"] == "GITHUB_PINNED")
    marketplace_count = len(data["sources"]) - github_count
    print("POD_CAPABILITY_ACQUISITION_VALID")
    print(f"sources={len(data['sources'])}")
    print(f"github_pinned={github_count}")
    print(f"marketplace_pinned={marketplace_count}")
    print("donor_runtime_coupling=0")
    print(f"external_sources_verified={'true' if args.source_root else 'not_requested'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
