#!/bin/bash

set -e

if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    version=$(python -c 'import sys; print(sys.version_info[0])')
    if [ "$version" -eq 3 ]; then
        PYTHON_CMD="python"
    else
        echo "ERROR: Python 3 is required but found Python 2"
        echo "Please install Python 3 to continue"
        exit 1
    fi
else
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3 to continue. You can download it from:"
    echo "https://www.python.org/downloads/"
    exit 1
fi

echo "Found Python 3 installation: $($PYTHON_CMD --version)"

clear
echo "Please enter your NordVPN API token (you can get it from https://my.nordaccount.com/dashboard/nordvpn/access-tokens/):"
read -r token

if [ -z "$token" ]; then
    echo "ERROR: Token cannot be empty"
    exit 1
fi

if ! "$PYTHON_CMD" generate_config.py "$token"; then
    echo "ERROR: Configuration generation failed"
    exit 1
fi