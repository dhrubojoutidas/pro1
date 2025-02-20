# Synopsis
Assignment 02 of Fundamentals of Programming  (FOP1005)


# 🧛 Human-Vampire Interaction Simulation  


Readme -  readme file for Assignment 02 - FOP1005 (30% of the unit Grading )


This project simulates **interactions between humans, vampires, and environmental elements (Food, Water, Garlic)** in a **2D map-based simulation**. The simulation models movement, interactions, and health dynamics using **Python & Matplotlib**, while a **Bash script automates parameter sweeps for different population sizes**.



## 📂 **Repository Structure**  

📁 **1. Python Simulation** (`Animation.py`)  
- Simulates **movement and interaction** of humans, vampires, and items.  
- Uses **Object-Oriented Programming (OOP)** principles.  
- Displays an **animated scatter plot** showing interactions.  
- Saves data to a CSV file for further analysis.  


📁 **2. Bash Script for Parameter Sweeps** (`parameter.sweeps.sh`)  
- Automates simulation runs with **different population sizes**.  
- Saves results to a CSV file for analysis.  
- Uses **loops and conditionals** to automate batch executions.  

📁 **3. Simulation Data Output** (`simulation_output.csv`)  
- Stores **initial and final populations** of humans and vampires for each run.  
- Used to analyze **trends, survival rates, and simulation outcomes**.  

📁 **4. Reports & Documentation**  
- 📜 `REPORT_ASSIGNMENT_2.pdf` - **Detailed methodology, results, and analysis**.  
- 📜 `Document_ASSIGNMENT_02.pdf` - **User guide and program overview**.  
- 📜 `README.txt` - Basic overview of the project (initial version).  

---

## 🚀 **How to Run the Simulation**  

### **1️⃣ Running the Python Simulation**  
#### **Prerequisites**  
- Python 3.x  
- Install required libraries  
  ```sh
  pip install matplotlib


# Dependencies 

assignment02.py 
VMware  Workstation  Pro application
matplotlib. pyplot package is required
random packages
sys package is requred



python Animation.py 00 to run the simulation

***Running Parameter Sweeps (Bash Script) ****

chmod +x parameter.sweeps.sh
./parameter.sweeps.sh


-------   Runs multiple simulations with different population settings and stores results in simulation_output.csv.



📊 Key Features & Functionality
✅ OOP Design: Implements classes for Humans, Vampires, and Items (Food, Water, Garlic).
✅ Randomized Movement: Humans move 4 spaces, Vampires move 8 spaces.
✅ Health Dynamics:

Humans gain/lose health based on interactions.
Vampires can infect humans.
Food, Water, and Garlic impact human health.
✅ Data Logging: Saves initial and final counts to simulation_output.csv.
✅ Parameter Sweep Automation: Bash script runs multiple simulations for analysis.




# 
# Aurthor 
#        Dhrubo Jouti Das Troyee
# Version 
#          202301.W2.01
# Revision 
#     19/09/2023 12:41 PM
#Date 
19/08/2023










