SHELL:=bash
.ONESHELL:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

.PHONY: regression
regression: ## Runs regression tests via Docker Compose
	./scripts/compose-runner.sh '-f docker-compose.yml' --abort-on-container-exit

