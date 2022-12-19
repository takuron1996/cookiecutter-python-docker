SHELL = /bin/bash
CONTAINER_NAME = {{cookiecutter.container_name}}
APPLICATION = {{cookiecutter.workdir}}
DOCKER = docker exec $(CONTAINER_NAME)
PYLINT = $(DOCKER) poetry run pylint
FORMAT_BLACK = $(DOCKER) poetry run black
FORMAT_ISORT = $(DOCKER) poetry run isort
LINTRCF	= pylintrc.txt
LINTRST = pylintresult.txt
RUN_FILE = {{cookiecutter.project_name}}/example.py
TEST = tests
COVERAGE = $(APPLICATION)/htmlcov
DOCS = docs
PYCS = $(shell find . -type d -name .venv -prune -o -type d -name "__pycache__" -print)
VENV = .venv
EXCLUDE = -not -name .coveragerc -not -name .gitignore

prepare: build	up	install

run: format
	$(DOCKER) poetry run python $(RUN_FILE)

test: format
	$(DOCKER) poetry run pytest --cov -v --cov-report=html

sh:
	docker exec -it $(CONTAINER_NAME) /bin/sh

up:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

lint: format
	@if [ ! -e $(APPLICATION)/$(LINTRCF) ]; then $(PYLINT) --generate-rcfile > $(APPLICATION)/$(LINTRCF) 2> /dev/null ; fi
	@$(PYLINT) --rcfile=$(LINTRCF) `find . -name "*.py" | sed -e "s@/$(APPLICATION)@@"` > $(APPLICATION)/$(LINTRST); \
	less $(APPLICATION)/$(LINTRST)

format:
	@$(FORMAT_BLACK) .
	@$(FORMAT_ISORT) .

clean:
	@if [ -d $(COVERAGE) ]; then echo "rm -rf $(COVERAGE)"; rm -rf $(COVERAGE); fi
	@if [ -e $(APPLICATION)/$(LINTRST) ] ; then echo "rm -f $(APPLICATION)/$(LINTRST)" ; rm -f $(APPLICATION)/$(LINTRST) ; fi
	@find . -maxdepth 1 $(EXCLUDE) -type f -name ".*" -exec rm {} ";" -exec echo rm -f {} ";"
	@for each in ${PYCS} ; do echo "rm -rf $${each}" ; rm -rf $${each} ; done

install:
	$(DOCKER) poetry install

update:
	$(DOCKER) poetry update

docs:
	$(DOCKER) poetry run pdoc {{cookiecutter.project_name}} --html -o $(DOCS) --force
	$(DOCKER) poetry run pdoc tests --html -o $(DOCS) --force

check: format
	$(DOCKER) poetry run mypy --install-types --non-interactive
