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


    print("\nSolving Egg Drop Problem with 7 eggs:")
    attempts = egg_drop_7_eggs()
    print(f"Attempts made: {attempts}")
