def subtract(a, b):
    return a - b

# Bug: Arguments flipped
print(subtract(3, 5))  # Correct: returns -2
print(subtract(5, 3))  # Correct: returns 2
