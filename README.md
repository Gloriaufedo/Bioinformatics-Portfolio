# 🧬 Computational Genomics & Bioinformatics Portfolio

Welcome to my bioinformatics portfolio. This repository contains data-driven genomics pipelines where I work with public cancer genomics and transcriptomic data. I built these projects to extract biological signals from raw data, calculate immune cell presence inside tumors, and predict patient survival outcomes using statistical models.

---

## 📂 Repository Architecture

```text
├── Erastin_Ferrostatin_RNAseq_Anal.../
│   ├── Data/
│   ├── figures/
│   ├── results/
│   ├── README.md
│   ├── analysis.ipynb
│   └── requirements.txt
│
├── Ferroptosis Biomarker Discovery i.../
│   ├── data/
│   ├── figures/
│   ├── results/
│   ├── README.md
│   ├── TCGA_LIHC_analysis.ipynb
│   └── requirements.txt
│
└── Immune Microenvironment Analys.../
    ├── figures/
    ├── results/
    ├── Immune_Microenvironment_TCG...
    ├── README.md
    └── requirements.txt
```
---

🛠️ Core Tech Stack & Frameworks

`Bioinformatics Core: GSEApy, Biopython, GDC API Client`

`Survival Analytics: Lifelines (Cox Proportional Hazards, Kaplan-Meier models)`

`Statistical Modeling & ML: Scikit-learn, SciPy, Statsmodels`

`Data Processing: Pandas, NumPy`

`Visualization Dashboarding: Matplotlib, Seaborn`

---

## 📋 Portfolio Projects Overview

**🧬 Project 1: Erastin & Ferrostatin RNA-seq Analysis in HepG2 Cells**

- Objective: I investigated the transcriptomic changes in HepG2 liver cancer cells when ferroptosis is turned on using Erastin and when it is blocked using Ferrostatin to spot the exact genes and molecular pathways controlling oxidative stress, lipid damage, and iron-dependent cell death.

- Methodology:

  - I loaded the expression matrix from GEO and applied a log2​(x+1) transformation to normalize expression values across all samples.

  - I used Ordinary Least Squares (OLS) linear modeling to run two main comparisons: Erastin vs Control and Ferrostatin vs Control, calculating False Discovery Rate (FDR) adjusted p-values using the Benjamini–Hochberg correction.

  - I ran pathway enrichment using gseapy via the Enrichr API against KEGG, GO Biological Process, and Reactome databases.

- Key Analytical Result: Erastin triggered a heavy shift in genes tied to oxidative stress responses, lipid metabolism issues, and direct ferroptosis pathways. The analysis proved that Ferrostatin partially reversed these Erastin-induced shifts, confirming its protective rescue effect at the transcriptomic level.

**📊 Project 2: Ferroptosis Biomarker Discovery in TCGA-LIHC**

- Objective: I used transcriptomic and clinical data from the TCGA-LIHC project to study how ferroptosis changes at the molecular level in liver cancer and evaluated the prognostic significance of GPX4, a key regulator of ferroptosis resistance.

- Methodology:

  - I streamed high-throughput RNA-Seq counts and matched clinical metrics directly from the GDC API, applying a log2​(Counts+1) transformation to stabilize variance.

  - I used a non-parametric Wilcoxon Rank-Sum test to validate GPX4 expression levels between healthy tissue and tumor tissue.

  - I partitioned the cohort using an automated median expression cutoff into High GPX4 and Low GPX4 arms to estimate 5-year overall survival probabilities via Kaplan-Meier curves and Log-rank testing.

- Key Analytical Result: GPX4 expression levels were heavily elevated in primary tumor samples compared to healthy liver tissues (p<0.001). Patients with high GPX4 levels in their tumors had a faster, steeper drop in survival probability over the 5-year tracking window (p<0.05), proving that high GPX4 levels match up with poorer clinical outcomes.

**🧬 Project 3: Immune Microenvironment Analysis in TCGA-LIHC**

- Objective: I investigated how the presence of immune cells inside tumors relates to how long liver cancer patients live, focusing on determining whether CD8 T-cell enrichment acts as an independent prognostic biomarker after removing the effects of clinical risks like age and tumor stage.

- Methodology:

  - I used single-sample Gene Set Enrichment Analysis (ssGSEA) via gseapy to rank target marker genes within individual patient profiles, minimizing transcriptomic background noise to isolate CD8 T-cell signatures.

  - I built a Multivariable Cox Proportional Hazards model using lifelines to evaluate the CD8 T-cell scores as a continuous gradient alongside clinical covariates like age at diagnosis and AJCC tumor stage.

- Key Analytical Result: While my initial univariable Kaplan-Meier split failed to cross the line for statistical significance (p=0.120), switching to a multivariable model successfully isolated the true biological signal. After adjusting for age and tumor stage, CD8 T-cell infiltration emerged as a highly significant protective factor (p=0.04, Hazard Ratio = 0.61), indicating a 39% reduction in overall mortality risk per unit increase in enrichment.

--- 

# 🔬 Key Engineering Principles Applied

1. Controlling for Confounders: I look beyond basic single-variable charts to run robust multivariable regressions. This makes sure that heavy clinical risks like a patient's cancer stage do not hide important biological facts.

2. Rank-Based Normalization: I use ranking methods like ssGSEA instead of simple arithmetic averages. This gives reproducible metrics that do not suffer from background sequencing noise or scale differences.

3. Clean Code and Structure: I keep my data tables, environment setup files (requirements.txt), and analysis notebooks structured side by side in every directory so anyone can deploy and run the pipelines easily. data tables, environment setup files (requirements.txt), and analysis notebooks organized side by side so anyone can run the pipelines easily.
