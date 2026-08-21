import numpy as np
import pandas as pd

attendance_data = {
    "employee_id": [101,101,101,102,102,102,103,103,103,104,104,104],
    "employee": ["Rahul","Rahul","Rahul","Priya","Priya","Priya",
                 "Amit","Amit","Amit","Neha","Neha","Neha"],
    "login_time": [
        "2026-08-10 09:05:00",
        "2026-08-11 08:55:00",
        "2026-08-12 09:20:00",
        "2026-08-10 09:30:00",
        "2026-08-11 09:10:00",
        "2026-08-12 08:50:00",
        "2026-08-10 08:45:00",
        "2026-08-11 08:40:00",
        "2026-08-12 09:05:00",
        "2026-08-10 10:00:00",
        "2026-08-11 09:45:00",
        "2026-08-12 10:15:00"
    ],
    "logout_time": [
        "2026-08-10 18:00:00",
        "2026-08-11 17:30:00",
        "2026-08-12 18:15:00",
        "2026-08-10 18:30:00",
        "2026-08-11 17:45:00",
        "2026-08-12 18:00:00",
        "2026-08-10 17:30:00",
        "2026-08-11 17:20:00",
        "2026-08-12 18:10:00",
        "2026-08-10 19:00:00",
        "2026-08-11 18:30:00",
        "2026-08-12 19:15:00"
    ]
}

attendance = pd.DataFrame(attendance_data)

#Convert login_time and logout_time to datetime.
attendance["login_time"] = pd.to_datetime(attendance["login_time"])
attendance["logout_time"] = pd.to_datetime(attendance["logout_time"])


#Create a column working_hours.
attendance["working_hours"] = (
    attendance["logout_time"] - attendance["login_time"]
).dt.total_seconds() / 3600


#Find the average working hours of each employee.
avg_hours = attendance.groupby("employee")["working_hours"].mean()
print(avg_hours)


#Find employees whose average login time is after 9:00 AM.
login_seconds = (
    attendance["login_time"].dt.hour * 3600
    + attendance["login_time"].dt.minute * 60
    + attendance["login_time"].dt.second
)

attendance["login_seconds"] = login_seconds

avg_login = attendance.groupby("employee")["login_seconds"].mean()
after_9 = avg_login > 9 * 3600
print(avg_login[after_9])

#Find the earliest login time recorded.
earliest_login = attendance["login_time"].min()
print(earliest_login)

#Find the latest logout time recorded.
latest_logout = attendance["logout_time"].max()
print(latest_logout)

#Find the day on which the most employees logged in before 9:00 AM.
before_9 = attendance["login_time"].dt.time < pd.to_datetime("09:00:00").time()

early_logins = (
    attendance[before_9]
    .groupby(attendance.loc[before_9, "login_time"].dt.date)
    .size()
)

print(early_logins)


#Add a column containing the day of the week.
attendance["day_of_week"] = attendance["login_time"].dt.day_name()
print(attendance[["employee", "login_time", "day_of_week"]])

#Find the average working hours by day of the week.
avg_hours_day = (
    attendance.groupby("day_of_week")["working_hours"]
    .mean()
)

print(avg_hours_day)


#Identify employees who worked more than 9 hours on any day.
more_than_9 = attendance[attendance["working_hours"] > 9]
employees_over_9 = more_than_9["employee"].unique()

print(employees_over_9)