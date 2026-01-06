.PHONY: setup run docker docker-build docker-up docker-test test

# Setup local venv and install dependencies
setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip setuptools wheel
	.venv/bin/pip install -r requirements.txt

# Run Django server locally
run:
	. .venv/bin/activate && python manage.py runserver

# Docker build
docker-build:
	docker build -t access_control_app .

# Docker run
docker-up:
	docker-compose up -d

# Run tests locally
test:
	@echo "Running tests locally in virtual environment..."
	. .venv/bin/activate && python manage.py test

# Run tests in Docker
docker-test:
	@echo "Running tests inside Docker..."
	docker-compose run --rm web python manage.py test
