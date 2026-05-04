# Prophet Intelligence Foundry v0.1

Status: Draft contract spine

## Purpose

The Prophet Intelligence Foundry is the contract-first program plane for turning model work into auditable, governable, SourceOS-carryable intelligence services.

It is not a runtime router, workspace controller, chat UI, or model-weight repository. It defines how model families, data manifests, training runs, post-training runs, reward models, evals, safety reports, interpretability reports, release decisions, runtime reasoning plans, tool contracts, capability grants, run capsules, and Agent Machine receipts connect across the SocioProphet and SourceOS estate.

## Boundary statement

- `functional-model-surfaces` defines the contracts.
- `model-governance-ledger` records evidence, factsheets, evals, release decisions, rollback records, and compliance state.
- `model-router` selects governed model/service routes at runtime.
- `guardrail-fabric` applies safety and runtime governance around models, agents, tools, RAG packages, and knowledge bases.
- `sourceos-model-carry` carries approved service references, launch profiles, cache policy, fallback references, ReleaseSet and BootReleaseSet bindings, and evidence collectors.
- `agent-machine` owns machine-local runtime probing, inference providers, model residency, cache-aware scheduling facts, AgentPod envelopes, and AgentMachineReceipt evidence.
- `agentplane` owns validated execution, run capsules, replay, and evidence capture.
- `sociosphere` owns workspace state and materialization. It does not own cognitive routing or model release governance.

## v0.1 contract families

The v0.1 schema intentionally starts as a contract spine rather than full final schemas for every object. The goal is to reserve canonical names, repository authority, minimum fields, and must-not-own boundaries before runtime code grows around unstable assumptions.

Required families:

- `ModelSpec`
- `ModelFamilySpec`
- `AdapterSpec`
- `DatasetSpec`
- `DataManifest`
- `TrainingRun`
- `PostTrainingRun`
- `RewardModelSpec`
- `EvalSuite`
- `EvalReport`
- `SafetyReport`
- `InterpretabilityReport`
- `ModelReleaseDecision`
- `ReasoningRuntimePlan`
- `ModelRoutingDecision`
- `MemoryRoutingPlan`
- `ToolContract`
- `CapabilityGrant`
- `WorkspaceLease`
- `RunCapsule`
- `AgentMachineReceipt`
- `ModelResidency`
- `InferenceProvider`
- `ContextBundle`
- `VerifierQuorum`

## Promotion law

A lab candidate is not a product service until it passes the foundry path:

```text
lab manifest
→ data manifest
→ eval report
→ safety / guardrail review
→ model governance ledger release decision
→ model-router admission
→ sourceos-model-carry approved reference
→ agent-machine runtime placement evidence
→ agentplane run capsule
→ SourceOS/operator surface readout
```

## Runtime law

Runtime work must preserve this split:

```text
Model Mesh routes.
Policy Fabric authorizes.
AgentPlane executes.
Agent Machine places and proves local runtime facts.
Sociosphere materializes workspace state.
TurtleTerm, BearBrowser, AgentTerm, sourceosctl, and SourceOS Shell expose operator surfaces.
model-governance-ledger records durable release and evidence state.
```

## What v0.1 deliberately does not do

- It does not ship model weights.
- It does not define a training framework implementation.
- It does not grant authority to any agent or tool.
- It does not create SourceOS boot or carry state.
- It does not replace existing `functional-service.v1` manifests.
- It does not make `smart-tree` or any MCP tool trusted by default.

## Acceptance criteria

The initial contract spine is valid when:

1. `schemas/prophet-foundry-contract-spine.schema.json` is valid JSON Schema.
2. `examples/prophet-foundry-contract-spine.example.json` validates against it.
3. `make validate` checks the new schema and example.
4. The README advertises the contract family without implying runtime readiness.
5. Downstream repos can reference the reserved contract family names without inventing competing names.
