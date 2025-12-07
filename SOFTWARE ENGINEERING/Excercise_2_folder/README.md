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

## 📝 Q3 – Unit Testing (Black Box,  BVA, White Box)  

### ✅ Q3PartA – Equivalence Partitioning  (Black-Box) 
- **Production file:** [`Q3PartA.py`](Q3PartA.py)  
- **Function:** `funmean(num1, num2, num3, num4)`  
- **Purpose:** Computes the mean of four numbers only when:
  - `num1 > num2` **and** `num3 >= num4` → returns the mean  
  - otherwise → returns `-1`  

**Test file:** [`testQ3PartA.py`](testQ3PartA.py)  
  - Black-box tests using **Equivalence Partitioning (EP)**  
  - Contains **8 unit test cases** covering valid and invalid input partitions for `funmean()`  


---

### ✅ Q3PartB – Boundary Value Analysis (BVA)  
- **Production file:** [`Q3PartB.py`](Q3PartB.py)  
- **Function:** `El_COVID(age)`  
- **Purpose:** Determines COVID vaccine eligibility messages based on age groups.

- **Test file:** [`testQ3PartB.py`](testQ3PartB.py)  
  - Designed using **Boundary Value Analysis (BVA)**  
  - Includes test cases covering all critical age boundaries:
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

### ✅ Q3PartC – White‑Box Testing  (Median Function)
- **Production file:** [`Q3PartC.py`](Q3PartC.py)  
- **Function:** Computes the **median of three numbers**.  
- **Focus:**  
  - White-box testing  
  - Path / branch coverage  
  - Input validation  
  - Simulated user input (patched in tests)

- **Test file:** [`testQ3PartC.py`](testQ3PartC.py)  
  - White-box unit tests covering:
    - Valid numeric inputs  
    - Equal values   
    - Negative numbers 
    - Invalid input handling  
    - All internal decision paths in the median logic  

---


### 🟦 Combined Test Runner

- **File:** [`Unittesting.py`](Unittesting.py)  
- **Purpose:**  A consolidated script that runs all unit tests together:
  - Mean function tests (Q3PartA)  
  - COVID eligibility tests (Q3PartB)  
  - Median function tests (Q3PartC)  



---

## 📝 **Q4.py — Identified Modularity Issues**

- Excessive global variables  
- Weak cohesion  
- Tight coupling  
- Flag‑based logic issues
- Repeated logic  
- Poor function structure
Used for analysis in **Q4A** and **Q4B**.

 
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



---



### Test Execution Environment
All tests executed in the **VMWare Linux environment** as required.

---

**Skills Demonstrated:**  
- Test case design (**EP, BVA, white-box**)  
- Python `unittest` framework  
- Debugging and validation of logic  
- Handling edge cases and input errors

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
- Git (version control)
  
---



## 🎯  Final Note
This submission reflects my hands-on understanding of software engineering principles, from planning and testing to ethical reasoning and modular design. The repository is structured to be both academically complete and recruiter-friendly.

Thank you for reviewing my work!
