# Exercises — Rebuilding Programming Logic

Personal repository for daily practice aimed at recovering and sharpening algorithmic fluency by solving problems in **Python** and **SQL**.

Profile: Data Scientist / ML Engineer. The goal isn't to produce code, but to train the muscle of **decomposing problems and reaching solutions fast**, using a strict self-review methodology.

---

## How it works

- **One exercise per day**, with a **strict 30–60 min timebox**.
- Before coding: write the approach in 2–3 lines and estimate the complexity.
- If it doesn't come out in time: stop, understand the solution, and **redo it the next day without looking**.
- Each exercise ships with `pytest` tests — defining the test cases *before* solving is part of the exercise.
- When done, state the solution's **time and space complexity**.

Difficulty ramps up in phases over ~8 weeks: from reactivating fundamentals, to patterns, decomposition, and finally advanced topics.

---

## What we'll work on with Python

The focus is logic and data structures, progressing from simple to complex.

### Phase 1 · Reactivation
Lists, strings, and dictionaries · `set` and `Counter` · comprehensions · sorting with `key` and tie-breaks · slicing.

### Phase 2 · Patterns
Two pointers · sliding window · hash maps and frequency counting · prefix sums.

### Phase 3 · Decomposition
Recursion · backtracking · binary search · sorting · matrix traversal.

### Phase 4 · Advanced
Dynamic programming (1D → 2D) · graphs and trees (BFS / DFS) · heaps (`heapq`).

### DS / MLE extension *(post phase 4)*
Implementing metrics from scratch (AUC, F1, NDCG) · vectorization with NumPy · feature-engineering logic · sampling.

> The **SQL** track runs in parallel (aggregations and joins → CTEs and window functions → gaps & islands and complex analytics), practiced locally with DuckDB.

---

## Repository structure

```
exercises/
├─ week_01/
│  ├─ day_01_top_k.py
│  └─ test_day_01.py
├─ week_02/
├─ requirements.txt
├─ .gitignore
└─ README.md
```

One solution file + one test file per exercise, grouped by week.

---

## Environment setup

```bash
py -m venv .venv
.venv\Scripts\Activate.ps1        # Windows / PowerShell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Base dependencies: `pytest` (tests) and `duckdb` (SQL practice). `pandas` and `numpy` are added when reaching the DS/MLE extension.

Run a given day's tests:
```bash
pytest week_01/test_day_01.py -v
```
