"""
Helper functions for the calculator application.
"""

def parse_args(args):
    """Parse command line arguments."""
    if len(args) != 3:
        raise ValueError("Usage: calc.py <operation> <x> <y>")
    
    operation, x, y = args
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        raise ValueError("Both x and y must be numbers")
    
    return {'operation': operation, 'x': x, 'y': y}

def calculate(operation, x, y):
    """Perform calculation based on operation."""
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y
    else:
        raise ValueError(f"Unknown operation: {operation}. Use add, subtract, multiply, or divide.")