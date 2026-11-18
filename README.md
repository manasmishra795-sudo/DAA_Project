# CryptoPower Lab

DAA project: Fast Power for Cryptographic Services using Divide and Conquer.

## Setup on Windows

Open this folder in VS Code, then run these commands in the terminal:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python --version
streamlit --version
```

## Structure
- algorithms/: naive, recursive, iterative and modular exponentiation
- modules/: validation, verification, benchmarking, visualisation and CSV handling
- datasets/: small, medium and large synthetic datasets
- results/: generated reports and graphs
- main.py: command-line entry point
- app.py: Streamlit interface

This is an educational prototype, not a production cryptographic library. Do not use it with real secret keys.
