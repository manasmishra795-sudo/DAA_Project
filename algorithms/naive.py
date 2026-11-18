"""Baseline repeated-multiplication exponentiation."""
def naive_power(base: int, exponent: int, *, return_stats: bool = False):
    """Calculate base**exponent using repeated multiplication.

    Time: O(exponent) multiplications. Space: O(1).
    """
    if not isinstance(base, int) or not isinstance(exponent, int):
        raise TypeError("Base and exponent must be integers.")
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    result = 1
    multiplications = 0
    for _ in range(exponent):
        result *= base
        multiplications += 1
    if return_stats:
        return result, {"multiplications": multiplications, "steps": exponent}
    return result
