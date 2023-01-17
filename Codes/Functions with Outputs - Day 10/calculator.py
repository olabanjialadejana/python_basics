import os


# The screen clear function
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

# Create functions for all the operations


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def division(num1, num2):
    return num1 / num2


def multiplication(num1, num2):
    return num1 * num2


def modulus(num1, num2):
    return num1 % num2


# Add all the operations to a dictionary
operation_dictionary = {
    "+": addition,
    "-": subtraction,
    "/": division,
    "*": multiplication,
    "%": modulus,
}


def calculator():
    num1 = float(input("Type a number: "))
    for symbol in operation_dictionary:
        print(symbol)

    calculation_continue = True
    while calculation_continue:
        operation_symbol = input("Choose an operation from the display: ")
        num2 = float(input("Type another number: "))

        calculation_function = operation_dictionary[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input("Do you want to continue calculating with previous answer? Type 'y' for yes, type 'n' to start afresh:") == 'y':
            num1 = answer

        else:
            calculation_continue = False
            screen_clear()
            calculator()


calculator()
