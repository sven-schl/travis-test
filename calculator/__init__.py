"""A simple implementation of some basic calculator operations."""


class Calculator:
    """Provides all basic math operations."""

    def add(self, a, b):
        """Add a to b and return the sum."""
        return a + b

    def sub(self, a, b):
        """Subtract b from a and return the difference."""
        return a - b

    def mul(self, a, b):
        """Multiply a and b and return the product."""
        return a * b

    def div(self, dividend, divisor):
        """Divide ``dividend`` by ``divisor`` and return the quotient."""
        return dividend / divisor
