import time
import math
import matplotlib.pyplot as plt # type: ignore


def efficient_cube_root(n):
    """
    Efficiently compute the cube root of an integer using binary search.
    This method works for both positive and negative integers.
    """
    if n == 0:
        return 0, 1  # One step to determine the result is zero

    # Work with positive version and fix sign at the end
    negative = n < 0
    n_abs = abs(n)

    low = 0
    high = n_abs
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        mid_cubed = mid ** 3
        if mid_cubed == n_abs:
            return -mid if negative else mid, steps
        elif mid_cubed < n_abs:
            low = mid + 1
        else:
            high = mid - 1

    return -high if negative else high, steps  # Return floor of cube root


# Graphing cube root computation
def graph_cube_root_performance():
    digit_lengths = list(range(1, 15))
    steps_list = []
    times_list = []

    for digits in digit_lengths:
        num = 10 ** digits - 1
        start_time = time.time()
        _, steps = efficient_cube_root(num)
        end_time = time.time()

        steps_list.append(steps)
        times_list.append(end_time - start_time)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(digit_lengths, steps_list, marker='o')
    plt.title("Steps vs Number of Digits")
    plt.xlabel("Number of Digits")
    plt.ylabel("Steps Taken")

    plt.subplot(1, 2, 2)
    plt.plot(digit_lengths, times_list, marker='x', label='Python Time')
    # Note: C comparison would require implementing in C and timing externally
    plt.title("Time vs Number of Digits")
    plt.xlabel("Number of Digits")
    plt.ylabel("Time Taken (seconds)")
    plt.legend()

    plt.tight_layout()
    plt.show()


# Prime testing and sum of primes
def is_prime(n):
    """Efficient primality test"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def sum_primes(limit):
    return sum(i for i in range(3, limit + 1) if is_prime(i))


# Egg Drop Problem using 7 eggs and binary-like strategy
def egg_drop_7_eggs(floors=102):
    """
    Solves the egg drop problem with up to 7 eggs using a mathematical strategy
    based on reducing the maximum number of drops needed using optimal spacing.
    """
    attempts = 0
    egg_breaks = False
    drop_from = 0
    egg_limit = 7

    # Calculate drop interval using triangular numbers approach
    interval = 1
    while interval * (interval + 1) // 2 < floors:
        interval += 1

    current_floor = interval
    previous_floor = 0

    # Simulate unknown threshold at floor 76 for this implementation
    threshold = 76
    eggs_used = 0

    while current_floor <= floors and eggs_used < egg_limit:
        attempts += 1
        if current_floor >= threshold:
            egg_breaks = True
            break
        interval -= 1
        previous_floor = current_floor
        current_floor += interval
        eggs_used += 1

    # Linear search after break
    for floor in range(previous_floor + 1, current_floor):
        attempts += 1
        if floor >= threshold:
            break

    return attempts


# Call key functions
if __name__ == "__main__":
    print("Cube root of -729:")
    result, steps = efficient_cube_root(-729)
    print(f"Result: {result}, Steps: {steps}")

    print("\nGraphing cube root steps and performance:")
    graph_cube_root_performance()

    print("\nSum of primes between 3 and 1000:")
    print(sum_primes(1000))

    print("\nSolving Egg Drop Problem with 7 eggs:")
    attempts = egg_drop_7_eggs()
    print(f"Attempts made: {attempts}")
