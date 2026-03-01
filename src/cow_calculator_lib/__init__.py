import cowsay


def add(a: int, b: int) -> int:
    cowsay.cow(f"Adding {a} and {b}")
    return a + b


def subtract(a: int, b: int) -> int:
    cowsay.cow(f"Subtracting {a} by {b}")
    return a - b


def multiply(a: int, b: int) -> int:
    cowsay.cow(f"Multiplying {a} by {b}")
    return a * b


def divide(a: int, b: int) -> float:
    cowsay.cow(f"Dividing {a} by {b}")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return float(a / b)
