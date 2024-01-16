# Take two numbers from user and perform at least 4 arithmetic operations on them.

# Receive two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Printing the results
print(f"Sum: {num1} + {num2} = {addition}")
print(f"Difference: {num1} - {num2} = {subtraction}")
print(f"Product: {num1} * {num2} = {multiplication}")

# Verify whether the second number is non-zero before executing the division operation
if num2 != 0:
    division_result = num1 / num2
    print(f"Quotient: {num1} / {num2} = {division_result}")
else:
    print("Cannot divide by zero.")