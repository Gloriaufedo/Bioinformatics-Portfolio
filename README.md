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
**🧬 Project 1: Immune Microenvironment Analysis in TCGA-LIHC**

- Objective: I checked how the presence of adaptive immune cells affects how long liver cancer (TCGA-LIHC) patients live. The main goal was to see if CD8 T-cell levels can predict survival on their own after removing the effects of clinical risks like age and cancer stage.

- Methodology:

  - I pulled raw gene expression data directly from the GDC API.
    
  - I used single-sample Gene Set Enrichment Analysis (ssGSEA) with the gseapy library to rank and score immune cells for each patient, which helped cut out background noise from the data.
    
  - I used a Multivariable Cox Proportional Hazards Model to analyze the continuous CD8 T-cell scores while controlling for clinical factors like patient age and AJCC tumor stage.

- Key Analytical Result: My initial Kaplan-Meier test showed a non-significant result (p=0.120) because the high death rates in late-stage cancer patients were covering up the true pattern. Once I switched to the multivariable model and controlled for cancer stages, the real biological signal came out. CD8 T-cell presence proved to be a significant independent protective factor (p=0.04, Hazard Ratio = 0.61). This means that as CD8 T-cell levels increase, patient mortality risk drops by 39%.

**📊 Project 2: Transcriptomic Differential Expression Pipeline**

- Objective: I mapped out the differences in gene expression between healthy control tissues and matching tumor biopsies to find the specific genes driving cancer growth.

- Methodology:

  - I handled quality control filtering and normalizations across the raw sequencing data.
    
  -I built automated workflows to pick out highly relevant genes using log2-fold change thresholds alongside adjusted p-values (q<0.05).

- Key Analytical Result: I successfully isolated specific biomarker targets and visualized them clearly using high-resolution volcano plots and clustered heatmaps to show how different tissues separate based on their transcripts.

**🧬 Project 3: High-Throughput Genomic Variant Calling Framework**

    Objective: I built an end-to-end pipeline to align gene sequences, fix quality scores, and spot single-nucleotide variants (SNVs) in genomic data.

    Methodology:

        I wrote structured code using fast alignment tools like BWA-MEM to map raw reads directly to reference genomes.

        I integrated standard filtering tools like Samtools and GATK to separate true somatic mutations from sequencing errors.

    Key Analytical Result: The pipeline produced clean variant files showing mutation profiles, allele frequencies, and micro-insertions that are ready for clinical use.

🔬 Key Engineering Principles Applied

    Controlling for Confounders: I look beyond basic single-variable charts to run multivariable regressions. This makes sure that clinical risks like a patient's age or cancer stage do not hide important biological facts.

    Rank-Based Normalization: I use ranking methods like ssGSEA instead of simple averages. This gives reproducible metrics that do not suffer from batch effects or scale differences.

    Clean Code and Structure: I keep my data tables, environment setup files (requirements.txt), and analysis notebooks organized side by side so anyone can run the pipelines easily.
