PYTHON := python3
VENV := .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python
MANAGE := $(PY) manage.py

.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "Available commands:"
	@echo "  make venv        Create virtual environment"
	@echo "  make install     Install dependencies"
	@echo "  make migrate     Run database migrations"
	@echo "  make run         Run development server"
	@echo "  make test        Run unit tests"
	@echo "  make clean       Remove virtualenv and cache files"
	@echo ""

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install django djangorestframework

migrate:
	$(MANAGE) migrate
run:
	$(MANAGE) runserver
test:
	$(MANAGE) test access_control

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.log" -delete
