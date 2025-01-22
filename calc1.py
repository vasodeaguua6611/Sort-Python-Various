# Simple terminal calculator. Made it to test arithmetic python knowledge. It probably sucks, but eh.
# WARNING: THIS CALC ONLY WORKS WITH THE BASIC OPERATORS (+, -, *, /)
# WARNING 2: THIS CALC ONLY WORKS WITH 2 NUMBERS. I WAS TOO LAZY TO MAKE IT MORE COMPLEX. IT'S 3:29 AM, HELP ME.
# WARNING 3: IT WILL BREAK IF YOU DIVIDE BY 0.
# LAST WARNING : IF YOU USE ANYTHING OTHER THAN NUMBERS, IT WILL BREAK. 
# Copyright : Gabrielito


operator = input("Enter ur operator boi: ")
num1 = float(input("Enter ur first number: "))
num2 = float(input("Enter ur second number: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print("Dude, this is a simple calculator. How did you mess up the operator?")