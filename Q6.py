import pandas as pd
import numpy as np
data = {
    "transaction_id": range(1, 16),

    "customer_id": [
        "C01","C02","C03","C01","C04",
        "C02","C05","C03","C01","C04",
        "C05","C02","C03","C06","C01"
    ],

    "transaction_date": [
        "2026-07-01 10:30:00",
        "2026-07-01 11:15:00",
        "2026-07-02 09:20:00",
        "2026-07-03 14:10:00",
        "2026-07-04 16:45:00",
        "2026-07-05 12:30:00",
        "2026-07-06 18:20:00",
        "2026-07-07 20:15:00",
        "2026-07-08 09:10:00",
        "2026-07-09 13:45:00",
        "2026-07-10 17:30:00",
        "2026-07-11 11:00:00",
        "2026-07-12 19:40:00",
        "2026-07-13 08:50:00",
        "2026-07-14 21:10:00"
    ],

    "category": [
        "Electronics","Grocery","Electronics","Grocery","Clothing",
        "Electronics","Grocery","Clothing","Electronics","Grocery",
        "Clothing","Electronics","Grocery","Electronics","Clothing"
    ],

    "amount": [
        5000,1200,3500,1800,2500,
        4500,900,3200,6000,1500,
        2800,5200,1100,4800,3500
    ]
}

transactions = pd.DataFrame(data)

#Convert transaction_date to datetime.
#Add month, day, and hour columns.
#Categorize transactions into:
#"Morning" → before 12 PM
#"Afternoon" → 12 PM to 5 PM
#"Evening" → after 5 PM
#Find total transaction amount by category.
#Find the top 3 customers by total transaction amount.
#Find the average transaction amount by category.
#Find the highest-value transaction for each customer.
#Find the day with the highest total transaction amount.
#Find customers whose total spending is above the average customer spending.
#Find the percentage of transactions that occurred after 5 PM.
#Find the category with the highest average transaction amount.
#Sort the transactions chronologically and calculate the difference in hours between consecutive transactions.
#Find the longest gap between two consecutive transactions.
#Identify the customer responsible for the highest-value transaction.
#Bonus: Calculate a 3-day rolling average of total daily transaction amount.


# Convert date
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Date components
transactions["month"] = transactions["transaction_date"].dt.month
transactions["day"] = transactions["transaction_date"].dt.day
transactions["hour"] = transactions["transaction_date"].dt.hour

# Time categorization
conditions = [
    transactions["hour"] < 12,
    transactions["hour"].between(12, 17),
    transactions["hour"] > 17
]

choices = ["Morning", "Afternoon", "Evening"]

transactions["time_period"] = np.select(
    conditions,
    choices
)

# Total amount by category
total_amt = transactions.groupby("category")["amount"].sum()
print(total_amt)

# Top 3 customers
total_cust_trans = transactions.groupby("customer_id")["amount"].sum()
top_customers = total_cust_trans.nlargest(3)
print(top_customers)

# Average transaction amount by category
avg_per_cat = transactions.groupby("category")["amount"].mean()
print(avg_per_cat)

# Highest-value transaction for each customer
highest_transactions = transactions.loc[
    transactions.groupby("customer_id")["amount"].idxmax()
]

print(highest_transactions[
    ["customer_id", "transaction_id", "amount"]
])

# Day with highest total transaction amount
transactions["date"] = transactions["transaction_date"].dt.date

daily_amount = transactions.groupby("date")["amount"].sum()

print(daily_amount.idxmax())

# Customers above average spending
avg_spending = total_cust_trans.mean()

above_average = total_cust_trans[
    total_cust_trans > avg_spending
]

print(above_average)