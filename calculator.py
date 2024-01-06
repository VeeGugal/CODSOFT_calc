def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Get user input
num1 = float(input("Enter the first number using which you wanna perform arithmetic opration: "))
num2 = float(input("Enter the second number using which you wanna perform arithmetic operation: "))

# Display operation choices
print("Choose any one of the given operation:")
print("1. Addition Operation")
print("2. Subtraction Operation")
print("3. Multiplication Operation")
print("4. Division Operation")

# Get user operation choice
choice = input("Please enter your operation choice (1/2/3/4): ")

# Perform calculation based on user choice
if choice in ('1', '2', '3', '4'):
    if choice == '1':
        result = add(num1, num2)
        operator = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operator = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operator = '*'
    else:
        result = divide(num1, num2)
        operator = '/'
    print(f"{num1} {operator} {num2} = {result}")
else:
    print("The input you have given is invalid . Please choose a valid operation (1/2/3/4).")
