# Python CLI System (Mini OS)

A password-protected command-line system built using Python.  
After successful authentication, the user is presented with a menu that allows them to run different programs such as a calculator, viewing the current time, viewing the current date, or exiting the system.

This project is designed to simulate a basic operating-system–style menu interface using core Python concepts.

---

## Features

- Password authentication system
- Menu-driven interface
- Calculator program
- Show current time
- Show current date
- Persistent menu loop until exit
- Modular file structure
- Clean terminal UI with colors

---

## Project Structure

```bash
System/
│
├── main.py # Entry point, authentication & control flow
├── menu.py # Start screen and menu display
├── function.py # Calculator, date, and time functions
├── colors.py # ANSI color codes for terminal styling
├── README.md
└── .gitignore
```
---

## How It Works

1. The program starts by asking the user to enter a password.
2. If the password is correct:
   - A welcome screen is shown.
   - The main menu appears.
3. The user can select options:
   - Calculator
   - Show current time
   - Show current date
   - Exit
4. After each operation, the menu is displayed again until the user exits.

---

## Requirements

- Python 3.x
- Works on Windows, Linux, and macOS terminals

---

## How to Run
```bash
python main.py



Author

Developed by Najesh Afroz Shah
(Student | Python Learner)
