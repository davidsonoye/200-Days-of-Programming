import inspect

# 1. Global vs Local vs Enclosing Scope
x = "global"

def outer():
    x = "enclosed"              # Enclosing scope variable

    def inner_local():
        x = "inner-local"       # Local to inner_local
        print("inner_local x:", x)  # Prints "inner-local"

    def inner_enclosed():
        print("inner_enclosed x:", x)  # Finds 'x' in the enclosing scope
    inner_local()
    inner_enclosed()
    print("outer x after calls:", x)   # Prints "enclosed"

outer()
print("global x remains:", x)         # Prints "global"


# 2. Closure and nonlocal modification
def make_counter():
    count = 0                     # Enclosing scope

    def counter():
        nonlocal count           # Modify the enclosing 'count'
        count += 1
        print("counter value:", count)
    return counter

c = make_counter()
c()  # counter value: 1
c()  # counter value: 2


# 3. Inspecting the Call Stack
def a():
    print("Stack at a():", [f.function for f in inspect.stack()])
    b()

def b():
    print("Stack at b():", [f.function for f in inspect.stack()])
    c()

def c():
    print("Stack at c():", [f.function for f in inspect.stack()])

a()

"""
OUTPUT
Inside f(), after x + 1, x = 3
Inside h(), z = 3
Inside g(), x = abc
Inside f(), after g() and h(), x = 3
After f(x), z = <function f.<locals>.g at 0x...>
Inside g(), x = abc
Global x = 2
"""
