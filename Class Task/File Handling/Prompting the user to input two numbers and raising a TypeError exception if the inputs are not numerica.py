try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Sum:", num1 + num2)
except ValueError:
    print("Error: Invalid input! Please enter numerical values.")
