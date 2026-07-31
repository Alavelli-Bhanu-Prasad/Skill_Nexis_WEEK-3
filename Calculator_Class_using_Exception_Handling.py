class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except TypeError:
            return "Error: Invalid input for addition"

    def subtract(self, a, b):
        try:
            return a - b
        except TypeError:
            return "Error: Invalid input for subtraction"

    def multiply(self, a, b):
        try:
            return a * b
        except TypeError:
            return "Error: Invalid input for multiplication"
    def divide(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError
            return a / b
        except ZeroDivisionError:
            return "Error: Cannot divide by zero"
        except TypeError:
            return "Error: Invalid input for division"

if __name__ == "__main__":
    calc = Calculator()
    print("Addition:", calc.add(10, 5))
    print("Subtraction:", calc.subtract(10, 5))
    print("Multiplication:", calc.multiply(10, 5))
    print("Division:", calc.divide(10, 5))
    print("Division by zero:", calc.divide(10, 0))
    print("Invalid input:", calc.add("a", 5))