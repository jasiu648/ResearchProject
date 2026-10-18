# Project structure

This repository is organized into data, notebooks, source code, and documentation.

## Main folders

- `src/` — reusable Python modules (`data_preparation.py` — imputation helpers and error metrics)
- `notebooks/` — Jupyter notebooks for EDA, imputation experiments, and ML modelling
- `data/raw/` — original hourly xlsx files from GIOŚ monitoring stations (2023)
- `data/processed/` — imputed and cleaned datasets produced by the notebooks
- `docs/reports/` — static HTML exports of interactive Plotly visualisations
