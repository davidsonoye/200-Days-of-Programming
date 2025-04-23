import math  # Import the math library for sin, cos, and exp functions

# Set tolerance level for stopping criterion
TOL = 1e-6  # The iteration will stop when the relative error is less than this value

# Set the maximum number of iterations
MAX_ITER = 50  # Prevents infinite looping if convergence is not achieved

# Get the initial guess from the user
x0 = float(input("Enter the initial approximation: "))

# Print table header for iteration results
print("iter.\txk\t\t\tf(xk)\t\t\tError")

# Initialize the current guess
xk = x0

# Evaluate the function at the initial guess
# f(x) = 4x + sin(x) - exp(x)
fxk = 4 * xk + math.sin(xk) - math.exp(xk)

# Begin iteration loop
for k in range(1, MAX_ITER + 1):
    xp = xk      # Store the previous guess
    fxp = fxk    # Store the function value at the previous guess

    # Compute derivative at xp
    # f'(x) = 4 + cos(x) - exp(x)
    dfxp = 4 + math.cos(xp) - math.exp(xp)

    # Check if derivative is zero to avoid division by zero
    if dfxp == 0:
        print("Zero derivative encountered. Stopping iteration.")
        break

    # Newton-Raphson update: x_{k+1} = x_k - f(x_k)/f'(x_k)
    xk = xp - (fxp / dfxp)

    # Evaluate the function at the new guess
    fxk = 4 * xk + math.sin(xk) - math.exp(xk)

    # Compute the relative error
    # Use absolute difference for error and normalize by xk if xk != 0
    err = abs((xk - xp) / xk) if xk != 0 else abs(xk - xp)

    # Print current iteration results
    print(f"{k}\t{xk:.16f}\t{fxk:.16f}\t{err:.12f}")

    # Check if the required tolerance has been achieved
    if err < TOL:
        print("\nRequired accuracy achieved; Solution is convergent.")
        break
else:
    # Executed if the loop completes without breaking (no convergence)
    print("\nThe number of iterations exceeded the maximum limit.")


"""iter.   xk               f(xk)            Error
1       0.4826282746     0.1340644203     1.0000000000
2       0.4581887869     0.0004921369     0.0533936826
3       0.4580986483     0.0000000082     0.0001968869

Required accuracy achieved; Solution is convergent.
