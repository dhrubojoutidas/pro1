
# CMPE3001 – Embedded Systems Engineering

## 📌 Overview
This folder contains assessed work for **CMPE3001 (Embedded Systems Engineering)** at Curtin University.

Across three assignments, I applied **embedded systems engineering principles** spanning:
- market and feasibility analysis,
- firmware fundamentals on MSP430,
- and hands-on hardware–software integration.

The work demonstrates skills relevant to **embedded, firmware, and IoT engineering roles**.

---

## 📁 Assessments Overview

### 1) [Market Research & Costing Plan – Smart Vending System](./Market_Reserch_Project.pdf)

This report analyses the **vending machine industry** and proposes a **smart vending business concept** focused on sanitary and personal hygiene products in high-traffic environments (universities, workplaces, shopping centres, transport hubs).

The objective was to evaluate **commercial feasibility and viability** using structured market analysis, similar to early-stage validation before embedded system development.

**Key focus areas:**
- Industry and environmental analysis (PEST & industry trends)
- Competitor analysis and market positioning
- Product/service definition and customer value proposition
- Pricing strategy with cost, markup, and profit calculations
- SWOT  (Strengths, weaknesses, opportunities, and threats) analysis supported by academic and industry references

---

 ### 2)  Embedded Systems Design Assignment

This project presents the design and development of an embedded system as part of the Embedded Systems Design course. The aim of this assignment is to demonstrate a structured approach to embedded system design, from problem identification through to implementation and evaluation.

The report explains the overall system concept, design methodology, and technical decisions made throughout the project. It provides clear insight into how both hardware and software components work together to meet the system requirements.

## Contents
The document covers the following key aspects:
- Problem statement 
- General plan for system implementation  
- Hardware components and design details  
- Software design and program flow  
- System constraints (cost, performance, size, and power consumption)  
- Safety and security considerations  
- Maintainability and reliability of the system  
- Future enhancements and stretch goals

---


 ### 3) [Getting Started with Energia and MSP430 Experimenter’s Board ](./LAB1_Getting%20Started%20with%20Energia%20and%20MSP430%20Experimenter%E2%80%99s%20Board%20.pdf)

This assignment involved implementing a series of **hands-on embedded system tasks** using the **MSP430FR5739 microcontroller**, focusing on the fundamentals of **firmware development and hardware interaction**.

The work progressed from basic digital I/O control to more advanced concepts such as **interrupt handling, PWM-based actuator control, and analog sensor interfacing**, reflecting the core building blocks used in real embedded systems.

The project emphasised understanding how software interacts with hardware at a low level, including timing, signal control, and responsiveness to external events.

- [Check the REPORT](./LAB1_Getting_start_project_REPORT.pdf)



**Key skills and concepts demonstrated:**
- Embedded programming in **C/C++** using the **Energia (Arduino-style) framework**
- GPIO configuration and LED control (including round-robin sequencing)
- **Interrupt-driven programming** for push-button inputs
- **PWM signal generation** for servo motor control
- **Analog-to-Digital Conversion (ADC)** for reading onboard temperature sensors
- Timing and control using microcontroller peripherals
- Hardware–software integration and debugging on physical boards
- Writing clear technical documentation and structured lab reports

---

### 4) [Embedded Systems Laboratory Project – MSP430 & Arduino (Energiaa](./Embedded%20Systems%20lab%20workduring%20lab%20session.pdf)

This laboratory project involved completing a series of **supervised, hands-on embedded systems tasks** using the **MSP430FR5739 Experimenter Board** and **Energia IDE**, focusing on practical interaction between software and hardware components.

Although the final modified source code from the lab sessions was not retained, the tasks were completed, demonstrated, and explained during the laboratory assessments. The work required understanding, implementing, and justifying embedded system behaviour in real time.

**Core tasks completed and demonstrated:**
- Programming the MSP430 to output data to the serial monitor
- Interfacing a **servo motor** and controlling its motion based on **temperature thresholds**
- Reading onboard **temperature sensor data** and reacting to environmental changes
- Using the onboard **accelerometer** and mapping axis data to LED outputs
- Implementing **calibration logic** using push buttons to reset sensor baselines
- Combining multiple functionalities into a **mode-based embedded program**
- Switching operating modes using hardware buttons with serial feedback
- Establishing **SPI communication between MSP430 and Arduino**
- Sending strings and control signals from MSP430 to Arduino and displaying output on an **I2C LCD**

**Technical concepts applied:**
- Embedded C/C++ programming using Energia
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
10. [SPI V1 folder ](./SPI%20V1)
11. [SPI V2 folder](./SPI%20V2)

 ---

*Academic work for CMPE3001 – Curtin University.*

