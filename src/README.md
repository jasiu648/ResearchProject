# Source code

Reusable Python utilities for the project.

## `data_preparation.py`

| Function | Description |
|---|---|
| `randomly_null_values` | Introduce synthetic missing values for evaluation |
| `apply_iterative_imputer` | MICE-style imputation via scikit-learn `IterativeImputer` |
| `input_constant_values` | Fill gaps with mean, median, or mode |
| `impute_locf` | Last Observation Carried Forward |
| `calculate_errors` | Compute MSE, RMSE, MAE, MPE on imputed vs. original values |
