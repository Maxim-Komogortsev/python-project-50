install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

setup: install build package-install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint