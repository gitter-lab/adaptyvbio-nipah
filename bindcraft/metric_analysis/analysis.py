import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
import itertools
import os

def main():

    # Load
    df = pd.read_csv("bindcraft/Nivg_ipsae_taj.csv")

    # Main metric
    ip = df["min_ipSAE"]

    # Numeric columns except ipSAE
    numeric = df.select_dtypes(include=[np.number]).columns.tolist()
    numeric = [c for c in numeric if c != "min_ipSAE"]

    # -----------------------------
    #  FLIP TRUE ENERGY METRICS
    # -----------------------------
    energy_like = [
        "Binder_Energy_Score",
        "dG",
        # dSASA is positive -> don't flip
        # "dG/dSASA" is also positive -> don't flip
    ]

    for col in energy_like:
        if col in df.columns:
            df[col] = -df[col]   # flip sign so higher = better

    # Output folder
    outdir = "bindcraft/metric_analysis/plots_Nivg_ipsae_taj"
    os.makedirs(outdir, exist_ok=True)

    ###########################################################################
    #                         1️⃣ Single-metric plots                          #
    ###########################################################################
    for col in numeric:
        x = df[col]
        mask = ~(ip.isna() | x.isna())
        rho, _ = spearmanr(ip[mask], x[mask])
        n = mask.sum()

        plt.figure(figsize=(10, 6))
        plt.scatter(ip[mask], x[mask], s=10)
        plt.xlabel("min_ipSAE")
        plt.ylabel(col)
        plt.title(f"{col} vs ipSAE (n={n}, rho={rho:.2f})")

        out = f"{outdir}/{col.replace('/','_')}_vs_ipSAE.png"
        plt.tight_layout()
        plt.savefig(out, dpi=100)
        plt.close()

    ###########################################################################
    #                     2️⃣ Two-metric ensemble plots                        #
    ###########################################################################
    metric_pairs = list(itertools.combinations(numeric, 2))

    for col1, col2 in metric_pairs:
        x1 = df[col1]
        x2 = df[col2]

        # Ensemble: sum AFTER sign correction
        ensemble = x1 + x2

        mask = ~(ip.isna() | ensemble.isna())
        rho, _ = spearmanr(ip[mask], ensemble[mask])
        n = mask.sum()

        plt.figure(figsize=(10, 6))
        plt.scatter(ip[mask], ensemble[mask], s=10)
        plt.xlabel("min_ipSAE")
        plt.ylabel(f"{col1} + {col2}")
        plt.title(f"{col1} + {col2} vs ipSAE (n={n}, rho={rho:.2f})")

        outname = f"{col1}__PLUS__{col2}".replace("/", "_")
        out = f"{outdir}/{outname}_vs_ipSAE.png"
        plt.tight_layout()
        plt.savefig(out, dpi=100)
        plt.close()

    print("Finished generating all single and ensemble plots (with correct sign flips).")


def sort():
    df= pd.read_csv('bindcraft/aggregated_trajectory_stats.csv')
    df_scored = pd.read_csv('bindcraft/Nivg_ipsae_taj.csv').sort_values(by='min_ipSAE').tail(10)
    df_sorted=df.sort_values(by='Binder_Energy_Score').copy().head(13)

    all_sequences = set(df_scored['Sequence'])
    all_sequences.add("MLDVNMIVDMVADSGPLAAMDMANHMGGLVWFMWFWAGPEDKETNLVVTALYAEVDELWAYFTEQYEAGTSEQEMAPNVRAKVPGVLERVILAASKFRATRDEAVAILIHNIIVFALDNNMVTEAHVKGLRMLKQWFMASTDRTAQKVVISSMEHWIYILMHQVPPSEHDRVRQVDQNVYDGMVNFDKGADPKPFMNVAMDLLIDIIWTNFM")

    overlap = set(df_sorted['Sequence']).intersection(all_sequences)

    df_sorted.set_index('Sequence',inplace=True)

    df_sorted.drop(inplace=True,index=list(overlap))

    with open("bindcraft/metric_analysis/final_sequences/submission_nov26.fasta", "w") as f:
        for i, seq in enumerate(df_sorted.index):
            f.write(f">seq_{i + 1}\n{seq}\n")

if __name__ == "__main__":
    # main()
    sort()
