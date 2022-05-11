PYTHON_VERSION = 3.9

VENV = venv
VENV_DEVELOP = venv_develop


install: install-all

install-all:
	-rm -rf $(VENV)
	python$(PYTHON_VERSION) -m venv $(VENV)

	$(VENV)/bin/pip install -r requirements/base.txt
	$(VENV)/bin/pip install -r requirements/cli.txt
	$(VENV)/bin/pip install -r requirements/bot.txt

install-cli:
	-rm -rf $(VENV)
	python$(PYTHON_VERSION) -m venv $(VENV)

	$(VENV)/bin/pip install -r requirements/base.txt
	$(VENV)/bin/pip install -r requirements/cli.txt

install-bot:
	-rm -rf $(VENV)
	python$(PYTHON_VERSION) -m venv $(VENV)

	$(VENV)/bin/pip install -r requirements/base.txt
	$(VENV)/bin/pip install -r requirements/cli.txt

develop:
	-rm -rf $(VENV_DEVELOP)
	python$(PYTHON_VERSION) -m venv $(VENV_DEVELOP)

	$(VENV_DEVELOP)/bin/pip install -r requirements/development.txt
