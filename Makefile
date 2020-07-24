.PHONY: help
## help: Prints this help message
help:
	@echo "Usage: \n"
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'

.PHONY: down
## down: brings down the containers and volumes
down:
	docker-compose down -v

.PHONY: up
## up: brings the contai back up 
up:
	docker-compose up --build -d

.PHONY: init-db
## init-db: set up Tortoise and then generates the schema
init-db:
	docker-compose exec web python app/db.py

.PHONY: web-db
## web-db: access to the database via psql
web-db:
	docker-compose exec web-db psql -U postgres

.PHONY: test
## test: runs all the tests in the app
test:
	docker-compose exec web python -m pytest -v

.PHONY: silent-test
## silent-test: runs all tests in the app disabling warnings
silent-test:
	docker-compose exec web python -m pytest -p no:warnings -v

.PHONY: test-ping
## test-ping: runs all tests that have ping in their name
test-ping:
	docker-compose exec web python -m pytest -k ping -v

.PHONY: test-summary
## test-summary: runs all tests that have summary in their name
test-summary:
	docker-compose exec web python -m pytest -k "summar and not test_read" -v

.PHONY: test-read
## test-read: runs all the test that have read in their name
test-read:
	docker-compose exec web python -m pytest -k read -v

.PHONY: test-cov
## test-cov: runs the tests with coverage
test-cov:
	docker-compose exec web python -m pytest --cov="."

.PHONY: test-html-cov
## test-html-cov: generates a html report on testing coverage
test-html-cov:
	docker-compose exec web python -m pytest --cov="." --cov-report html

.PHONY: flake
## flake: runs flake8
flake:
	docker-compose exec web flake8 .

.PHONY: black-check
## black-check: runs the black checker
black-check:
	docker-compose exec web flake8 .

.PHONY: black-diff
## black-diff: shows the possible result of the black formatter
black-diff:
	docker-compose exec web black . --diff

.PHONY: black
## black: runs the black formatter
black:
	docker-compose exec web black .
