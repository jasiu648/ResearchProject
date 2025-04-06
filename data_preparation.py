import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression

def randomly_null_values(series: pd.Series, percentage: float = 10, seed: int = 42) -> pd.Series:
    """
    Randomly nulls a given percentage of values in a Pandas Series.
    
    :param series: Pandas Series to modify.
    :param percentage: Percentage of values to set as NaN (0-100).
    :param seed: Random seed for reproducibility.
    :return: Pandas Series with randomly null values.
    """
    np.random.seed(seed)
    total_values = len(series)
    num_nulls = int((percentage / 100) * total_values)
    
    # Select random indices to null
    null_indices = np.random.choice(series.index, num_nulls, replace=False)
    series.loc[null_indices] = np.nan
    
    return series

def apply_iterative_imputer(series: pd.Series) -> pd.Series:
    """
    Applies IterativeImputer to a Pandas Series to fill missing values.
    
    :param series: Pandas Series with missing values.
    :return: Imputed Pandas Series.
    """
    imputer = IterativeImputer(max_iter=100, random_state=42)
    
    # Reshape data for imputer
    series_imputed = imputer.fit_transform(series.values.reshape(-1, 1))
    
    return pd.Series(series_imputed.flatten(), index=series.index)

def calculate_errors(original: pd.Series, null_values: pd.Series, imputed: pd.Series) -> dict:
    """
    Calculates MSE, RMSE, MAE, and MPE between the original and imputed series.
    
    :param original: Original Pandas Series before nulling values.
    :param null_values: Series that indicates which values were originally null.
    :param imputed: Imputed Pandas Series.
    :return: Dictionary with MSE, RMSE, MAE, and MPE.
    """

    # Identify indices where original values were missing
    mask = null_values.isna()

    # Compute error metrics
    mse = mean_squared_error(original[mask], imputed[mask])
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(original[mask], imputed[mask])
    
    original_nonzero = original[mask].replace(0, np.nan)  # Replace 0 with NaN to avoid -inf
    mpe = np.nanmean((np.abs(original_nonzero - imputed[mask])) / original_nonzero) * 100  # Compute MPE safely

    return {"MSE": mse, "RMSE": rmse, "MAE": mae, "MPE": mpe}

def input_constant_values(series: pd.Series, option: str = "mean") -> pd.Series:
    """
    Imputes missing values in a Pandas Series using mean, median, or mode.
    
    :param series: Pandas Series with missing values.
    :param option: The method to use for imputation. Options: "mean", "median", "mode".
    :return: Pandas Series with missing values filled.
    """
    if option == "mean":
        value = series.mean()
    elif option == "median":
        value = series.median()
    elif option == "mode":
        value = series.mode()[0]  # Mode can return multiple values, take the first one
    else:
        raise ValueError("Invalid option! Choose from 'mean', 'median', or 'mode'.")

    return series.fillna(value)

def impute_locf(series: pd.Series) -> pd.Series:
    """
    Imputes missing values using Last Observation Carried Forward (LOCF).
    
    :param series: Pandas Series with missing values.
    :return: Pandas Series with missing values filled using LOCF.
    """
    return series.ffill()  # Forward Fill (LOCF)

def impute_regression(df: pd.DataFrame) -> pd.DataFrame:
    """
    Imputes missing values in the target column using regression on other columns.

    :param df: Pandas DataFrame with missing values.
    :param target_column: Column to be imputed using regression.
    :return: DataFrame with imputed values.
    """
    df_copy = df.copy()

    # Identify rows with and without missing values
    missing_mask = df_copy.isna()
    
    if missing_mask.sum() == 0:
        print("No missing values found in the target column.")
        return df_copy  # Return unchanged if no missing values
    
    # Define predictors (all other columns)
    predictors = df_copy.drop()

    # Split into training (non-missing) and test (missing)
    X_train = predictors[~missing_mask]
    y_train = df_copy.loc[~missing_mask, target_column]
    
    X_test = predictors[missing_mask]

    # Train Linear Regression Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict missing values
    df_copy.loc[missing_mask, target_column] = model.predict(X_test)

    return df_copy
