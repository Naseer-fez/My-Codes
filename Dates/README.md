# 📅 Date  (C-Optimized)

**A low-level, high-performance Date manipulation library built using C and Python**

This project deliberately avoids Python’s built-in date/time abstractions.  
All date logic is implemented **from scratch in C**, while Python is used **only as a thin interface layer** via `ctypes`.

This is an engineering-first project focused on **control, correctness, and performance**, not convenience.

---

## 📖 Motivation

Most high-level date libraries:
- Hide memory layout
- Abstract validation logic
- Trade control for simplicity

This project exists to:
- Understand how date systems work internally
- Manually manage memory using `malloc`
- Expose raw C pointers to Python safely
- Build a solid foundation for future time-based features

The goal is **clarity over comfort**.

---

## 🎯 Design Principles

- Deterministic behavior
- Explicit memory ownership
- Minimal abstraction layers
- No dependency on system date libraries
- Predictable execution cost
- Cross-platform compilation

---

## 🧠 Architecture Overview

The system is split into:
- **C backend** → all computation and memory management
- **Python frontend** → API, validation, error handling

Python never performs date logic.  
All real work happens in C.

---

## 🚀 Features

### Implemented

- Manual heap allocation using `malloc`
- Date storage as raw C integer arrays
- Pointer-based access from Python
- Numeric-only input validation
- Intelligent handling of partial date inputs
- Full date validation including leap years
- Day-of-week calculation using Zeller’s Congruence
- Modular C architecture with strict separation of concerns

---

### Supported Input Formats

The parser accepts both formatted and compact input:

| Input        | Interpretation |
|-------------|----------------|
| `29-03-2005` | DD-MM-YYYY |
| `29032005`   | DDMMYYYY |
| `2903`       | DDMM (year inferred) |
| `29`         | Day only (expanded internally) |

Short or incomplete inputs are expanded using logical defaults.

---

## 🧱 Internal Memory Model

All dates are stored in heap-allocated C arrays.

### Memory Layout

Index | Value
0 | Format identifier
1 | Day
2 | Month
3 | Year

yaml
Copy code

- Memory is allocated in C
- Ownership remains with the C layer
- Python receives a raw pointer (`int *`)
- Direct index access is allowed for inspection

This approach avoids Python object overhead and enables predictable performance.

---

## ⚙️ Module Breakdown

Each C module has a single responsibility.

---

### `memory_Date.c`
- Allocates heap memory for date arrays
- Internal-only API
- Not accessible to end users

---

### `Datecheck.c`
- Ensures input contains only numeric characters
- Rejects malformed input early

---

### `Date_Filler.c`
Core logic engine.

Functions:
- `datearrangement` → central dispatcher
- `less_values` → handles partial inputs
- `datevalidater` → validates day, month, year (leap year support)

---

### `Day_of_Year.c`
- Computes weekday using Zeller’s Congruence
- Pure mathematical implementation
- No lookup tables or system calls

---

## 🐍 Python Interface

**Public Class:** `Date_Time`

This class is the only user-facing API.

### Public Methods

- `Date(date: str, format=1)`
  - Validates input
  - Allocates memory via C
  - Returns pointer to C date array

- `Day_of_the_year(date_ptr)`
  - Accepts a C pointer
  - Returns weekday name as a string

---

## 🛠️ Compilation & Setup

### Requirements

- Python **3.12**
- GCC Compiler  
  - Windows: **MinGW**
  - Linux/macOS: **GCC / Clang**

---

### Windows Build

```bash
gcc -shared -o memory_Date.dll -fPIC memory_Date.c
gcc -shared -o Datecheck.dll -fPIC Datecheck.c
gcc -shared -o Date_Filler.dll -fPIC Date_Filler.c
gcc -shared -o Day_of_Year.dll -fPIC Day_of_Year.c
Linux / macOS Build
bash
Copy code
gcc -shared -o memory_Date.so -fPIC memory_Date.c
gcc -shared -o Datecheck.so -fPIC Datecheck.c
gcc -shared -o Date_Filler.so -fPIC Date_Filler.c
gcc -shared -o Day_of_Year.so -fPIC Day_of_Year.c
```
💻 Usage Example
python
Copy code
```
import Main as mp

dt = mp.Date_Time()

try:
    date_ptr = dt.Date("29-03-2005")
    print("Weekday:", dt.Day_of_the_year(date_ptr))
    print("Stored Year:", date_ptr[3])  # Raw C memory access

except TypeError as err:
    print("Date Error:", err)
```
🚧 Known Limitations
- No automatic memory deallocation API yet

- No timezone support

- No time (HH:MM:SS) module

- Limited error granularity

- Not packaged for pip

These limitations are known and intentional at this stage.

⏸️ Time Module Status
The Time module is currently paused by design.

Reason:

- High complexity in precision handling

- Need for a clean and extensible memory model

- Avoiding architectural debt

- The Date module is stable and complete.
  Time will be implemented only after a solid design is finalized.




# Built by Naseer

A systems-oriented project focused on:
Low-level understanding
Predictable software design
Learning through implementation

# ⚠️ Disclaimer
This project is educational and experimental.
It is not intended to replace production-grade date libraries.
This is just a experiment

# Use it to learn, explore, and experiment.

