# Day 1 Homework

## Scenario

You are given a file called **jobs.json** which contains automation tasks.

Your job is to write a Python script that processes these tasks.

---

## Tasks

1. Read the jobs.json file.

2. Loop through each job.

3. Print the following fields:

- job_id
- task
- status

Example output:

Processing Job 1  
Task: login  
Status: pending

---

## Processing Logic

If job status is **pending**

Change it to:

processing

---

## Function Requirement

Create a function:

process_job(job)

This function should:

- print job details
- update job status

---

## Error Handling

Use try/except to handle errors.

The script should not crash if a job is missing fields.

---

## Final Output

After processing all jobs print the updated list.

---

## Bonus

Add a priority field and display it.