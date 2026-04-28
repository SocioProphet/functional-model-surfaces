# Distribution and Installability

## Position

Functional model surfaces must be installable products, not only source repositories.

Every product-facing surface must produce a versioned command-line or service binary, publish release artifacts, expose a Homebrew-installable formula, and emit local evidence proving what was installed and what service references it can invoke.

## Golden path

The default user path is one suite command surface:

```bash
brew tap SocioProphet/prophet
brew install prophet-cli
prophet doctor
prophet devtools doctor
prophet devtools profile apply ai-core
prophet sourceos carry list
prophet holmes analyze ./document.txt
```

Specialized tools may also be installed directly, but every direct tool must have an equivalent `prophet <surface>` path.

## SourceOS Developer Tools

`sourceos-devtools` is the Linux/AI-native developer tools layer for SourceOS and SocioProphet.

It is analogous in product role to Apple developer tooling, but it is built for local-first AI governance, lab profile selection, release engineering, model/service lifecycle control, and SourceOS workstation workflows.

It must install a toolchain manager and profile resolver. It must not blindly install every heavy lab dependency, dataset, or model artifact.

Initial profile families:

- `sourceos-devtools-core`: git, gh, make, jq/yq, direnv, shell integration, evidence tooling.
- `sourceos-devtools-build`: Go/Rust/Python/Node build support, release tooling, checksums, SBOM, attestations.
- `sourceos-devtools-containers`: podman/buildah, Docker-compatible hooks, devcontainers, local registry support.
- `sourceos-devtools-k8s`: kubectl, helm, kustomize, kind/k3d, local cluster hooks.
- `sourceos-devtools-ai-core`: prophet, sourceos-ai, holmes, model-router, guardrail-fabric, agent-registry.
- `sourceos-devtools-labs`: nlplab, translationlab, embeddinglab, speechlab, ocrlab, imagelab, videolab, timeserieslab, graphlab.
- `sourceos-devtools-security`: cosign, SBOM/scanning tools, secret handling, provenance, policy checks.

The user should be able to select only the profiles needed:

```bash
prophet devtools profile list
prophet devtools profile apply core,ai-core,containers
prophet lab enable image video embedding nlplab
```

SourceOS installer should also accept devtools profile selection:

```bash
prophet sourceos install --target m2 --channel dev --devtools core,ai-core,containers --labs image,video,embedding,nlplab
```

## Artifact policy

Do not commit compiled binaries into the repository as long-lived `build/` contents.

Build outputs must be produced by CI and attached to GitHub Releases or release artifact storage. Repositories may contain fixtures, examples, and generated manifests, but product binaries are release artifacts.

## Tap repository

The public install target is a Homebrew tap:

```text
SocioProphet/homebrew-prophet
```

This gives the short tap name:

```bash
brew tap SocioProphet/prophet
```

## Core formulae

Initial formulae:

- `prophet-cli`: installs the `prophet` façade command.
- `sourceos-devtools`: installs the SourceOS developer tools profile manager and lab launcher.
- `sourceos-ai`: SourceOS AI carry client and local service launcher.
- `sourceos-installer`: SourceOS installer and BootReleaseSet orchestration launcher.
- `holmes`: Holmes language intelligence CLI and local service controller.
- `model-router`: model/service routing client and policy simulator.
- `guardrail-fabric`: guardrail test and local policy evaluation CLI.
- `agent-registry`: agent spec and identity registry client.

Lab formulae are lightweight launchers. They install scaffolding and reproducible environment launchers, not large unmanaged model artifacts:

- `nlplab`
- `translationlab`
- `embeddinglab`
- `timeserieslab`
- `graphlab`

## Binary strategy

Each product repo must provide:

- CLI or service entrypoint;
- `Makefile` target `build`;
- `Makefile` target `test`;
- `Makefile` target `validate`;
- `Makefile` target `dist`;
- `Makefile` target `release-dry-run`;
- GitHub Actions release workflow;
- release checksum generation;
- SBOM generation;
- artifact attestation;
- Homebrew formula update path.

Recommended platforms:

- `darwin-arm64` for Apple Silicon;
- `darwin-amd64` where needed;
- `linux-amd64`;
- `linux-arm64`.

## Mandatory command contract

Every installable tool must implement:

```bash
<tool> --version
<tool> doctor
<tool> self-test
<tool> emit-evidence
```

`prophet` must expose façade commands for every product surface:

```bash
prophet doctor
prophet version
prophet devtools doctor
prophet devtools profile list
prophet devtools profile apply ai-core
prophet lab list
prophet lab enable image video embedding nlplab
prophet sourceos install
prophet sourceos carry list
prophet sourceos carry validate
prophet holmes analyze
prophet model route
prophet guardrail test
prophet agent registry list
```

## Distribution modes

Use the right distribution mode for the artifact:

- Homebrew formula: CLI tools and lightweight local service launchers.
- Homebrew cask: later GUI apps such as 221B workspace, if produced.
- Container image: server workloads and platform services.
- Nix package/dev shell: SourceOS and SociOS reproducible environments.
- BootReleaseSet/ReleaseSet: OS installer, recovery, rollback, and system plane artifacts.

Homebrew installs orchestrators and clients. It does not distribute raw OS images or unmanaged model artifacts.

## SourceOS rule

SourceOS installables may install clients, launchers, profile managers, cache managers, installer orchestrators, and evidence collectors.

SourceOS installables must not install mutable model lifecycle authority.

## Lab rule

SociOS lab installables may install lab CLIs and environment launchers.

Heavy training frameworks, datasets, and adapters should be pulled through signed, reproducible lab environment definitions rather than bundled into Homebrew formulae.

## Release chain

```text
source commit
  -> CI test
  -> build matrix
  -> checksums
  -> SBOM
  -> artifact attestation
  -> signed GitHub Release
  -> Homebrew formula update
  -> brew audit/test
  -> brew install
  -> doctor/self-test
  -> local evidence receipt
```

## Definition of done

A product surface is not release-ready until:

1. it has a binary or executable CLI entrypoint;
2. it publishes a GitHub Release artifact;
3. it has checksums;
4. it has an SBOM;
5. it has an artifact attestation;
6. it has a Homebrew formula;
7. `brew install` works on Apple Silicon;
8. `--version`, `doctor`, `self-test`, and `emit-evidence` commands work;
9. it emits enough local evidence to identify version, build source, platform, policy, and service references;
10. it has a rollback or previous-version recovery path when it modifies device state;
11. devtools and lab profile selection are recorded as evidence when installed through SourceOS or Prophet CLI.
