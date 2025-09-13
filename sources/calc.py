#!/usr/bin/env python3
"""
Main calculation module. Provides basic arithmetic functions.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    # Simple CLI interface for demonstration
    import sys
    from .helpers import parse_args, calculate

    try:
        args = parse_args(sys.argv[1:])
        result = calculate(args['operation'], args['x'], args['y'])
        print(f"The result of {args['x']} {args['operation']} {args['y']} is: {result}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)