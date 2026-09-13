def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


number1 = float(input("Enter the first number: "))
operation = input("Choose + or -: ")
number2 = float(input("Enter the second number: "))

if operation == "+":
    print("Result:", add(number1, number2))
elif operation == "-":
    print("Result:", subtract(number1, number2))
else:
    print("Unknown operation")
