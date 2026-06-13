# Yiheng Forge

A unified training framework for multi-modal models.

## Installation

```bash
git clone https://github.com/GitYiheng/yiheng-forge.git
cd yiheng-forge
conda env create -f environment.yml
conda activate yiheng-forge
```

The conda environment is defined in `environment.yml`. Python package metadata
and dependencies are defined in `pyproject.toml`, which is installed in editable
mode with the `dev` extras.

## Run

```bash
python scripts/train.py
```

Override config values with Hydra:

```bash
python scripts/train.py trainer.max_steps=3 runner.output_dir=outputs/dev
```

## Test

```bash
python -m pytest -q
```
