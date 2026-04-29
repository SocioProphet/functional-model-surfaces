# Lab Repository Template

This document describes the required skeleton for a `SociOS-Linux/*lab` repository and the `functional-service.v1` manifest it must emit before a service can be promoted through the SocioProphet governance chain.

---

## Purpose

A lab repository is the workspace where a modality team trains, tunes, evaluates, and packages evidence for a functional AI surface. It is **not** a production service. Its outputs are manifests and evidence records that feed governance, not deployable images or model weights in the estate runtime.

---

## Required skeleton

```
<org>/<name>lab/
├── README.md                          # Purpose, modality, owners, status
├── repo.maturity.yaml                 # Maturity record (see schemas/repo-maturity.schema.json)
├── lab.manifest.json                  # Lab identity and capabilities (free-form, optional schema)
├── examples/
│   └── functional-service.example.json  # Candidate functional-service.v1 manifest
├── evals/
│   └── <eval-id>.json                 # Evaluation results referenced by the manifest
├── Makefile                           # validate, test, lint targets
├── requirements.txt                   # Python validation dependencies
└── .github/
    └── workflows/
        └── validate.yml               # CI that runs make validate
```

### README.md

Must state:

- Modality (e.g. speech, OCR, image, embedding).
- Current lab status (`experimental`, `incubating`, etc.).
- Named owner(s).
- Link to the corresponding functional service schema in `SocioProphet/functional-model-surfaces`.
- What the lab ships (evidence, manifests) and what it does **not** ship (runtime services, production secrets).

### repo.maturity.yaml

Must validate against `schemas/repo-maturity.schema.json` from `SocioProphet/functional-model-surfaces`. Minimum required fields:

```yaml
schemaVersion: repo-maturity.v1
repository: <org>/<name>lab
plane: socios-lab
status: incubating
canonicality: reference
owners:
  - <org>
maturity:
  level: M1
  targetLevel: M3
  evidence:
    - README.md states lab purpose and modality.
validation:
  commands:
    - make validate
  ciRequired: true
  lastKnownStatus: not-configured
integrations:
  - repository: SocioProphet/functional-model-surfaces
    relationship: emits functional-service.v1 manifests
    required: true
  - repository: SocioProphet/model-governance-ledger
    relationship: sends promotion evidence
    required: true
  - repository: SocioProphet/sociosphere
    relationship: registers maturity and evidence status
    required: true
```

---

## The `functional-service.v1` manifest

When a lab produces a candidate service, it emits a `functional-service.v1` JSON manifest under `examples/`. This manifest is the primary artifact passed to governance for promotion review.

### Schema reference

`schemas/functional-service.schema.json` in `SocioProphet/functional-model-surfaces`.

### Annotated example

```json
{
  "schemaVersion": "functional-service.v1",

  "service": {
    "id": "speech-transcription-baseline",
    "name": "Speech Transcription Baseline",
    "ownerRepository": "SociOS-Linux/speechlab",
    "status": "experimental",
    "description": "Whisper-based transcription surface, lab candidate."
  },

  "function": "speech",

  "model": {
    "modelRef": "oci://registry.example/socios/speech-transcription:0.1.0",
    "adapterRefs": ["oci://registry.example/socios/speech-transcription-adapter:0.1.0"],
    "runtime": "container",
    "mutableStatePolicy": "forbidden-in-sourceos"
  },

  "inputs": ["audio/wav", "audio/flac"],
  "outputs": ["application/json+transcript"],

  "evals": {
    "required": true,
    "references": ["evals/wer-baseline-001.json"],
    "minimumPromotionGate": "candidate requires signed eval and dataset provenance"
  },

  "governance": {
    "ledgerRequired": true,
    "guardrailRequired": true,
    "routingRequired": true,
    "policyRefs": ["guardrail-fabric/policies/speech-transcription-default"]
  },

  "sourceosCarry": {
    "allowed": true,
    "carriesMutableModelState": false,
    "clientRefRequired": true,
    "launchProfileRefs": ["sourceos-model-carry/launch-profiles/speech-transcription"]
  }
}
```

### Field guidance

