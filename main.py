"""Command-line demonstration for CryptoPower Lab."""
import argparse
from algorithms.naive import naive_power
from algorithms.fast_power import recursive_fast_power, iterative_fast_power
from algorithms.modular_power import modular_fast_power

def main():
    parser = argparse.ArgumentParser(description="CryptoPower Lab demonstration")
    parser.add_argument("--base", type=int, default=7)
    parser.add_argument("--exponent", type=int, default=13)
    parser.add_argument("--modulus", type=int, default=11)
    args = parser.parse_args()
    print(f"Input: base={args.base}, exponent={args.exponent}, modulus={args.modulus}")
    print("Naive:", naive_power(args.base, args.exponent))
    print("Recursive fast power:", recursive_fast_power(args.base, args.exponent))
    print("Iterative fast power:", iterative_fast_power(args.base, args.exponent))
    print("Modular fast power:", modular_fast_power(args.base, args.exponent, args.modulus))
    print("Independent check:", pow(args.base, args.exponent, args.modulus))

if __name__ == "__main__":
    main()
