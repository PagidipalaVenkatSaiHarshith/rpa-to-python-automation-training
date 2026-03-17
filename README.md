
# RPA to Python Automation Training

This repository contains a structured **7‑day training program** designed to transition from **UiPath‑based RPA workflows** to **Python automation using Playwright, SQL Server, and Azure Queue**.

The goal is to help an RPA developer understand how automation pipelines can be implemented using **Python‑based frameworks instead of drag‑and‑drop tools**.

---

# Training Objective

By the end of this training, the learner should be able to:

- Write Python scripts for automation
- Work with structured data (JSON, dictionaries, lists)
- Connect Python scripts to SQL Server
- Automate web workflows using Playwright
- Process jobs using Azure Queue
- Build a simple automation worker that processes jobs end‑to‑end

---

# Technology Stack

This training uses the following technologies:

- Python
- Playwright (browser automation)
- SQL Server
- Azure Queue Storage
- JSON for data exchange
- GitHub for version control

---

# UiPath to Python Mapping

| UiPath Concept | Python Equivalent |
|---|---|
| Workflow | Python script |
| Activity | Python function |
| Selector | Playwright locator |
| Try Catch | try/except |
| DataTable | list / dictionary |
| Orchestrator Queue | Azure Queue |
| Invoke Workflow | Function call / module |

---

# Training Structure

The training is divided into **7 sessions**, each focusing on a core concept required for Python‑based automation.

| Day | Topic |
|---|---|
| Day 1 | Python Basics for Automation |
| Day 2 | Python + SQL Server Integration |
| Day 3 | Playwright Browser Automation Basics |
| Day 4 | Advanced Playwright Automation |
| Day 5 | Azure Queue Integration |
| Day 6 | Building an Automation Worker |
| Day 7 | End‑to‑End Automation Pipeline |

---

# Repository Structure

```
rpa-to-python-automation-training/
│
├── day1-python-basics/
├── day2-sql-server/
├── day3-playwright-basics/
├── day4-playwright-advanced/
├── day5-azure-queue/
├── day6-automation-worker/
└── day7-end-to-end-project/
```

Each folder contains:
- example scripts
- exercises
- small automation examples

---

# End Goal

By Day 7, we will build a simple **automation pipeline**:

```
Azure Queue
      ↓
Python Worker
      ↓
Playwright Automation
      ↓
SQL Server Update
```

This architecture replaces traditional **UiPath orchestrator-based automation** with a **code-driven automation system**.

---

# Running the Examples

Clone the repository:

```
git clone https://github.com/yourusername/rpa-to-python-automation-training.git
```

Navigate to a specific day:

```
cd day1-python-basics
```

Run a script:

```
python 01_variables.py
```

---

# Recommended Tools

- Python 3.10+
- VS Code
- Playwright
- Git

---

# Notes

This repository focuses on **practical automation development**, not theoretical programming.

The examples are designed to help RPA developers transition smoothly into **Python-based automation engineering**.

---

# Future Extensions

Possible future improvements:

- Docker-based automation workers
- Logging frameworks
- Distributed queue processing
- CI/CD pipelines for automation deployment
