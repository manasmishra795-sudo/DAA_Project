"""Input and CSV validation helpers."""
REQUIRED_COLUMNS = ["request_id", "timestamp", "base_a", "exponent_e", "modulus_n", "bit_length", "status"]

def validate_inputs(base, exponent, modulus=None):
    for label, value in (("Base", base), ("Exponent", exponent)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{label} must be an integer.")
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    if modulus is not None:
        if isinstance(modulus, bool) or not isinstance(modulus, int):
            raise ValueError("Modulus must be an integer.")
        if modulus <= 1:
            raise ValueError("Modulus must be greater than 1.")
    return True

def validate_dataset(df):
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError("Missing required CSV columns: " + ", ".join(missing))
    if df["request_id"].isna().any():
        raise ValueError("request_id contains empty values.")
    if df["request_id"].duplicated().any():
        raise ValueError("Duplicate request_id values found.")
    for col in ["base_a", "exponent_e", "modulus_n"]:
        if df[col].isna().any():
            raise ValueError(f"{col} contains empty values.")
        try:
            values = [int(value) for value in df[col]]
        except (TypeError, ValueError, OverflowError):
            raise ValueError(f"{col} must contain integer values.")
        if col == "exponent_e" and any(value < 0 for value in values):
            raise ValueError("Dataset contains a negative exponent.")
        if col == "modulus_n" and any(value <= 1 for value in values):
            raise ValueError("Dataset contains a modulus less than or equal to 1.")
    return True
