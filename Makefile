PYTHON = python3
RM = /bin/rm

build:
	@echo "building package"
	$(PYTHON) setup.py sdist

env: 
	@echo "creating virtual environment"
	$(PYTHON) -m venv .venv

install:
	@echo "installing Intelix CLI"
	pip install -r requirements.txt
	$(PYTHON) setup.py install

upload: build
	$(PYTHON) setup.py sdist -r local

uninstall:
	@echo "uninstalling Intelix CLI"
	$(RM) -rf dist *.egg-info build
	$(RM) -f .venv/bin/intelix-*
	$(RM) -f .venv/lib/python3.*/site-packages/Intelix_CLI-*
