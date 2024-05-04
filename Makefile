# Variables
VENV_DIR := env
PYTHON := python3
ACTIVATE := source $(VENV_DIR)/bin/activate
REQUIREMENTS := requirements.txt
SETUP_SCRIPT := setup.sh
# Targets
.PHONY: all venv install-dev install clean

all: setup

setup: venv
	zsh $(SETUP_SCRIPT)

# Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV_DIR)

# Install dependencies
install: venv
	$(ACTIVATE) && pip install -r $(REQUIREMENTS)

# Clean up the virtual environment
clean:
	rm -rf $(VENV_DIR)
