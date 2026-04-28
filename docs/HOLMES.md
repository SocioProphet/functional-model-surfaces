# Holmes

Holmes is the SocioProphet language intelligence fabric.

Holmes exists to outgrow assistant-grade discovery. It is not a chatbot wrapper and it is not a domain-specific NLP repo. It is the governed language layer above search, retrieval, linguistic analysis, semantic graph conversion, agents, tools, evals, and evidence-first discovery.

## Product line

- **Holmes**: language intelligence fabric.
- **Sherlock Search**: discovery, retrieval, evidence search, and investigation engine.
- **221B**: casefile and workspace surface.
- **Mycroft**: model routing, policy intelligence, and strategic selection.
- **Moriarty Bench**: adversarial eval and red-team harness.
- **Irene Shield**: privacy, masking, identity-sensitive redaction, and sensitive-context handling.
- **The Canon**: curated evidence corpus, provenance records, accepted facts, and source trust.
- **Deduction Engine**: synthesis, contradiction detection, claim extraction, fallacy analysis, and reasoning workflows.

## Positioning

Watson-style systems answer. Holmes investigates.

Holmes combines classical NLP, neural NLP, retrieval, semantic graphs, foundation language services, guardrails, evals, agent tools, and governed evidence workflows.

## Layer stack

1. ingestion;
2. linguistic primitives;
3. rule and table techniques;
4. classical ML NLP;
5. neural NLP;
6. foundation language services;
7. retrieval and knowledge;
8. guardrails and governance;
9. agent and tool orchestration.

## Method families

Internal methods should be TriTRPC-first. Gateway routes can exist for browser and external clients.

Recommended method families:

- `language.primitive.v1/Analyze`
- `language.entity.v1/Extract`
- `language.relation.v1/Extract`
- `language.classify.v1/Classify`
- `language.embed.v1/Embed`
- `language.rerank.v1/Rerank`
- `language.translate.v1/Translate`
- `language.summarize.v1/Summarize`
- `language.rag.v1/Answer`
- `language.graph.v1/ToSemanticGraph`
- `language.govern.v1/Evaluate`

## Repo placement

- `SocioProphet/functional-model-surfaces`: normative surface and object standards.
- `SocioProphet/holmes`: Holmes product repo and CLI/service surface.
- `SocioProphet/sherlock-search`: discovery, retrieval, evidence search, and investigation engine.
- `SocioProphet/prophet-core-query`: governed shared query contracts.
- `SocioProphet/prophet-platform`: runtime implementation once contracts are valid.
- `SociOS-Linux/nlplab`: local NLP lab execution and pipeline experiments.
- `SourceOS-Linux/sourceos-model-carry`: carry refs and on-device launch integration.

## Non-goals

Holmes must not become a loose model zoo, a single monolithic model, or a domain-specific application. It is a governed language intelligence fabric that domains consume through adapters, policies, evals, and evidence.
