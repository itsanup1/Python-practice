class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    """

    def add(self, x, y):
        """
        Adds two numbers.
        """
        return x + y

    def subtract(self, x, y):
        """
        Subtracts two numbers.
        """
        return x - y

    def multiply(self, x, y):
        """
        Multiplies two numbers.
        """
        return x * y

    def divide(self, x, y):
        """
        Divides two numbers. Handles division by zero.
        """
        if y == 0:
            return "Error: Cannot divide by zero!"
        return x / y

def get_number_input(prompt):
    """
    Helper function to get a valid number input from the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator_input():
    """
    Helper function to get a valid operator input from the user.
    """
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in ('+', '-', '*', '/'):
            return operator
        else:
            print("Invalid operator. Please choose from +, -, *, /.")

if __name__ == "__main__":
    calculator = Calculator()
    print("Welcome to the Python OOP Calculator!")

    while True:
        num1 = get_number_input("Enter first number: ")
        operator = get_operator_input()
        num2 = get_number_input("Enter second number: ")

        result = None
        if operator == '+':
            result = calculator.add(num1, num2)
        elif operator == '-':
            result = calculator.subtract(num1, num2)
        elif operator == '*':
            result = calculator.multiply(num1, num2)
        elif operator == '/':
            result = calculator.divide(num1, num2)

        print(f"Result: {result}")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break
