# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SIID (Sistemas de Información e Inteligencia de los Datos) is a PhD course at UNAB. This repository is a data science project analyzing the **DataCo Smart Supply Chain** dataset (180,519 records, 53 variables). The primary objectives are EDA and ML benchmarking for **late delivery risk prediction** (classification) and **sales prediction** (regression).

## Commands

```bash
# Install dependencies
uv sync

# Download dataset from Kaggle into data/raw/
uv run src/load_data.py

# Lint and format
uv run ruff check .
uv run ruff format .

# Render the Quarto report (requires Quarto CLI installed)
quarto render report/report.qmd
```

No test suite exists — validation happens through notebook execution.

## Architecture

The project follows a **notebook-first** data science workflow:

1. **`notebooks/01.load_data.ipynb`** — data acquisition via Kaggle Hub
2. **`notebooks/02.EDA.ipynb`** — exploratory analysis, feature understanding, distributions
3. **`notebooks/03.model.ipynb`** — model benchmarking (4 regression + 4 classification models)

**`src/load_data.py`** is the script form of notebook 01, downloading the dataset to `data/raw/`.

**`report/report.qmd`** is the authoritative technical report (Quarto). It embeds code from the notebooks and renders to `report/report.html` and `report/report.pdf`. The 10-section report covers EDA, regression benchmarking, classification benchmarking, feature importance, ROC curves, and conclusions.

### ML Pipeline Pattern

Models in `03.model.ipynb` use sklearn `Pipeline` objects:
- **Imputation** → `SimpleImputer(strategy="median")`
- **Scaling** → `StandardScaler`
- **Estimator** → Linear/Ridge/Lasso, Decision Tree, Random Forest, or XGBoost

Feature selection uses importance thresholding (≥1%). Be careful to avoid **data leakage** — the notebook already guards against this.

### Data Conventions

- `data/raw/` — read-only; never modify source CSVs
- `data/processed/` — for any transformed/cleaned data (not yet created)
- Kaggle credentials must be configured locally for `kagglehub` to work

## Linting

Ruff is configured in `pyproject.toml`. Key ignores: `E501` (long lines), `F401`/`F811` (unused imports/redefinitions — common in notebooks), `E402` (late imports — common in analysis scripts). The `src` package is treated as first-party for import ordering.
