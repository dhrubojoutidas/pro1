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

## 👨‍💻 Author

* Developed as part of UCP (Unix & C Programming) coursework

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


## ⚙️ Compilation

Make sure you are in the project directory, then run:

```bash
make
```

---
## ▶️ Run the Project

```bash
make
./laserTank data.txt
```
## ▶️ Game Interface
<img width="229" height="288" alt="image" src="https://github.com/user-attachments/assets/eaea06ad-18db-4cfb-b460-d87e3fc61836" />

---
