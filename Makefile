dev:
	pip install -e ".[dev]"
	python -c "import validator.post_install"

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
