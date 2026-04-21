# SIID Project Overview

SIID (Sistemas de Información e Inteligencia de los Datos) is a data analysis project focused on the **DataCo Smart Supply Chain** dataset. The project aims to perform exploratory data analysis (EDA) and build predictive models for supply chain optimization, such as late delivery risk assessment.

## Project Structure

- `data/raw/`: Contains the raw CSV datasets (e.g., `DataCoSupplyChainDataset.csv`).
- `notebooks/`: Jupyter notebooks for iterative development and exploration.
    - `01.load_data.ipynb`: Data loading process.
    - `02.EDA.ipynb`: Exploratory Data Analysis.
    - `03.model.ipynb`: Model training and evaluation.
- `report/`: Analytical reports generated using Quarto.
- `poster/`: Academic poster source using Quarto/Typst.
- `src/`: Core source code.
    - `load_data.py`: Script to download the dataset from Kaggle using `kagglehub`.
- `main.py`: The main entry point for the application.
- `render-poster.sh`: Script to generate the academic poster.
- `pyproject.toml` & `uv.lock`: Configuration and dependency management using `uv`.

## Tech Stack

- **Language:** Python (>=3.14)
- **Data Analysis:** Pandas, NumPy, SciPy, Statsmodels.
- **Machine Learning:** Scikit-learn, XGBoost.
- **Visualization:** Seaborn, Matplotlib.
- **Reporting:** Quarto, Typst.
- **Package Manager:** [uv](https://github.com/astral-sh/uv).
- **Linting/Formatting:** Ruff.

## Building and Running

### Prerequisites

Ensure you have `uv` and `quarto` installed.

### Installation

Sync the project dependencies:
```bash
uv sync
```

### Loading Data

To download the dataset from Kaggle and place it in the `data/raw/` directory, run:
```bash
# From the project root
uv run src/load_data.py
```

### Generating Reports and Posters

To render the analytical report:
```bash
quarto render report/report.qmd
```

To generate the academic poster:
```bash
./render-poster.sh
```

### Working with Notebooks

The project includes an `ipykernel` dependency. You can use your preferred Jupyter environment (VS Code, JupyterLab, etc.) and select the project's virtual environment as the kernel.

## Development Conventions

- **Data Handling:** Raw data should always be kept in `data/raw/` and never modified directly. Processed data should be saved in a separate directory (e.g., `data/processed/`).
- **Code Quality:** Use `ruff` for linting and formatting.
- **Dependency Management:** Use `uv add <package>` to add new dependencies and `uv sync` to keep the environment updated.
- **Coding Style:** Follow standard Python (PEP 8) conventions enforced by Ruff.
