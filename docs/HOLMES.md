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

Holmes should combine classical NLP, neural NLP, retrieval, semantic graphs, foundation language services, guardrails, evals, agent tools, and governed evidence workflows.

## Layer stack

### Layer 0: Ingestion

- file loaders;
- PDF and document extraction;
- HTML extraction;
- OCR handoff;
- transcript handoff;
- table extraction;
- metadata extraction;
- language detection.

### Layer 1: Linguistic primitives

- tokenization;
- sentence detection;
- lemmatization;
- stemming;
- part-of-speech tagging;
- morphology;
- dependency parsing;
- constituency parsing;
- named entity recognition;
- numeric and temporal normalization.

### Layer 2: Rule and table techniques

- regex and phrase matching;
- gazetteers;
- spaCy matchers and entity rulers;
- taxonomy matchers;
- table parsers;
- header detection;
- schema extraction;
- rule-based relation extraction.

### Layer 3: Classical ML NLP

- scikit-learn classifiers;
- clustering;
- topic models;
- keyword extraction;
- sentiment baselines;
- calibration;
- explainable baseline models.

### Layer 4: Neural NLP

- PyTorch pipelines;
- transformer encoders and decoders;
- token classification;
- sequence classification;
- span extraction;
- relation extraction;
- embeddings;
- rerankers;
- multilingual encoders.

### Layer 5: Foundation language services

- extraction;
- summarization;
- reasoning;
- generation;
- translation;
- text-to-SQL;
- RAG answering;
- long-context analysis;
- tool planning.

### Layer 6: Retrieval and knowledge

- sparse search;
- dense search;
- hybrid retrieval;
- rerank;
- vector stores;
- GraphBrain integration;
- semantic-serdes integration;
- ontogenesis integration;
- Sherlock Search integration;
- Slash Topics integration.

### Layer 7: Guardrails and governance

- PII and sensitive data detection;
- prompt-injection checks;
- source provenance checks;
- citation requirements;
- policy gates;
- eval gates;
- factsheets;
- promotion records.

### Layer 8: Agent and tool orchestration

- tool contracts;
- agent identity;
- session state;
- memory state;
- MCP/A2A integration;
- execution traces;
- workspace policy;
- model routing.

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
- `SocioProphet/holmes`: dedicated Holmes product repo once created.
- `SocioProphet/sherlock-search`: Watson Discovery competitor surface and investigation engine.
- `SocioProphet/prophet-platform`: runtime implementation once contracts are valid.
- `SociOS-Linux/nlplab`: local NLP lab execution and pipeline experiments once created.
- `SourceOS-Linux/sourceos-model-carry`: carry refs and on-device launch integration.

## Non-goals

Holmes must not be a loose model zoo, a single monolithic model, or a domain-specific application. It is a governed language intelligence fabric that domains consume through adapters, policies, evals, and evidence.
