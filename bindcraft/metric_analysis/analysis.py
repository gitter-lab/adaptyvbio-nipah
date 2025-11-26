
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

plt.rcParams['font.size'] = 14


def main():
    df = pd.read_csv('bindcraft/Nivg_ipsae_taj.csv')
    ip = df['min_ipSAE']
    numeric = df.select_dtypes(include=[np.number]).columns
    numeric = [c for c in numeric if c!='min_ipSAE']

    outs=[]
    for i,col in enumerate(numeric):
        x=df[col]; mask=~(ip.isna()|x.isna())
        rho,_=spearmanr(ip[mask],x[mask]); n=mask.sum()
        plt.figure(figsize=(10,6))
        plt.scatter(ip[mask], x[mask], s=10)
        plt.xlabel('min_ipSAE'); plt.ylabel(col)
        plt.title(f'{col} vs ipSAE (n={n}, rho={rho:.2f})')

        out=f'bindcraft/metric_analysis/plots_Nivg_ipsae_taj/{col.replace("/","_")}_vs_ipSAE.png'
        plt.tight_layout(); plt.savefig(out,dpi=100); plt.close()
        outs.append(out)

if __name__ == '__main__':
    main()