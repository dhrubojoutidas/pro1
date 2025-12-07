
# 🖥️ Software Engineering Project 2  
**Author:** Dhrubo Troyee  
**Course:** ISEN1000 – Introduction to Software Engineering  
**Institution:** Curtin University  
**Trimester:** 3, 2023  

---

## 📌 Overview  
This repository contains my full submission for **Exercise 2**, demonstrating practical skills across:

- Agile project management  
- Requirements engineering  
- UML modelling  
- Python unit testing (EP, BVA, white‑box)  
- Code modularity analysis & refactoring  
- Ethical reasoning  
- Git version control  

The goal of this project was to apply core software engineering principles through documentation, analysis, and hands‑on coding.

---


## 📑 Table of Contents  
- [Repository Structure](#-repository-structure)  
- [Q1 – Planning & Agile Project Management](#-q1_planning--agile-project-management)  
- [Q2 – Functional & Non-Functional Requirements](#-q2--functional--non-functional-requirements)
- [Q3 – Unit Testing (Python)](#-q3--unit-testing-python)  
- [Q4 – Code Modularity & Refactoring](#-q4--code-modularity--refactoring)  
- [Q5 – Ethics & Professionalism](#-q5--ethics--professionalism)  
- [Git Version Control & Workflow](#-git-version-control--workflow)  
- [Tools & Technologies Used](#-tools--technologies-used)  

---

### 📂 **Repository Structure**
- [Assessment question file](presentations/CTP1_Project_IDEA_1st_pptx)
- [All Python code for Q3 & Q4]( CTP_1/CTP1_Equipment_List_2nd_pptx.pdf  )
- [README.md](CTP1_Project_Logic_3rd_PPTX.pdf)
- [Report Document](CTP1_Project_Logic_3rd_PPTX.pdf)

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

1. **Online Flight Tracking Software (Flightradar24)**  
   - Planning failures → safety risks  
   - Incorrect data → collisions, financial loss  

2. **Video Calling Software**  
   - Project management failures → delays, privacy issues  

3. **Stock Market Application**  
   - Security failures → financial harm, data breaches
     
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

## 🎯  Final Note
This submission reflects my hands-on understanding of software engineering principles, from planning and testing to ethical reasoning and modular design. The repository is structured to be both academically complete and recruiter-friendly.

Thank you for reviewing my work!

