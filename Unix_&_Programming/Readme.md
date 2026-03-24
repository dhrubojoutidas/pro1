# 🚀 Laser Tank Game (C)

## 📌 Overview

This project is a terminal-based **Laser Tank game** implemented in **C (C89 standard)**.
The player navigates a grid-based map, fires lasers, and attempts to destroy the enemy tank while avoiding defeat.

---

## 🎮 Features

* ⬆️ Player movement using `W`, `A`, `S`, `D`
* 🔫 Laser shooting system (`F`)
* 🪞 Mirror reflection mechanics for laser redirection
* 🎯 Win/Lose condition detection
* 📜 Game state logging to file
* 🔗 Linked List implementation for storing map history
* 🖥️ Dynamic terminal rendering with screen refresh

---

## 🗂️ Project Structure

```
.
├── main.c              # Main game loop
├── PlayerMove.c       # Player movement logic
├── UserInput.c        # Input handling
├── UpdateGame.c       # Game state updates (laser, logic)
├── LinkedList.c       # Linked list implementation
├── mirror.c           # Mirror reflection logic
├── printmap.c         # Map rendering
├── screenclear.c      # Terminal screen clearing
├── ucpSleep.c         # Animation timing
├── data.txt           # Input configuration file
├── log.txt            # Game log output
└── Makefile           # Build configuration
└── instruction.h      # instruction logic 


 - [main.c](main.c) – Main game loop

[DisplayBoard.c](DisplayBoard.c) – Board display [PlayerMove.c](PlayerMove.c) – Player movement [UserInput.c](UserInput.c) – Input handling [UpdateGame.c](UpdateGame.c) – Game updates [LinkedList.c](LinkedList.c) – Linked list logic [mirror.c](mirror.c) – Mirror reflection [EnemyLaser.c](EnemyLaser.c) – Enemy laser logic [printmap.c](printmap.c) – Map rendering [screenclear.c](screenclear.c) – Clear terminal [ucpSleep.c](ucpSleep.c) – Animation delay [data.txt](data.txt) – Input configuration [log.txt](log.txt) – Game output log [makefile](makefile) – Compilation file
```

---

## ⚙️ Compilation

Make sure you are in the project directory, then run:

```bash
make
```

---

## ▶️ How to Run

```bash
./laserTank data.txt
```

---

## 🎮 Controls

| Key | Action     |
| --- | ---------- |
| `w` | Move Up    |
| `s` | Move Down  |
| `a` | Move Left  |
| `d` | Move Right |
| `f` | Fire Laser |
| `q` | Quit Game  |

---

## 🧠 Game Logic

* The player shoots lasers in the direction they are facing.
* Lasers travel until they:

  * Hit the enemy (WIN 🏆)
  * Hit a wall (stop)
  * Hit a mirror (reflect direction)
* The player loses if they move into the enemy’s line of sight (LOSE ❌)

---

## 📄 Requirements

* GCC compiler
* Linux / Unix-based terminal (recommended)

---

## ⚠️ Notes

* Uses dynamic memory allocation (`malloc`)
* All allocated memory is freed at program termination
* Designed following modular programming principles
* Built according to academic assignment constraints (C89 standard)

---

## 👨‍💻 Author

* Developed as part of UCP (Unix & C Programming) coursework

---
---

## 🖼️ Game Preview

<img width="800" alt="Laser Tank Game" src="https://via.placeholder.com/800x400.png?text=Laser+Tank+Game" />

---

## 📝 Project Files

### 1. 🔧 Core Files

* [main.c](main.c)
* [game.c](game.c)
* [game.h](game.h)
* [UpdateGame.c](UpdateGame.c)
* [UpdateGame.h](UpdateGame.h)

---

### 2. 🎮 Gameplay Modules

* [PlayerMove.c](PlayerMove.c)
* [PlayerMove.h](PlayerMove.h)
* [UserInput.c](UserInput.c)
* [UserInput.h](UserInput.h)
* [condition.c](condition.c)
* [condition.h](condition.h)

---

### 3. 🧠 Game Logic & Features

* [mirror.c](mirror.c)
* [mirror.h](mirror.h)
* [EnemyLaser.c](EnemyLaser.c)
* [EnemyLaser.h](EnemyLaser.h)

---

### 4. 🖥️ Display & Interface

* [DisplayBoard.c](DisplayBoard.c)
* [DisplayBoard.h](DisplayBoard.h)
* [printmap.c](printmap.c)
* [printmap.h](printmap.h)
* [instruction.c](instruction.c)
* [instruction.h](instruction.h)
* [screenclear.c](screenclear.c)
* [screenclear.h](screenclear.h)

---

### 5. 📂 Data Structures & Utilities

* [LinkedList.c](LinkedList.c)
* [LinkedList.h](LinkedList.h)
* [ucpSleep.c](ucpSleep.c)
* [ucpSleep.h](ucpSleep.h)

---

### 6. 📄 Input & Output Files

* [data.txt](data.txt)
* [log.txt](log.txt)

---

### 7. ⚙️ Build File

* [makefile](makefile)

---

## ▶️ Run the Project

```bash
make
./laserTank data.txt
```

---
