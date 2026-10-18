# Air Quality Missing Data Imputation

Research project analysing PM10 particulate-matter measurements from Polish State Environmental Monitoring (PMŚ) stations in 2023. The main goal is to compare multiple imputation strategies for filling gaps in hourly time-series air quality data, and evaluate predictive models trained on the imputed datasets.

## Research questions

- Which imputation method (MICE, LOCF, mean/median/mode, regression) preserves the statistical properties of the original PM10 series most faithfully?
- How does imputation quality affect downstream ML model performance (Random Forest, MLP, regression)?

## Repository structure

```
data/
  raw/          # Original hourly xlsx files per pollutant (PM10, PM2.5, NO2, O3 …)
  processed/    # Imputed and cleaned datasets ready for modelling
docs/
  reports/      # Static HTML interactive visualisations
  project-structure.md
notebooks/
  missing_data.ipynb        # EDA and comparison of imputation methods
  data_visualization.ipynb  # Station-level and time-series visualisations
  regression.ipynb          # Regression-based imputation and evaluation
  random_forest.ipynb       # Random Forest imputation and prediction
  mlp.ipynb                 # MLP (neural network) imputation
  imputation_testing.ipynb  # Unit-style tests of the data_preparation helpers
src/
  data_preparation.py  # Reusable imputation and error-metric functions
requirements.txt
```

## Quickstart

```bash
pip install -r requirements.txt
jupyter lab
```

Open any notebook under `notebooks/` — they import from `src/` and load data from `data/raw/`.

## Data

Source: [Główny Inspektorat Ochrony Środowiska (GIOŚ)](https://www.gios.gov.pl/) — hourly averaged concentrations (µg/m³) measured at monitoring stations across Poland, 2023.

Pollutants covered: PM10, PM2.5, NO₂, NO, NOₓ, O₃, SO₂, CO, C₆H₆.

## Methods

| Method | Module / notebook |
|---|---|
| Iterative Imputer (MICE) | `src/data_preparation.py` |
| Last Observation Carried Forward (LOCF) | `src/data_preparation.py` |
| Constant-value (mean / median / mode) | `src/data_preparation.py` |
| Bayesian Ridge regression | `notebooks/regression.ipynb` |
| Random Forest | `notebooks/random_forest.ipynb` |
| MLP (TensorFlow/Keras) | `notebooks/mlp.ipynb` |

Error metrics reported: MSE, RMSE, MAE, MPE.

## Requirements

- Python ≥ 3.10
- pandas, numpy, scikit-learn, openpyxl, jupyter
- tensorflow (for `mlp.ipynb`)
- plotly, missingno (for visualisation notebooks)
