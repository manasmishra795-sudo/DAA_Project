
"""CSV loading and saving."""

from pathlib import Path
import pandas as pd

from .validator import validate_dataset
from algorithms.modular_power import modular_fast_power


def load_dataset(path):
    df = pd.read_csv(path)
    validate_dataset(df)
    return df


def process_dataset(df):
    # Validate the input dataset
    validate_dataset(df)

    # Create a copy so the original dataset remains unchanged
    output = df.copy()

    # Calculate modular exponentiation for every request
    output["result"] = [
        modular_fast_power(
            int(row.base_a),
            int(row.exponent_e),
            int(row.modulus_n)
        )
        for row in output.itertuples()
    ]

    # Independently verify each calculated result
    output["verified"] = [
        value == pow(
            int(row.base_a),
            int(row.exponent_e),
            int(row.modulus_n)
        )
        for value, row in zip(
            output["result"],
            output.itertuples()
        )
    ]

    # Update request status based on verification
    output["status"] = [
        "completed" if verified else "failed"
        for verified in output["verified"]
    ]

    return output


def save_results(df, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
