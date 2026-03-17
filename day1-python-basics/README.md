
# Day 1 – Python Basics for Automation

## Objective

The goal of Day 1 is to introduce the Python fundamentals required for building automation scripts.  
Since the learner already has experience with RPA tools like UiPath, this session focuses on mapping 
RPA concepts to Python-based automation.

By the end of this session you should understand:

- Python syntax and execution
- Variables and basic data types
- Lists and dictionaries
- Conditional logic
- Loops
- Functions
- Error handling using try/except
- JSON handling
- Basic automation script structure

---

## Why Python for Automation?

Traditional RPA tools use drag‑and‑drop workflows.  
In Python automation, the same logic is written as code.

Example transformation:

UiPath Workflow  
↓  
Python Script

Automation activities are replaced with Python logic.

| UiPath | Python |
|------|------|
| Workflow | Python script |
| Activity | Python statement |
| Assign | Variable assignment |
| If activity | if condition |
| For Each | for loop |
| Try Catch | try / except |
| Invoke Workflow | Function |

---

## Topics Covered

1. Python variables and data types
2. Lists
3. Dictionaries
4. Conditions (if / else)
5. Loops (for loops)
6. Functions
7. Error handling (try / except)
8. JSON data handling
9. Mini automation example

---

## Folder Structure

day1-python-basics/

data/
jobs.json

src/
01_variables.py
02_lists.py
03_dictionaries.py
04_conditions.py
05_loops.py
06_functions.py
07_try_except.py
08_json_basics.py
09_mini_automation.py
homework.py

---

## Example Automation Flow

Input Data  
↓  
Python Script  
↓  
Process Each Job  
↓  
Update Job Status

---

## Exercise

Modify the automation script to:

- Read jobs from `jobs.json`
- Process each job
- Change job status from `pending` to `processing`
- Handle errors using `try/except`

---

## Homework

Create a script that:

1. Reads job data from JSON
2. Loops through all jobs
3. Prints job details
4. Updates job status
5. Uses try/except to handle failures

---

## Next Session

Day 2 will cover:

Python + SQL Server integration.

We will start building automation workflows that interact with databases.
