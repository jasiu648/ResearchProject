# Data

Raw and processed air quality data from GIOŚ monitoring stations (Poland, 2023).

## Structure

```
data/
├── raw/         # Original hourly xlsx files per pollutant
├── processed/   # Imputed and cleaned datasets
└── README.md
```

- `raw/` — unmodified source files downloaded from GIOŚ (PM10, PM2.5, NO₂, NO, NOₓ, O₃, SO₂, CO, C₆H₆)
- `processed/` — outputs of imputation pipelines ready for model training
