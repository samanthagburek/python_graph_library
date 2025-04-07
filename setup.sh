#!/bin/bash
set -e

echo "Detecting operating system..."

OS="$(uname -s)"

install_boost() {
    echo "Installing Boost C++ library..."

    case "$OS" in
        Linux)
            echo "Detected Linux"
            sudo apt update
            sudo apt install -y libboost-all-dev
            ;;
        Darwin)
            echo "Detected macOS"
            # Make sure Homebrew is installed
            if ! command -v brew &> /dev/null; then
                echo "Homebrew not found. Please install Homebrew first: https://brew.sh/"
                exit 1
            fi
            brew install boost
            ;;
        MINGW*|MSYS*|CYGWIN*)
            echo "Detected Windows (Git Bash / MSYS / Cygwin)"
            echo "Please install Boost manually from https://www.boost.org/users/download/ or via vcpkg/choco."
            ;;
        *)
            echo "Unsupported OS: $OS"
            exit 1
            ;;
    esac
}

install_python_deps() {
    echo "Installing Python dependencies..."
    pip install nanobind
    pip install . # this is making use of the toml
}

install_boost
install_python_deps

echo "✅ Setup complete."
