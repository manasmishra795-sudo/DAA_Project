"""CryptoPower Lab — interactive Streamlit application."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
import pandas as pd
from algorithms.naive import naive_power
from algorithms.fast_power import recursive_fast_power, iterative_fast_power
from algorithms.modular_power import modular_fast_power
from modules.validator import validate_inputs
from modules.benchmark import benchmark_power, benchmark_modular
from modules.visualizer import comparison_chart, multiplication_chart
from modules.csv_handler import load_dataset, process_dataset

st.set_page_config(page_title="CryptoPower Lab", page_icon="🔐", layout="wide")
st.title("🔐 CryptoPower Lab")
st.caption("A Divide and Conquer demonstration of fast exponentiation for cryptographic-style calculations.")

with st.sidebar:
    st.header("Navigation")
    page = st.radio("Choose a section", ["Calculator", "Algorithm comparison", "CSV batch processing", "About"])

if page == "Calculator":
    st.subheader("Calculate a power")
    mode = st.radio("Calculation type", ["Ordinary power (a^e)", "Modular power (a^e mod n)"], horizontal=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        base = st.number_input("Base (a)", value=7, step=1, format="%d")
    with c2:
        exponent = st.number_input("Exponent (e)", min_value=0, value=13, step=1, format="%d")
    with c3:
        modulus = st.number_input("Modulus (n)", min_value=2, value=11, step=1, format="%d", disabled=(mode == "Ordinary power (a^e)"))
    if st.button("Calculate", type="primary"):
        try:
            a, e, n = int(base), int(exponent), int(modulus)
            if mode == "Ordinary power (a^e)":
                validate_inputs(a, e)
                st.success(f"Result: {iterative_fast_power(a, e)}")
                st.write("Recursive result:", recursive_fast_power(a, e))
                st.write("Naive result:", naive_power(a, e) if e <= 100000 else "Skipped for large exponent.")
            else:
                validate_inputs(a, e, n)
                result, stats = modular_fast_power(a, e, n, return_stats=True)
                st.success(f"Result: {result}")
                st.write(f"Independent verification using Python pow(): **{pow(a, e, n) == result}**")
                st.write(f"Multiplication operations counted: **{stats['multiplications']}**")
                st.write("Execution trace:")
                st.dataframe(pd.DataFrame(stats["steps"]), use_container_width=True)
        except Exception as exc:
            st.error(str(exc))

elif page == "Algorithm comparison":
    st.subheader("Compare exponentiation algorithms")
    st.info("Naive repeated multiplication is intentionally skipped for exponents above 100,000 to avoid an unnecessarily long run.")
    c1, c2 = st.columns(2)
    with c1:
        base = st.number_input("Base", value=3, step=1, key="bench_base")
    with c2:
        exponent = st.number_input("Exponent", min_value=0, value=500, step=1, key="bench_exp")
    if st.button("Run comparison", type="primary"):
        try:
            a, e = int(base), int(exponent)
            results = benchmark_power(a, e, include_naive=(e <= 100000))
            st.dataframe(pd.DataFrame(results), use_container_width=True)
            st.pyplot(comparison_chart(results))
            st.pyplot(multiplication_chart(results))
            st.caption("Measured times depend on the computer, Python version and system load. Multiplication counts are implementation-level counts.")
        except Exception as exc:
            st.error(str(exc))
    st.divider()
    st.subheader("Modular exponentiation")
    mc1, mc2, mc3 = st.columns(3)
    with mc1: ma = st.number_input("Base", value=7, step=1, key="mod_a")
    with mc2: me = st.number_input("Exponent", min_value=0, value=13, step=1, key="mod_e")
    with mc3: mn = st.number_input("Modulus", min_value=2, value=11, step=1, key="mod_n")
    if st.button("Run modular calculation"):
        try:
            result = benchmark_modular(int(ma), int(me), int(mn))
            st.dataframe(pd.DataFrame(result), use_container_width=True)
        except Exception as exc:
            st.error(str(exc))

elif page == "CSV batch processing":
    st.subheader("Process a CSV dataset")
    st.write("Upload a CSV with the columns shown below, or select one of the included sample datasets.")
    st.code("request_id,timestamp,base_a,exponent_e,modulus_n,bit_length,status")
    sample = st.selectbox("Included dataset", ["small.csv", "medium.csv", "large.csv"])
    uploaded = st.file_uploader("Or upload your own CSV", type=["csv"])
    if uploaded is not None:
        df = pd.read_csv(uploaded)
    else:
        path = Path(__file__).parent / "datasets" / sample
        df = pd.read_csv(path)
    st.write(f"Rows loaded: {len(df)}")
    st.dataframe(df.head(20), use_container_width=True)
    if st.button("Validate and process dataset", type="primary"):
        try:
            output = process_dataset(df)
            st.success(f"Processed {len(output)} requests. All modular results verified.")
            st.dataframe(output.head(100), use_container_width=True)
            st.download_button("Download processed results", output.to_csv(index=False), "cryptopower_results.csv", "text/csv")
        except Exception as exc:
            st.error(str(exc))

else:
    st.subheader("Project overview")
    st.markdown("""
**Problem:** Repeated multiplication becomes inefficient when the exponent is large.

**Selected paradigm:** Divide and Conquer.

**Main method:** Exponentiation by Squaring. It repeatedly halves the exponent, reducing the number of multiplication steps from linear to logarithmic.

**Algorithms included**
- Naive repeated multiplication — baseline, O(e) time.
- Recursive exponentiation by squaring — O(log e) time and O(log e) call-stack space.
- Iterative exponentiation by squaring — O(log e) time and O(1) auxiliary space.
- Modular exponentiation by squaring — calculates `(a^e) mod n` while keeping intermediate values reduced modulo `n`.

**Correctness check:** Python's built-in `pow(a, e, n)` is used as an independent verifier, not as the algorithm being benchmarked.

**Educational limitation:** This project demonstrates algorithms. It is not a production cryptographic library and should not be used to protect real secrets or private keys.
""")
    st.subheader("Worked example")
    st.latex(r"7^{13} \\bmod 11 = 2")
    st.write("For the example inputs, the modular algorithm returns 2.")
