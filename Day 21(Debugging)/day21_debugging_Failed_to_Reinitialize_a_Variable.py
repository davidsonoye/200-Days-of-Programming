counter = 0

def add_one():
    global counter
    counter += 1
    return counter

add_one()
add_one()
# Bug: counter wasn’t reset — it keeps increasing
