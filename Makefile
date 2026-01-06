.PHONY: setup run docker-build docker-up docker-test test

setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip setuptools wheel
	.venv/bin/pip install -r requirements.txt

run:
	. .venv/bin/activate && python manage.py runserver

docker-build:
	docker build -t access_control_app .

docker-up:
	docker-compose up -d

test:
	@echo "Running tests locally..."
	. .venv/bin/activate && python manage.py test

docker-test:
	@echo "Running tests inside Docker..."
	docker-compose run --rm web python manage.py test
