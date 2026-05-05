.PHONY: validate test lint examples maturity negatives

validate: lint examples maturity negatives

lint:
	python3 -m json.tool schemas/repo-maturity.schema.json >/dev/null
	python3 -m json.tool schemas/functional-service.schema.json >/dev/null
	python3 -m json.tool schemas/prophet-foundry-contract-spine.schema.json >/dev/null
	python3 -m json.tool schemas/trustops-receipt.schema.json >/dev/null
	python3 -m json.tool schemas/trust-gate-policy.schema.json >/dev/null
	python3 -m json.tool schemas/dataset-risk-manifest.schema.json >/dev/null
	python3 -m json.tool examples/functional-service.example.json >/dev/null
	python3 -m json.tool examples/prophet-foundry-contract-spine.example.json >/dev/null
	python3 -m json.tool examples/trustops-receipt.art-smoke.example.json >/dev/null
	python3 -m json.tool examples/trust-gate-policy.example.json >/dev/null
	python3 -m json.tool examples/dataset-risk-manifest.example.json >/dev/null

examples:
	python3 tools/validate_json.py schemas/functional-service.schema.json examples/functional-service.example.json
	python3 tools/validate_json.py schemas/prophet-foundry-contract-spine.schema.json examples/prophet-foundry-contract-spine.example.json
	python3 tools/validate_json.py schemas/trustops-receipt.schema.json examples/trustops-receipt.art-smoke.example.json
	python3 tools/validate_json.py schemas/trust-gate-policy.schema.json examples/trust-gate-policy.example.json
	python3 tools/validate_json.py schemas/dataset-risk-manifest.schema.json examples/dataset-risk-manifest.example.json

maturity:
	python3 tools/validate_maturity.py schemas/repo-maturity.schema.json repo.maturity.yaml

negatives:
	python3 tools/run_negative_fixtures.py

test: validate
