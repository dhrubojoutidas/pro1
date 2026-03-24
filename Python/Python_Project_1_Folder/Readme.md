

## 🧛 FOP Assignment 2 – Vampire Simulation

## 📄 Assignment Specification

* [Assignment 02 Instructions](Assignment%2002%20202203%20Bentley.pdf)

---

## 📝 Deliverables

### 📘 1. Assignment Report

* [Final Report](REPORT_ASSIGNMENT_2.pdf)

### 📑 2. Documentation

* [User Documentation](Document%20_ASSIGNMENT_02.pdf)


### 📜 3. Declaration

* [Declaration of Originality](declaration_of_originality_ONLINE%20-%20Fillable%20Form%5B68%5D.pdf)

---

## 💻 Source Code

* 🧠 [Animation.py](Animation.py)
  → Main simulation logic (Humans, Vampires, Items, Interactions)

* 🍤 [shrimp.py](shrimp.py)
  → Object class example (movement + lifecycle) 

* 📦 [shrimpBase.py](shrimpBase.py)
  → Base structure for simulation

---

## 📂 Supporting Files

* 📊 [simulation_output.csv](simulation_output.csv)
  → Stores initial & final populations

* ⚙️ [parameter.sweeps.sh](parameter.sweeps.sh)
  → Bash script for parameter sweep automation

* 📘 [README.txt](README.txt)
  → Original project notes 

---

## ⚙️ Features Implemented

* ✔️ Timesteps simulation loop
* ✔️ Object-oriented design (Human, Vampire, Items)
* ✔️ Random movement system
* ✔️ Interaction system (Human ↔ Vampire ↔ Items)
* ✔️ Scatter plot visualization using `matplotlib`
* ✔️ CSV data logging
* ✔️ Parameter sweep automation

(Aligned with assignment requirements )

---

## ▶️ How to Run

```bash
python Animation.py
```

---

## 🧠 Simulation Overview

* Humans:

  * Start with health = 100 and random age
  * Move up to 4 steps
* Vampires:

  * Move up to 8 steps
  * Infect humans
* Items:

  * Food (+30 health)
  * Water (+50 health)
  * Garlic (+100 health)



---

## 📊 Output

* Scatter plot showing:

  * Humans (green)
  * Vampires (red)
  * Food (brown)
  * Water (blue)
  * Garlic (gray)

* CSV file with:

  * Initial & final human/vampire counts
<img width="1159" height="724" alt="image" src="https://github.com/user-attachments/assets/4e47926a-9476-40de-8b2c-cf02426e6f4b" />

---

## 👨‍💻 Author

* Dhrubo Jouti Das Troyee
* Student ID: 90028995

---
