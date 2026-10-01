-- E-Commerce Sales Analysis

-- 1. Total Revenue
SELECT SUM(Sales) AS Total_Revenue
FROM ecommerce_sales;

-- 2. Total Quantity Sold
SELECT SUM(Quantity) AS Total_Quantity_Sold
FROM ecommerce_sales;

-- 3. Category-wise Sales
SELECT Category, SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 4. Region-wise Sales
SELECT Region, SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 5. Top 5 Products
SELECT Product, SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Product
ORDER BY Total_Sales DESC
LIMIT 5;

-- 6. Payment Method Analysis
SELECT Payment_Method, SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Payment_Method
ORDER BY Total_Sales DESC;

-- 7. Customer Type Analysis
SELECT Customer_Type, SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Customer_Type
ORDER BY Total_Sales DESC;
