import unittest

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y

def main():
    while True:
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")
        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ["add", "subtract", "multiply", "divide"]:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if user_input == "add":
                result = add(x, y)
            elif user_input == "subtract":
                result = subtract(x, y)
            elif user_input == "multiply":
                result = multiply(x, y)
            elif user_input == "divide":
                try:
                    result = divide(x, y)
                except ValueError:
                    print("Error: Can not divide by zero!")
                    continue
            print("Result: ", result)
        else:
            print("Unknown input")

if __name__ == '__main__':
    main()

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()