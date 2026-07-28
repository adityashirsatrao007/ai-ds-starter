#!/bin/bash
# Bootstrap a new AI/DS project from this template
set -euo pipefail

echo "Setting up new project..."

# Init git if needed
if [ ! -d .git ]; then
    git init
fi

# Create virtual env
python3 -m venv .venv
source .venv/bin/activate

# Install deps
pip install --upgrade pip
pip install -r requirements.txt

# Init DVC
dvc init

# Copy secrets
if [ -f ~/.config/global-apikeys/keys.env ]; then
    echo "Keys found at ~/.config/global-apikeys/keys.env"
fi

echo "Done! Activate with: source .venv/bin/activate"
