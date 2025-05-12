'''Create a function that asks the user for two numbers and prints out the sum, difference, product, and quotient of those numbers.'''

def calculate_operations():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    if num2 != 0:
        quotient = num1 / num2
    else:
        quotient = "undefined (division by zero)"

    print(f"Sum: {sum_result}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Quotient: {quotient}")

calculate_operations()