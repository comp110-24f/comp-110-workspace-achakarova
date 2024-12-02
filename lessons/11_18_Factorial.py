# Factorial
def factorial(n: int) -> int:
    """Calculates factorial of int n."""
    # Edge Case
    if n < 0:
        return -1
    # Base Case
    if n == 1 or n == 0:
        return 1
    # Recursive case
    if n > 1:
        return n * factorial(n - 1)


print(factorial(6))
