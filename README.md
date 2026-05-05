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
7. TrustOps provider libraries are runner backends and regression oracles. SocioProphet owns the receipts, gates, policy interpretation, local-first execution semantics, and runtime enforcement loop.

## Contracts in this repo

| Contract | Path | Purpose |
| --- | --- | --- |
| Repository maturity | `schemas/repo-maturity.schema.json` | Standard scorecard for repo readiness. |
| Functional service | `schemas/functional-service.schema.json` | Manifest emitted by labs and consumed by runtime/governance. |
| Prophet Foundry contract spine | `schemas/prophet-foundry-contract-spine.schema.json` | v0.1 contract spine reserving canonical names, authority repos, minimum fields, promotion flow, and must-not-own boundaries for Prophet model/data/training/eval/release/runtime contracts. |
| TrustOps receipt | `schemas/trustops-receipt.schema.json` | Evidence receipt for fairness, robustness, explanation, uncertainty, RAG, ranking, dataset, and agent-trust evaluations. |
| Trust gate policy | `schemas/trust-gate-policy.schema.json` | Policy contract that converts TrustOps receipts into allow, warn, review, quarantine, block, rollback, or revocation decisions. |
| Dataset risk manifest | `schemas/dataset-risk-manifest.schema.json` | Dataset contract for lineage, labels, protected/sensitive attributes, data boundary, consent, and risk controls. |
| Example maturity record | `examples/repo.maturity.example.yaml` | Copyable starting point for other repos. |
| Example functional service | `examples/functional-service.example.json` | Copyable service manifest fixture. |
| Example Foundry spine | `examples/prophet-foundry-contract-spine.example.json` | Copyable v0.1 Foundry contract fixture. |
| Example TrustOps receipt | `examples/trustops-receipt.art-smoke.example.json` | ART-first robustness receipt fixture for TrustOps runner integration. |
| Example TrustOps gate policy | `examples/trust-gate-policy.example.json` | Platform-default gate policy fixture for receipt-to-action mapping. |
| Example dataset risk manifest | `examples/dataset-risk-manifest.example.json` | Synthetic dataset risk fixture for fairness/privacy evaluation. |
| This repo's maturity record | `repo.maturity.yaml` | Current maturity state for this standards repo. |

## TrustOps Fabric

TrustOps Fabric turns responsible-AI libraries into enforceable platform governance. AIF360, ART, AIX360, UQ-style libraries, and future providers are isolated runners. Core platform services consume normalized receipts and policies, not provider-specific Python objects.

Start here:

- `docs/TRUSTOPS_FABRIC.md`
- `schemas/trustops-receipt.schema.json`
- `schemas/trust-gate-policy.schema.json`
- `schemas/dataset-risk-manifest.schema.json`

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

## TrustOps vertical slice

`functional-model-surfaces -> prophet-platform trustops runner -> model-governance-ledger receipt -> guardrail-fabric policy action -> model-router route/fallback/block -> agent-registry authority effect -> SourceOS local/enterprise runner -> Sociosphere trust posture`

The proof condition is also simple: a service emits a manifest, TrustOps runs an ART-first robustness profile, the ledger records the receipt, guardrails and routing consume the decision, agent authority is adjusted where required, and only signed/redacted evidence leaves local or enterprise data boundaries by default.