| Field | Requirement | Notes |
|-------|-------------|-------|
| `schemaVersion` | Required, fixed | Must be exactly `"functional-service.v1"`. |
| `service.id` | Required | Lowercase alphanumeric with `_`, `.`, `-`. Stable identifier; do not change after promotion. |
| `service.ownerRepository` | Required | The lab repository in `org/repo` form. |
| `service.status` | Required | Use `draft` or `experimental` while in the lab. |
| `function` | Required | One of the enumerated functional families in the schema. |
| `model.modelRef` | Required | OCI reference or equivalent addressable digest. No inline weights. |
| `model.mutableStatePolicy` | Required | Must be `forbidden-in-sourceos` for any surface destined for SourceOS carry. |
| `inputs` / `outputs` | Required | MIME types or structured type strings. |
| `evals.required` | Required | Set to `true` for any surface that will be promoted to `candidate` or above. |
| `evals.references` | Required | At least one eval result file path (relative to the lab repo root). |
| `governance.ledgerRequired` | Required | `true` for all promoted surfaces. |
| `sourceosCarry.carriesMutableModelState` | Required | Must be `false`. The schema enforces this. |

---

## Promotion flow

A lab manifest moves through the following stages before reaching production:

```
lab experiment
  │
  ├─ dataset evidence recorded
  ├─ training / tuning run logged
  ├─ model artifact digest captured
  ├─ eval gate run and signed
  │
  └─► functional-service.v1 manifest emitted (status: experimental)
        │
        ├─ governance review in model-governance-ledger
        ├─ guardrail policy applied in guardrail-fabric
        ├─ routing policy registered in model-router
        │
        └─► manifest status promoted to candidate / approved
              │
              ├─ runtime deployment in prophet-platform
              └─ SourceOS carry reference registered in sourceos-model-carry
```

A lab **never** bypasses governance. Even if a model is technically ready, it must pass through the ledger, guardrail, and routing gate before it appears in any runtime or SourceOS carry surface.

---

## What the lab must NOT contain

| Prohibited content | Reason |
|--------------------|--------|
| Model weight files (`.bin`, `.safetensors`, `.gguf`, etc.) | Weights belong in an OCI registry, not in a git repository. |
| Production secrets or API keys | Use secret management; never commit credentials. |
| SourceOS image state | SourceOS carry refs are managed by `SourceOS-Linux/sourceos-model-carry`. |
| Runtime deployment configuration | Deployment belongs in `SocioProphet/prophet-platform`. |
| Promotion evidence written directly to the ledger | The ledger is written by governance tooling, not by the lab. |

---

## Makefile minimum

```makefile
.PHONY: validate test lint

validate: lint examples maturity

lint:
	python3 -m json.tool examples/functional-service.example.json >/dev/null

examples:
	python3 -m pip install jsonschema PyYAML -q
	python3 -c "import json, jsonschema; \
	    schema = json.load(open('schemas/functional-service.schema.json')); \
	    doc = json.load(open('examples/functional-service.example.json')); \
	    jsonschema.validate(doc, schema); print('ok')"

maturity:
	python3 -c "import json, yaml, jsonschema; \
	    schema = json.load(open('schemas/repo-maturity.schema.json')); \
	    doc = yaml.safe_load(open('repo.maturity.yaml')); \
	    jsonschema.validate(doc, schema); print('ok')"

test: validate
```

Lab repos should copy the full Makefile and validation tooling from `SocioProphet/functional-model-surfaces` for consistency. The `schemas/` directory can be kept in sync by pinning a known-good commit reference.

---

## CI minimum

```yaml
name: validate

on:
  pull_request:
  push:
    branches:
      - main

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: python -m pip install jsonschema PyYAML
      - run: make validate
```

---

## Checklist before opening a promotion PR

- [ ] `functional-service.example.json` validates against `schemas/functional-service.schema.json`.
- [ ] `repo.maturity.yaml` validates against `schemas/repo-maturity.schema.json`.
- [ ] At least one eval result is referenced and the file exists.
- [ ] `evals.required` is `true`.
- [ ] `sourceosCarry.carriesMutableModelState` is `false`.
- [ ] `service.status` is `experimental` or `candidate` (not `draft`).
- [ ] CI is green.
- [ ] No model weights, secrets, or runtime state committed to the repository.
