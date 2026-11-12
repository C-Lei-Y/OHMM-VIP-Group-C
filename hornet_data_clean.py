import pandas as pd
import numpy as np

dataset = pd.read_excel("2021MCMProblemC_DataSet.xlsx")
'''
Check Excel Sheet Datatypes
print(dataset.head())
print(dataset.columns.tolist())
print(dataset.dtypes)
'''

print("Dataset shape:", dataset.shape)
print("\nMissing values:")
print(dataset.isna().sum())

print("\nDuplicate records:")
print(dataset["GlobalID"].duplicated().sum())

dataset["Detection Date"] = pd.to_datetime(dataset["Detection Date"], errors="coerce")
dataset["Submission Date"] = pd.to_datetime(dataset["Submission Date"], errors="coerce")
invalid_dates = (dataset["Detection Date"] > dataset["Submission Date"])

print("\nInvalid dates:", invalid_dates.sum(), "\n")

dataset["target"] = dataset["Lab Status"].map({
    "Positive ID": 1,
    "Negative ID": 0
    })

print("Classification counts:")
print(dataset["target"].value_counts(dropna=False))

invalid_locations = (
    ~dataset["Latitude"].between(-90, 90)
    | ~dataset["Longitude"].between(-180, 180)
)

print("\nInvalid geographic coordinates:")
print(invalid_locations.sum())

outside_region = (
    ~dataset["Latitude"].between(45.5, 49.1)
    | ~dataset["Longitude"].between(-125.0, -116.8)
)

print("\nLocations outside study region:")
print(outside_region.sum())

print("\nSuspicious location records:")
print(dataset.loc[
    invalid_locations | outside_region,
    ["GlobalID", "Latitude", "Longitude"]
].head(20))
