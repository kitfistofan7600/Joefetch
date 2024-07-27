# Variables
SCRIPT = joefetch.py
EXECUTABLE = joefetch
BUILD_DIR = $(CURDIR)
INSTALL_DIR = /usr/bin

# Default target
all: build

# Build the executable using PyInstaller
build:
	pyinstaller --onefile --name $(EXECUTABLE) $(SCRIPT)

# Install the executable to /usr/bin
install: build
	sudo cp $(BUILD_DIR)/$(EXECUTABLE) $(INSTALL_DIR)/$(EXECUTABLE)

# Clean up build artifacts
clean:
	rm -rf build dist $(EXECUTABLE).spec
