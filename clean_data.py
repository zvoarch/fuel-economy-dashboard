"""Build data/vehicles_clean.csv from the raw EPA download.

Download vehicles.csv from https://www.fueleconomy.gov/feg/download.shtml,
put it in data/raw/, then run: python clean_data.py
"""

import pandas as pd

RAW_PATH = "data/raw/vehicles.csv"
CLEAN_PATH = "data/vehicles_clean.csv"

COLUMNS = ["make", "model", "year", "cylinders", "fuelType1", "atvType", "comb08", "fuelCost08"]


def clean(df):
    """Keep the columns the app uses and remove rows it can't use."""
    df = df[COLUMNS]

    # Remove hydrogen vehicles and rows with no fuel type (EPA has no fuel cost for them)
    df = df[df["fuelType1"].notna() & (df["fuelType1"] != "Hydrogen")].copy()

    # An empty technology type means a regular engine (no hybrid, electric or flex-fuel system)
    df["atvType"] = df["atvType"].fillna("Conventional")

    # Whole numbers for cylinders; electric vehicles have none, so they stay empty
    df["cylinders"] = df["cylinders"].astype("Int64")

    return df.sort_values(["year", "make", "model"])


if __name__ == "__main__":
    raw = pd.read_csv(RAW_PATH, usecols=COLUMNS)
    clean_df = clean(raw)
    clean_df.to_csv(CLEAN_PATH, index=False)
    print(f"Saved {len(clean_df):,} of {len(raw):,} vehicles to {CLEAN_PATH}")
