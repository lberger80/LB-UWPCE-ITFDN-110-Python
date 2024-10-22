# ---------------------------------------------------------------------------- #
# Title: Module02-Lab03-AlgebraicOperators
# Desc: Practice working with algebraic operators
# Change Log: (Who, When, What)
#   Lora Berger,2024-10-21,Created Script
# ---------------------------------------------------------------------------- #

# Define program data
first_number:float = 0
second_number:float = 0
sum:float = 0
difference:float = 0
product:float = 0
quotient:float = 0
modulo:float = 0

# Input user data using is the assignment operator
first_number:float = float(input("Enter the first number: "))
second_number:float = float(input("Enter the second number: "))

# Process data using addition, subtraction, multiplication, and division operators
sum:float = first_number + second_number
difference:float = first_number - second_number
product:float = first_number * second_number
quotient:float = first_number / second_number
modulo:float = first_number % second_number

# Output processed data to the user
print(f"The sum is: {sum}")
print(f"The difference is: {difference}")
print(f"The product is: {product}")
print(f"The quotient is: {quotient}")
print(f"The modulo is: {modulo}")