print("Day 1 - Conditions")

status = "pending"

if status == "pending":
    print("Start processing")
else:
    print("Skip job")

job_status = "completed"

if job_status == "completed":
    print("Job finished successfully")
elif job_status == "failed":
    print("Job failed")
else:
    print("Job still in progress")
