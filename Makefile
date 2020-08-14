SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules


DOCKER_REGISTRY=andersonvc
BE_IMAGE_NAME=jira-rrhea-be
BACKEND_IMAGE_ID="${DOCKER_REGISTRY}/${BE_IMAGE_NAME}:latest"

FE_IMAGE_NAME=jira-rrhea-fe
FRONTEND_IMAGE_ID="${DOCKER_REGISTRY}/${FE_IMAGE_NAME}:latest"


build: out/image-id out/fe-image-id
.PHONY: build

# Clean up the output directories; since all the sentinel files go under tmp, this will cause everything to get rebuilt
clean:
	rm -rf tmp
	rm -rf out
.PHONY: clean

run: build
	docker-compose up
.PHONY: run

backend: 
	poetry run uvicorn src.backend.main:app --host 0.0.0.0 --reload --port 5555
.PHONY: backend

frontend: 
	cd src/vue-frontend && yarn serve
.PHONY: frontend

test: tmp/.tests-passed.sentinel
.PHONY: test

# Docker image - re-built if the webpack output has been rebuilt
out/image-id: tmp/.tests-passed.sentinel
	mkdir -p $(@D)
	docker build --tag="${BACKEND_IMAGE_ID}" .
	echo "${BACKEND_IMAGE_ID}" > out/image-id


# Tests - re-ran if any file under src has been changed since tmp/.tests-passed.sentinel was last touched
tmp/.tests-passed.sentinel: $(shell find src -type f)
	mkdir -p $(@D)
	poetry update
	poetry export --without-hashes -f requirements.txt > requirements.txt
	poetry run black
	poetry install
	poetry run pytest
	touch $@ 

# Webpack - re-built if the tests have been rebuilt (and so, by proxy, whenever the source files have changed)
tmp/.packed.sentinel: tmp/.tests-passed.sentinel
	mkdir -p $(@D)
	poetry build
	touch $@


# Docker image - re-built if the webpack output has been rebuilt
out/fe-image-id: $(shell find src/frontend -type f)
	mkdir -p $(@D)
	docker build --tag="${FRONTEND_IMAGE_ID}" ./src/vue-frontend
	echo "${FRONTEND_IMAGE_ID}" > out/fe-image-id
 