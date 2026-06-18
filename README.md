# 🧬 Computational Genomics & Bioinformatics Portfolio

This repository serves as a centralized hub for production-grade computational biology pipelines leveraging public cancer genomics and transcriptomic data. The workflows focus on extracting high-fidelity biological signals, quantifying cellular microenvironments, and modeling patient survival using advanced statistical frameworks.

---

## 📂 Repository Architecture

```text
├── Project_1_Immune_Microenvironment/
│   ├── data/
│   │   ├── survival_statistics.csv
│   │   ├── immune_scores_tcga_lihc.csv
│   │   └── cox_model_summary.csv
│   ├── images/
│   │   └── cox_multivariable_forest_plot.png
│   ├── TCGA_LIHC_analysis.ipynb
│   └── requirements.txt
│
├── Project_2_Differential_Expression/
│   ├── data/            # Log-transformed count matrices & fold-change tables
│   ├── plots/           # Volcano plots and hierarchical clustering heatmaps
│   └── DESeq2_pipeline.ipynb
│
├── Project_3_Genomic_Variant_Calling/
│   ├── config/          # Reference genomes and alignment parameters
│   ├── pipeline/        # BWA-MEM, Samtools, and GATK variant scripts
│   └── variant_calling_workflow.ipynb
│
└── README.md            # Global Portfolio Directory

🛠️ Core Tech Stack & Frameworks

    Bioinformatics Core: GSEApy, Biopython, GDC API Client

    Survival Analytics: Lifelines (Cox Proportional Hazards, Kaplan-Meier models)

    Statistical Modeling & ML: Scikit-learn, SciPy, Statsmodels

    Data Processing: Pandas, NumPy

    Visualization Dashboarding: Matplotlib, Seaborn

📋 Portfolio Projects Overview
🧬 Project 1: Immune Microenvironment Analysis in TCGA-LIHC

    Objective: Investigate the relationship between adaptive immune cell infiltration and patient survival in Liver Hepatocellular Carcinoma cohorts, determining whether CD8 T-cell enrichment serves as an independent prognostic biomarker after controlling for key clinical risk factors.

    Methodology: * Streamed absolute expression matrices directly from the GDC API.

        Deployed single-sample Gene Set Enrichment Analysis (ssGSEA) via gseapy to score intra-sample cell populations via relative rank distributions, bypassing transcriptomic background noise.

        Modeled continuous CD8 T-cell scores via a Multivariable Cox Proportional Hazards Model while statistically controlling for clinical confounding elements (Age and AJCC Tumor Staging).

    Key Analytical Result: While univariable Kaplan-Meier stratification yielded non-significant margins (p=0.120) due to stage-specific mortality confounders, the multivariable regression successfully isolated a definitive biological signal. CD8 T-cell enrichment emerged as a significant independent protective factor (p=0.04, Hazard Ratio = 0.61), indicating a 39% reduction in overall mortality risk per unit increase in enrichment.

📊 Project 2: Transcriptomic Differential Expression Pipeline

    Objective: Map robust expression gradients between healthy control tissue and matched tumor biopsies to isolate malignant driver profiles.

    Methodology:

        Implemented quality control filters and structural normalization matrices across raw sequencing reads.

        Designed automated workflows evaluating log2-fold variance thresholds paired with adjusted p-value matrices (q<0.05).

    Key Analytical Result: Successfully isolated distinct biomarker targets and generated high-resolution volcano plots alongside bidirectionally clustered heatmaps detailing clear transcriptional segregation.

🧬 Project 3: High-Throughput Genomic Variant Calling Framework

    Objective: Build a self-contained pipeline for sequence alignment, quality score recalibration, and single-nucleotide variant (SNV) identification.

    Methodology:

        Developed structured notebooks utilizing fast alignment scripts (BWA-MEM) mapped directly to reference genome builds.

        Integrated multi-tiered filtering engines (Samtools and GATK) to isolate somatic mutations from raw sequencing background errors.

    Key Analytical Result: Generated structured variant files detailing clean somatic mutation profiles, variant allele frequencies, and micro-insertion metrics ready for clinical annotation steps.

🔬 Key Engineering Principles Applied

    Confounder Control: Moving beyond basic univariable models to run robust multivariable regressions, ensuring clinical risk factors do not obscure critical biological insights.

    Rank-Based Normalization: Utilizing intra-sample ranking mechanisms (ssGSEA) over simple arithmetic means to secure reproducible metrics resilient to batch differences.

    Clean Code & Reproducibility: Structuring data tables, environment files (requirements.txt), and production notebooks side by side to ensure seamless pipeline deployment.bility: Structuring data tables, environment files (requirements.txt), and production notebooks side by side to ensure seamless pipeline deployment.
