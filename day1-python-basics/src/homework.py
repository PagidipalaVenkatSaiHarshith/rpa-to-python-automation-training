import json
from pathlib import Path

print("Day 1 - Homework")


def process_job(job):
    try:
        print("Job ID:", job["job_id"])
        print("Task:", job["task"])
        print("Status before:", job["status"])

        if job["status"] == "pending":
            job["status"] = "processing"

        print("Status after:", job["status"])
        print("-" * 40)

    except Exception as e:
        print("Error:", e)
        print("-" * 40)


input_path = Path(__file__).resolve().parent.parent / "data" / "jobs.json"
with open(input_path, "r") as f:
    jobs = json.load(f)

for job in jobs:
    process_job(job)

print("Final jobs output:")
print(json.dumps(jobs, indent=2))
