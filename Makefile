PYTHON = python3

build:
	@echo "building package..."
	$(PYTHON) setup.py sdist

env: 
	@echo "creating virtual environment..."
	$(PYTHON) -m venv .venv

install:
	pip install -r requirements.txt
	$(PYTHON) setup.py install

upload: build
	$(PYTHON) setup.py sdist -r local

uninstall:
	rm -rf dist *.egg-info build