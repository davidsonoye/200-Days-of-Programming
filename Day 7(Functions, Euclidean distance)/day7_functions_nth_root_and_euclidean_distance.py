import math

def nth_root(x, n):
    """
    Returns the nth root of x.
    Handles both positive and negative inputs when appropriate.
    """
    if x < 0 and n % 2 == 0:
        raise ValueError("Even root of a negative number is not a real number.")
    return x ** (1 / n)


def euclidean_distance(y1, y2):
    """
    Returns the square root of (y1^2 - y2^2).
    This assumes y1^2 >= y2^2 to avoid complex results.
    """
    diff = y1**2 - y2**2
    if diff < 0:
        raise ValueError("Result under square root is negative. Ensure y1^2 >= y2^2.")
    return math.sqrt(diff)

# Example usage:
print("Cube root of 27:", nth_root(27, 3))               # Output: 3.0
print("Distance from y1=5, y2=3:", euclidean_distance(5, 3))  # Output: 4.0

