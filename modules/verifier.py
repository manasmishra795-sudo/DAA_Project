"""Independent correctness checks using Python's built-in pow."""
def verify_power(base, exponent, result):
    return result == pow(base, exponent)

def verify_modular_power(base, exponent, modulus, result):
    return result == pow(base, exponent, modulus)
