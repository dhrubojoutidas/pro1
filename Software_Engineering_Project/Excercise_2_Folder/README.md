

# 🖥️ Software Engineering  Project 2  -Testing, Modularity & Agile
**Author:** Dhrubo Troyee  
**Course:** ISEN1000 – Introduction to Software Engineering  
**Institution:** Curtin University  
**Trimester:** 3, 2023  

---

## 📌 Overview  
This project demonstrates practical software engineering skills through:
 
- [Q1 – Planning & Agile Project Management](#q1---planning--agile-project-management)
- [Q2 – Functional & Non-Functional Requirements](#-q2--functional--non-functional-requirements)
- [Q3 – Unit Testing (Python)](#-q3--unit-testing-python)  
- [Q4 – Code Modularity & Refactoring](#-q4--code-modularity--refactoring)  
- [Q5 – Ethics & Professionalism](#-q5--ethics--professionalism)  
- [Git Version Control ](#-git-version-control--workflow)  
- [Tools & Technologies Used](#-tools--technologies-used)
- [Running the Tests](#-tools--technologies-used)


📄 **Full Academic Report:**

- [`Exercise2_Report.docx`](Exercise_2_Report.docx )
- [`All coding File`](Excercise_2_all_code)
- [`Exercise_2_question.pdf`](Exercise_2_question.pdf)


## 📝Q1 - Planning & Agile Project Management
Key deliverables include:

-Task Dependencies 
- 13 node AON network diagram  
- ES/EF/LS/LF calculations  
- Slack time & critical path  Method (CPM)
- PERT expected duration  
- Burn‑up chart interpretation  
- Kanban board (two scenarios)  
- Scrum backlog updates for new tasks  (N,O,P)
- Roles of Scrum Master, Product Owner & Dev Team  

**Skills:** Agile planing, scheduling, workflow modelling.
<img width="1173" height="737" alt="image" src="https://github.com/user-attachments/assets/07649569-1510-48d6-a467-fc3cbd13e172" />

---

## 📝 Q2 – Functional & Non‑Functional Requirements  
Analysed two applications:

 * ✔ Weather Update App
 * ✔ Rental Accommodation Booking App

Deliverables:

- Stakeholders & actors  (Human , Non-Human)
- User stories  
- Use cases  
- UML use case diagram  
- Reliability metrics (MTTF, MTBF, ROCOF, Availability)  
- Usability requirements  

**Skills:** Requirements engineering, UML, system analysis.

---

## 📝 Q3 – Unit Testing (Python)

### ✅ Q3PartA – Equivalence Partitioning (Black‑Box)  
- **Production file:** [Q3PartA.py](Excercise_2_all_code/Q3PartA.py)
- **Test file:** [ testQ3PartA.py](Excercise_2_all_code/testQ3PartA.py)
- Tests: 8 EP‑based cases validating valid/invalid partitions for a mean-calculation function.

  
### ✅ Q3PartB – Boundary Value Analysis (BVA)  
- **Production file:** [Q3PartB.py](Excercise_2_all_code/Q3PartB.py)
- **Test file:** [`testQ3PartB.py`](Excercise_2_all_code/testQ3PartB.py)
- Function: `El_COVID(age)`  
- Tests age-based eligibility logic.


### ✅ Q3PartC – White‑Box Testing (Median Function)  
- **Production file:** [Q3PartC.py](Excercise_2_all_code/Q3PartC.py)
- **Test file:** [`testQ3PartC.py`](Excercise_2_all_code/testQ3PartC.py)
-  Median-of-three logic tested for all internal paths.
     

### 🟦 Combined Test Runner

*  Runs all tests for Q3PartA, Q3PartB, and Q3PartC in one script :
  → [`Unittesting.py`](Excercise_2_all_code/Unittesting.py)
---


## 📝 Q4 – Code Modularity & Refactoring  


### ✅ [`Q4.py`](Excercise_2_all_code/Q4.py) – Production  Code (Issues Identified)    
- Global variables  
- Tight coupling  
- Low cohesion  
- Flag‑based logic  
- Repeated code  
- Poor structure  

### ✅ [`newQ4.py`](Excercise_2_all_code/newQ4.py) – Refactored Modular Version  
- No global variables  
- Clear parameters & return values  
- Better naming  
- Improved readability & maintainability  
- Structured main logic

---

## 📝 Q5 – Ethics & Professionalism  

Three software-related ethical case studies:

1. **Flight tracking system – safety & reliability issues**
2. **Video call system – privacy impacts**
3. **Stock market application – security & financial risks**

**Skills:** Ethical analysis, professional responsibility.

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
This project demonstrates core software engineering competencies across planning, analysis, testing, refactoring, and professional practice.
