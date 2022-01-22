# main module
SRC := ./radium
RUN_MODULE := $(SRC)/__main__.py
# run commands in virtual environment
BIN := poetry run

help: $(eval SHELL:=/bin/bash) # Help (target description).
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%-15s %s\n" "target" "help" ; \
	printf "%-15s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-15s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done

cz: ## Check commit message `make cz m="commit_message"`.
	$(BIN) $@ check -m "$m"

hook: ## Install pre-commint hook `make m="hook_name"`.
	$(BIN) pre-commit install --hook-type "$m"

isort: ## Format imports with isort.
	$(BIN) $@ $(SRC)

black: ## Format style with black.
	$(BIN) $@ $(SRC)

style: ## Check style with flake8.
	$(BIN) flake8 $(SRC)

mypy: ## Check types with mypy.
	$(BIN) $@ $(SRC)

check: ## Check all (imports, styles, typos).
	make -j4 isort black style mypy

test: ## Test with pytest and measure code with coverage (and report).
	$(BIN) coverage run --source=. -m pytest .
	$(BIN) coverage report -m

all: ## All checks and tests.
	make check test

run: ## Run this project.
	$(BIN) python3 $(RUN_MODULE)
