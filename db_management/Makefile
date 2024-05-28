COMPOSE_FILE=docker-compose.yml

include env.local

docker-run:
	docker-compose -f ${COMPOSE_FILE} up -d

docker-clean:
	docker-compose -f ${COMPOSE_FILE} down

docker-respawn:
	docker rm -f postgres_container && docker-compose -f ${COMPOSE_FILE} up -d postgres

migrate:
	set -a	&& . ./env.local && pipenv run head

upgrade:
	set -a	&& . ./env.local && pipenv run upgrade

downgrade:
	set -a	&& . ./env.local && pipenv run downgrade