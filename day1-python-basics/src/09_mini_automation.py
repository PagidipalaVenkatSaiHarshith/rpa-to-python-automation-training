import json
from pathlib import Path

print("Day 1 - Mini Automation Example")


def process_job(job):
    try:
        print(f"Starting job {job['job_id']}")
        print(f"Task: {job['task']}")
        print(f"Status before: {job['status']}")

        job["status"] = "completed"

        print(f"Status after: {job['status']}")
        print("-" * 40)

    except Exception as e:
        print(f"Error in job {job.get('job_id', 'unknown')}: {e}")
        print("-" * 40)


input_path = Path(__file__).resolve().parent.parent / "data" / "jobs.json"
with open(input_path, "r") as f:
    jobs = json.load(f)

for job in jobs:
    process_job(job)
