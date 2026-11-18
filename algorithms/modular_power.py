"""Modular exponentiation by squaring."""
def modular_fast_power(base: int, exponent: int, modulus: int, *, return_stats: bool = False):
    """Calculate (base**exponent) % modulus without constructing base**exponent.

    Time: O(log exponent) modular multiplication steps.
    """
    if not all(isinstance(x, int) for x in (base, exponent, modulus)):
        raise TypeError("Base, exponent and modulus must be integers.")
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    if modulus <= 1:
        raise ValueError("Modulus must be greater than 1.")
    result = 1 % modulus
    factor = base % modulus
    power = exponent
    count = 0
    trace = []
    while power > 0:
        before = power
        if power & 1:
            result = (result * factor) % modulus
            count += 1
        factor = (factor * factor) % modulus
        count += 1
        power >>= 1
        trace.append({
            "exponent_before": before,
            "result": result,
            "factor": factor,
            "exponent_after": power
        })
    if return_stats:
        return result, {"multiplications": count, "steps": trace}
    return result
