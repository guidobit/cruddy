#/bin/bash

COMPOSE_FILE=docker-compose.yml:docker-compose.test.yml docker-compose run backend python -m unittest discover