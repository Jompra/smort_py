.PHONY: install local lint flake8 black black-fix

install: poetry-config
	poetry install

update:
	poetry update

local: install
	poetry run pre-commit install

lint: flake8 black

flake8:
	poetry run flake8

black:
	poetry run black --diff --check .

black-fix:
	poetry run black .
