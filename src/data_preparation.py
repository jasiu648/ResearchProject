import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression


def randomly_null_values(series: pd.Series, percentage: float = 10, seed: int = 42) -> pd.Series:
    """Randomly null a percentage of values in a pandas Series."""
    np.random.seed(seed)
    total_values = len(series)
    num_nulls = int((percentage / 100) * total_values)
    null_indices = np.random.choice(series.index, num_nulls, replace=False)
    series.loc[null_indices] = np.nan
    return series


def apply_iterative_imputer(series: pd.Series) -> pd.Series:
    """Apply a scikit-learn iterative imputer to a series."""
    imputer = IterativeImputer(max_iter=100, random_state=42)
    imputed = imputer.fit_transform(series.values.reshape(-1, 1))
    return pd.Series(imputed.flatten(), index=series.index)


def calculate_errors(original: pd.Series, null_values: pd.Series, imputed: pd.Series) -> dict:
    """Calculate standard error metrics between original and imputed values."""
    mask = null_values.isna()
    mse = mean_squared_error(original[mask], imputed[mask])
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(original[mask], imputed[mask])

    original_nonzero = original[mask].replace(0, np.nan)
    mpe = np.nanmean((np.abs(original_nonzero - imputed[mask])) / original_nonzero) * 100

    return {"MSE": mse, "RMSE": rmse, "MAE": mae, "MPE": mpe}


def input_constant_values(series: pd.Series, option: str = "mean") -> pd.Series:
    """Impute missing values using mean, median, or mode."""
    if option == "mean":
        value = series.mean()
    elif option == "median":
        value = series.median()
    elif option == "mode":
        value = series.mode()[0]
    else:
        raise ValueError("Invalid option! Choose from 'mean', 'median', or 'mode'.")

    return series.fillna(value)


def impute_locf(series: pd.Series) -> pd.Series:
    """Impute using last observation carried forward."""
    return series.ffill()


def impute_regression(df: pd.DataFrame) -> pd.DataFrame:
    """Impute missing values with a simple regression-based workflow."""
    df_copy = df.copy()
    missing_mask = df_copy.isna()

    if missing_mask.sum() == 0:
        print("No missing values found in the target column.")
        return df_copy

    raise NotImplementedError("This helper needs a clear target column definition to work reliably.")
