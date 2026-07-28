# AI/DS Starter Template

Fully-loaded GitHub template for AI/Data Science projects.

## Features

- **DVC** dataset & model versioning
- **GitHub Actions** — CI, DVC pipeline, model deploy
- **Dependabot** — auto-update dependencies
- **Codespaces** — one-click dev environment
- **Secrets** — all API keys pre-configured
- **W&B** experiment tracking
- **Hugging Face** model deployment

## Quick Start

```bash
pip install -r requirements.txt
dvc init
dvc remote add default s3://your-bucket
dvc push
```

## Structure

```
src/          # Source code
data/         # Datasets (DVC-tracked)
models/       # Trained models (DVC-tracked)
notebooks/    # Jupyter notebooks
tests/        # Unit tests
scripts/      # Deployment scripts
```
