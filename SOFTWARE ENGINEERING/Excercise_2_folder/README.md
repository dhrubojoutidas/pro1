
# 🖥️ Software Engineering  Project 2  -Testing, Modularity & Agile
**Author:** Dhrubo Troyee  
**Course:** ISEN1000 – Introduction to Software Engineering  
**Institution:** Curtin University  
**Trimester:** 3, 2023  


## 📌 Overview  
This project demonstrates practical software engineering skills through:
 
- [Repository Structure](#-repository-structure)
- [Q1 – Planning & Agile Project Management](#-q1_planning--agile-project-management)  
- [Q2 – Functional & Non-Functional Requirements](#-q2--functional--non-functional-requirements)
- [Q3 – Unit Testing (Python)](#-q3--unit-testing-python)  
- [Q4 – Code Modularity & Refactoring](#-q4--code-modularity--refactoring)  
- [Q5 – Ethics & Professionalism](#-q5--ethics--professionalism)  
- [Git Version Control ](#-git-version-control--workflow)  
- [Tools & Technologies Used](#-tools--technologies-used)
- [Running the Tests)

📄 **Full Academic Report:**
[`Exercise2_Report.pdf`](path/to/report.pdf)
[**Assessment question file**] (./)


---

## 📝 Q1 – Planning & Agile Project Management  
Key deliverables include:

-Task Dependencies & Missing Dependencies Table
- AON network diagram (13 nodes)  
- ES/EF/LS/LF calculations  
- Slack time & critical path  Method (CPM)
- PERT expected duration  
- Burn‑up chart interpretation  
- Kanban board (two scenarios)  
- Scrum backlog updates for new tasks  (N,O,P)
- Roles of Scrum Master, Product Owner & Dev Team  

**Skills:** Agile planing, scheduling, workflow modelling.


---

## 📝 Q2 – Functional & Non‑Functional Requirements  
Analysed two applications:

- ✅ Weather Update App  
- ✅ Rental Accommodation Booking  App  

Deliverables:

- Stakeholders & actors  (Human , Non-Human)
- User stories  
- Written use cases  
- UML use case diagram  
- Reliability metrics (MTTF, MTBF, ROCOF, Availability)  
- Usability requirements  

**Skills:** Requirements engineering, UML, system analysis.

---

## 📝 Q3 – Unit Testing (Python)

### ✅ Q3PartA – Equivalence Partitioning (Black‑Box)  
- **Production file:** [`Q3PartA.py`](Q3PartA.py)  
- **Test file:** [`testQ3PartA.py`](testQ3PartA.py)  
- Function: `funmean(num1, num2, num3, num4)`  
- Tests: 8 EP‑based cases validating valid/invalid partitions.

---

### ✅ Q3PartB – Boundary Value Analysis (BVA)  
- **Production file:** [`Q3PartB.py`](Q3PartB.py)  
- **Test file:** [`testQ3PartB.py`](testQ3PartB.py)  
- Function: `El_COVID(age)`  
- Tests cover all critical boundaries: negative, 0–5, 6–12, 13–16, 17–25, 26–45, 46–60, 61–85, >85.

---

### ✅ Q3PartC – White‑Box Testing (Median Function)  
- **Production file:** [`Q3PartC.py`](Q3PartC.py)  
- **Test file:** [`testQ3PartC.py`](testQ3PartC.py)  
- Focus:  
  - Path/branch coverage  
  - Input validation  
  - Error handling  
  - Simulated user input
     
### 🟦 Combined Test Runner  
- **File:** [`Unittesting.py`](Unittesting.py)  
Runs all tests for Q3PartA, Q3PartB, and Q3PartC in one script.

---

## 📝 Q4 – Code Modularity & Refactoring  

### ✅ Q4.py – Original Code (Issues Identified)  
Problems analysed:  
- Global variables  
- Tight coupling  
- Low cohesion  
- Flag‑based logic  
- Repeated code  
- Poor structure  

### ✅ newQ4.py – Refactored Modular Version  
Improvements:  
- No global variables  
- Clear parameters & return values  
- Better naming  
- Separated responsibilities  
-  A structured  main program  

**Skills:** Refactoring, modular design, code quality improvement.

---

## 📝 Q5 – Ethics & Professionalism  

📜Three detailed case studies📜:

1. safety risks  in **Online Flight Tracking Software (Flightradar24)**  
2. privacy issues  in **Video Calling Software**  
3. Security failures in **Stock Market Application**
   
**Skills:** Ethical reasoning, professional responsibility.

---


## 📌 Git Version Control & Workflow  

### ✅ Branching Strategy  
- `main` → stable branch  
- `development` → active work  
- `feature-*` → new features & fixes  

### ✅ Commands Used  
```sh
git init
git checkout -b development
git add .
git commit -m "Initial commit for Exercise 2"
git push -u origin development
```


---

## 🛠 Tools & Technologies Used  

- Python 3 (VMWare Linux environment)  
- `unittest` (Python testing framework)  
- Draw.io (diagrams)  
- VS Code (development)
- Git & GitHub (version control)
  
---

## ▶️ Running the Tests
```sh
python3 -m unittest
```

Or run individual test files:
```sh
python3 testQ3PartA.py
python3 testQ3PartB.py
python3 testQ3PartC.py
```


---
## 🎯  Final Note
This submission reflects my hands-on understanding of software engineering principles, from planning and testing to ethical reasoning and modular design. The repository is structured to be both academically complete and recruiter-friendly.




Got it — you want me to **write the final polished `README.md`** *right now*, even without knowing your exact folder structure.

So I will create a **clean, recruiter-friendly + academic-friendly README**, and I will **leave the clickable link paths in a format you can easily replace** later.

👉 All you need to do is replace:
`path/to/file` with your real folder names.

Here is your final **professional README.md** 👇
(You can copy-paste directly into GitHub.)

---





# 📝 Q1 – Planning & Agile Project Management

Key deliverables included:

* Task dependency table
* 13-node AON network
* ES/EF/LS/LF calculations
* Slack time identification
* Critical Path Method (CPM)
* PERT expected duration
* Burn-up chart interpretation
* Kanban board (two scenarios)
* Updated Scrum backlog for new tasks (N, O, P)
* Roles of Scrum Master, PO, Dev Team

**Skills:** Agile planning, workflow modelling, engineering scheduling.

---

# 📝 Q2 – Functional & Non-Functional Requirements

Applications analysed:

* ✔ Weather Update App
* ✔ Rental Accommodation Booking App

Deliverables:

* Stakeholders & actors (human & system)
* User stories
* Structured use cases
* UML use case diagram
* Reliability metrics (MTTF, MTBF, ROCOF, availability)
* Usability metrics

**Skills:** Requirements engineering, UML, system modelling.

---

# 📝 Q3 – Unit Testing (Python)

### ✔ Q3PartA – Equivalence Partitioning (EP)

* **File:** [`Q3PartA.py`](path/to/Q3PartA.py)
* Tests input partitions for a mean-calculation function.
* **Test file:** [`testQ3PartA.py`](path/to/testQ3PartA.py)

---

### ✔ Q3PartB – Boundary Value Analysis (BVA)

* **File:** [`Q3PartB.py`](path/to/Q3PartB.py)
* Tests age-based eligibility logic.
* **Test file:** [`testQ3PartB.py`](path/to/testQ3PartB.py)

---

### ✔ Q3PartC – White-Box Testing

* **File:** [`Q3PartC.py`](path/to/Q3PartC.py)
* Median-of-three logic tested for all internal paths.
* **Test file:** [`testQ3PartC.py`](path/to/testQ3PartC.py)

---

### 🟦 Combined Test Runner

* Runs all test suites together:
  → [`Unittesting.py`](path/to/Unittesting.py)

---

## 📝 Q4 – Code Modularity & Refactoring

### ❌ Q4.py – Issues Identified

* Global variables
* Tight coupling
* Low cohesion
* Repeated code
* Mixed responsibilities
* Hard to test

### ✔ newQ4.py – Refactored Version

* Clean modular functions
* No global variables
* Clear parameter passing
* Structured main logic
* Improved readability & maintainability

---

# 📝 Q5 – Ethics & Professionalism

Three software-related ethical case studies:

1. **Flight tracking system – safety & reliability issues**
2. **Video call system – privacy impacts**
3. **Stock market application – security & financial risks**

**Skills:** Ethical analysis, professional responsibility.

---

# ⛓ Git Version Control

* Proper branching workflow
* Feature branches (`feature-*`)
* Clean commit history

Basic commands used:

```sh
git init
git checkout -b development
git add .
git commit -m "Initial commit"
git push -u origin development
```

---

# ▶️ Running the Tests

Run all:

```sh
python3 -m unittest
```

Run specific tests:

```sh
python3 testQ3PartA.py
python3 testQ3PartB.py
python3 testQ3PartC.py
```

---

# 🎯 Final Note

This project demonstrates core software engineering competencies across planning, analysis, testing, refactoring, and professional practice.
The repository is structured for **easy navigation**, whether you're a recruiter or an academic reviewer.

Thank you for viewing my work!



Thank you for reviewing my work!

