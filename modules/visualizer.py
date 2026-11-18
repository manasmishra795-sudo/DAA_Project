"""Plotting helpers used by the Streamlit dashboard."""
import matplotlib.pyplot as plt
import pandas as pd

def comparison_chart(results):
    df = pd.DataFrame(results)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.bar(df["Algorithm"], df["Time (ms)"])
    ax.set_ylabel("Execution time (milliseconds)")
    ax.set_title("Execution-time comparison")
    ax.tick_params(axis="x", rotation=18)
    fig.tight_layout()
    return fig

def multiplication_chart(results):
    df = pd.DataFrame(results)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.bar(df["Algorithm"], df["Multiplications"])
    ax.set_ylabel("Multiplication count")
    ax.set_title("Multiplication-count comparison")
    ax.tick_params(axis="x", rotation=18)
    fig.tight_layout()
    return fig
