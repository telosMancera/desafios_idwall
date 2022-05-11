PYTHON_VERSION = 3.9

VENV = venv


install:
	-rm -rf $(VENV)
	python$(PYTHON_VERSION) -m venv $(VENV)

	$(VENV)/bin/pip install -r requirements/production.txt

develop:
	-rm -rf $(VENV)
	python$(PYTHON_VERSION) -m venv $(VENV)

	$(VENV)/bin/pip install -r requirements/development.txt

test:
	$(VENV)/bin/python -m pytest
