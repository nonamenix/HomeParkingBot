PROJECT = HomeParkingBot

PYTHON_VER = python3.6

REQUIREMENTS = requirements.txt
VIRTUAL_ENV ?= .venv

PYTHON ?= $(VIRTUAL_ENV)/bin/python
PYTEST ?= $(VIRTUAL_ENV)/bin/pytest
PYLINT ?= $(VIRTUAL_ENV)/bin/pylint

venv: venv_init
	$(VIRTUAL_ENV)/bin/pip install -r $(REQUIREMENTS)
	ln -sf $(VIRTUAL_ENV)/bin/activate activate

venv_init:
	if [ ! -d $(VIRTUAL_ENV) ]; then \
		virtualenv -p $(PYTHON_VER) $(VIRTUAL_ENV) --prompt="($(PROJECT))"; \
	fi

test: venv
	$(VIRTUAL_ENV)/bin/py.test

test_coverage: venv
	$(VIRTUAL_ENV)/bin/py.test --cov-report html --cov-config .coveragerc --cov $(PROJECT)

black: venv
	black $(PROJECT)/ --check --config pyproject.toml

flake8: venv
	flake8 $(PROJECT)/

clean_venv:
	rm -rf $(VIRTUAL_ENV)

clean_pyc:
	find . -name \*.pyc -delete

clean: clean_venv clean_pyc
