# Functional Model Surfaces

Functional Model Surfaces is the normative standards home for SocioProphet functional AI capability surfaces.

This repository defines the cross-plane contracts for reusable capability families such as speech/audio, OCR/document vision, image/vision, video/temporal media, translation/multilingual, embeddings/retrieval, guardrails, tools, agents, routing, evaluation, promotion, and SourceOS carry references.

## Doctrine

Domains consume functional surfaces. Domains do not own foundation capability surfaces.

SocioProphet owns platform service contracts, catalog entries, runtime bindings, evaluation gates, evidence records, routing policy, and signed promotion state.

SociOS Linux owns local lab execution, training/tuning experiments, workstation runtime integration, accelerator integration, datasets, and candidate artifacts.

SourceOS carries service clients, launch profiles, pinned service references, ReleaseSet/BootReleaseSet wiring, cache policy, and evidence collectors. SourceOS does not carry mutable model-update authority.

## Initial surfaces

- speech/audio
- OCR/document vision
- image/vision
- video/temporal media
- translation/multilingual
- embeddings/retrieval/rerank
- safety/guardrails
- agent/tool orchestration

## Initial repo mapping

- `SocioProphet/prophet-platform`: runtime service implementation and platform records
- `SociOS-Linux/speechlab`: speech/audio lab execution
- `SociOS-Linux/ocrlab`: OCR/document vision lab execution
- `SociOS-Linux/imagelab`: image/vision lab execution
- `SociOS-Linux/videolab`: video/temporal media lab execution
- `SociOS-Linux/translationlab`: planned translation/multilingual lab execution
- `SociOS-Linux/embeddinglab`: planned embeddings/retrieval lab execution
- `SourceOS-Linux/sourceos-spec`: SourceOS carry references and conformance

## Reading order

1. `docs/ARCHITECTURE.md`
2. `docs/OWNERSHIP.md`
3. `contracts/README.md`
4. `examples/README.md`
5. `tools/README.md`

## Current phase

This repository is being bootstrapped as a standards spine. Runtime service code belongs in `SocioProphet/prophet-platform` after contracts are validated.
