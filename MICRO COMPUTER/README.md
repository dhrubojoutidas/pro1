
# CMPE2003 – Microcomputers  
### Interrupt-Driven Embedded System on CLIC3 Board

---

## 📌 Project Summary

This project involved designing and implementing an **interrupt-based embedded system** on the **CLIC3 microcontroller board** as part of the CMPE2003 (Microcomputers) unit at Curtin University.

The system measures the **ON duration of a physical switch**, processes user-defined thresholds, and provides **real-time feedback** using LEDs, seven-segment displays, and an LCD.

The implementation reflects embedded systems and firmware development practices aligned with real-world workflows

---

## 🧩 What Was Built

The embedded system performs the following:

- Measures the ON-time of switch **S3** using hardware timers  
- Displays elapsed time (00–99 seconds) on dual seven-segment displays  
- Accepts a user-defined threshold via keypad input  
- Triggers a blinking LED alarm when the threshold is exceeded  
- Uses LEDs to indicate real-time switch status  
- Handles repeated switch activations independently  
- Implements debouncing and interrupt-driven timing  
- Provides user feedback through an LCD interface  

---


  ## 🛠️ Technical Approach

- Interrupt-driven design (no polling)
- Hardware timers for accurate time measurement
- External interrupts for switch state detection
- Modular, low-level embedded programming (primarily Assembly, with C where applicable)
- State-based control flow for reliability and clarity


---

## ⚡ Sustainability & Efficiency

The design incorporates **energy-aware embedded principles**, including:

- Interrupt-based execution to minimise CPU active time  
- Reduced peripheral usage when idle  
- Efficient timer configuration for low-power operation  

---


## 📂 Project Files

- 📄 [Design Assignment Brief (PDF)](./CMPE2003%20Design%20Assignment%202025%20S2.pdf)
- 📄 [Final Design Report (PDF)](./CMPE2003%20MICROCOMPUTERS_Design_Report2025.pdf)
- 🎥 [Demonstration Video](./mico_Ass_demo_Video.mp4)

### 🧠 Assembly Source Files
- [Initialization Code](./Initial.asm)
- [PORT2 Interrupt Service Routine](./PORT2_ISR.asm)
- [Bus Read Routine](./BusRead2.asm)
- [Bus Write Routine](./BusWrite2.asm)
- [Digital Lookup Logic](./DigitalLookup.asm)
- [Main Assembly File](./asm.s43)


 ## 🖼️ System Demonstration

The images below show the system in operation:
- LCD confirming a user-entered threshold value (20 seconds)
- Seven-segment display showing elapsed ON-time
- LED indicators reflecting switch state and threshold alarm


- The system after setup is highlighted in Figure 1 below. The LCD validates the stored threshold after a threshold value of 20 seconds was entered correctly using the keypad.
<img width="968" height="682" alt="image" src="https://github.com/user-attachments/assets/1b3750e1-b01b-4ad8-82ac-1bea28326c0f" />

<img width="1232" height="789" alt="image" src="https://github.com/user-attachments/assets/6efcde5c-5f0e-4f80-b17c-26e35676e3d2" />
<img width="1115" height="772" alt="image" src="https://github.com/user-attachments/assets/f3577fca-226b-4048-a013-2d2ab563a626" />
<img width="1281" height="681" alt="image" src="https://github.com/user-attachments/assets/ebe07e48-9f07-4f2a-a369-d13318c908be" />



---

## 🎯 Outcome

This project demonstrates my ability to:

- Design and implement real-time embedded systems  
- Work with microcontroller peripherals (timers, interrupts, I/O)  
- Apply low-power and sustainability considerations  
- Debug and document embedded firmware  
- Translate hardware requirements into reliable software  

---

*Academic project completed for CMPE2003 – Curtin University.*
