
# 1. Project Title

## Digital Logic Design using Logisim

---

# 2. 📌 Overview
This repository showcases a collection of digital logic circuits designed and simulated using Logisim.  
The project demonstrates practical implementation of combinational logic, modular circuit design, and construction of a functional 4-bit ALU.

It reflects hands-on experience with core computer engineering concepts such as multiplexing, encoding, and arithmetic logic design.


---



## 3 .🔧 Implemented Circuits

### Multiplexers (MUX)
- 2:1 Multiplexer
- 4:1 Multiplexer (using K-map & SOP design)
- 8:1 Multiplexer
- 8:1 MUX using:
  - 4:1 MUX
  - 2:1 MUX
  - OR gates

### Encoders
- 4:2 Encoder
- 4:2 Encoder with 7-segment display output
- 16:4 Encoder
- 16:4 Encoder with 7-segment display

### Arithmetic Circuits
- Full Adder (1-bit)
- 4-bit Adder using 1-bit full adders
- Subtractor design (using 2’s complement logic)
- Combined Adder/Subtractor circuit

### ALU (Arithmetic Logic Unit)
- 1-bit ALU (using MUX)
- 4-bit ALU (modular design)
- Supports:
  - Addition
  - Subtraction
  - Logical operations
- Includes test cases and simulation outputs

---

## 4. 🧠 Design Approach

- Applied **Karnaugh Map (K-map)** simplification to optimize logic circuits
- Implemented **Sum of Products (SOP)** expressions
- Designed circuits using a **modular and hierarchical approach**
- Built complex systems (4-bit ALU) by integrating smaller subcircuits
- Focused on clarity, scalability, and reusability of components


---

## 5. 🛠  Tools & Technologies

- Logisim Evolution
- Digital Logic Design principles
- Boolean Algebra
- Karnaugh Maps (K-map)


---


## 6. 📁 Project Structure


---


## 7. 📸 Screenshots

### The 16:4 encoder compresses input signals into a 4-bit representation, which is then expanded using a 4:16 decoder.
<img width="872" height="769" alt="image" src="https://github.com/user-attachments/assets/2ab76f7c-6ea3-4ee8-83c9-bad68f3477d6" />

- The design uses a combination of encoding and decoding stages.
-  The decoder output is selectively connected to a 7-segment display to represent decimal digits.
-  This approach demonstrates hierarchical circuit design and signal transformation between different logic stages.

### 8:1 Multiplexer
![MUX](screenshots/mux.png)


##  8. 📚 Learning Outcomes

- Developed strong understanding of combinational logic design
- Gained experience in building modular hardware systems
- Implemented and tested a functional 4-bit ALU
- Improved problem-solving skills in digital system design

---

##  9.  🚀 Future Improvements
- Extend ALU to support more operations (AND, OR, XOR, NOT)
- Implement sequential circuits (flip-flops, registers)
- Integrate timing analysis and optimization

---



