SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules


BACKEND_IMAGE="andersonvc/jirarrhea-backend:latest"
FRONTEND_IMAGE="andersonvc/jirarrhea-frontend:latest"


build: deployments/artifacts/backend-image-id deployments/artifacts/frontend-image-id
.PHONY: build

# Clean up the output directories; since all the sentinel files go under tmp, this will cause everything to get rebuilt
clean:
	rm -rf deployments/artifacts
	mkdir deployments/artifacts
.PHONY: clean

run: build
	docker-compose up
.PHONY: run

backend: 
	poetry run uvicorn src.backend.main:app --host 0.0.0.0 --reload --port 5555
.PHONY: backend

frontend: 
	cd frontend 
	yarn serve
.PHONY: frontend

test: tmp/.tests-passed.sentinel
.PHONY: test

init:
	cd frontend
	sudo yarn add @vue/cli-service
	sudo npm install .
	cd ..
	cd backend 
	pyenv local 3.8.5
	cd ..

# Tests - re-ran if any file under src has been changed since tmp/.tests-passed.sentinel was last touched
deployments/artifacts/.backend-tests-passed.sentinel: $(shell find backend -type f)
	mkdir -p $(@D)
	cd backend 
	poetry update
	poetry export --without-hashes -f requirements.txt > requirements.txt
	poetry run black
	poetry install
	poetry run pytest
	cd ..
	touch $@ 

# Docker image - re-built if the test output has been rebuilt
deployments/artifacts/backend-image-id: deployments/artifacts/.backend-tests-passed.sentinel
	mkdir -p $(@D)
	docker build --tag="${BACKEND_IMAGE}" ./backend
	echo "${BACKEND_IMAGE}" > deployments/artifacts/backend-image-id



# Docker image - re-built if the webpack output has been rebuilt
deployments/artifacts/frontend-image-id: $(shell find frontend/src -type f)
	mkdir -p $(@D)
	docker build --tag="${FRONTEND_IMAGE}" ./frontend
	echo "${FRONTEND_IMAGE}" > deployments/artifacts/frontend-image-id
 
