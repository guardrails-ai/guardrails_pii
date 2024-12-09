dev:
	pip install -e ".[dev]"

lint:
	ruff check .

test:
	pytest ./tests

type:
	pyright validator

qa:
	make lint
	make type
	make test
