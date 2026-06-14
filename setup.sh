#!/bin/bash
set -e

ENV_NAME="yiheng-forge"
YAML_FILE="environment.yml"

echo "=== Step 1: Creating Conda environment (system layer) ==="
if conda env list | grep -q "^${ENV_NAME} "; then
    echo "Environment '${ENV_NAME}' already exists. Updating..."
    conda env update -n "${ENV_NAME}" -f "${YAML_FILE}"
else
    conda env create -f "${YAML_FILE}"
fi

echo "=== Step 2: Activating environment ==="
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${ENV_NAME}"

echo "=== Step 3: Installing Python packages with UV (application layer) ==="
uv sync --active --extra dev --locked

echo "=== Setup complete. Activate with: conda activate ${ENV_NAME} ==="
