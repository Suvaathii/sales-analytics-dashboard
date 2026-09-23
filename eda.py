import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")

# Category-wise sales
category_sales = df.groupby("Category")["Sales"].sum()

print("Category Sales:")
print(category_sales)

# Create a bar chart
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("sales_by_category.png")

plt.show()

