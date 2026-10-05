#!/usr/bin/env python3
"""Run the immutable V003 validator while allowing later explicitly scoped DOCSETs.

This wrapper does not change V003 canonical content or its manifest. It only
prevents the historical single-active-set check from treating ACTIVE documents
that explicitly belong to another DOCSET as contamination of V003.
"""

from __future__ import annotations

import validate_docs as legacy


def validate_single_active_set_scoped(errors: list[str]) -> None:
    active_paths = {
        document.path for document in legacy.CANONICAL if document.status == "ACTIVE"
    }
    for path in (legacy.ROOT / "docs").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if legacy.metadata_value(text, "Status") != "ACTIVE":
            continue

        relative = path.relative_to(legacy.ROOT).as_posix()
        if relative in active_paths:
            continue

        declared_set = (
            legacy.metadata_value(text, "Conjunto")
            or legacy.metadata_value(text, "Conjunto alvo")
        )
        if declared_set and declared_set != legacy.DOCSET_ID:
            continue

        errors.append(f"documento ACTIVE fora do manifesto V003: {relative}")


legacy.validate_single_active_set = validate_single_active_set_scoped

if __name__ == "__main__":
    raise SystemExit(legacy.main())
