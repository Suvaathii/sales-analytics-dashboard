import pandas as pd

df = pd.read_csv("data/sales_data.csv")

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numeric values with 0
df["Sales"] = df["Sales"].fillna(0)
df["Quantity"] = df["Quantity"].fillna(0)

print("\nCleaned Data:")
print(df)

print("\nTotal Sales:", df["Sales"].sum())