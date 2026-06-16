# 🧬 Ferroptosis Transcriptomic Analysis in HepG2 Cells

# Objective

To investigate transcriptional changes in HepG2 liver cancer cells under ferroptosis induction (Erastin) and inhibition (Ferrostatin), identifying key genes and pathways involved in oxidative stress, lipid peroxidation, and iron-dependent cell death.

# Dataset

Gene expression dataset (GSE104462) obtained from GEO database, consisting of:

- Control samples (C1–C3)
- Erastin-treated samples (E1–E3)
- Ferrostatin-treated samples (F1–F3)

# Methods

1. **Data Pre-processing**
- Loaded expression matrix from GEO
- Set gene IDs as index
- Applied log2(x + 1) transformation to normalize expression values
- Constructed metadata table for sample grouping

2. **Differential Expression Analysis**
Linear modeling using Ordinary Least Squares (OLS)
- Comparison:
  
i. Erastin vs Control

ii. Ferrostatin vs Control

- Computed:

i. log2 fold change

ii. p-values

iii. FDR-adjusted p-values (Benjamini–Hochberg correction)

3. **PCA (Principal Component Analysis**
- Reduced dimensionality of transcriptomic profiles
- Visualized sample clustering across treatment groups
- Assessed global transcriptional separation

4. **Volcano Plots**
- Visualized significance vs effect size
- Highlighted differentially expressed genes using thresholds:
|log2FC| > 1
padj < 0.05

5. **Heatmap**
- Top differentially expressed genes visualized across samples
- Used hierarchical clustering to identify expression patterns across:
  
i. Control

ii. Erastin

iii. Ferrostatin

6. **GSEA (Gene Set Enrichment Analysis)**
- Performed enrichment using gseapy (Enrichr API)
- Gene sets used:
  
i. KEGG 2021 Human

ii. GO Biological Process 2023

iii. Reactome 2022

# Results

1. Erastin induced strong transcriptional reprogramming associated with:
- Oxidative stress response
- Lipid metabolism disruption
- Ferroptosis activation pathways
- Ferrostatin partially reversed Erastin-induced expression changes, confirming rescue effect.
  
2. Key enriched pathways:
- Glutathione metabolism
- Reactive oxygen species detoxification
- Iron-dependent lipid peroxidation

# Conclusions

This study demonstrates clear transcriptomic signatures of ferroptosis in HepG2 cells. The combination of differential expression, PCA, and pathway enrichment provides strong evidence of:

- Erastin-driven ferroptotic activation
- Ferrostatin-mediated protective reversal
- Key regulatory genes involved in oxidative stress and lipid peroxidation
