# Maturity Model

This document describes the M0–M5 maturity levels used by the SocioProphet estate, the evidence requirements for each gate, and how `Sociosphere/workspace-inventory` ingests and scores maturity records.

---

## Levels at a glance

| Level | Name | Summary |
|-------|------|---------|
| M0 | Named | Repository exists and has a name. No governance signal yet. |
| M1 | Documented | README, ownership, purpose, license/status, and a roadmap stub are present. |
| M2 | Validated | Schemas, examples, a working local validation target, and an integration map exist. |
| M3 | CI-hardened | Continuous integration validates schemas, fixtures, and maturity records. Negative fixtures confirm rejection of invalid documents. |
| M4 | Release-ready | Versioned release artifacts with checksums, SBOM or provenance attestation, and signed releases. |
| M5 | Operationally mature | Upgrade/rollback runbooks, a compatibility matrix, and an evidence export consumable by external governance tooling. |

---

## Level definitions and evidence requirements

### M0 — Named

**Gate condition:** A repository has been created.

**Required evidence:** none beyond the repository's existence.

**Typical state:** placeholder or early bootstrap.

---

### M1 — Documented

**Gate condition:** Human readers can understand the purpose, owners, and current status of the repository without external context.

**Required evidence:**

- `README.md` that states: purpose, doctrine or guiding principles, role in the wider estate, and integration links.
- At least one named owner (GitHub org or user handle) listed in `repo.maturity.yaml` under `owners`.
- `status` field set to a valid value (`active`, `experimental`, `incubating`, `archival`, or `deprecated`).
- A `nextActions` list or equivalent roadmap stub.

**Standards plane note:** For a standards repo, the README must also describe what the repo ships (contracts, schemas, docs) and what it intentionally does *not* ship (weights, secrets, runtime state).

---

### M2 — Validated

**Gate condition:** The repository's contracts are machine-readable, locally verifiable, and correctly mapped to the estate.

**Required evidence:**

- JSON Schema files present and valid (`python3 -m json.tool` passes).
- At least one positive example fixture that validates cleanly against each schema.
- A local validation command (`make validate` or equivalent) that exits `0`.
- `repo.maturity.yaml` present and validates against `schemas/repo-maturity.schema.json`.
- `integrations` list in `repo.maturity.yaml` names every upstream and downstream repository dependency.

---

### M3 — CI-hardened

**Gate condition:** A Continuous Integration workflow enforces all M2 checks automatically on every commit and pull request. Negative fixtures confirm the schema correctly rejects malformed documents.

**Required evidence:**

- A `.github/workflows/` (or equivalent CI) file that installs dependencies and runs `make validate`.
- At least two negative fixture documents for each schema, each stored under `fixtures/invalid/`, each failing validation for a documented reason.
- A negative fixture runner (`tools/run_negative_fixtures.py` or equivalent) that exits non-zero if any fixture unexpectedly passes.
- `validation.ciRequired` set to `true` and `validation.lastKnownStatus` set to `passing` in `repo.maturity.yaml`.
- Security and boundary documentation clarifying what the repository does *not* carry (model weights, runtime secrets, SourceOS image state).

---

### M4 — Release-ready

**Gate condition:** Artifacts can be versioned, verified, and attributed.

**Required evidence:**

- Tagged releases with a changelog or release notes.
- Checksums (`sha256`) or content-digest attestation for each release artifact.
- SBOM (Software Bill of Materials) or provenance record (SLSA level 1 or higher).
- Signed releases (GPG, Sigstore, or equivalent) where the signing identity is documented.

---

### M5 — Operationally mature

**Gate condition:** The repository can be safely updated, rolled back, and its contracts consumed by downstream systems in a machine-readable way.

**Required evidence:**

- Upgrade and rollback runbook (documented procedure, not just a commit message).
- Compatibility matrix specifying which version ranges of consumer repositories are supported.
- Evidence export in a format consumable by `SocioProphet/sociosphere` or `SocioProphet/workspace-inventory` (see ingestion section below).
- All M0–M4 evidence present.

---

## Evidence format in `repo.maturity.yaml`

Each evidence item in `maturity.evidence` should be a human-readable string that names a specific artifact and what it demonstrates. Examples:

