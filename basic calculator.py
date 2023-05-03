import time
time_wait = 0.01
# menu
def menu():
    print("Welcome to The Basic Calculator")
    repeat_ = 0
    while repeat_ < 30:
        print("_", end="")
        repeat_ += 1
        time.sleep(time_wait)
    print("_")
    time.sleep(time_wait)
    print("(Hit enter to continue)")
    pause = input()
    select()
# multiplication
def multiply():
    print("")
    print("MULTIPLICATION SELECTED")
    repeat_ = 0
    while repeat_ < 22:
        print("_", end="")
        repeat_ += 1
        time.sleep(time_wait)
    print("_")
    number1 = float(input("First Number:"))
    number2 = float(input("Second Number:"))
    result = (number1 * number2)
    print(number1, "*", number2, "=", result)
    pause = ""
    print("(Press enter to continue)")
    pause = input()
    pause = ""
    print(pause)
    select()
# division
def divide():
    print("")
    print("DIVISION SELECTED")
    repeat_ = 0
    while repeat_ < 16:
        print("_", end="")
        repeat_ += 1
        time.sleep(time_wait)
    print("_")
    number1 = float(input("First Number:"))
    number2 = float(input("Second Number:"))
    result = (number1 / number2)
    print(number1, "/", number2, "=", result)
    pause = ""
    print("(Press enter to continue)")
    pause = input()
    pause = ""
    print(pause)
    select()
# addition
def add():
    print("")
    print("ADDITION SELECTED")
    repeat_ = 0
    while repeat_ < 16:
        print("_", end="")
        repeat_ += 1
        time.sleep(time_wait)
    print("_")
    number1 = float(input("First Number:"))
    number2 = float(input("Second Number:"))
    result = (number1 + number2)
    print(number1, "+", number2, "=", result)
    pause = ""
    print("(Press enter to continue)")
    pause = input()
    pause = ""
    print(pause)
    select()
# subtraction
def subtract():
    print("")
    print("SUBTRACTION SELECTED")
    repeat_ = 0
    while repeat_ < 19:
        print("_", end="")
        repeat_ += 1
        time.sleep(time_wait)
    print("_")
    number1 = float(input("First Number:"))
    number2 = float(input("Second Number:"))
    result = (number1 - number2)
    print(number1, "-", number2, "=", result)
    pause = ""
    print("(Press enter to continue)")
    pause = input()
    pause = ""
    print(pause)
    select()
# selection of operation
def select():
    repeat_ = 0
    while repeat_ < 100:
        print("")
        repeat_ += 1
    print("Please type one of the following:")
    time.sleep(time_wait)
    print("(type the item in parenthesis, not the operation)")
    time.sleep(time_wait)
    print("__________________________________________________")
    time.sleep(time_wait)
    print("Type \"menu()\" whenever you recieve an error message.")
    print("______________________________________________________")
    time.sleep(time_wait)
    print("Multiplication (*)")
    time.sleep(time_wait)
    print("Division (/)")
    time.sleep(time_wait)
    print("Addition (+)")
    time.sleep(time_wait)
    print("Subtraction (-)")
    time.sleep(time_wait)
    print("Type Here:", end="")
    time.sleep(time_wait)
    operation_choice = input("Operation choice:")
    if operation_choice == "*":
        multiply()
    elif operation_choice == "/":
        divide()
    elif operation_choice == "+":
        add()
    elif operation_choice == "-":
        subtract()
    else:
        print("I don't know what you are typing")
        time.sleep(0.1)
        select()

menu()