PACKAGE_NAME = qcs_api_client

.PHONY: style
style:
	poetry run black .
	poetry run flake8 .

.PHONY: style-check
style-check:
	poetry run black --check --diff .
	poetry run flake8 .

.PHONY: test
test:
	poetry run pytest -x tests

.PHONY: docs
docs:
	$(MAKE) -C docs html

.PHONY: watch-docs
watch-docs:
	sphinx-autobuild docs docs/_build/html
