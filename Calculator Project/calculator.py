# Description
# A simple program for calculation

from calculatorart import logo

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)
    num1 = float(input('Type in the number x -> '))

    should_accumulate = True
    while should_accumulate:
        num2 = float(input('Type in the number y -> '))
        for symbol in operations:
            print(symbol)
        which_operator = input('Type in an operator -> ')
        result = operations[which_operator](num1, num2)
        print(f'{num1} {which_operator} {num2} = {result}')
        choice = input(f'Type y to continue calculating with {result}, or type n to start a new calculation. -> ')
        if choice == 'y':
            num1 = result

        else:
            should_accumulate = False
            print('\n' * 20)
            calculator()
calculator()