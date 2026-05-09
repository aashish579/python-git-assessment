# app.py

def greet_user(name):
    return f"Hello, {name}! Welcome to the Git and GitHub assessment."


def add_numbers(a, b):
    return a + b


def main():
    user_name = input("Enter your name: ")
    message = greet_user(user_name)
    print(message)

    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    result = add_numbers(first_number, second_number)
    print(f"The sum is: {result}")


if __name__ == "__main__":
    main()