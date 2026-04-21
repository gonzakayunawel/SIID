# SIID: Sistemas de Información e Inteligencia de los Datos

SIID es un proyecto de análisis de datos enfocado en el conjunto de datos **DataCo Smart Supply Chain**. El objetivo principal es realizar un análisis exploratorio de datos (EDA) y construir modelos predictivos para la optimización de la cadena de suministro, como la evaluación del riesgo de entregas tardías.

## 🚀 Estructura del Proyecto

```text
/
├── data/raw/          # Datasets originales (CSV)
├── notebooks/         # Notebooks de Jupyter para experimentación
│   ├── 01.load_data.ipynb
│   ├── 02.EDA.ipynb
│   └── 03.model.ipynb
├── report/            # Reportes generados (Quarto)
├── src/               # Código fuente (scripts de carga y procesamiento)
│   └── load_data.py
├── main.py            # Punto de entrada principal
├── pyproject.toml     # Configuración de dependencias (uv)
└── GEMINI.md          # Documentación interna del proyecto
```

## 🛠️ Tecnologías

- **Lenguaje:** Python (>=3.14)
- **Análisis de Datos:** Pandas, NumPy, SciPy, Statsmodels.
- **Machine Learning:** Scikit-learn.
- **Visualización:** Seaborn, Matplotlib.
- **Reportes:** Quarto.
- **Gestor de Paquetes:** [uv](https://github.com/astral-sh/uv).

## ⚙️ Instalación y Uso

### Prerrequisitos

Asegúrate de tener instalado `uv`. Puedes instalarlo con el siguiente comando:

```bash
curl -LsSf https://astral-sh.uv.io/install.sh | sh
```

### Configuración del Entorno

Sincroniza las dependencias del proyecto:

```bash
uv sync
```

### Descarga de Datos

Para descargar el dataset desde Kaggle y ubicarlo en `data/raw/`:

```bash
uv run src/load_data.py
```

### Ejecución de Notebooks

El proyecto incluye la dependencia `ipykernel`. Puedes usar tu entorno preferido (VS Code, JupyterLab, etc.) y seleccionar el entorno virtual del proyecto como kernel.

## 📈 Desarrollo

- **Manejo de Datos:** Los datos crudos en `data/raw/` no deben modificarse directamente.
- **Estilo:** Se siguen las convenciones estándar de Python (PEP 8).
- **Dependencias:** Usa `uv add <paquete>` para agregar nuevas dependencias y `uv sync` para mantener el entorno actualizado.
