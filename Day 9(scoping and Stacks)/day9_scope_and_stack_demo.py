def f(x):
    def g():
        x = 'abc'        # Local x in g (shadows outer x)
        print('x =', x)  # Uses g's x ('abc')

    def h():
        z = x            # Uses f's x (4)
        print('z =', z)  # z = 4

    x = x + 1            # Modifies f's x (3 → 4)
    print('x =', x)      # x = 4
    h()
    g()
    print('x =', x)      # Still f's x (4)
    return g

x = 3                   # Global x
z = f(x)                # z becomes the function g
print('x =', x)         # Global x remains 3
print('z =', z)         # z is the function g
z()                     # Calls g(), prints 'abc'



"""
x = 4      # From f(x)
z = 4      # From h()
x = abc    # From g()
x = 4      # After g() completes
x = 3      # Global x unchanged
z = <function f.<locals>.g ...>  
x = abc    # From z() (calling g())
"""
