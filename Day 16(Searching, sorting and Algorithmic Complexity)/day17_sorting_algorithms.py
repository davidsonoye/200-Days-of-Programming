import random
import time

# Generate 1000 random sensor readings
sensor_data = [random.uniform(20.0, 100.0) for _ in range(1000)]


# --------- SORTING ALGORITHMS ---------

# 1. Bubble Sort
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 2. Selection Sort
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 3. Insertion Sort
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 4. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 5. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 6. Heap Sort
import heapq
def heap_sort(arr):
    arr = arr.copy()
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


# --------- TESTING ---------

target_value = sensor_data[500]  # Randomly pick an existing value for search

print("\n--- SORTING ---")

# Bubble Sort
start = time.time()
bubble_sorted = bubble_sort(sensor_data)
print(f"Bubble Sort Time: {time.time() - start:.6f} sec")

# Selection Sort
start = time.time()
selection_sorted = selection_sort(sensor_data)
print(f"Selection Sort Time: {time.time() - start:.6f} sec")

# Insertion Sort
start = time.time()
insertion_sorted = insertion_sort(sensor_data)
print(f"Insertion Sort Time: {time.time() - start:.6f} sec")

# Merge Sort
start = time.time()
merge_sorted = merge_sort(sensor_data)
print(f"Merge Sort Time: {time.time() - start:.6f} sec")

# Quick Sort
start = time.time()
quick_sorted = quick_sort(sensor_data)
print(f"Quick Sort Time: {time.time() - start:.6f} sec")

# Heap Sort
start = time.time()
heap_sorted = heap_sort(sensor_data)
print(f"Heap Sort Time: {time.time() - start:.6f} sec")
