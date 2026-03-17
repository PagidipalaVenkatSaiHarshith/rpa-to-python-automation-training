import json
from pathlib import Path

print("Day 1 - JSON Basics")

job_data = [
    {"job_id": 1, "task": "login", "status": "pending"},
    {"job_id": 2, "task": "download", "status": "pending"},
    {"job_id": 3, "task": "upload", "status": "pending"}
]

print("Python object:")
print(job_data)

print("-" * 40)

json_text = json.dumps(job_data, indent=2)

print("JSON text:")
print(json_text)

print("-" * 40)

output_path = Path(__file__).resolve().parent.parent / "data" / "jobs_output.json"
with open(output_path, "w") as f:
    json.dump(job_data, f, indent=2)

print(f"{output_path.name} file created")

print("-" * 40)

input_path = Path(__file__).resolve().parent.parent / "data" / "jobs.json"
with open(input_path, "r") as f:
    jobs_from_file = json.load(f)

print("Read from jobs.json:")
print(jobs_from_file)

print("-" * 40)

for job in jobs_from_file:
    print(f"Job {job['job_id']} -> {job['task']} -> {job['status']}")
