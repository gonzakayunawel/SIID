# SIID Project Overview

SIID (Smart Industrial Information Dashboard) is a data analysis project focused on the **DataCo Smart Supply Chain** dataset. The project aims to perform exploratory data analysis (EDA) and potentially build predictive models for supply chain optimization, such as late delivery risk assessment.

## Project Structure

- `data/raw/`: Contains the raw CSV datasets (e.g., `DataCoSupplyChainDataset.csv`).
- `notebooks/`: Jupyter notebooks for iterative development and exploration.
    - `exploratory_DA.ipynb`: Primary EDA notebook.
    - `load_data.ipynb`: Notebook version of the data loading process.
- `src/`: Core source code.
    - `load_data.py`: Script to download the dataset from Kaggle using `kagglehub`.
- `main.py`: The main entry point for the application (currently a placeholder).
- `pyproject.toml` & `uv.lock`: Configuration and dependency management using `uv`.

## Tech Stack

- **Language:** Python (>=3.14)
- **Data Analysis:** Pandas, NumPy, SciPy, Statsmodels.
- **Machine Learning:** Scikit-learn.
- **Visualization:** Seaborn, Matplotlib.
- **Data Acquisition:** Kagglehub.
- **Package Manager:** [uv](https://github.com/astral-sh/uv).

## Building and Running

### Prerequisites

Ensure you have `uv` installed. You can install it via:
```bash
curl -LsSf https://astral-sh.uv.io/install.sh | sh
```

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

### Running the Application

To run the main entry point:
```bash
uv run main.py
```

### Working with Notebooks

The project includes an `ipykernel` dependency. You can use your preferred Jupyter environment (VS Code, JupyterLab, etc.) and select the project's virtual environment as the kernel.

## Development Conventions

- **Data Handling:** Raw data should always be kept in `data/raw/` and never modified directly. Processed data should be saved in a separate directory (e.g., `data/processed/`).
- **Dependency Management:** Use `uv add <package>` to add new dependencies and `uv sync` to keep the environment updated.
- **Coding Style:** Follow standard Python (PEP 8) conventions.
