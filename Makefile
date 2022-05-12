.PHONY: install build test cov

.DEFAULT_GOAL := install

test:
	python -m pytest

cov:
	python -m pytest --cov=selector_py_pod --cov-branch --cov-report term-missing

build:
	python -m build

install:
	python -m pip install -r requirements.txt -e .