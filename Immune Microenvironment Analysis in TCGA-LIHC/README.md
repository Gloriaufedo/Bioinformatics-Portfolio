# 🧬 Immune Microenvironment Analysis in TCGA-LIHC

## Objective
To investigate the relationship between tumor immune infiltration and patient survival in Liver Hepatocellular Carcinoma (TCGA-LIHC), with a focus on determining whether CD8 T-cell enrichment serves as an independent prognostic biomarker after controlling for key clinical risk factors.

## Dataset
Transcriptomic and clinical data were obtained from The Cancer Genome Atlas (TCGA-LIHC) through the Genomic Data Commons (GDC) API.
The study integrates:
* Bulk RNA-sequencing gene expression counts
* Clinical metadata
* Demographic variables
* AJCC pathological staging information
* Survival outcomes

## Tools
`Python`
`Pandas`
`NumPy`
`GSEApy`
`Lifelines`
`Scikit-learn`
`Matplotlib`
`Seaborn`

## Key Analyses
✔ RNA-seq Data Processing

✔ Single-Sample Gene Set Enrichment Analysis (ssGSEA)

✔ Immune Signature Quantification

✔ Principal Component Analysis (PCA)

✔ Cox Proportional Hazards Modeling

✔ Kaplan-Meier Survival Analysis

✔ Clinical Covariate Adjustment

## Methods

### 1. Data Acquisition & Preprocessing
* Retrieved TCGA-LIHC RNA-seq count data directly from the Genomic Data Commons (GDC) API.
* Downloaded matched clinical metadata and constructed a patient-level expression matrix.
* Applied quality control, preprocessing steps, and merged transcriptomic and clinical datasets.

### 2. Immune Profiling using ssGSEA
* Implemented single-sample Gene Set Enrichment Analysis (ssGSEA) using `gseapy`.
* Calculated robust enrichment scores for immune cell populations by ranking target marker genes within each individual patient expression profile to minimize background noise.
* Focused on CD8 T-cell signatures as indicators of anti-tumor immune activity.

### 3. Exploratory Transcriptomic Analysis
* Applied Principal Component Analysis (PCA) to evaluate global transcriptomic variation across the cohort.
* Investigated patterns and overlaps associated with immune infiltration levels.

### 4. Survival Analysis
* Performed Kaplan-Meier survival analysis to stratify patients according to immune infiltration scores.
* Assessed baseline differences in overall survival probabilities between groups.

### 5. Multivariable Cox Regression
* Built a Multivariable Cox Proportional Hazards model using `lifelines` to analyze CD8 T-cell scores as a continuous gradient.
* Modeled continuous immune enrichment scores alongside clinical covariates (**Age at diagnosis** and **AJCC tumor stage**) to control for confounding risks.

## Results

### 1. Immune Infiltration Profiling
ssGSEA successfully quantified immune activity across individual tumor samples, generating normalized, patient-level CD8 T-cell enrichment scores for downstream prognostic analyses.

### 2. Survival Analysis
Initial univariable Kaplan-Meier stratification showed a visible visual trend toward improved survival in patients with higher CD8 T-cell infiltration, but failed to reach statistical significance.
* **Log-rank test:** $p = 0.120$

### 3. Multivariable Cox Regression
Once clinical baseline risk variations were explicitly modeled, the true biological signal was isolated. After adjusting for age and tumor stage, CD8 T-cell infiltration emerged as a statistically significant, independent predictor of survival:
* **Hazard Ratio (HR):** $0.61$
* **p-value:** $0.04$

This indicates that an increased baseline enrichment of CD8 T-cells correlates with a **39% reduction in mortality risk** ($1 - 0.61 = 0.39$).

### 4. Clinical Covariates
Advanced disease burden exerted an expectedly heavy impact on patient mortality:
* **Stage IV Hazard Ratio:** $5.74$

This demonstrates that high mortality rates in late-stage tumors create significant clinical confounding that masks the protective immune signal when analyzed through an unadjusted, univariable model.

## Key Findings
**Independent Prognosis:** CD8 T-cell infiltration is a statistically significant, independent protective factor in TCGA-LIHC ($p = 0.04$).

**Risk Mitigation:** Higher continuous immune infiltration is associated with a 39% reduction in patient mortality risk.

**Methodological Rigor:** Multivariable modeling successfully uncovered biological signatures obscured in unadjusted survival comparisons.

**Clinical Staging:** Tumor stage remains a dominant determinant of clinical outcome, with Stage IV increasing mortality hazard over 5-fold.

**Enrichment Utility:** ssGSEA provides a robust, noise-resilient framework for capturing high-fidelity immune contexture profiles from bulk RNA-seq data.

## Conclusions
This study demonstrates the value of integrating transcriptomic data with clinical metadata to chart tumor-immune interactions in hepatocellular carcinoma. By shifting from simple arithmetic gene averaging to an industry-standard ssGSEA framework and controlling for clinical confounders with a multivariable Cox regression model, this analysis successfully confirms CD8 T-cell infiltration as a protective prognostic factor independent of traditional clinical variables. These findings highlight the importance of modeling clinical covariates in computational oncology and illustrate how advanced survival analytics can uncover actionable biomarkers within massive public cancer genomics datasets.
