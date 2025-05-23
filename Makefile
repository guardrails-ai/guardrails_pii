dev:
	pip install -e ".[dev]"
	python validator/post-install.py

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
