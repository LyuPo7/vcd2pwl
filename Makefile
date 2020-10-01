install:
	poetry install

test:
	poetry run pytest -vv --cov=vcd2pwl --cov-report xml tests/tests.py

lint:
	poetry run flake8 vcd2pwl --show-source --ignore=T001,I001,WPS342,E131,WPS211,WPS210,WPS318 --verbose

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

.PHONY: install test lint selfcheck check build
