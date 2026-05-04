# Functional Model Surfaces

Functional Model Surfaces is the SocioProphet standards spine for governed model, adapter, dataset, evaluation, guardrail, tool, agent, routing, promotion, and SourceOS carry contracts.

This repository defines contracts. It does not ship model weights, mutable adapters, runtime secrets, or SourceOS image state.

## Role in the estate

The SocioProphet roadmap calls for AI/NLP collaboration, a community model zoo, prebuilt AI-as-a-Service models, reproducible project artifacts, knowledge engineering, and a central cloud-to-edge AI surface. This repository is the standards layer that lets those product surfaces become auditable software instead of disconnected experiments.

| Plane | Repositories | Role |
| --- | --- | --- |
| Standards | `SocioProphet/functional-model-surfaces` | Functional AI surface contracts and maturity gates. |
| Runtime | `SocioProphet/prophet-platform` | Graduated service implementation home. |
| CLI | `SocioProphet/prophet-cli` | User/operator command surface that consumes these contracts. |
| Governance | `SocioProphet/model-governance-ledger`, `SocioProphet/guardrail-fabric`, `SocioProphet/model-router`, `SocioProphet/agent-registry` | Promotion, policy, routing, guardrails, and agent authority. |
| OS carry | `SourceOS-Linux/sourceos-model-carry` | Carry-only references for SourceOS; no mutable model updates in OS images. |
| Local runtime | `SourceOS-Linux/agent-machine` | Machine-local runtime probing, inference provider lifecycle, model residency, cache-aware scheduling facts, AgentPod placement, and receipts. |
| Labs | `SociOS-Linux/*lab` | Modality-specific workspaces that emit functional service manifests. |
| Workspace governance | `SocioProphet/sociosphere`, `SocioProphet/workspace-inventory` | Estate registration, validation, and maturity telemetry. |

## Doctrine

1. Foundation surfaces are organized by function first, then tuned for domain use.
2. Lab repos may train, tune, evaluate, and package evidence, but promotion requires governance.
3. SourceOS carries service references, launch profiles, cache policy, and refusal gates; it does not carry mutable model updates.
4. Every functional service must be auditable through datasets, adapters, evals, guardrails, routing policy, and ledger evidence.
5. Every active repo must emit a maturity record consumable by Sociosphere/workspace governance.
6. Prophet Intelligence Foundry contracts are lifecycle contracts. They do not make this repository a training runtime, model-weight store, or workspace controller.

## Contracts in this repo

| Contract | Path | Purpose |
| --- | --- | --- |
| Repository maturity | `schemas/repo-maturity.schema.json` | Standard scorecard for repo readiness. |
| Functional service | `schemas/functional-service.schema.json` | Manifest emitted by labs and consumed by runtime/governance. |
| Prophet Foundry contract spine | `schemas/prophet-foundry-contract-spine.schema.json` | v0.1 contract spine reserving canonical names, authority repos, minimum fields, promotion flow, and must-not-own boundaries for Prophet model/data/training/eval/release/runtime contracts. |
| Example maturity record | `examples/repo.maturity.example.yaml` | Copyable starting point for other repos. |
| Example functional service | `examples/functional-service.example.json` | Copyable service manifest fixture. |
| Example Foundry spine | `examples/prophet-foundry-contract-spine.example.json` | Copyable v0.1 Foundry contract fixture. |
| This repo's maturity record | `repo.maturity.yaml` | Current maturity state for this standards repo. |

## Maturity gates

| Level | Meaning |
| --- | --- |
| M0 | Named repo only. |
| M1 | README, purpose, ownership, license/status, roadmap. |
| M2 | Schemas, examples, validation target, integration map. |
| M3 | CI, tests, fixtures, security docs, integration evidence. |
| M4 | Release artifacts, checksums, SBOM/provenance, signed releases. |
| M5 | Operational readiness, upgrade/rollback, compatibility matrix, evidence export. |

## Local validation

```bash
make validate
```

## First vertical slice

`functional-model-surfaces -> lab repo -> model-governance-ledger -> model-router -> guardrail-fabric -> agent-registry -> sourceos-model-carry -> agent-machine -> agentplane -> sociosphere`

The proof condition is simple: a lab emits a functional service manifest, governance validates it, SourceOS carries the approved reference, Agent Machine proves runtime placement, AgentPlane captures run evidence, and Sociosphere records maturity/evidence for the whole path.
