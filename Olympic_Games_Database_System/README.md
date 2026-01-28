Database System (SQL & Python)

This project was completed as part of a **Database Systems unit** at Curtin University and demonstrates the **design, implementation, and use of a relational database**, integrated with **Python** for dynamic data access.

The system models real-world data from the **Olympic Games**, including athletes, teams, events, schedules, coaches, and medal results.

---

## 🔧 Project Overview

The project involved:
- Designing an **Entity–Relationship (ER) model** and relational schema
- Implementing the database in **MySQL**
- Loading and querying real-world style data
- Using **advanced SQL features** (joins, subqueries, views, stored procedures)
- Connecting the database to **Python** for programmatic querying

An ER diagram is included to illustrate the database structure and relationships.

---

## 🗄️ Technologies Used
- **MySQL 8.0**
- **SQL** (DDL, DML, joins, subqueries, views, stored procedures)
- **Python 3** (MySQL Connector)
- Linux environment (VMware)

---

## 📂 Key Files (Click to Open)

- 📘 **[Database Report](./report_DBS_22663281.pdf)** – design decisions, schema, queries, and reflection  
- 📗 **[User Guide – Implement & Use Database](./User_guide_to_implement_and_%20use_olympicGame_database_.pdf)**  
- 📄 **[Assignment Specification](./assignnmnt_DMS.pdf)**
- 📗 **[Full Code File ZIP ](./Olympic_Games_Database_System/dbs_olympic_game_22663281.zip)**
- 🧩 **ER Diagram** – visual database model 
<img width="1716" height="903" alt="SQL_OYLMPIC_GAME_PIC" src="https://github.com/user-attachments/assets/fe7f55cc-5c15-4f4d-82c1-1f020e9524c4" />

---

## 🧠 Skills Demonstrated
- Relational database design (ER modelling, normalisation)
- SQL querying and optimisation
- Advanced database features (views, procedures)
- Python–MySQL integration
- Structured problem-solving and documentation
- Translating real-world requirements into a data model

---

📌 
*This project reflects my ability to design and implement a complete database system and integrate it with application-level code.*



---

 ✅  Command.txt file 

````md
## ▶️ How to Run the Project (SQL & Python)

This project includes a complete set of **MySQL and Python commands** for creating, loading, querying, and interacting with the Olympic Games database.

📄 **[View full command list](./command.txt)**

---

### 1️⃣ Connect to MySQL Server
Enable local file loading (required for data import):

```sql
SET GLOBAL local_infile = 1;
SHOW GLOBAL VARIABLES LIKE 'local_infile';
````

Check MySQL version:

```bash
mysql -V
```

Log in to MySQL:

```bash
mysql --local-infile=1 -u dsuser -p
```

---

### 2️⃣ Create and Select Database

```sql
CREATE DATABASE IF NOT EXISTS Olympic_Game_2024_22663281;
USE Olympic_Game_2024_22663281;
```

---

### 3️⃣ Create Tables and Load Data

```sql
\. CreateTable.sql
\. LoadData.sql
```

---

### 4️⃣ Run Queries

Simple queries:

```sql
\. Query.sql
```

Advanced queries:

```sql
\. advanceQuery.sql
```

---

### 5️⃣ Python–MySQL Integration

Install the required connector:

```bash
pip3 install mysql-connector-python
```

Run the Python connection script:

```bash
python3 pythonConnect.py
```

Insert and manage data using Python:

```bash
python3 eventdata.py
python3 scheduleData.py
python3 insert.py
```

---

📌 *All commands above are provided in detail in `command.txt` for easy execution and reference.*

```


<img width="1716" height="903" alt="SQL_OYLMPIC_GAME_PIC" src="https://github.com/user-attachments/assets/c449c72b-4c87-4167-972b-bc07a93ab958" />

