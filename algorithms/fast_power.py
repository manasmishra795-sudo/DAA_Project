"""Recursive and iterative exponentiation by squaring."""
def recursive_fast_power(base: int, exponent: int, *, return_stats: bool = False):
    """Calculate base**exponent recursively in O(log exponent) multiplications."""
    if not isinstance(base, int) or not isinstance(exponent, int):
        raise TypeError("Base and exponent must be integers.")
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    count = 0
    def solve(b, e):
        nonlocal count
        if e == 0:
            return 1
        half = solve(b, e // 2)
        count += 1
        square = half * half
        if e % 2:
            count += 1
            return square * b
        return square
    value = solve(base, exponent)
    if return_stats:
        return value, {"multiplications": count, "steps": count}
    return value


def iterative_fast_power(base: int, exponent: int, *, return_stats: bool = False):
    """Calculate base**exponent iteratively in O(log exponent) time, O(1) space."""
    if not isinstance(base, int) or not isinstance(exponent, int):
        raise TypeError("Base and exponent must be integers.")
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    result = 1
    factor = base
    power = exponent
    count = 0
    steps = []
    while power > 0:
        before = power
        if power % 2 == 1:
            result *= factor
            count += 1
        factor *= factor
        count += 1
        power //= 2
        steps.append({
            "exponent_before": before,
            "result_after": result,
            "factor_after_squaring": factor,
            "exponent_after": power
        })
    if return_stats:
        return result, {"multiplications": count, "steps": steps}
    return result
