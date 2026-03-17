print("Day 1 - Dictionaries")

job = {
    "job_id": 101,
    "task": "login",
    "status": "pending"
}

print("Full dictionary:", job)
print("Task:", job["task"])
print("Status:", job["status"])

job["status"] = "processing"

print("Updated job:", job)
