import pandas as pd
import numpy as np

dataset = pd.read_excel("2021MCMProblemC_DataSet.xlsx")

# read check - printing all data and specific columns
# print(dataset)
# result = dataset.iloc[4:20, 2]
# print(result)

print("Dataset shape:", dataset.shape)
print("\nMissing values:")
print(dataset.isna().sum())