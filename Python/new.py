import os  # unused import
import sys  # unused import

def test_function():
    unused_var = "hello"  # unused variable
    another_unused = 42   # unused variable
    return "world"

# Type error test
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers("hello", "world")  # Should show type error
