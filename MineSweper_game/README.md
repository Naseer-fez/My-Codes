# 🧨  Minesweeper (Console Game)

A simple **Minesweeper game** written entirely in **C**, playable in your terminal.  
It randomly places mines on a grid, and you must uncover all safe spots without hitting a mine!

---

## 🎮 Features

- Random mine placement each time you play  
- Keeps track of discovered safe cells  
- Simple **text-based grid display** (using `O`, `X`, and `*`)  
- Allows replaying after hitting a mine  
- Adjustable grid size (via `#define Totalgrids`)  
- Lightweight — no external dependencies beyond the standard C library  

---

## 🧩 Game Logic Overview

| Symbol | Meaning |
|:-------|:--------|
| `O` | Unopened grid cell |
| `X` | Successfully uncovered safe cell |
| `*` | Mine (displayed after losing) |

- The grid is 1D (for simplicity) but formatted to show 10 cells per row.  
- Mines are randomly distributed using `rand()` seeded by `time(0)`.  
- You win if you uncover all safe cells without triggering a mine.  
- You lose instantly if you pick a cell containing a mine.  

---

## ⚙️ How It Works

1. The program randomly plants mines in the grid (20% of total cells).  
2. You input a number between **1 and Totalgrids** to uncover that cell.  
3. If you hit a mine → 💥 Game Over.  
4. If not, it marks the cell as cleared (`X`) and you continue.  
5. You win when all non-mine cells are cleared.  

---

## 🧠 Code Structure

| Function | Description |
|-----------|-------------|
| `main()` | Initializes game, starts main loop |
| `display()` | Shows the initial grid |
| `counter()` | Randomly plants mines |
| `takingvalue()` | Handles user input and validation |
| `minesweeper()` | Checks if chosen cell has a mine |
| `success()` | Updates grid display after each move |
| `ask()` | Prompts to replay or exit after losing |
| `choices()` | Manages invalid input and restarts |
| `grids()` | Main gameplay loop |

---

## 🧱 How to Compile and Run

### 🔧 Compile
```bash
gcc minesweeper.c -o minesweeper
