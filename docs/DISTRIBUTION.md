# Distribution and Installability

## Position

Functional model surfaces must be installable products, not only source repositories.

Every product-facing surface should produce a versioned command-line or service binary, publish release artifacts, and expose a Homebrew-installable formula through the SocioProphet tap.

## Artifact policy

Do not commit compiled binaries into the repository as long-lived `build/` contents.

Build outputs should be produced by CI and attached to GitHub Releases or release artifact storage. Repositories may contain fixtures, examples, and generated manifests, but product binaries should be release artifacts.

## Install surfaces

The public install target should be a Homebrew tap:

```bash
brew tap SocioProphet/prophet
brew install holmes
brew install sourceos-ai
brew install prophet-cli
```

The initial tap repository should be:

```text
SocioProphet/homebrew-prophet
```

This provides the short tap name:

```text
SocioProphet/prophet
```

## Product formulae

Initial formulae should include:

- `holmes`: Holmes language intelligence CLI and local service controller.
- `sourceos-ai`: SourceOS AI carry client and local service launcher.
- `prophet-cli`: Prophet platform operator CLI.
- `model-router`: model/service routing client and policy simulator.
- `guardrail-fabric`: guardrail test and local policy evaluation CLI.
- `agent-registry`: agent spec and identity registry client.

Lab formulae should be lightweight. They should install scaffolding and reproducible environment launchers, not large unmanaged model artifacts.

- `nlplab`
- `translationlab`
- `embeddinglab`
- `timeserieslab`
- `graphlab`

## Binary strategy

Each product repo should provide:

- `cmd/<name>/` or equivalent CLI entrypoint;
- `Makefile` target `build`;
- `Makefile` target `test`;
- `Makefile` target `dist`;
- GitHub Actions release workflow;
- release checksum generation;
- Homebrew formula update path.

Recommended platforms:

- `darwin-arm64` for Apple Silicon;
- `darwin-amd64` where needed;
- `linux-amd64`;
- `linux-arm64`.

## SourceOS rule

SourceOS installables may install clients, launchers, profile managers, cache managers, and evidence collectors.

SourceOS installables must not install mutable model lifecycle authority.

## Lab rule

SociOS lab installables may install lab CLIs and environment launchers.

Heavy training frameworks, model artifacts, datasets, and adapters should be pulled through signed, reproducible lab environment definitions rather than bundled into Homebrew formulae.

## Release chain

```text
source commit
  -> CI build
  -> tests
  -> signed release artifacts
  -> checksums
  -> Homebrew formula update
  -> brew install
  -> local evidence receipt
```

## Definition of done

A product surface is not release-ready until:

1. it has a binary or executable CLI entrypoint;
2. it publishes a GitHub Release artifact;
3. it has checksums;
4. it has a Homebrew formula;
5. `brew install` works on Apple Silicon;
6. `--version` and `doctor` commands work;
7. it emits enough local evidence to identify version, build source, and service references.
