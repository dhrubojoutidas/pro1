
# CMPE3001 – Embedded Systems Engineering

## 📌 Overview
This repository contains assessed work completed for CMPE3001 (Embedded Systems Engineering).

Across multiple assignments and lab projects, I applied embedded systems principles covering:
- Market and feasibility analysis
- Firmware development on the MSP430FR5739
- Hardware–software integration using Energia
- Real‑time debugging, communication protocols, and embedded design methodology

The work demonstrates skills relevant to **embedded, firmware, and IoT engineering roles**.

---

## 📁 Assessments Overview

### 1) [Market Research & Costing Plan – Smart Vending System](./Market_Reserch_Project.pdf)

A structured commercial analysis exploring the feasibility of a **smart vending machine** offering hygiene and sanitary products in high‑traffic environments.

**Key focus areas:**
- SWOT  (Strengths, weaknesses, opportunities, and threats) analysis supported by academic and industry references
- PEST analysis & industry trends
- Competitor and market positioning
- Customer value proposition
- Pricing, cost modelling, and profit calculations

---

 ### 2) [ Embedded Systems Design Assignment](Design%20assignment.pdf)

A complete embedded system design workflow—from problem definition to implementation and evaluation.

 Covered in the report:
- Problem statement & system requirements
- Hardware architecture and component selection
- Software design, flowcharts, and program structure
- Constraints: cost, performance, size, power
- Safety, security, maintainability, and reliability
- Future improvements and stretch goals
  
---


 ### 3) [Getting Started with Energia and MSP430 Experimenter’s Board ](./LAB1_Getting%20Started%20with%20Energia%20and%20MSP430%20Experimenter%E2%80%99s%20Board%20.pdf)
Hands‑on firmware development using the **MSP430FR5739 microcontroller**,and Energia (Arduino‑style) framework.

- [Check the REPORT](./LAB1_Getting_start_project_REPORT.pdf)


**Key skills and concepts demonstrated:**
- Embedded programming in **C/C++** using the **Energia (Arduino-style) framework**
- GPIO configuration and LED control (including round-robin sequencing)
- **Interrupt-driven programming** for push-button inputs
- **PWM signal generation** for servo motor control
- **Analog-to-Digital Conversion (ADC)** for reading onboard temperature sensors
- Timing, signal control, and low‑level hardware interaction using microcontroller peripherals 
- Hardware–software integration and debugging on physical boards
- Writing structured technical documentation

---

### 4) [Embedded Systems Laboratory Project – MSP430 & Arduino (Energiaa](./Embedded%20Systems%20lab%20workduring%20lab%20session.pdf)

A series of **supervised, hands-on embedded systems tasks** using the **MSP430FR5739 Experimenter Board** and **Energia IDE**, focusing on practical interaction between software and hardware components.

Although the final modified source code from the lab sessions was not retained, the tasks were completed, demonstrated, and explained during the laboratory assessments. The work required understanding, implementing, and justifying embedded system behaviour in real time.

**Core tasks completed and demonstrated:**

- Programmed the MSP430 to send readable data to the serial monitor for debugging and system feedback.
- Interfaced **servo motor** and controlled its motion based on **temperature thresholds**
- Read **temperature sensor data** and reacted when temperature changes
- Used the onboard **accelerometer** and mapped X/Y/Z axis movement to LED indicators.
- Implementied **calibration logic** using push buttons to reset sensor baselines during runtime.
- Combining multiple functionalities into a **mode-based embedded program**
- Switched modes using hardware buttons, with updates shown on the serial monitor.
- Set up **SPI communication between MSP430 and Arduino**
- Sent text and control signals  from MSP430  to the Arduino, which displayed them on an **I2C LCD**.

**Technical concepts applied:**
- Embedded C/C++  Energia
- GPIO control and digital output mapping
- Interrupt-driven input handling
- PWM-based servo control
- ADC usage for sensor input
- SPI and I2C communication protocols
- Hardware–software integration and debugging
- Real-time explanation and justification of embedded behaviour during lab demonstrations

---

### 💻 Embedded Source Code (Energia / MSP430)
5. **[Round Robin LED Control Example](./Round_Robin_Example.ino)**  
   GPIO sequencing and timing control using Energia.

6. **[Push Button Interrupt Example](./Push_Button_Example.ino)**  
   Interrupt-driven input handling with debouncing concepts.

7. **[NTC Temperature Sensor – Energia Sketch](./NTC_FRAM.ino)**  
   Reading temperature data and reacting to threshold conditions.

8. **[NTC Sensor Header File](./FraunchPad_NTC.h)**  
   Sensor interface definitions.

9. **[NTC Sensor Source File](./FraunchPad_NTC.cpp)**
    Sensor logic and data processing implementation.
11. [SPI V1 folder ](./SPI%20V1)
12. [SPI V2 folder](./SPI%20V2)

 ---

*Academic work for CMPE3001 – Curtin University.*

