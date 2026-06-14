# Yiheng Forge

A unified training framework for multi-modal models.

---

## Installation

### Prerequisites

- [conda](https://docs.conda.io/en/latest/miniconda.html) (for CUDA, NCCL, and Python)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (for fast Python package management)

### Quick Start

```bash
git clone https://github.com/GitYiheng/yiheng-forge.git
cd yiheng-forge

# Create or update the conda environment, then sync Python dependencies from uv.lock
./setup.sh
```

If the script is not executable yet:

```bash
chmod +x setup.sh
./setup.sh
```

Manual setup:

```bash
# 1. Create the conda environment (system layer)
conda env create -f environment.yml
conda activate yiheng-forge

# 2. Install Python dependencies exactly as locked by uv.lock (Python layer)
uv sync --active --extra dev --locked
```

---

## Run

```bash
python scripts/train.py
```

Override config values with Hydra:

```bash
python scripts/train.py trainer.max_steps=3 runner.output_dir=outputs/dev
```

---

## Test

```bash
python -m pytest -q
```

### Test Markers

Tests are expected to be split by pytest markers as the framework grows:

- `unit`: fast tests for a small function, class, or module. These should run on CPU and avoid large files, network access, and GPUs.
- `integration`: tests for several modules working together, such as config loading, workspace initialization, and a tiny training loop.
- `e2e`: full user-facing flows, such as launching the training entry point and checking generated outputs.
- `gpu`: tests that require CUDA or GPU-specific behavior. These should be easy to skip on CPU-only machines.

Useful commands:

```bash
python -m pytest -q -m unit
python -m pytest -q -m "not gpu"
python -m pytest -q -m "integration or e2e"
```
