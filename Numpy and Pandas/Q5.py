import pandas as pd

pipeline_data = {
    "run_id": [1,2,3,4,5,6,7,8,9,10,11,12],
    "pipeline": ["orders","orders","orders","users","users","users",
                  "payments","payments","payments","orders","users","payments"],
    "run_date": [
        "2026-08-01 01:15:00",
        "2026-08-02 01:10:00",
        "2026-08-03 01:20:00",
        "2026-08-01 02:00:00",
        "2026-08-02 02:05:00",
        "2026-08-03 02:10:00",
        "2026-08-01 03:00:00",
        "2026-08-02 03:10:00",
        "2026-08-03 03:05:00",
        "2026-08-04 01:25:00",
        "2026-08-04 02:15:00",
        "2026-08-04 03:20:00"
    ],
    "records_processed": [10000,12000,11000,5000,5500,5300,8000,8500,8200,13000,5600,9000],
    "duration_minutes": [20,25,22,10,12,11,30,32,31,27,13,35],
    "status": ["success","success","failed","success","success","success",
               "success","failed","success","success","success","success"]
}

pipeline = pd.DataFrame(pipeline_data)

#Convert run_date to datetime.
#Find the total number of records processed by each pipeline.
#Find the average pipeline duration for each pipeline.
#Calculate the success rate of each pipeline.
#Find the pipeline with the highest average duration.
#Find all failed pipeline runs.
#Find the date on which the maximum number of records were processed.
#Calculate the average records processed per successful run for each pipeline.
#Find the pipeline that processed the most records in a single run.
#For each pipeline, identify its latest run.


#Solutions

# 1. Convert run_date to datetime
pipeline["run_date"] = pd.to_datetime(pipeline["run_date"])


# 2. Total records processed by each pipeline
total_records = (
    pipeline
    .groupby("pipeline")["records_processed"]
    .sum()
)

print("Total records:")
print(total_records)


# 3. Average pipeline duration
avg_duration = (
    pipeline
    .groupby("pipeline")["duration_minutes"]
    .mean()
)

print("\nAverage duration:")
print(avg_duration)


# 4. Success rate of each pipeline
pipeline["success"] = pipeline["status"] == "success"

success_rate = (
    pipeline
    .groupby("pipeline")["success"]
    .mean() * 100
)

print("\nSuccess rate:")
print(success_rate)


# 5. Pipeline with highest average duration
slowest_pipeline = avg_duration.idxmax()

print("\nSlowest pipeline:")
print(slowest_pipeline)


# 6. Total failed pipeline runs
total_failed = (
    pipeline["status"] == "failed"
).sum()

print("\nTotal failed runs:")
print(total_failed)


# 7. Find all failed runs
failed_runs = pipeline[
    pipeline["status"] == "failed"
]

print("\nFailed runs:")
print(failed_runs)


# 8. Date with maximum records processed
pipeline["date"] = pipeline["run_date"].dt.date

daily_records = (
    pipeline
    .groupby("date")["records_processed"]
    .sum()
)

max_record_date = daily_records.idxmax()

print("\nDate with maximum records:")
print(max_record_date)


# 9. Average records processed per successful run
successful = pipeline[
    pipeline["status"] == "success"
]

avg_records = (
    successful
    .groupby("pipeline")["records_processed"]
    .mean()
)

print("\nAverage records per successful run:")
print(avg_records)


# 10. Pipeline/run with maximum records in a single run
max_run = pipeline.loc[
    pipeline["records_processed"].idxmax()
]

print("\nRun with maximum records:")
print(max_run)


# 11. Latest run for each pipeline
latest_runs = pipeline.loc[
    pipeline.groupby("pipeline")["run_date"].idxmax()
]

print("\nLatest run for each pipeline:")
print(latest_runs)