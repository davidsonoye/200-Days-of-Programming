import math

# Constants
MAX_ITER = 100
TOL = 1e-5

# Define f(x)
def fval(x):
    return 4 * x + math.sin(x) - math.exp(x)

# Define f'(x)
def dfval(x):
    return 4 + math.cos(x) - math.exp(x)

# Initial guess
x0 = 0.0

print("Iter\t xk\t\t\t f(xk)\t\t\t Error")
xk = x0
fxk = fval(xk)

for k in range(1, MAX_ITER + 1):
    xp = xk
    fxp = fxk
    dfxp = dfval(xp)
    
    if dfxp == 0:
        print("Zero derivative encountered. Stopping iteration.")
        break

    xk = xp - fxp / dfxp
    fxk = fval(xk)
    err = abs((xk - xp) / xk) if xk != 0 else abs(xk - xp)
    
    print(f"{k}\t{xk:.10f}\t{fxk:.10f}\t{err:.10f}")
    
    if err < TOL:
        print("\nRequired accuracy achieved. Solution is convergent.")
        break
else:
    print("\nThe number of iterations exceeded the maximum limit.")


"""Iter     xk               f(xk)             Error
1        0.0000000000     -1.0000000000     1.0000000000
2        0.4826282746     0.1340644203      1.0000000000
3        0.4581887869     0.0004921369      0.0533936826
4        0.4580986483     0.0000000082      0.0001968869

Required accuracy achieved. Solution is convergent.

