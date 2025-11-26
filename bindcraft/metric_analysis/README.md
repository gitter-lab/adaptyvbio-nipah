# Metric Analysis 

## Submission 1 (November 26, 2025)

To determine which binders to submit in the second round (where we don't have ipSAE scores yet).

I decided to plot each metric that was already calculated vs ipSAE for the binders that we do have (`bindcraft/Nivg_ipsae_taj.csv`) 
to see if any correlation exists. 

What I found: 

Interestingly 3 metrics slightly correlate with ipSAE , not sure if it is due to length or not :

* [Binder_energy_score](bindcraft/metric_analysis/plots_Nivg_ipsae_taj/Binder_Energy_Score_vs_ipSAE.png)  - negatively correlated which is good 
* [dSASA (solvent accessibility) ](bindcraft/metric_analysis/plots_Nivg_ipsae_taj/dSASA_vs_ipSAE.png) - shows a similar correlation to length so I think this is length dependent.  
* [number interface residues](bindcraft/metric_analysis/plots_Nivg_ipsae_taj/n_InterfaceResidues_vs_ipSAE.png) - looks to be length dependent 
* [Length ](bindcraft/metric_analysis/plots_Nivg_ipsae_taj/Length_vs_ipSAE.png)
* [pLDDT ](bindcraft/metric_analysis/plots_Nivg_ipsae_taj/pLDDT_vs_ipSAE.png) - looks to also be somewhat length dependent - the longer the worse it is    

I’m going to choose binder_energy_score to select binders since it doesn’t look length dependent.
Also , all linear ensembles of two values did not lead to improvements in correlations (plots not pushed due to size.)


Using `Binder_energy_score` as the metric and sorting (`bindcraft/aggregated_trajectory_stats.csv`). 


Of the top 10 lowest `Binder_energy_score`, 
Three sequences selected did overlap with the highest min_ipSAE from the first submission. (One was only found by ProteinBase)
As such, I had to select the top 13 sequences and remove the ones that had overlap. 

I then submitted the remaining [10 sequences](bindcraft/metric_analysis/final_sequences/submission_nov26.fasta) as the first submission. 




