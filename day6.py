import math
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."  
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: ")) 
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
choice = input("Enter your choice (1-4): ")
if choice == '1':
    print("Addition:", add(num1, num2)) 
elif choice == '2':
    print("Subtraction:", subtract(num1, num2))
elif choice == '3':
    print("Multiplication:", multiply(num1, num2))  
elif choice == '4':
    print("Division:", divide(num1, num2))  
else:
    print("Invalid choice. Please select a valid option (1-4).")

