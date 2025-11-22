# 📘 Tkinter Calculator

A simple and clean GUI-based Calculator application built using **Python Tkinter**. This calculator supports basic arithmetic operations such as **addition, subtraction, multiplication, and division**.

---

## 🚀 Features

* Basic arithmetic operations
* Responsive button-based GUI
* Real-time expression display
* Error handling for invalid expressions
* Clear button to reset the calculator
* Built entirely in Python without external libraries

---

## 🛠 Technologies Used

| Component     | Technology |
| ------------- | ---------- |
| Language      | Python 3.x |
| GUI Framework | Tkinter    |

---

## 📂 Project Structure

```
calculator.py
README.md
```

---

## ▶ How to Run

### 1. Install Python

Make sure you have **Python 3.x** installed.

### 2. Run the Application

Use the following command:

```bash
python calculator.py
```

The calculator window will appear.

---

## 📑 Code Overview

Key functions used in `calculator.py`:

* **press()** → Appends digits/operators to the display
* **equal()** → Evaluates the expression using `eval()`
* **clear()** → Clears the display
* Tkinter widgets: `Entry`, `Button`, `Frame` for creating calculator layout

---

## 📸 GUI Layout

The calculator interface contains buttons arranged in this layout:

```
7 8 9 /
4 5 6 *
3 2 1 -
0 . = +
```

A **Clear** button is placed at the bottom.

---

## 🧩 Future Improvements

* Add scientific calculator functions
* Add theme modes (light/dark)
* Add keyboard input support
* Add calculation history

---

## 📘 Extended Explanation

### 🧠 How the Calculator Works Internally

The calculator operates by maintaining a global **expression string**. Each time the user presses a button, the value is appended to this string and displayed on the screen. When the user presses `=`, the entire expression is evaluated using Python's built-in `eval()` function, producing the final result.

Internally:

* Numbers and operators pressed → appended to `expression`
* Display is updated using a `StringVar()`
* Pressing **Clear** resets everything to an empty state

This makes the calculator efficient and easy to expand.

---

## ⚙️ Application Architecture (Step-by-Step)

### 1. **Main Window**

A Tkinter root window is created with a title and fixed geometry.

### 2. **Display Screen**

An `Entry` widget is used as the calculator display. It is linked to a `StringVar()`, so any change updates instantly.

### 3. **Button Grid Layout**

The numerical and operator buttons are placed inside a `Frame` using the `grid()` method, giving a clean layout.

### 4. **Main Functions**

* `press()` – Handles input
* `equal()` – Performs calculation
* `clear()` – Resets the calculator

### 5. **Event Handling**

Each button triggers a command, making interaction dynamic.

---

## 🧮 Supported Operations

The calculator supports the following operations:

* Addition: `+`
* Subtraction: `-`
* Multiplication: `*`
* Division: `/`
* Decimal values

This ensures the user can perform all typical basic arithmetic tasks.

---

## 🧱 GUI Enhancements You Can Add

Here are optional features you may implement:

### 🔹 Add KBD Input Support

Allow direct keyboard input for faster operation.

### 🔹 Add Dark Mode

Use Tkinter styles to switch between Light and Dark themes.

### 🔹 Add Memory Functions

Implement buttons such as:

* `M+`
* `M-`
* `MR`
* `MC`

### 🔹 Add Scientific Features

Include functions like:

* sin, cos, tan
* logarithm
* exponential
