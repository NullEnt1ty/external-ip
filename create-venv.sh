#!/usr/bin/env bash
set -e

dir="$(cd "$(dirname "$0")" && pwd)"
venv_dir="$dir/.venv"

if [[ -d "$venv_dir" ]]; then
  echo ">>> virtual environment '$venv_dir' already exists. Skipping creation"
else
  echo ">>> Creating virtual environment"
  python3 -m venv "$venv_dir"
fi

source "$venv_dir/bin/activate"

echo ">>> Upgrading pip"
pip install --upgrade pip
pip install wheel

echo ">>> Installing dependencies"
pip install -r requirements.txt
