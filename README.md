# ResearchProject

Project for analysis of air-quality data and missing-value imputation in 2023 pollutant measurements.

## Overview
This repository contains the experimental workflow used to process environmental monitoring data, test missing-value imputation methods, and visualize temporal trends for selected pollutants.

## Repository structure

```text
ResearchProject/
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   ├── README.md
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── README.md
│   ├── data_visualization.ipynb
│   ├── missing_data.ipynb
│   ├── mlp.ipynb
│   ├── random_forest.ipynb
│   ├── regression.ipynb
│   └── test1.ipynb
├── src/
│   ├── __init__.py
│   ├── README.md
│   └── data_preparation.py
├── docs/
│   └── project-structure.md
├── 2023_PM10_1g.xlsx
├── 2023_PM10_1g_imputed.xlsx
├── cleaned_time_series_data.xlsx
├── DataVisualization.html
├── DataVisualizationPerStation.html
├── DataVisualizationWithSlider.html
├── dane2023/
├── data_preparation.py
└── ...
```

## Main goal
Analyze pollutant time-series data, compare imputation methods, and generate interpretable visualizations of air-quality trends.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Dependencies

- pandas
- numpy
- scikit-learn
- openpyxl
- jupyter

## Recommended workflow

1. Keep raw input files under `data/raw/`.
2. Store cleaned outputs in `data/processed/`.
3. Put experiments and visualizations in `notebooks/`.
4. Keep reusable logic in `src/`.
5. Document decisions in `docs/`.

## Notes
This project is intended for research and analysis work related to environmental monitoring and data-quality evaluation.
