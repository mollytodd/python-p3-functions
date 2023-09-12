def greet_programmer(name = "programmer"):
    print (f"Hello, {name}!")

greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

greet("Naureen")

def greet_with_default(name = "programmer"):
    print(f"Hello, {name}!")

greet_with_default()

def add(num1, num2):
    return num1+num2

add(1, 1)


def halve(number):
    if not isinstance(number, (int, float)):
        return None

    return number / 2