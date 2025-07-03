class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b

    def subtract(self, a, b):
        self.result = a - b

    def multiply(self, a, b):
        self.result = a * b

    def divide(self, a, b):
        self.result = a / b

    def get_result(self):
        return self.result


def greet(name):
    print(f"Hello, {name}!")

    def temp():
        print("temp")

class Animal:
    def __init__(self, name):
        self.name = name