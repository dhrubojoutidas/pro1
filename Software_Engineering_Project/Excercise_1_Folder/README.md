# 🛫 SkyFly Airline Reservation System — Requirements & Planning  
**ISEN1000 – Introduction to Software Engineering**  
**Exercise 1 – Requirement Analysis & Project Planning**  
**Author:** Dhrubo Troyee  

---

## 📌 Overview  
This project presents a complete **requirements analysis**, **project planning**, and **version control strategy** for *SkyFly*, an airline reservation and seat‑management system.  
The work includes WBS, AON/PERT scheduling, critical path analysis, user stories, use cases, UML diagrams, and non‑functional requirements.

This repository contains all planning documents, diagrams, and supporting files for the assessment.

---

## 📂 Repository Structure  
```plaintext
Excercise_1_Folder/
│── Exercise1_Report.docx
│── Exercise1_question.pdf
│── README.md   ← (this file)
└── diagrams/   ← AON, UML, Use Cases (if included)
```

---

## ✅ 1. Planning & Scheduling

### **Work Breakdown Structure (WBS)**  
A detailed WBS was created to break the SkyFly system into manageable components, including:  
- User management  
- Passenger information handling  
- Flight search & scheduling  
- Seat allocation  
- Ticketing & cancellation  
- Payment & billing  
- Notifications & updates  
- Reservation enquiries  
- Technical support  

### **AON Network Diagram & Critical Path**  
- All activities were mapped with dependencies and durations.  
- ES, EF, LS, LF, and Slack were calculated.  
- **Critical Path:**  
  **1 → 4.1 → 4.2 → 4.3 → 5.1 → 5.2 → 8.1 → 8.2 → 9.1 → 9.2 → 10**  
- **Project Completion Time:** 54 weeks  
- **PERT Expected Duration:** ~52.13 weeks  

---

## ✅ 2. Functional Requirement Analysis

### **Actors Identified**
- Passengers  
- Pilots / Crew  
- Front Desk Representatives  
- Admin / Management Staff  
- Database System  
- Payment Gateway Service  

### **User Stories (Sample)**
- As a passenger, I want to view real‑time flight status so I can plan my travel.  
- As an admin, I want to manage user access levels to protect sensitive data.  
- As a customer service representative, I want to process refunds smoothly.  
- As a pilot, I want to access detailed flight plans before departure.  
- As a passenger, I want to download my boarding pass for airport access.  

*(Full list included in the report.)*

### **Use Cases**
Four detailed use cases were developed, including:  
- Managing seating arrangements  
- Processing refunds  
- Accessing passenger details  
- Downloading boarding passes  

Each use case includes:  
✅ Goal  
✅ Actors  
✅ Preconditions  
✅ Triggers  
✅ Flow of Events  
✅ Extensions  

### **UML Use Case Diagram**  
A complete UML diagram shows all actors and system interactions.

---

## ✅ 3. Non‑Functional Requirements

### **Usability Requirements**
- User‑friendly interface  
- Quick access to flight information  
- Accessibility features (screen reader, multi‑language support)

### **Performance Requirements**
- Payment processing < 4 seconds  
- Page load < 4 seconds  
- System handles high user volume  

### **Reliability Requirements**
- 99.99% availability for user registration  
- Regular backups  
- Error‑handling mechanisms  

---

## ✅ 4. Version Control Strategy

### **Branching Model**
- **Main Branch:** Stable, production‑ready planning documents  
- **Development Branch:** Latest updates, weekly merges  
- **Feature Branches:** One per user story or major component  

### **Branch Workflow**
- Day 1: Create `main` and `development`  
- Weekly: Merge feature → development  
- After all features complete: Merge development → main  

### **Git Commands Used**
```bash
git init
git checkout -b development
git checkout -b feature/<feature-name>
git add .
git commit -m "Message"
git push -u origin <branch>
```

---

## 📄 Assessment Files  
| File | Description |
|------|-------------|
| [`Exercise1_Report.docx`](Exercise1_Report.docx) | Full written submission |
| [`Exercise1_question.pdf`](Exercise1_question.pdf) | Original assessment brief |
| `diagrams/` | AON, PERT, UML, Use Case diagrams |

---

## ✅ Summary  
This project demonstrates a complete software engineering planning workflow, including requirement analysis, scheduling, UML modelling, and version control strategy. It reflects industry‑standard documentation practices and structured project planning.

---

If you'd like, I can also:  
✅ Add badges, emojis, or styling  
✅ Create a collapsible Table of Contents  
✅ Add links to diagrams  
✅ Format this for your GitHub portfolio style  


Absolutely — I can create a **clean, professional, recruiter-friendly GitHub README.md** for your **Exercise 1 (SkyFly Airline Reservation Requirement Analysis & Planning)** based on the documents you uploaded.

