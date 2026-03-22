#IMPORTS
from datetime import datetime as now
import os
# Calculator for the System
def calculator():
    user_input=input(">>")
    allowed_char='0123456789/*+-.() '
    try:
        if all(char in allowed_char for char in user_input):
            result=eval(user_input, { "__builtins__":None}, {})
            print(result)
        else:
            print("characters used not allowed!")
    except ZeroDivisionError:
        print("cannot divide by zero")
    except(SyntaxError, NameError):
       print("sorry! something went wrong")

# Shows date
def show_date():
    print(f"The date is {now.now().strftime("%d/%m/%y")}")

# shows time
def show_time():
     print(f"The time is {now.now().strftime("%H:%M:%S")}")

# clears screen
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

# Notes Application
def notepad():
    while True:
        
        print(r"""    ----Note Pad----  """)
        print(r"""    1. Add Note       """)
        print(r"""    2. Delete Note    """)
        print(r"""    3. View Note      """)
        print(r"""    4. Close Note Pad """)

        try:
            choice = int(input("choose an option: "))

            if choice == 1:
                clear_screen()
                note = input("Enter your thoughts:\n")
                
                with open('note2.txt', 'a') as file:
                    file.write(note + '\n')
                    clear_screen()
                print("File saved Successfully!")
            elif choice == 2:
                with open('note2.txt', 'w'):
                    pass
                    clear_screen()
                    print("file deleted successfully! ")
            elif choice == 3:
                clear_screen()
                with open('note2.txt', 'r') as file:
                    content = file.read()
                    print(f'\n {content}')
            elif choice == 4:
                clear_screen()
                break
            else:
                clear_screen()
                print("Invalid choice!")
                continue
        except ValueError:
            clear_screen()
            print("Please Enter a numeric value")
            continue