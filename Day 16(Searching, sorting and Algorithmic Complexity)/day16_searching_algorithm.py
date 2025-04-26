import random
import time

# Generate 1000 random sensor readings
sensor_data = [random.uniform(20.0, 100.0) for _ in range(1000)]


# --------- SEARCHING ALGORITHMS ---------

# 1. Linear Search
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# 2. Binary Search (requires sorted data)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 3. Hash Search
def hash_search(hash_table, target):
    return hash_table.get(target, -1)



target_value = sensor_data[500]  # Randomly pick an existing value for search

print("\n--- SEARCHING ---")

# Linear Search
start = time.time()
linear_result = linear_search(sensor_data, target_value)
print(f"Linear Search Index: {linear_result}, Time: {time.time() - start:.6f} sec")

# Binary Search
sorted_sensor_data = sorted(sensor_data)
start = time.time()
binary_result = binary_search(sorted_sensor_data, target_value)
print(f"Binary Search Index: {binary_result}, Time: {time.time() - start:.6f} sec")

# Hash Search
sensor_hash = {val: idx for idx, val in enumerate(sensor_data)}
start = time.time()
hash_result = hash_search(sensor_hash, target_value)
print(f"Hash Search Index: {hash_result}, Time: {time.time() - start:.6f} sec")


print("\n--- SORTING ---")
