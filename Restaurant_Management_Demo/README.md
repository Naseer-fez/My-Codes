 # 🍽️ Restaurant_Management_Demo

This is a simple **C-based restaurant order management system** that allows a restaurant to manage multiple tables, take food orders, calculate bills, and generate a final report for all tables.  
It demonstrates the use of **structs, arrays, sorting, user input validation, and multi-table order tracking** in C.

---

## 🚀 Features

✅ **Dynamic Menu**  
- Menu can be predefined or entered manually.  
- Each item has an `ID`, `Name`, and `Price`.

✅ **Table Management**  
- Supports up to 10 tables (`totaltabels = 10`).  
- Each table can place multiple orders.  
- Prevents duplicate table entries.

✅ **Order System**  
- Each table can order multiple food items.  
- Prevents duplicate item selection in a single order.  
- Displays itemized bills with calculated totals.

✅ **Sorting and Reporting**  
- Orders are sorted by item ID before displaying.  
- Generates a final report of all tables and their orders.

✅ **Error Handling**  
- Limits invalid attempts for incorrect inputs.  
- Asks user before exiting or adding new tables.

---

## 📂 Project Structure

| File | Description |
|------|--------------|
| `main.c` | Main C source file containing all logic |
| `README.md` | Project documentation (this file) |

---

## 🧩 How It Works

1. The program first defines the restaurant menu (20 items).  
2. The user is prompted to enter a table number.  
3. The system checks if the table already exists.  
4. The menu is displayed, and the user selects items with quantities.  
5. The total bill is calculated per table.  
6. The user can repeat for more tables.  
7. A final report can be generated showing all tables and their total bills.

---

## 💻 Compilation & Execution

### **Compile**
```bash
gcc main.c -o restaurant
