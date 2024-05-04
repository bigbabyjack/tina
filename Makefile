# Variables
VENV_DIR := env
PYTHON := python3
ACTIVATE := $(VENV_DIR)/bin/activate
REQUIREMENTS := requirements.txt
SETUP_SCRIPT := setup.sh
BIN_DIR := /usr/local/bin

# Targets
.PHONY: all setup venv install clean link unlink

all: setup

setup: clean install link activate

# Activate the virtual environment
activate:
	source $(ACTIVATE) && exec zsh

# Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV_DIR)

# Install dependencies
install: venv
	source $(ACTIVATE) && pip install -r $(REQUIREMENTS)

# Create a symbolic link to the 'tina' script
link:
	sudo ln -sf $(PWD)/tina $(BIN_DIR)/tina

# Remove the symbolic link to 'tina'
unlink:
	sudo rm -f $(BIN_DIR)/tina

# Clean up the virtual environment
clean: unlink
	rm -rf $(VENV_DIR)
