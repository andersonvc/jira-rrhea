SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

DOCKER_REGISTRY=andersonvc
IMAGE_NAME=jira-rrhea




build: out/image-id
.PHONY: build

# Clean up the output directories; since all the sentinel files go under tmp, this will cause everything to get rebuilt
clean:
> rm -rf tmp
> rm -rf out
.PHONY: clean

run: build
> docker-compose up
.PHONY: run

test: tmp/.tests-passed.sentinel
.PHONY: test

# Docker image - re-built if the webpack output has been rebuilt
out/image-id: tmp/.tests-passed.sentinel
> mkdir -p $(@D)
> image_id="${DOCKER_REGISTRY}/${IMAGE_NAME}:latest"
> docker build --tag="$${image_id}" .
> image_id="${DOCKER_REGISTRY}/${IMAGE_NAME}:$$(pwgen -1)"
> docker build --tag="$${image_id}" .
> echo "$${image_id}" > out/image-id


# Tests - re-ran if any file under src has been changed since tmp/.tests-passed.sentinel was last touched
tmp/.tests-passed.sentinel: $(shell find src -type f)
> mkdir -p $(@D)
> poetry update
> poetry export --without-hashes -f requirements.txt > requirements.txt
> poetry run black
> poetry install
> poetry run pytest
> touch $@ 

# Webpack - re-built if the tests have been rebuilt (and so, by proxy, whenever the source files have changed)
tmp/.packed.sentinel: tmp/.tests-passed.sentinel
> mkdir -p $(@D)
> poetry build
> touch $@
