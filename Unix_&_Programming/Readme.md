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
