# Final submissions (by Tapan Ravi and Bryce Johnson)

## Submission 1 

**Overview:** The FASTA file contains 4 sequences, all generated using BindCraft with the following configuration:

**BindCraft Settings:**
- Default BindCraft filters and advanced settings were applied
- No specific interaction sites were specified
- Sequence lengths ranged from 10 to 250 residues
- `predict_initial_guess = True` (generates initial structure predictions to guide design)
- `fix_mpnn_interface = False` (allows ProteinMPNN to redesign the interface residues)

---

## Submission 2 

**Overview:** The FASTA file contains 2 sequences that were iteratively optimized based on initial high-scoring submissions.

**Design Pipeline:**

1. **Warm-Start BindCraft Generation:** Starting sequences were generated using a customized BindCraft implementation that employs a warm-start initialization strategy rather than standard random initialization:
   - **Warm-Start Modification:** Initializes sequence logits biased toward a known binding sequence (z₀[i, a] = β·δ(a = a_known[i]) + ε).
   
2. **Large-Scale Screening:** 666 successful BindCraft trajectories were generated and evaluated using Boltz2 to predict ipSAE scores.

3. **Machine Learning-Based Selection:** A sequence classifier was developed to predict sequences likely to achieve ipSAE > 0.8 using ESM-C embeddings.

4. **Rational Mutagenesis:** Mutations were introduced in regions predicted to be less critical for binding (residues distant from the binding interface based on 3D structure analysis).

5. **Final Selection:** Mutated sequences were scored by the ESM-C classifier, and the highest-confidence predictions were submitted.

---

## BindCraft NIVG settings
The structure (PDB [2VSM](https://www.rcsb.org/structure/2vsm)) and interaction sites are those provided by [Adaptyv](https://design.adaptyvbio.com/).
A different HTCondor submission file `run_bindcraft_EGFR_<n>.sub` was used for each of the settings below with the same executable script `run_bindcraft_EGFR.sh`.

Environment variables controlled which BindCraft settings in the `NIVG` or `NIVG512` subdirectory were passed to the script.
1. Default BindCraft filters and advanced settings. Interaction sites from Adaptype that were also present in the PDB [188-207, 211-603]. Lengths 50 to 250.
2. Default BindCraft filters and advanced settings. No interaction sites specified. Lengths 10 to 250.
3. Default BindCraft filters and advanced settings. Full sequence of interest passed as  interaction sites. Lengths 50 to 250.
4. Default BindCraft filters and advanced settings. Interaction sites: [385-395,435-445], based on binding sites and burried fraction in the pdb metadata. Lengths 60 to 200.
5. Default BindCraft filters and advanced settings. Interaction sites: [340-350,360-365,385-395,435-445], based on binding sites and burried fraction in the pdb metadata, used all possible pockets. Lengths 60 to 120.
6. Default BindCraft filters and advanced settings. Interaction sites: [388-392,438-442], based on binding sites and burried fraction in the pdb metadata. Chose 2 main pockets, used a larger range. Lengths 60 to 120.
7. Same as 6, modified advanced settings to increase weights_pae_inter and weights_iptm 4x and weights_helicity to -1.
8. Same as 6, modified advanced settings to increase the number of iterations.

9. Default BindCraft filters and advanced settings. All interaction sites from Adaptyv. Lengths 50 to 200. Similar to setting 1 but reconfigured into a single design per job and increased max allowed runtime. Post-competition.
10. Default BindCraft filters and advanced settings. Interaction sites: [388-392,438-442], based on binding sites and burried fraction in the pdb metadata. Chose 2 high confidence pockets, same as 6, a more conservative range. Lengths 60 to 120.

11. Same as 10, higher acceptance rate.

12. Same as 2, higher acceptance rate.

13. Same as 12, with mpnn_fix_interface= False. The mpnn checks keep failing with the selected interface.

14. Same as 2, with predict_initial_guess= True

15. Default BindCraft filters and advanced settings. Interaction sites: [A559,A579,A580,A581,A588] (conservative), based on binding residue in the pdb literature and mpnn_fix_interface= False.

16. Default BindCraft filters and advanced settings. Interaction sites: [A559,A579,A580,A581,A588,A504], based on binding residue in the pdb literature and mpnn_fix_interface= False.

17. Same as 15, but with mpnn_fix_interface= True

19. Same as 15, running Bindcraft v1.5.2 additional advanced setting : predict_initial_guess: true.

## Results

1. - 13. : Multiple successful trajectories, MPNN generates sequences but none of them pass the next AF2 filtering phase, thus no final accepted designs.

## Some ideas to try
1. Start with a known binder sequence instead of DeNovo. Binder sequences: ephrin, NiV41 and NiV42

2. Start with a wild-type antibody: Use the same coding V,D,J genes and rearrange the random substitutions.


