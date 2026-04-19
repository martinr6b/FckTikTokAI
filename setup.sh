#!/bin/bash
# FckTikTokAI Setup Script
# Simple shell script for Unix-like systems (Linux, macOS)

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_PATH="$SCRIPT_DIR/.venv"

print_header() {
    echo ""
    echo "============================================================"
    echo "  $1"
    echo "============================================================"
    echo ""
}

print_success() {
    echo "✓ $1"
}

print_error() {
    echo "✗ $1"
    exit 1
}

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
else
    print_error "Unsupported OS: $OSTYPE"
fi

echo "FckTikTokAI Setup Script"
echo "OS: $OS"

# Detect Linux distribution
if [ "$OS" = "Linux" ]; then
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        DISTRO=$(echo $ID | tr '[:upper:]' '[:lower:]')
        echo "Distro: $DISTRO"
    fi
fi

# Install Tkinter
print_header "Installing Tkinter"

if [ "$OS" = "Linux" ]; then
    case "$DISTRO" in
        arch|manjaro)
            echo "  → Installing tk (pacman)"
            sudo pacman -S --noconfirm tk
            print_success "Installed tk"
            ;;
        ubuntu|debian)
            echo "  → Updating package lists"
            sudo apt-get update
            echo "  → Installing python3-tk"
            sudo apt-get install -y python3-tk
            print_success "Installed python3-tk"
            ;;
        fedora|rhel|centos)
            echo "  → Installing python3-tkinter"
            sudo dnf install -y python3-tkinter
            print_success "Installed python3-tkinter"
            ;;
        opensuse*)
            echo "  → Installing python3-tkinter"
            sudo zypper install -y python3-tkinter
            print_success "Installed python3-tkinter"
            ;;
        *)
            echo "⚠ Unknown distribution. Please install tkinter manually:"
            echo "   - Arch: sudo pacman -S tk"
            echo "   - Debian/Ubuntu: sudo apt-get install python3-tk"
            echo "   - Fedora: sudo dnf install python3-tkinter"
            echo "   - openSUSE: sudo zypper install python3-tkinter"
            ;;
    esac
elif [ "$OS" = "macOS" ]; then
    if command -v brew &> /dev/null; then
        echo "  → Installing python-tk (Homebrew)"
        brew install python-tk
        print_success "Installed python-tk"
    else
        echo "⚠ Homebrew not found. Install from https://brew.sh"
        echo "  Then run: brew install python-tk"
    fi
fi

# Create virtual environment
print_header "Setting up Virtual Environment"

if [ -d "$VENV_PATH" ]; then
    print_success "Virtual environment already exists at $VENV_PATH"
else
    echo "  → Creating virtual environment"
    python3 -m venv "$VENV_PATH"
    print_success "Created virtual environment"
fi

# Activate venv for pip
source "$VENV_PATH/bin/activate"

# Install Python dependencies
print_header "Installing Python Dependencies"

echo "  → Upgrading pip"
pip install --upgrade pip
print_success "Upgraded pip"

if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
    echo "  → Installing dependencies from requirements.txt"
    pip install -r "$SCRIPT_DIR/requirements.txt"
    print_success "Installed dependencies"
else
    print_error "requirements.txt not found"
fi

# Completion message
print_header "Setup Complete!"

echo "To use the GUI, run:"
echo ""
echo "  source $VENV_PATH/bin/activate"
echo "  python gui.py"
echo ""
echo "Or directly:"
echo ""
echo "  $VENV_PATH/bin/python gui.py"
echo ""
