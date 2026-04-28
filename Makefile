.PHONY: validate test lint examples maturity

validate: lint examples maturity

lint:
	python3 -m json.tool schemas/repo-maturity.schema.json >/dev/null
	python3 -m json.tool schemas/functional-service.schema.json >/dev/null
	python3 -m json.tool examples/functional-service.example.json >/dev/null

examples:
	python3 tools/validate_json.py schemas/functional-service.schema.json examples/functional-service.example.json

maturity:
	python3 tools/validate_maturity.py schemas/repo-maturity.schema.json repo.maturity.yaml

test: validate
