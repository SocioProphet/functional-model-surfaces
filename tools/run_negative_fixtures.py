#!/usr/bin/env python3
"""Run negative fixture tests: each document must FAIL schema validation.

Each entry is a (schema_path, fixture_path, format) tuple.
The script exits non-zero if any fixture unexpectedly passes validation.
"""
import json
import sys
from pathlib import Path

try:
    import jsonschema
except Exception as exc:  # pragma: no cover
    print(f"jsonschema import failed: {exc}", file=sys.stderr)
    sys.exit(2)

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print(f"PyYAML import failed: {exc}", file=sys.stderr)
    sys.exit(2)

FIXTURES = [
    (
        "schemas/functional-service.schema.json",
        "fixtures/invalid/functional-service.missing-schema-version.json",
        "json",
    ),
    (
        "schemas/functional-service.schema.json",
        "fixtures/invalid/functional-service.invalid-status.json",
        "json",
    ),
    (
        "schemas/repo-maturity.schema.json",
        "fixtures/invalid/maturity.invalid-level.yaml",
        "yaml",
    ),
    (
        "schemas/repo-maturity.schema.json",
        "fixtures/invalid/maturity.empty-owners.yaml",
        "yaml",
    ),
]


def load(path: str, fmt: str):
    text = Path(path).read_text()
    if fmt == "yaml":
        return yaml.safe_load(text)
    return json.loads(text)


def main() -> int:
    unexpected_passes = []
    for schema_file, doc_file, fmt in FIXTURES:
        schema = json.loads(Path(schema_file).read_text())
        document = load(doc_file, fmt)
        try:
            jsonschema.validate(instance=document, schema=schema)
            unexpected_passes.append(doc_file)
            print(f"FAIL (expected validation error): {doc_file}", file=sys.stderr)
        except jsonschema.ValidationError as exc:
            print(f"ok (expected failure): {doc_file} — {exc.message}")

    if unexpected_passes:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
