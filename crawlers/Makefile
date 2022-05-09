VENV = venv
VENV_DEVELOP = venv_develop

.PHONY: $(VENV) $(VENV_DEVELOP)

PYTHON_VERSION = 3.9

$(VENV):
	-rm -rf $(VENV)
	python$(PYTHON_VERSION) -m venv $(VENV)

	$(VENV)/bin/pip install -r requirements/production.txt

$(VENV_DEVELOP):
	-rm -rf $(VENV_DEVELOP)
	python$(PYTHON_VERSION) -m venv $(VENV_DEVELOP)

	$(VENV_DEVELOP)/bin/pip install -r requirements/development.txt
