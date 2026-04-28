#!/usr/bin/env python3
"""Validate a JSON document against a JSON Schema."""
import json
import sys
from pathlib import Path

try:
    import jsonschema
except Exception as exc:  # pragma: no cover
    print(f"jsonschema import failed: {exc}", file=sys.stderr)
    sys.exit(2)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: validate_json.py <schema.json> <document.json>", file=sys.stderr)
        return 2
    schema_path = Path(sys.argv[1])
    doc_path = Path(sys.argv[2])
    schema = json.loads(schema_path.read_text())
    document = json.loads(doc_path.read_text())
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.validate(instance=document, schema=schema)
    print(f"ok: {doc_path} validates against {schema_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
