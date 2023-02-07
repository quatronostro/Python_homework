"""
Hello, I'm Berke Baramuk - This is my first python calculator program
"""
import time


def add(a, b):
    """Return the sum of two numbers"""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers"""
    return a - b


def multiply(a, b):
    """Return the product of two numbers"""
    return a * b


def divide(a, b):
    """Return the division of two numbers"""
    return a / b


# A dictionary to map user inputs to functions.
operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide
}


def sliding_text(text, delay=0.1):
    """Print text one character at a time with a given delay"""
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()


# Main loop to run the calculator until the user decides to quit.
while True:

    print("""
    === Welcome to Calculator ===
    [1] For addition in calculator please press 1
    [2] For subtraction in calculator please press 2
    [3] For multiplication in calculator please press 3
    [4] For division in calculator please press 4
    [Q] To exit to calculator please press Q

        """)

    num = input("Choose your operation: ")
    print()

    if num == "1":
        try:
            x = float(input("First number you entered: "))
            y = float(input("Second number you entered: "))
        except ValueError:
            sliding_text("You have entered a letter, please enter a number!")
            print(20 * "=")
            continue
        sliding_text("Calculating...")
        time.sleep(1)
        print("Result", f"\n{x} + {y} = {x + y}")
        print(20 * "=")

    elif num == "2":
        try:
            x = float(input("First number you entered: "))
            y = float(input("Second number you entered: "))
        except ValueError:
            sliding_text("You have entered a letter, please enter a number!")
            print(20 * "=")
            continue
        sliding_text("Calculating...")
        time.sleep(1)
        print("Result", f"\n{x} - {y} = {x - y}")
        print(20 * "=")

    elif num == "3":
        try:
            x = float(input("First number you entered: "))
            y = float(input("Second number you entered: "))
        except ValueError:
            sliding_text("You have entered a letter, please enter a number!")
            print(20 * "=")
            continue
        sliding_text("Calculating...")
        time.sleep(1)
        print("Result", f"\n{x} * {y} = {x * y}")
        print(20 * "=")

    elif num == "4":
        try:
            x = float(input("First number you entered: "))
            y = float(input("Second number you entered: "))
        except ValueError:
            sliding_text("You have entered a letter, please enter a number!")
            print(20 * "=")
            continue
        sliding_text("Calculating...")
        time.sleep(1)
        print("Result", f"\n{x} / {y} = {x / y}")
        print(20 * "=")

    elif num in ['q', 'Q']:
        sliding_text("\nExiting Calculator... ")
        time.sleep(3)
        print("See you again...")
        print(20 * "=")
        quit()

    else:
        sliding_text("\nYou have entered incorrectly!")
        print(20 * "=")
