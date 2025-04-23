import math

# Target function
def f(x):
    return 4 * x + math.sin(x) - math.exp(x)

# Derivative for Newton-Raphson
def df(x):
    return 4 + math.cos(x) - math.exp(x)

# Newton-Raphson Method
def newton_raphson(x0, tol=1e-6, max_iter=50):
    xk = x0
    for k in range(1, max_iter + 1):
        fx = f(xk)
        dfx = df(xk)

        if dfx == 0:
            return None, k, False  # Derivative is zero

        xk_next = xk - fx / dfx
        err = abs((xk_next - xk) / xk_next) if xk_next != 0 else abs(xk_next - xk)

        if err < tol:
            return xk_next, k, True

        xk = xk_next

    return xk, max_iter, False  # Max iterations reached

# Bisection Method
def bisection(a, b, tol=1e-6, max_iter=50):
    if f(a) * f(b) > 0:
        return None, 0, False  # Root not guaranteed in interval

    for k in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < tol or abs(b - a) / 2 < tol:
            return c, k, True

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return c, max_iter, False  # Max iterations reached

# Comparison Function
def compare_methods():
    print("Comparing Newton-Raphson vs Bisection for:")
    print("f(x) = 4x + sin(x) - exp(x)\n")

    # Initial conditions
    x0 = 0.0           # Initial guess for Newton-Raphson
    a, b = 0, 1        # Interval for Bisection

    # Run both methods
    root_nr, steps_nr, success_nr = newton_raphson(x0)
    root_bi, steps_bi, success_bi = bisection(a, b)

    # Display results
    print(f"Newton-Raphson:")
    print(f"  Root: {root_nr:.10f}" if root_nr else "  Failed to converge")
    print(f"  Steps: {steps_nr}")
    print(f"  f(root): {f(root_nr):.2e}" if root_nr else "")

    print(f"\nBisection:")
    print(f"  Root: {root_bi:.10f}" if root_bi else "  Failed to converge")
    print(f"  Steps: {steps_bi}")
    print(f"  f(root): {f(root_bi):.2e}" if root_bi else "")

# Run comparison
compare_methods()



"""Comparing Newton-Raphson vs Bisection for:
f(x) = 4x + sin(x) - exp(x)

Newton-Raphson:
  Root: 0.4580986483
  Steps: 4
  f(root): 8.22e-09

Bisection:
  Root: 0.4580993652
  Steps: 24
  f(root): -1.00e-07
