.PHONY: install format lint test all

install:
	pip install -r requirements.txt

format:
	black .

lint:
	flake8 --ignore=E203,E266,E501,W503,F403,F401 .

test:
	pytest

all: lint format test