```yaml
maturity:
  level: M3
  targetLevel: M4
  evidence:
    - README.md defines purpose, doctrine, role, maturity gates, and integration path.
    - schemas/repo-maturity.schema.json defines estate maturity record shape.
    - schemas/functional-service.schema.json defines functional service manifest shape.
    - .github/workflows/validate.yml runs make validate on every PR and push to main.
    - fixtures/invalid/ contains 4 negative fixtures verified by tools/run_negative_fixtures.py.
    - docs/MATURITY_MODEL.md and docs/LAB_TEMPLATE.md document standards, lab outputs, and governance.
```

Avoid vague strings like "CI is set up." Name the file and the claim.

---

## Sociosphere / workspace-inventory ingestion

`SocioProphet/sociosphere` and its companion `SocioProphet/workspace-inventory` score every registered repository against the maturity gates above. The ingestion contract works as follows:

### Pull model

`workspace-inventory` periodically fetches `repo.maturity.yaml` from the default branch of each registered repository. The file must be at the repository root and validate against `schemas/repo-maturity.schema.json` from **this** repository.

### Scorecard fields used by ingestion

| Field | Use |
|-------|-----|
| `schemaVersion` | Version gate; must be `repo-maturity.v1`. |
| `repository` | Canonical `org/repo` identifier used as the primary key. |
| `plane` | Groups repositories into estate planes for dashboards. |
| `status` | Used to filter out archival/deprecated repos from active scorecards. |
| `maturity.level` | Current maturity score rendered in the workspace scorecard. |
| `maturity.targetLevel` | Indicates roadmap intent; used for gap-analysis views. |
| `maturity.evidence` | Displayed in the repo detail page; must be non-empty at M1+. |
| `validation.ciRequired` | If `true` and `lastKnownStatus` ≠ `passing`, the repo is flagged. |
| `validation.lastKnownStatus` | Updated by CI badge push or manual update after each run. |
| `owners` | Used to attribute scorecard entries to teams or individuals. |
| `integrations` | Rendered as the estate dependency graph in Sociosphere. |

### Registering a new repository

1. Add `repo.maturity.yaml` to the root of the repository.
2. Open a pull request against `SocioProphet/workspace-inventory` that adds the `org/repo` slug to the registry manifest.
3. Sociosphere will pick up the record on the next scheduled sync (or on webhook trigger if configured).

### Keeping the record current

- Update `maturity.level` when you merge evidence that satisfies a gate.
- Set `validation.lastKnownStatus` to `passing` once CI is green; the CI workflow itself may push this update.
- Keep `nextActions` in sync with open work so the Sociosphere gap-analysis view reflects actual intent.

---

## Plane taxonomy

| Plane | Description |
|-------|-------------|
| `standards` | Contract, schema, and doctrine repositories. Ships no runtime state. |
| `runtime` | Service implementations that consume standards contracts. |
| `governance` | Promotion ledger, guardrail fabric, routing policy, agent registry. |
| `sourceos-carry` | SourceOS carry references only; no mutable model updates in OS images. |
| `socios-lab` | Modality-specific lab workspaces that emit functional service manifests. |
| `workspace-governance` | Estate registration, scorecard, and maturity telemetry. |
| `cli` | Operator command surfaces that consume standards contracts. |
| `research` | Exploratory or pre-incubation work not yet bound to estate contracts. |
| `archive` | Inactive repositories retained for historical reference. |

---

## Standards vs. other planes

| Concern | Where it lives | What this repo provides |
|---------|---------------|------------------------|
| Contract schema | **This repo** (`standards`) | `schemas/*.schema.json` |
| Maturity scorecard | **This repo** (`standards`) | `schemas/repo-maturity.schema.json`, `repo.maturity.yaml` |
| Lab experiment outputs | `socios-lab` repos | Emits `functional-service.v1` manifests per `docs/LAB_TEMPLATE.md` |
| Runtime promotion | `runtime` + `governance` repos | Consumes manifests; writes ledger evidence |
| SourceOS carry | `sourceos-carry` repos | Carry-only references, launch profiles, no weights |
| Workspace scorecard | `workspace-governance` repos | Ingests `repo.maturity.yaml`; renders dashboards |

This repository ships **contracts only**. It does not ship model weights, mutable adapters, runtime secrets, datasets, or SourceOS image state.
