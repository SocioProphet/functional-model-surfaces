# Distribution and Installability

## Position

Functional model surfaces must become installable, testable product surfaces. A repo is not product-grade until it can produce validated artifacts, a command or service entrypoint, and evidence proving what was built and installed.

## Golden path

```bash
brew tap SocioProphet/prophet
brew install prophet-cli
prophet doctor
prophet devtools profile list
prophet sourceos carry list
prophet holmes analyze ./document.txt
```

Specialized binaries may exist, but every product path should also be available through `prophet`.

## Core formulae

Initial Homebrew targets:

- `prophet-cli`
- `sourceos-ai`
- `holmes`
- `sourceos-devtools`
- `sourceos-installer`
- `model-router`
- `guardrail-fabric`
- `agent-registry`

Lab formulae are lightweight launchers and environment selectors, not bundles of large artifacts:

- `nlplab`
- `translationlab`
- `embeddinglab`
- `timeserieslab`
- `graphlab`
- `imagelab`
- `speechlab`
- `ocrlab`
- `videolab`

## SourceOS Developer Tools

`sourceos-devtools` is the Linux/AI-native developer tools layer for SourceOS and SocioProphet.

It installs a governed profile manager and lab launcher. It must not blindly install every heavy dependency, dataset, or model artifact.

Initial profile families:

- `core`
- `build`
- `containers`
- `k8s`
- `ai-core`
- `labs`
- `security`

## Mandatory command contract

Every installable tool should implement:

```bash
<tool> --version
<tool> doctor
<tool> self-test
<tool> emit-evidence
```

`prophet` should expose facade commands for every product surface:

```bash
prophet doctor
prophet version
prophet devtools profile list
prophet lab list
prophet sourceos install
prophet sourceos carry validate
prophet holmes analyze
prophet model route
prophet guardrail test
prophet agent registry list
```

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
  -> local evidence receipt
```

## Artifact policy

Do not commit long-lived compiled binaries into source repositories. Build outputs belong in CI artifacts, signed releases, or release storage.

## SourceOS rule

SourceOS may carry clients, launchers, profile managers, cache managers, installer orchestrators, signed service references, and evidence collectors.

SourceOS must not carry mutable model lifecycle authority.

## Definition of done

A product surface is not release-ready until:

1. it has a command or service entrypoint;
2. validation passes in CI;
3. release artifacts are checksummed;
4. SBOM/provenance exists;
5. evidence output exists;
6. install path is documented;
7. rollback or recovery behavior is described where state changes occur.
