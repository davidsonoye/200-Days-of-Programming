import matplotlib.pyplot as plt
import time
import math
import numpy as np

def cube_root(n, precision=1e-10):
    """Efficient cube root calculation using bisection method
    Args:
        n: integer to find cube root of (can be negative)
        precision: acceptable error margin
    Returns:
        (approximated_root, steps_taken, execution_time)
    start_time = time.perf_counter()  # High precision timing
    steps = 0
    
    """Handle negative inputs by working with absolute values
    sign = -1 if n < 0 else 1
    n = abs(n)
    
    """Initialize search boundaries
    low = 0
    high = max(1, n)  # Ensure high > n^(1/3)
    
    """Bisection algorithm
    while True:
        steps += 1
        mid = (low + high) / 2
        cube = mid ** 3
        
        """Check if we've reached desired precision
        if abs(cube - n) <= precision:
            break
            
       """Narrow search range
        if cube < n:
            low = mid
        else:
            high = mid
    
    return (sign * mid, steps, time.perf_counter() - start_time)

def analyze_cube_root_performance():
    """Analyze and visualize cube root performance"""
    digits_range = range(1, 10)  # Test numbers from 1 to 9 digits
    steps_data = []
    time_data = []
    
    for d in digits_range:
        n = 10 ** d
        _, steps, t = cube_root(n)
        steps_data.append(steps)
        time_data.append(t * 1000)  # Convert to milliseconds
    
    """Plotting
    plt.figure(figsize=(12, 5))
    
    """Steps vs Digits plot
    plt.subplot(1, 2, 1)
    plt.plot(digits_range, steps_data, 'bo-')
    plt.xlabel('Number of Digits')
    plt.ylabel('Steps Taken')
    plt.title('Bisection Method Complexity')
    plt.grid(True)
    
    # Time vs Digits plot
    plt.subplot(1, 2, 2)
    plt.plot(digits_range, time_data, 'ro-')
    plt.xlabel('Number of Digits')
    plt.ylabel('Time (ms)')
    plt.title('Execution Time (Python)')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def is_prime(n):
    """Optimized primality test using trial division"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    # Check divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_primes(start=3, end=1000):
    """Calculate sum of primes in given range"""
    return sum(n for n in range(start, end + 1) if is_prime(n))

def egg_drop_solver(total_floors=102, max_eggs=7):
    """
    Optimal egg drop solution using binary search approach
    Args:
        total_floors: building height
        max_eggs: maximum allowed egg breaks
    Returns:
        (critical_floor, eggs_used)
    """
    low, high = 1, total_floors
    eggs_used = 0
    
    while low <= high and eggs_used < max_eggs:
        eggs_used += 1
        mid = (low + high) // 2
        
        # Simulate egg drop (in real scenario, this would be physical test)
        if mid >= 78:  # Assume 78 is the critical floor for demonstration
            high = mid - 1  # Egg broke, search lower floors
        else:
            low = mid + 1  # Egg survived, search higher floors
    
    return (high, eggs_used)

def main():
    print("Cube Root Analysis:")
    analyze_cube_root_performance()
    
    print("\nPrimality Testing:")
    prime_sum = sum_primes()
    print(f"Sum of primes between 3-1000: {prime_sum}")
    
    print("\nEgg Drop Problem Solution:")
    critical_floor, eggs_used = egg_drop_solver()
    print(f"Critical floor: {critical_floor}, Eggs used: {eggs_used}")
    
    # C vs Python performance comparison note
    print("\nPerformance Note:")
    print("For 9-digit numbers, C implementation would be ~100x faster")
    print("due to compiled vs interpreted execution.")

if name == "__main__":
    main()
