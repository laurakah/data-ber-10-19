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
