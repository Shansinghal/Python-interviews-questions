import pandas as pd
import numpy as np

data = {
    "employee_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": ["Rahul", "Priya", "Amit", "Neha", "Karan", "Simran", "Arjun", "Megha"],
    "department": ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance", "IT"],
    "salary": [75000, 65000, np.nan, 82000, 90000, 62000, np.nan, 78000],
    "experience": [3, 2, 5, 7, 8, 1, 4, np.nan],
    "joining_date": [
        "2022-06-15",
        "2023-01-10",
        "2021-03-20",
        "2019-07-01",
        "2018-11-12",
        "2024-02-15",
        "2022-09-01",
        "2020-05-18"
    ]
}

df = pd.DataFrame(data)

#Display the basic information about the DataFrame.
#Find the number of missing values in each column.
#Replace missing salary values with the median salary of that department.
#Replace missing experience with the overall median experience.
#Convert joining_date into a proper Pandas datetime column.
#Add a column called experience_level:
#< 3 years → "Junior"
#3–5 years → "Mid"
#> 5 years → "Senior"
#Sort employees by salary from highest to lowest.
#Find the employee with the highest salary in each department.


#Solutions



# 1. Display basic information
print(df.info())


# 2. Find number of missing values in each column
print("\nMissing values:")
print(df.isnull().sum())


# 3. Replace missing salary with median salary of that department
df["salary"] = df["salary"].fillna(
    df.groupby("department")["salary"].transform("median")
)

print("\nSalary after filling missing values:")
print(df)


# 4. Replace missing experience with overall median
df["experience"] = df["experience"].fillna(
    df["experience"].median()
)

print("\nExperience after filling missing values:")
print(df)


# 5. Convert joining_date to datetime
df["joining_date"] = pd.to_datetime(df["joining_date"])

print("\nJoining date:")
print(df["joining_date"])


# 6. Create experience_level
df["experience_level"] = np.where(
    df["experience"] < 3,
    "Junior",
    np.where(
        df["experience"] <= 5,
        "Mid",
        "Senior"
    )
)

print("\nExperience level:")
print(df[["name", "experience", "experience_level"]])


# 7. Sort employees by salary from highest to lowest
sorted_df = df.sort_values("salary", ascending=False)

print("\nEmployees sorted by salary:")
print(sorted_df[["name", "salary"]])


# 8. Employee with highest salary in each department
highest_salary = df.loc[
    df.groupby("department")["salary"].idxmax()
]

print("\nHighest paid employee in each department:")
print(highest_salary[["department", "name", "salary"]])