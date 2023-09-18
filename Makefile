build:
	poetry build

package-install:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/hexlet_code-0.1.0-py3-none-any.whl
	
lint:
	poetry run flake8 gendiff

test:
	poetry run pytest --strict-markers --cov 
