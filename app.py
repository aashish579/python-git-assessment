# app.py

APP_VERSION = "1.0.0"


def greet_user(name):
    return f"Hello, {name}! Welcome to the Git and GitHub assessment."


def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def subtract_numbers(a, b):
    return a - b


def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def main():
    print(f"App Version: {APP_VERSION}")

    user_name = input("Enter your name: ")
    message = greet_user(user_name)
    print(message)

    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    sum_result = add_numbers(first_number, second_number)
    product_result = multiply_numbers(first_number, second_number)
    difference_result = subtract_numbers(first_number, second_number)
    division_result = divide_numbers(first_number, second_number)

    print(f"The sum is: {sum_result}")
    print(f"The product is: {product_result}")
    print(f"The difference is: {difference_result}")
    print(f"The division result is: {division_result}")


if __name__ == "__main__":
    main()