This README will:

✅ Summarize the assignment professionally
✅ Include **clickable links** (you can replace the paths with actual file paths once uploaded to GitHub)
✅ Highlight your skills clearly
✅ Stay concise and industry-appropriate
✅ NOT include long academic tables or walls of text

Here is your polished **README.md** ↓
(Just copy–paste into GitHub and update file paths.)

---

# ✈️ SkyFly Airline Reservation System – Requirement Analysis & Project Planning

**Author:** Dhrubo Troyee
**Course:** ISEN1000 – Introduction to Software Engineering
**Institution:** Curtin University
**Trimester:** 3, 2023

---

## 📌 Project Overview

This repository contains **Exercise Submission 1**, focused on **software requirement analysis**, **project planning**, and **version control strategy** for an airline reservation system called **SkyFly**.

The project demonstrates skills in:

* Requirements engineering
* Actor + user story modelling
* UML use case diagrams
* AON/PERT project scheduling
* Critical path identification
* Non-functional requirement specification
* Git version control planning

📄 **Full Report:**
➡️ [`Exercise1_Report.docx`](path/to/Excercise1.docx)
➡️ [`Assessment Instructions`](path/to/Exercise1_question.pdf)

---

## 🗂️ Repository Structure

| Section                  | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| `Excercise1.docx`        | Full written answer with WBS, AON, PERT, use cases, diagrams |
| `Exercise1_question.pdf` | Assignment instruction document                              |
| `/images/`               | UML diagrams / AON charts (add here if exported)             |
| `README.md`              | This file                                                    |

---

## 🧩 1. Work Breakdown Structure (WBS)

This section outlines all major tasks for building the SkyFly airline reservation system, including:

* User management
* Passenger information handling
* Flight search & details
* Seat management
* Ticketing (booking & cancellation)
* Payment processing
* Notifications & reminders
* Dashboard + support functions

The WBS was broken into logical sub-tasks as required by the assessment.
👉 See report: [`Excercise1.docx`](path/to/Excercise1.docx)

---

## 🔗 2. AON Diagram, Critical Path & PERT

This submission includes:

* Fully drawn **Activity-on-Node (AON)** diagram
* **Dependencies & durations**
* **Slack calculations**
* **Critical Path identification**
* **Estimated project duration: 54 weeks**
* **PERT expected duration: 52.13 weeks**

📷 (Optional but recommended): Export your AON diagram as PNG and link here:

```
![AON Diagram](images/AON.png)
```

---

## 👥 3. Requirements Analysis

### **Actors Identified**

* Passengers
* Customer service representatives
* Airline staff / admins
* Database system
* Payment gateway

### **User Stories (10+)**

Includes stories from the perspective of passengers, agents, admins, database, and payment systems.
➡️ Full list inside report.

### **Use Cases (4 fully written)**

Examples:

1. Seating arrangement management
2. Refund processing
3. Access passenger details
4. Download boarding pass

Each use case includes:

* Preconditions
* Triggers
* Step-by-step flow
* Extensions (exceptions)

### **UML Use Case Diagram**

All actors + user interactions included.
👉 Add export if desired:

```
![Use Case Diagram](images/usecase.png)
```

---

## ⚙️ 4. Non-Functional Requirements

### **Usability**

* User-friendly interface
* Screen reader support
* Multi-language support

### **Performance**

* Payment processing < 4 seconds
* Flight search response < 30 seconds
* Handle high passenger volume

### **Reliability**

* System availability 99.99%
* Backup and error-handling mechanisms
* Ticket printing failure < 0.1%

All NFRs documented in detail in the report.

---

## 🌿 5. Version Control Strategy (Git)

### **Branches**

| Branch        | Purpose                               |
| ------------- | ------------------------------------- |
| `main`        | Stable, final version                 |
| `development` | Ongoing updates                       |
| `feature-*`   | Individual features from user stories |

### **Workflow Summary**

* Create `main` + `development` on Day 1
* Create feature branches for major milestones
* Merge to `development` weekly or after tasks completed
* Merge `development` → `main` after final review

### **Commands Used**

```sh
git init
git checkout -b development
git checkout -b feature-userstory1
git add .
git commit -m "Added WBS and requirements"
git push -u origin development
```

---

## 📎 How to Navigate This Repository

1. Start with **README.md**
2. View **Excercise1.docx** for full detailed answers
3. Check attached **UML & AON diagrams** (if uploaded)
4. Review **assignment brief** for context

---

## 🎯 Final Note

This submission demonstrates industry-aligned skills in:

* Requirements gathering
* Project planning and estimation
* Use case + UML modelling
* Version control strategy

The repository is structured to clearly showcase academic work while remaining easy for recruiters and educators to navigate.

---


