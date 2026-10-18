class CalculatorError(Exception):
    """Base exception for calculator errors."""


class DivisionByZeroError(CalculatorError):
    """Raised when division or modulus by zero is attempted."""


class InvalidOperationError(CalculatorError):
    """Raised when an unsupported operation is requested."""