# TrustOps Fabric

TrustOps Fabric is the SocioProphet control-plane pattern for turning responsible-AI toolkits into enforceable platform governance.

The platform does not vendor a research toolkit as its architecture. AIF360, ART, AIX360, UQ360, and future providers are runner backends. SocioProphet owns the contracts, receipts, policy gates, local-first execution semantics, model-router controls, guardrail actions, ledger records, and agent-authority effects.

## First-class contracts

| Contract | Path | Purpose |
| --- | --- | --- |
| TrustOps receipt | `schemas/trustops-receipt.schema.json` | Canonical evidence receipt for fairness, robustness, explanation, uncertainty, RAG, ranking, dataset, and agent-trust evaluations. |
| Trust gate policy | `schemas/trust-gate-policy.schema.json` | Converts receipts into allow, warn, review, quarantine, block, rollback, or revocation decisions. |
| Dataset risk manifest | `schemas/dataset-risk-manifest.schema.json` | Declares lineage, label semantics, protected/sensitive attribute handling, data boundary, consent, and risk controls. |

## Provider strategy

Provider libraries are isolated runners, not core dependencies.

| Provider | Role |
| --- | --- |
| `trustops-art-runner` | Adversarial robustness, privacy leakage, extraction, inference, poisoning, evasion, prompt/tool/memory attack probes. |
| `trustops-aif360-runner` | Fairness metrics, subgroup scans, counterfactual fairness, ranking fairness, and mitigation comparison. |
| `trustops-aix360-runner` | Explanation generation, explanation quality, local/global and direct/post-hoc explanation evidence. |
| `trustops-uq-runner` | Uncertainty, calibration, abstention, fallback, and human-review signals. |
| `socioprophet-trust-kernel` | Small deterministic in-house metric and policy evaluator used for core checks and regression comparisons. |

## Control loop

1. A lab, model, adapter, RAG package, tool, agent, or functional service emits a manifest.
2. TrustOps selects provider runners from policy and data boundary.
3. Runners execute locally, in CI, in SourceOS, or in enterprise-controlled infrastructure.
4. Runners emit normalized TrustOps receipts.
5. `model-governance-ledger` records immutable receipts and factsheet evidence.
6. `guardrail-fabric` converts receipts into runtime controls.
7. `model-router` routes, falls back, blocks, or escalates.
8. `agent-registry` reduces, revokes, or restores tool grants, memory access, and runtime authority.
9. Sociosphere/workspace governance records maturity and operational posture.

## Non-negotiable invariants

- Core platform services consume receipts, not provider-specific Python objects.
- Raw regulated, personal, or customer-controlled data must not leave its boundary by default.
- Promotion requires current receipts for every required TrustOps gate.
- A failing robustness or privacy gate may quarantine or block deployment.
- A failing fairness gate blocks high-risk promotion unless an explicit governed waiver exists.
- High uncertainty must trigger fallback, abstention, or human review where policy requires it.
- Agent authority must be tied to trust posture, not static registration alone.
- Factsheets must be generated from evidence receipts, not manually maintained prose.

## Initial vertical slice

The first implementation lane is ART-first:

1. Add `robustness` support through `trustops-receipt.v1`.
2. Implement `trustops-art-runner` in `SocioProphet/prophet-platform`.
3. Record receipts in `SocioProphet/model-governance-ledger`.
4. Map receipt status to runtime controls in `SocioProphet/guardrail-fabric`.
5. Apply agent-authority impact in `SocioProphet/agent-registry`.
6. Expose a CLI/API path such as:

```bash
prophet trustops run --profile art-smoke --manifest examples/functional-service.example.json
```

## Build versus integrate

Trusted-AI libraries are useful as backends and regression oracles. They should not own the SocioProphet architecture.

Build ourselves:
- Schemas and receipts.
- Gate policy semantics.
- Ledger integration.
- Router and guardrail enforcement.
- Agent authority controls.
- SourceOS/local-first runner model.
- Deterministic trust kernel for stable core metrics.

Integrate selectively:
- ART for adversarial robustness coverage.
- AIF360 for fairness metric and mitigation breadth.
- AIX360 for explanation algorithms and taxonomy.
- UQ-style libraries for uncertainty methods where useful.

The long-term goal is a sovereign TrustOps Fabric: measure, explain, record, enforce, route, revoke, rollback, and improve.
