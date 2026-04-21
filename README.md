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
├── poster/            # Material para póster académico (Quarto/Typst)
├── src/               # Código fuente (scripts de carga y procesamiento)
│   └── load_data.py
├── main.py            # Punto de entrada principal
├── pyproject.toml     # Configuración de dependencias (uv)
├── render-poster.sh   # Script para generar el póster
└── GEMINI.md          # Documentación interna del proyecto
```

## 🛠️ Tecnologías

- **Lenguaje:** Python (>=3.14)
- **Análisis de Datos:** Pandas, NumPy, SciPy, Statsmodels.
- **Machine Learning:** Scikit-learn, XGBoost.
- **Visualización:** Seaborn, Matplotlib.
- **Reportes y Presentación:** Quarto, Typst.
- **Gestor de Paquetes:** [uv](https://github.com/astral-sh/uv).
- **Calidad de Código:** Ruff.

## ⚙️ Instalación y Uso

### Prerrequisitos

Asegúrate de tener instalado `uv` y `quarto`.

- Instalar `uv`:
  ```bash
  curl -LsSf https://astral-sh.uv.io/install.sh | sh
  ```
- [Instalar Quarto](https://quarto.org/docs/get-started/) (necesario para reportes y pósters).

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

## 📊 Reportes y Posters

### Generar Reporte HTML
Para renderizar el reporte analítico:
```bash
quarto render report/report.qmd
```

### Generar Póster Académico
El póster resume los hallazgos críticos del proyecto, incluyendo:
- **Análisis Bayesiano:** Probabilidad del 71.7% de entrega tardía ante envíos lentos.
- **Modelado Predictivo:** Uso de **XGBoost** y **Random Forest** con una precisión (**Accuracy**) superior al **95%**.
- **Hallazgos Clave:** Dominancia de variables logísticas (>99% de importancia) sobre las financieras/geográficas.

Para generar el póster en formato PDF (usa Typst internamente):
```bash
./render-poster.sh
```

## 📈 Desarrollo

- **Manejo de Datos:** Los datos crudos en `data/raw/` no deben modificarse directamente.
- **Calidad de Código:** Se utiliza `ruff` para mantener el estilo y la calidad del código.
- **Dependencias:** Usa `uv add <paquete>` para agregar nuevas dependencias y `uv sync` para mantener el entorno actualizado.
