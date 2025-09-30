import pandas as pd
import pytest
import importlib
import os

# Path to dataset
DATA_PATH = os.path.join(os.path.dirname(__file__), "all_commodities_data.csv")


@pytest.fixture(scope="module")
def df():
    return pd.read_csv(DATA_PATH)  # load data


# Test that data loads correctly
def test_data_loads(df):
    assert not df.empty, "Dataset should not be empty"


# Test that all expected columns are present
def test_expected_columns(df):
    expected = ["ticker", "commodity", "date", "open", "high", "low", "close", "volume"]
    assert list(df.columns) == expected, f"Unexpected columns: {df.columns}"


# Test that there are no null entries in the price records
def test_no_nulls_in_price_columns(df):
    price_columns = ["open", "high", "low", "close"]
    nulls = df[price_columns].isnull().sum().sum()
    assert nulls == 0, f"Found {nulls} null values in price columns"


# Check that Gold is present in the commodities
def test_gold_in_commodities():
    df = pd.read_csv(DATA_PATH)
    assert "commodity" in df.columns, "'commodity' column missing"
    assert "Gold" in df["commodity"].unique(), "'Gold' not found in commodities"


# Check required packages are importable
def test_required_packages_importable():
    packages = [
        "pandas",
        "numpy",
        "seaborn",
        "matplotlib",
        "sklearn.model_selection",
        "sklearn.linear_model",
        "sklearn.preprocessing",
        "sklearn.metrics",
        "sklearn.ensemble",
    ]
    for pkg in packages:
        try:
            importlib.import_module(pkg)
        except ImportError as e:
            raise AssertionError(f"Package {pkg} could not be imported: {e}")
