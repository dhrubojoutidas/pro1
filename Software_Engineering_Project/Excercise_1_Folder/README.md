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

Just tell me the vibe you want — clean, modern, flashy, academic, or recruiter‑friendly.
