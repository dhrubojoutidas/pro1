
# 🔌 **Transmission & Interface Design (ELEN2002) — Lab Portfolio**  
A curated collection of laboratory work completed for **ELEN2002: Transmission & Interface Design** at Curtin University.  
This portfolio demonstrates hands‑on experience with **serial communication protocols, digital IC behaviour, amplifiers, comparators, and embedded system interfaces**.

---

## 🎓 **Unit Overview**
This unit focuses on how digital and embedded systems communicate, process signals, and interface with external devices.  
Key skills developed:

- Serial communication (RS232, I²C, SPI)  
- Digital IC timing, propagation delay & VTC analysis  
- Op‑amp comparators & inverting amplifiers  
- BJT amplifier biasing & AC gain behaviour  
- Arduino‑based protocol implementation  
- Oscilloscope‑based measurement & signal interpretation  

---

# 📘 **Labs & Reports**

---

## ⚡ [**Lab 2 — Amplifiers & Comparators** ](./Lab%20Report%202%20_TRANSMISSION.pdf)


**Topics:** Inverting amplifier, comparator behaviour, BJT biasing, emitter bypass capacitor  
**Skills demonstrated:**  
- Calculated & measured closed‑loop gain  
- Observed comparator switching behaviour  
- Analysed BJT DC bias point & AC gain  
- Compared gain with/without emitter bypass capacitor  

📄 **[Open Lab 2 Report](#)**

---

## 🔧 **Lab 3 — Digital IC Performance (7404 Inverter)**  
**Topics:** Voltage transfer characteristics, propagation delay, rise/fall times, power consumption  
**Skills demonstrated:**  
- Measured VTC for 1‑load & 5‑load configurations  
- Analysed timing behaviour using oscilloscope  
- Evaluated dynamic vs static power consumption  
- Observed inverter response to analog inputs  

📄 **[Open Lab 3 Report](#)**

---

## 🔗 **Lab 5 — RS232, I²C & SPI Interfaces**  
**Topics:** Multi‑protocol communication using Arduino (Master/Slave)  
**Skills demonstrated:**  
- Implemented I²C single‑slave & multi‑slave communication  
- Relayed RS232 → I²C data between devices  
- Tested SPI at multiple clock speeds (DIV2, DIV8, DIV32)  
- Analysed data corruption, timing limits & bus behaviour  
- Used pull‑up resistors, bus wiring & protocol debugging  

📄 **[Open Lab 5 Report](#)**

---

## 🚗 **CAN Bus Presentation — Priority & Contention**  
**Topics:** CAN arbitration, message priority, dominant/recessive bits  
**Skills demonstrated:**  
- Explained CAN ID‑based priority  
- Demonstrated bitwise arbitration & collision avoidance  
- Presented real‑world automotive use cases  

📄 **[Open CAN Presentation](#)**

---

# 📝 **What This Portfolio Shows**
- Strong understanding of **digital communication protocols**  
- Ability to analyse **timing, signal integrity, and IC behaviour**  
- Practical experience with **Arduino, oscilloscopes, and serial buses**  
- Clear documentation and engineering communication  
- Skills relevant to **embedded systems, electronics, IoT, and hardware support roles**
  

---


Perfect — now that I can see your **Arduino folder** in your GitHub tab , I can give you a clean, professional description that explains **exactly what the coding folder is for**, what it contains, and why it matters.

You can paste this directly into your README under the “Arduino Source Code” section.

---

# [💻 Arduino Coding Folder — What It Contains & Why It Matters](./Arduino)

This folder contains all the **Arduino `.ino` programs** used to implement and test the communication protocols explored in **Lab 5: RS232, I²C, and SPI Interfaces**.  
These files demonstrate how microcontrollers communicate using different serial standards and how timing, addressing, and data integrity behave in real embedded systems.

## **📂 Part 1 — I²C Communication (Master & Slave)**  
Includes:  
- `Blink_I2C_Master.ino`  
- `Blink_I2C_Slave.ino`  
- `Blink_I2C_Master_2.ino`

**What this part shows:**  
- How a master sends commands over the I²C bus  
- How a slave responds using its assigned address  
- Multi‑slave communication using different addresses  
- LED control and bus behaviour when SDA/SCL are disconnected  

This demonstrates your understanding of **addressing, pull‑ups, synchronous communication, and multi‑device bus design**.

---

## **📂 Part 2 — RS232 → I²C Bridge (Serial to I²C)**  
Includes:  
- `Serial_I2C_Master.ino`  
- `Serial_I2C_Slave.ino`

**What this part shows:**  
- Receiving text from a PC via Serial (RS232‑style USB)  
- Forwarding that data over I²C to another Arduino  
- Slave printing the received data to Serial Monitor  
- How software delays affect timing and message flow  

This demonstrates your ability to **bridge two different communication standards** and manage timing between asynchronous and synchronous protocols.

---

## **📂 Part 3 — SPI Communication (High‑Speed Master & Slave)**  
Includes:  
- `SPI_Master.ino`  
- `SPI_Slave.ino`

**What this part shows:**  
- Full‑duplex SPI communication using MOSI, MISO, SCK, SS  
- Slave receiving data via SPI interrupt (`SPI_STC_vect`)  
- Testing different SPI clock speeds:  
  - `DIV32` → slow & stable  
  - `DIV8` → fast & reliable  
  - `DIV2` → very fast, causes corrupted data  
- How timing limits affect data integrity  

This demonstrates your understanding of **high‑speed serial buses, interrupt‑driven communication, and hardware timing constraints**.

---

## 🧠 Why This Folder Is Important  
This coding folder proves your ability to:  
- Write and debug embedded communication code  
- Work with **three major serial protocols** (I²C, SPI, RS232)  
- Understand timing, interrupts, and data buffering  
- Build real microcontroller‑to‑microcontroller communication systems  
- Analyse and fix data corruption issues at high clock speeds  


---


