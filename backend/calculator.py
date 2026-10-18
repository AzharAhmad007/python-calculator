from backend.exceptions import (
    DivisionByZeroError,
    InvalidOperationError,
)


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers."""

    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")

    return a / b


def modulus(a: float, b: float) -> float:
    """Return the remainder after division."""

    if b == 0:
        raise DivisionByZeroError(
            "Cannot calculate modulus with zero."
        )

    return a % b


def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b


def calculate(a: float, b: float, operation: str) -> float:
    """Execute a calculation based on the requested operation."""

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "modulus": modulus,
        "power": power,
    }

    if operation not in operations:
        raise InvalidOperationError(
            f"Unsupported operation: {operation}"
        )

    return operations[operation](a, b)