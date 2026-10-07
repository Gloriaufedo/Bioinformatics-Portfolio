# 🧬 Computational Genomics & Bioinformatics Portfolio

I am a Biochemistry graduate working at the intersection of molecular biology,
data analysis and computational genomics.

This portfolio contains reproducible analyses of public transcriptomics and
single-cell RNA-seq datasets. My current work focuses on ferroptosis,
differential expression, pathway enrichment, immune-cell infiltration and
survival analysis.

## Projects

### 1. Erastin & Ferrostatin RNA-seq Analysis — HepG2

**Question:** How does ferroptosis induction change gene expression, and can
ferrostatin reverse part of this response?

**Methods:** RNA-seq preprocessing, OLS differential expression, Benjamini-
Hochberg FDR correction, GSEApy pathway enrichment.

**Key finding:** [NUMBER OF DEGs], including [X] upregulated and [Y]
downregulated genes. [TOP PATHWAY] showed the strongest enrichment
([STATISTIC/P-VALUE]).

[View project]([https://github.com/Gloriaufedo/Bioinformatics-Portfolio/tree/d5d2958b0836f54cd0e5308009f5a2ed770e40c8/Erastin_Ferrostatin_RNAseq_Analysis])

---

### 2. Ferroptosis Biomarker Analysis — TCGA-LIHC

**Question:** Is GPX4 expression associated with tumor status and overall
survival in liver hepatocellular carcinoma?

**Methods:** GDC API, RNA-seq normalization, tumor-vs-normal comparison,
Kaplan-Meier analysis and log-rank testing.

**Key finding:** GPX4 expression was significantly higher in tumor tissue
(p < 0.001). [ADD HAZARD RATIO/CI IF AVAILABLE].

[View project](link)

---

### 3. Immune Microenvironment & Survival — TCGA-LIHC

**Question:** Is CD8 T-cell infiltration associated with survival after
accounting for clinical factors?

**Methods:** ssGSEA and multivariable Cox proportional hazards regression,
adjusting for age and AJCC stage.

**Key finding:** CD8 T-cell enrichment was associated with improved survival
(HR = 0.61, p = 0.04) after adjustment for clinical covariates.

[View project](link)

---

### 4. Single-Cell RNA-seq Analysis — Human PBMCs

**Question:** Can unsupervised clustering recover biologically distinct immune
cell populations from PBMC single-cell RNA-seq data?

**Methods:** QC, normalization, HVG selection, PCA, nearest-neighbor graph,
Leiden clustering, UMAP and marker-based annotation.

**Key finding:** [NUMBER OF CELLS RETAINED] cells were grouped into [NUMBER OF
CLUSTERS] transcriptionally distinct populations, including [CELL TYPES].

[View project](link)

## Methods & Tools

- Python: pandas, NumPy, SciPy, statsmodels
- Genomics: GDC API, GSEApy
- Survival analysis: lifelines
- Single-cell analysis: [ACTUAL PACKAGES USED]
- Visualization: Matplotlib, Seaborn
- Reproducibility: Jupyter, requirements.txt

## Research interests

Computational genomics, transcriptomics, ferroptosis, oxidative stress,
cancer biology, molecular biomarkers and statistical analysis of patient-level
data.
