# 🖥️  Software Engineering Project 2
**Author:** Dhrubo Troyee  
**Course:** ISEN1000 - Introduction to Software Engineering  
**Institution:** Curtin University  
**Trimester:** 3, 2023  
**Repository:**  `studentID_Exercise2_ISE`

---

## 📌 Overview  
This repository contains all work completed for **Exercise Submission 2**, demonstrating practical skills across:

- Agile project management  
- AON/PERT scheduling & critical path analysis  
- Requirements engineering  
- UML modelling  
- Unit testing (black‑box, white‑box, BVA)  
- Python test automation  
- Code modularity analysis & refactoring  
- Professional documentation  
- Git version control workflows  

---

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

## 📝 Q1_Planning & Agile Project Management  

- Task Dependencies & Missing Dependencies Table
- AON Graph (13‑node network)
- Early Start (ES), Early Finish (EF), Late Start (LS), Late Finish (LF)
-  Slack Time Identification
-  Critical Path Method (CPM)
-  PERT Chart & Expected Duration Calculation
-  Burn‑up Chart Interpretation
-  Kanban Board (Two Scenarios)
-  Scrum Backlog Adjustment for New Tasks (N, O, P)
-  Roles & Responsibilities of Scrum Master, Product Owner & Dev Team

**Skills Demonstrated:**  
Agile planning, scheduling, forecasting, workflow modelling.
    
---

## 📝 Q2 – Functional & Non‑Functional Requirements  

Applications analysed:

- ✅ Mobile Weather Update App  
- ✅ Rental Accommodation Booking App  

Includes:

- Stakeholder Identification  
- Actor Identification (Human & Non‑Human)  
- User Stories (per actor)  
- Written Use Cases (with extensions)  
- UML Use Case Diagram  
- Reliability Metrics (MTTF, MTBF, ROCOF, Availability)  
- Usability Requirements  

**Skills Demonstrated:**  
Requirements engineering, UML modelling, system analysis.


---


## 📝 Q3 – Unit Testing (Python)  

### ✅ Q3PartA – Equivalence Partitioning  
- Function: Mean of four numbers  
- Black‑box test table  
- Python unittest implementation (`TestQ3PartA.py`)

### ✅ Q3PartB – Boundary Value Analysis (BVA)  
- COVID vaccine eligibility function  
- Full BVA test table  
- Python unittest implementation (`TestQ3PartB.py`)

### ✅ Q3PartC – White‑Box Testing  
- Median of three numbers  
- Path coverage  
- Test fixtures  
- Input/output simulation  
- Error handling tests (`TestQ3PartC.py`)

### ✅ Test Execution Screenshots  
All tests executed in the **VMWare Linux environment** as required.

**Skills Demonstrated:**  
Test design, Python unittest, debugging, validation.

---

## 📝 Q4 – Code Modularity & Refactoring  

## **Q4.py — Identified Modularity Issues 

- Excessive global variables  
- Weak cohesion  
- Tight coupling  
- Flag‑based logic issues
- Repeated logic  
- Poor function structure

  Used for analysis in **Q4A** and **Q4B**.

###  Refactored Code (newQ4.py)  
## **newQ4.py — Refactored Modular Version**
Improved version of Q4.py, rewritten to demonstrate **good modularity**:
- Removed  global variables  
- Clear function parameters  
- Clean return values  
- Improved naming  
- Separated responsibilities  
- A structured main program  

This file satisfies **Q4C** (refactoring task).


**Skills Demonstrated:**  
Refactoring, modular programming, code quality improvement.









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

**Skills Demonstrated:**  
Ethical reasoning, risk analysis, professional responsibility.










# 🟦 Question 3 — Unit Testing (Black Box, White Box, BVA)

## **Q3PartA.py — Production Code (Mean Function)**
Implements the function `funmean(num1, num2, num3, num4)` used for **Equivalence Partitioning (EP)** in Question 3A.

Logic tested:
- If `num1 > num2` **and** `num3 >= num4` → return the mean  
- Otherwise → return `-1`

---

## **testQ3PartA.py — Black Box Tests (EP)**
Contains **8 unit test cases** designed using **Equivalence Partitioning** to validate the behaviour of `funmean()`.

---

## **Q3PartB.py — Production Code (COVID Eligibility)**
Implements the function `El_COVID(age)` used for **Boundary Value Analysis (BVA)** in Question 3B.

The function returns eligibility messages based on age ranges.

---

## **testQ3PartB.py — Boundary Value Tests (BVA)**
Includes test cases covering all critical age boundaries:
- Negative ages  
- 0–5  
- 6–12  
- 13–16  
- 17–25  
- 26–45  
- 46–60  
- 61–85  
- Above 85  

---

## **Q3PartC.py — Production Code (Median Function)**
Original code for computing the **median of three numbers**.  
Used for **white-box testing**, including:
- Path coverage  
- Input validation  
- Error handling  
- Patching user input  

---

## **testQ3PartC.py — White Box Tests**
Covers all internal paths of the median function, including:
- Valid inputs  
- Equal values  
- Negative numbers  
- Invalid input handling  
- Branch/path coverage  

---

## **Unittesting.py — Combined Test Runner (Optional)**
A consolidated script that runs:
- All mean tests  
- All COVID eligibility tests  
- All median tests  

Useful for demonstration, but not required by the assignment.

---

---



## ✅ Git Version Control & Workflow  

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


**Skills Demonstrated:**  
Branching, commit discipline, repository organisation.

---

## 🛠 Tools & Technologies Used  

- Python 3 (VMWare Linux environment)  
- `unittest` (Python testing framework)  
- Draw.io (diagrams)  
- VS Code (development)  
- Git (version control)

  
## 🎯  Final Note
This submission reflects my hands-on understanding of software engineering principles, from planning and testing to ethical reasoning and modular design. The repository is structured to be both academically complete and recruiter-friendly.

Thank you for reviewing my work!
