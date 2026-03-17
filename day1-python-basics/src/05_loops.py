print("Day 1 - Loops")

jobs = [101, 102, 103]

for job_id in jobs:
    print("Processing job:", job_id)

print("-" * 40)

job_list = [
    {"job_id": 1, "task": "login"},
    {"job_id": 2, "task": "download"},
    {"job_id": 3, "task": "upload"}
]

for job in job_list:
    print("Job ID:", job["job_id"], "| Task:", job["task"])
