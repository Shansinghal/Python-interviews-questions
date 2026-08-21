import pandas as pd
import numpy as np

sales = np.array([
    [12000, 15000, 13000, 17000, 16000, 18000],  # Rahul
    [10000, 11000, 12500, 12000, 14000, 15000],  # Priya
    [18000, 17500, 19000, 21000, 20000, 22000],  # Amit
    [9000,  9500,  10000, 10500, 11000, 11500],  # Neha
    [15000, 14500, 16000, 15500, 17000, 16500]   # Karan
])

employees = np.array(["Rahul", "Priya", "Amit", "Neha", "Karan"])

#Calculate the total sales made by each employee.
#Find the employee with the highest total sales.
#Calculate the average monthly sales for each employee.
#Find the month with the highest total sales across all employees.
#Find all employees whose average monthly sales > 14,000.
#Calculate the percentage contribution of each employee to the overall sales.


#Solutions

# 1. Calculate total sales made by each employee
sum_sales = np.sum(sales, axis=1)

print("Total sales:")
print(sum_sales)


# 2. Find employee with highest total sales
max_index = np.argmax(sum_sales)
print("\nEmployee with highest sales:")
print(employees[max_index])


# 3. Calculate average monthly sales for each employee
avg_monthly_sales = np.mean(sales, axis=1)

print("\nAverage monthly sales:")
print(avg_monthly_sales)


# 4. Find the month with highest total sales
monthly_sales = np.sum(sales, axis=0)

highest_month = np.argmax(monthly_sales)

print("\nMonthly sales:")
print(monthly_sales)

print("Month with highest sales:")
print(highest_month + 1)


# 5. Find employees whose average monthly sales > 14,000
high_performers = employees[avg_monthly_sales > 14000]

print("\nEmployees with average sales > 14,000:")
print(high_performers)


# 6. Calculate percentage contribution of each employee
total_sales = np.sum(sum_sales)

percentage_contribution = (sum_sales / total_sales) * 100

print("\nPercentage contribution:")
print(percentage_contribution)