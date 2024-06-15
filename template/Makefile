.PHONY: install clean format test check api build doc docker

## Install for production
install:
	@echo ">> Installing dependencies"
	@python -m pip install --upgrade pip
	@python -m pip install -e .
	@echo ">> Successfully installed! `{{ python_package_name }} --help`"

## Install for development
install-dev: install
	@python -m pip install -e ".[dev]"
	@pre-commit install

## Delete all temporary files
clean:
	@rm -rf .ipynb_checkpoints
	@rm -rf **/.ipynb_checkpoints
	@rm -rf .mypy_cache
	@rm -rf .ruff_cache
	@rm -rf .pytest_cache
	@rm -rf **/.pytest_cache
	@rm -rf __pycache__
	@rm -rf **/__pycache__
	@rm -rf build
	@rm -rf dist
	@rm -rf docs
	@rm -rf .coverage

## Format files using Ruff
format:
	@ruff check . --fix
	@ruff format .

## Run tests
test:
	@pytest -v --cov --cov-report term-missing:skip-covered --disable-pytest-warnings

## Run checks (ruff + test)
check:
	@ruff check .
	@ruff format --check .
	@mypy . --ignore-missing-imports --install-types --non-interactive

## Run api
api:
	@python -m uvicorn src.{{ python_package_name }}.api.main:app --reload

## Build using pip-tools
build:
	@python -m pip install --upgrade pip
	@python -m pip install --upgrade pip-tools
	@pip-compile --output-file=requirements.txt pyproject.toml --strip-extras
	@pip-compile --extra=dev --output-file=requirements-dev.txt pyproject.toml --strip-extras
	@pip wheel --no-deps . --wheel-dir dist

## Build the documentation
doc:
	PYTHONPATH=./src pdoc --math ./src -o ./docs

## Build the docker image
docker:
	docker build -f Dockerfile -t boilerplate .

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available commands:$$(tput sgr0)"
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
