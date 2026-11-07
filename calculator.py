"""A tiny calculator, used to demonstrate ContextGuard."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raises ValueError when b is zero."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def average(numbers):
    """Return the arithmetic mean of a non-empty list of numbers."""
    if not numbers:
        raise ValueError("average of an empty list")
    return sum(numbers) / len(numbers)
