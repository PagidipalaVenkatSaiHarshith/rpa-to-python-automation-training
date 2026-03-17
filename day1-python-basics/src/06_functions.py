print("Day 1 - Functions")


def process_job(job_id):
    print(f"Processing job {job_id}")


def process_job_details(job):
    print(f"Job {job['job_id']} is for task: {job['task']}")


process_job(101)
process_job(202)

sample_job = {
    "job_id": 301,
    "task": "invoice_download"
}

process_job_details(sample_job)
