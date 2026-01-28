## Database System (SQL & Python)

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
- 📗 **[Full Code File ZIP ](./dbs_olympic_game_22663281.zip)**
- 🧩 **ER Diagram** – visual database model 
<img width="1716" height="903" alt="SQL_OYLMPIC_GAME_PIC" src="https://github.com/user-attachments/assets/fe7f55cc-5c15-4f4d-82c1-1f020e9524c4" />

---


 ## 📌 How to Run the Project (MySQL & Python)

This section contains **all commands required to create, load, query, and manage** the Olympic Games database, as well as connect it to Python.  
All commands are preserved from [`command.txt`](./command.txt) and organised for clarity.



## 1️⃣ MySQL Setup & Database Execution

### Enable Local File Loading (Required)
```sql
SET GLOBAL local_infile = 1;
SHOW GLOBAL VARIABLES LIKE 'local_infile';

```



### Step 1: Check MySQL Version

```bash
mysql -V
```

---

### Step 2: Connect to MySQL Server

*(Used due to data loading errors without local-infile enabled)*

```bash
mysql --local-infile=1 -u dsuser -p
```

**Password:**

```
userCreateSQL
```

---

### Step 3: Show Existing Databases

```sql
SHOW DATABASES;
```

---

### Step 4: Create Database

```sql
CREATE DATABASE IF NOT EXISTS Olympic_Game_2024_22663281;
```

**Password:**

```
userCreateSQL
```

---

### Step 5: Verify Database Creation

```sql
SHOW DATABASES;
```

---

### Step 6: Use the Database

```sql
USE Olympic_Game_2024_22663281;
```

*(Optional – reset database if needed)*

```sql
DROP DATABASE Olympic_Game_2024_22663281;
```

---

## 3️⃣📦 Create Tables & Load Data

### Create All Tables

```sql
\. CreateTable.sql
```

### Load Data into Tables

```sql
\. LoadData.sql
```

---

## 4️⃣🔍 Run SQL Queries

### Simple Queries

```sql
\. Query.sql
```

### Advanced Queries

```sql
\. advanceQuery.sql
```

---


## ❌ Delete All Tables, Procedures & Views

```sql
\. DeleteTable.sql
```

---

##  5️⃣🐍 Python–MySQL Integration

### Python Files Used

```bash
python3 eventdata.py
python3 scheduleData.py
python3 pythonConnect.py
python3 insert.py
```

---

### Step 1: Confirm MySQL Installation

```bash
mysql -V
```

---

### Step 2: Install MySQL Connector for Python

```bash
pip3 install mysql-connector-python
```

---

### Step 3: Connect Python to MySQL

```bash
python3 pythonConnect.py
```

---

### Step 4: Insert Data Using Python Scripts

```bash
python3 eventdata.py
python3 scheduleData.py
python3 insert.py
```

---

