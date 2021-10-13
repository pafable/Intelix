PYTHON = python

build:
	@echo "building package..."
	$(PYTHON) setup.py sdist

env: 
	@echo "creating virtual environment"
	$(PYTHON) -m venv .venv

install:
	$(PYTHON) setup.py install

download:
	PIP_INDEX_URL=https://afable.jfrog.io/artifactory/api/pypi/pafable-pypi-local/simple $(PIP) install -U intelix_cli

upload: build
	$(PYTHON) setup.py sdist -r local

test: download
	intelix-file

clean:
	rm -rf dist *.egg-info build