def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y1

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the number corresponding to the operation you want to perform (1/2/3/4): ")

    if operation in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Invalid operation choice. Please try again.")

if __name__ == "__main__":
    calculator()
