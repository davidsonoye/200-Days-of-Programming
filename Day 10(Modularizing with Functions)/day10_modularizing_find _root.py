def find_root_bounds(x, power):
    """Finds bounds such that low**power <= x <= high**power"""
    low = min(-1, x)
    high = max(1, x)
    return low, high

def bisection_solve(x, power, epsilon, low, high):
    """Uses bisection to find root within epsilon"""
    ans = (high + low) / 2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

def find_root(x, power, epsilon):
    """Returns root of x to the given power within epsilon"""
    if x < 0 and power % 2 == 0:
        return None  # No real root for even powers of negative numbers
    low, high = find_root_bounds(x, power)
    return bisection_solve(x, power, epsilon, low, high)
