# Functional Model Surfaces Architecture

## Core thesis

Functional model surfaces are reusable capability families. They are not domain repositories and they are not application-specific feature folders.

A functional surface is the stable contract around a capability such as speech, OCR, image, video, translation, embeddings, rerank, guardrails, tools, or agents. Domains bind to those surfaces through adapters, datasets, policies, eval gates, and promotion records.

## Layer model

1. Functional foundation surface
2. Task adapter
3. Domain adapter
4. Organization, project, or user policy
5. Eval gate
6. Signed promotion
7. Runtime deployment
8. SourceOS carry reference

## Object graph

```text
FunctionalModelSurface
  -> FoundationModelRef
  -> TaskAdapter
  -> DomainAdapter
  -> DatasetArtifact
  -> TrainingRun
  -> ModelArtifact
  -> AdapterArtifact
  -> EvalRun
  -> GuardrailPolicy
  -> ToolContract
  -> KnowledgeBaseRef
  -> AgentSpec
  -> AgentIdentity
  -> RuntimeDeployment
  -> ModelRouterPolicy
  -> PromotionRecord
  -> SourceOSCarryRef
```

## Authority split

### SocioProphet

SocioProphet owns governed platform capability:

- standards and contracts;
- service catalog entries;
- runtime service manifests;
- TriTRPC and gateway bindings;
- evaluation gates;
- evidence and promotion records;
- guardrail and routing policy;
- model, adapter, dataset, tool, knowledge-base, and agent registries.

### SociOS Linux

SociOS Linux owns local lab execution:

- training and tuning experiments;
- datasets and local corpora;
- model and adapter candidates;
- workstation and accelerator integration;
- reproducible lab shells;
- local smoke tests and eval fixtures.

### SourceOS

SourceOS owns secure carriage and launch:

- clients;
- launch profiles;
- signed service references;
- ReleaseSet and BootReleaseSet wiring;
- cache policy;
- evidence collectors;
- offline-safe fallback references.

SourceOS must not become the authority for mutable model updates.

## Promotion chain

```text
lab experiment
  -> dataset evidence
  -> training or tuning evidence
  -> artifact digest
  -> eval gate
  -> guardrail policy
  -> deployment mode
  -> routing policy
  -> signed promotion
  -> SourceOS carry reference
```

## Runtime binding

Internal platform services should be TriTRPC-first. HTTP gateway routes may exist for browser and external access, but the normative internal service contract should remain typed, signed, and evidence-aware.

Recommended method families:

- `modality.speech.v1/*`
- `modality.ocr.v1/*`
- `modality.image.v1/*`
- `modality.video.v1/*`
- `modality.translation.v1/*`
- `modality.embedding.v1/*`
- `guardrail.fabric.v1/*`
- `model.router.v1/*`
- `agent.registry.v1/*`

## Non-goals

This repository does not store model binaries, mutable model update channels, domain datasets, or runtime service implementations.

Runtime implementation belongs in `SocioProphet/prophet-platform` or in explicitly designated service repos. Lab execution belongs in SociOS Linux lab repos. SourceOS carriage contracts belong in SourceOS standards and carry surfaces.
