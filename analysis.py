import pandas as pd

df = pd.read_csv("sales_data.csv")

print(df)
print("\nTotal Sales:", df["Sales"].sum())
print("\nCategory Sales:")
print(df.groupby("Category")["Sales"].sum())