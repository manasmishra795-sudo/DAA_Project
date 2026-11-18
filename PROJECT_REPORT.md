# CryptoPower Lab — Project Report

## Abstract
CryptoPower Lab demonstrates efficient exponentiation using the Divide and Conquer paradigm. It compares repeated multiplication with recursive and iterative exponentiation by squaring, and demonstrates modular exponentiation for cryptographic-style calculations. A Streamlit interface allows users to enter values, inspect execution traces, compare algorithms and process CSV requests.

## Problem statement
Calculating a power by multiplying the base repeatedly requires a number of multiplications proportional to the exponent. This becomes inefficient for large exponents. The project demonstrates a faster method that repeatedly divides the exponent by two.

## Objectives
1. Implement a straightforward baseline algorithm.
2. Implement recursive and iterative exponentiation by squaring.
3. Implement modular exponentiation.
4. Compare time and multiplication counts.
5. Validate inputs and verify results independently.
6. Provide an interface and CSV-based batch processing.

## Methodology
The project accepts an integer base and non-negative integer exponent. For modular calculations, the modulus must be an integer greater than one. The algorithms are implemented independently in Python. The built-in `pow` function is used only to verify outputs.

## Algorithms
### Naive repeated multiplication
Starts with result 1 and multiplies by the base exactly `e` times. Its time complexity is O(e), and its auxiliary space complexity is O(1).

### Recursive exponentiation by squaring
Recursively calculates the power for half the exponent, squares the result, and multiplies by the base once more when the exponent is odd. Its time complexity is O(log e), with O(log e) recursion-stack space.

### Iterative exponentiation by squaring
Uses a loop. When the current exponent is odd, it multiplies the result by the current factor. It then squares the factor and halves the exponent. Its time complexity is O(log e), with O(1) auxiliary space.

### Modular exponentiation
Uses the iterative fast-power pattern but applies modulo `n` after each multiplication. This avoids constructing the full power when only the remainder is needed.

## Complexity comparison

| Algorithm | Time | Auxiliary space |
|---|---|---|
| Naive | O(e) | O(1) |
| Recursive fast power | O(log e) | O(log e) |
| Iterative fast power | O(log e) | O(1) |
| Modular fast power | O(log e) modular steps | O(1) |

## Correctness
The fast algorithms follow the identities:
- `a^0 = 1`
- `a^(2k) = (a^k)^2`
- `a^(2k+1) = a × (a^k)^2`

For modular exponentiation, modular reduction is valid because `(x × y) mod n` is equal to `((x mod n) × (y mod n)) mod n`. The implementation is additionally checked against Python's built-in `pow`.

## Testing
The automated tests cover:
- A known power and modular-power example.
- Exponent zero.
- Zero base.
- Negative bases.
- Exponent one.
- Invalid negative exponents.
- Invalid modulus.
- A range of inputs cross-checked against the built-in power operation.

## Results and discussion
Run the application on the target machine to obtain measured timing values. Runtime depends on the computer and environment. The theoretical comparison is stable: naive repeated multiplication uses O(e) multiplication steps, whereas exponentiation by squaring uses O(log e) steps. The application displays actual timings and operation counts rather than hard-coding expected performance results.

## Conclusion
The project demonstrates why Divide and Conquer is effective for exponentiation. Exponentiation by squaring reduces the number of multiplication steps significantly for large exponents. The modular version is particularly relevant to cryptographic computations because it returns the required remainder without constructing the full power.

## Limitations
This implementation is for algorithm education. It is not a complete or secure cryptographic service and must not be used with production secrets or private keys.
