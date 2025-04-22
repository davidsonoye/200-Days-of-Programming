coordinates = (10.5, 20.3)     # (x, y)
# coordinates[0] = 15.0  ❌ Error! Tuples can't be changed
print(coordinates)            # Output: (10.5, 20.3)

# As function return
def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([4, 1, 9])
print(result)  # Output: (1, 9)
