import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/ecommerce_sales.csv")

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Basic information
print("Total Orders:", df["Order_ID"].nunique())
print("Total Quantity Sold:", df["Quantity"].sum())
print("Total Revenue: ₹", df["Sales"].sum())

# Category-wise sales
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nCategory-wise Sales:")
print(category_sales)

# Region-wise sales
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nRegion-wise Sales:")
print(region_sales)

# Monthly sales
monthly_sales = df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum()
print("\nMonthly Sales:")
print(monthly_sales)

# Top products
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products:")
print(top_products)

# Sales by payment method
payment_sales = df.groupby("Payment_Method")["Sales"].sum()
print("\nSales by Payment Method:")
print(payment_sales)

# Create category sales chart
category_sales.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.close()

print("\nAnalysis completed successfully.")
