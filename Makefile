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
	docker-compose exec web python -m pytest -vv

.PHONY: silent-test
## silent-test: runs all tests in the app disabling warnings
silent-test:
	docker-compose exec web python -m pytest -p no:warnings -vv

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
	docker-compose exec web python -m pytest --cov="." -vv

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
	docker-compose exec web black . --check

.PHONY: black-diff
## black-diff: shows the possible result of the black formatter
black-diff:
	docker-compose exec web black . --diff

.PHONY: black
## black: runs the black formatter
black:
	docker-compose exec web black .

.PHONY: isort-check
## isort-check: check the order of the imports
isort-check:
	docker-compose exec web /bin/sh -c "isort ./**/*.py --check-only"

.PHONY: isort-diff
## isort-diff: shows the differences after apply the changes
isort-diff:
	docker-compose exec web /bin/sh -c "isort ./**/*.py --diff"

.PHONY: isort
## isort:  quickly sort all our imports alphabetically and automatically separate them into sections
isort:
	docker-compose exec web /bin/sh -c "isort ./**/*.py"
