"""Benchmark algorithm implementations."""
from time import perf_counter
from algorithms.naive import naive_power
from algorithms.fast_power import recursive_fast_power, iterative_fast_power
from algorithms.modular_power import modular_fast_power

def benchmark_power(base, exponent, include_naive=True):
    rows = []
    methods = []
    if include_naive:
        methods.append(("Naive repeated multiplication", naive_power))
    methods.extend([
        ("Recursive exponentiation by squaring", recursive_fast_power),
        ("Iterative exponentiation by squaring", iterative_fast_power),
    ])
    expected = pow(base, exponent)
    for name, fn in methods:
        start = perf_counter()
        result, stats = fn(base, exponent, return_stats=True)
        elapsed = perf_counter() - start
        rows.append({
            "Algorithm": name,
            "Result correct": result == expected,
            "Time (ms)": elapsed * 1000,
            "Multiplications": stats["multiplications"]
        })
    return rows

def benchmark_modular(base, exponent, modulus):
    start = perf_counter()
    result, stats = modular_fast_power(base, exponent, modulus, return_stats=True)
    elapsed = perf_counter() - start
    return [{
        "Algorithm": "Modular exponentiation by squaring",
        "Result": result,
        "Verified": result == pow(base, exponent, modulus),
        "Time (ms)": elapsed * 1000,
        "Multiplications": stats["multiplications"]
    }]
