# 🧬 Computational Genomics & Bioinformatics Portfolio

Welcome to my bioinformatics portfolio. This repository contains data-driven genomics pipelines built using public cancer transcriptomics datasets. The goal of these projects is to extract biological signals from high-dimensional RNA-seq data, characterize tumor heterogeneity, and evaluate clinically relevant biomarkers using statistical and machine learning approaches.

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

🎯 Objective

To investigate transcriptional changes in HepG2 liver cancer cells under ferroptosis induction (Erastin) and inhibition (Ferrostatin), identifying key genes and pathways involved in oxidative stress, lipid peroxidation, and iron-dependent cell death.

⚙️ Methodology
- Loaded GEO RNA-seq expression matrix and applied log2(x + 1) normalization
- Performed differential expression analysis using Ordinary Least Squares (OLS) regression
- Controlled for multiple testing using Benjamini–Hochberg FDR correction
- Conducted pathway enrichment analysis using GSEApy (KEGG, GO, Reactome databases)
  
🔬 Key Result

Erastin induced strong transcriptional reprogramming associated with oxidative stress response, lipid metabolism disruption, and ferroptosis activation. Ferrostatin partially reversed these effects, confirming a protective transcriptional rescue effect.

**🧬 Project 2: Ferroptosis Biomarker Discovery in TCGA-LIHC**

🎯 Objective

To evaluate ferroptosis-related biomarkers in liver hepatocellular carcinoma (TCGA-LIHC), with a focus on GPX4 expression and its association with patient survival outcomes.

⚙️ Methodology
- Retrieved RNA-seq counts and clinical metadata via the GDC API
- Applied log2(Counts + 1) normalization
- Compared tumor vs normal expression using statistical testing
- Performed Kaplan-Meier survival analysis using median stratification
- Conducted log-rank tests for survival significance
  
🔬 Key Result

GPX4 was significantly upregulated in tumor tissues (p < 0.001). High GPX4 expression was associated with poorer overall survival over a 5-year follow-up period (p < 0.05).

**🧬 Project 3: Immune Microenvironment Analysis in TCGA-LIHC**

🎯 Objective

To investigate how tumor immune infiltration relates to patient survival in liver hepatocellular carcinoma, focusing on CD8 T-cell activity as a prognostic immune biomarker.

⚙️ Methodology
- Performed single-sample Gene Set Enrichment Analysis (ssGSEA) using GSEApy to quantify immune cell infiltration scores per patient
- Built a multivariable Cox Proportional Hazards model using lifelines
- Adjusted for clinical covariates including age at diagnosis and AJCC tumor stage
- Evaluated CD8 T-cell infiltration as a continuous variable rather than binary stratification

🔬 Key Result

While univariable Kaplan-Meier analysis showed no significant association (p = 0.120), multivariable Cox regression revealed that CD8 T-cell infiltration was significantly associated with improved survival outcomes after adjusting for clinical covariates (p = 0.04, HR = 0.61). This corresponds to an estimated 39% reduction in mortality risk per unit increase in CD8 T-cell enrichment.

--- 

## 🔬 Key Analytical Principles Applied
1. Control of Confounding Variables

Survival associations were evaluated using multivariable regression models to account for clinical confounders such as tumor stage and age.

2. Rank-Based Immune Scoring (ssGSEA)

Immune infiltration was quantified using ranking-based enrichment scoring, improving robustness to batch effects and expression scaling differences.

3. Reproducible Pipeline Design

Each project includes structured directories for raw data, processed results, figures, and executable notebooks to ensure reproducibility.
