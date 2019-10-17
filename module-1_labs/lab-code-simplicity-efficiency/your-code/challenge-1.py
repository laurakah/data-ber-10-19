"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

import operator

operators = {
    "plus": operator.add,
    "minus": operator.sub
}

numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')

number_first = (input('Please choose your first number (zero to five): ')).lower()
operator = (input('What do you want to do? plus or minus: ')).lower()
number_second = (input('Please choose your second number (zero to five): ')).lower()

if number_first in numbers and number_second in numbers and operator in operators:
    operating_function = operators[operator]
    result = operating_function(numbers[number_first], numbers[number_second])
    print("\n")
    print(number_first, operator, number_second, "equals", result)
    print("\n")
else:
    print("Sorry, I am not able to calculate this.")

print("Thanks for using this calculator, goodbye :)")
