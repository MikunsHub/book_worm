COMPOSE_FILE=docker-compose.yml
SHARED_FOLDER := $(shell dirname "$(realpath $(lastword $(MAKEFILE_LIST)))")/../shared
BACKEND_LIBRARY_FOLDER := $(shell dirname "$(realpath $(lastword $(MAKEFILE_LIST)))")/library
FILES_TO_COPY := database
include env.local

docker-run:
	docker-compose -f ${COMPOSE_FILE} up -d

docker-clean:
	docker-compose -f ${COMPOSE_FILE} down

docker-respawn:
	docker rm -f postgres_container && docker-compose -f ${COMPOSE_FILE} up -d postgres

copy-shared:
	@rm -rf "$(BACKEND_LIBRARY_FOLDER)"
	@mkdir -p "$(BACKEND_LIBRARY_FOLDER)"
	@for item in $(FILES_TO_COPY); do \
		cp -R "$(SHARED_FOLDER)/$$item" "$(BACKEND_LIBRARY_FOLDER)/"; \
	done
	@touch "$(BACKEND_LIBRARY_FOLDER)/__init__.py"
	@echo "Selected files and folders copied to backend project..."
	@echo "\033[0;31mWARNING\033[0m: DO NOT EDIT THE COPIED LIBRARY FOLDER DIRECTLY!!, THIS DELETES ON EVERY RESTART!!"

run-local:
	$(MAKE) copy-shared
	set -a && . ./env.local && pipenv run dev

test:
	pipenv run lint
	pipenv run type-check
	set -a && . ./env.local && pipenv run test

quick-test:
	# Pass ISOLATED_TEST env var to run a single test f.e. tests/unit/test_centurion.py::test_fetch_recent_data
	set -a && . ./env.local && pipenv run test ${ISOLATED_TEST}

auto-format:
	pipenv run ruff-fix
	pipenv run ruff-format
	pipenv run ruff
