# CancerOmics Design Document

## Project Overview

CancerOmics is a modular computational biology pipeline developed to identify transcriptomic biomarkers associated with ferroptosis and cancer progression using publicly available RNA sequencing datasets.

The project integrates differential expression analysis, functional enrichment, immune infiltration analysis, survival modelling, and machine learning into a reproducible workflow. It is designed to demonstrate practical bioinformatics software development while following reproducible research principles.

---

# Objectives

The project aims to:

- Build an end-to-end transcriptomics analysis workflow.
- Apply modern bioinformatics methods to cancer datasets.
- Produce reproducible analyses that can be extended to additional cancer types.
- Demonstrate software engineering practices within computational biology.

---

# Design Principles

The project was designed around five principles:

1. Reproducibility
2. Modular analysis
3. Readability
4. Scalability
5. Version control

Each analysis stage is isolated so that individual modules can be updated without affecting the rest of the pipeline.

---

# Workflow Architecture

```
Raw GEO / TCGA Data
        │
        ▼
Data Download
        │
        ▼
Quality Control
        │
        ▼
Normalization
        │
        ▼
Differential Expression
        │
        ▼
Functional Enrichment
        │
        ▼
Immune Cell Estimation
        │
        ▼
Survival Analysis
        │
        ▼
Machine Learning
        │
        ▼
Visualisation
```

---

# Directory Structure

```
CancerOmics/

data/
    raw/
    processed/

src/
    preprocessing/
    differential_expression/
    enrichment/
    immune_analysis/
    survival/
    machine_learning/
    visualization/

results/

figures/

notebooks/

tests/

docs/

```

Each module performs one clearly defined task.

---

# Technologies

| Tool | Purpose |
|-------|----------|
| Python | Main programming language |
| VS Code | Development environment |
| Pandas | Data manipulation |
| NumPy | Numerical computation |
| Scanpy | Single-cell analysis |
| Lifelines | Survival analysis |
| Scikit-learn | Machine learning |
| Matplotlib | Figures |
| Seaborn | Statistical visualization |
| Git | Version control |
| GitHub | Repository hosting |

---

# Software Design

The pipeline follows a modular architecture.

Each module receives standardized inputs and produces standardized outputs.

Example:

Input

```
expression_matrix.csv
metadata.csv
```

↓

Differential Expression Module

↓

Output

```
deg_results.csv
volcano_plot.png
```

This allows downstream analyses to be reused independently.

---

# Reproducibility

The project includes:

- requirements.txt
- pyproject.toml
- Git version control
- Documented workflow
- Fixed random seeds where applicable

This ensures analyses can be reproduced on another computer.

---

# Future Extensions

Planned improvements include:

- Snakemake workflow automation
- Docker container support
- Nextflow implementation
- Interactive Streamlit dashboard
- Multi-omics integration
- Additional TCGA cancer types

---

# Expected Outcome

The final project will provide:

- reproducible biomarker discovery pipeline
- publication-quality visualisations
- interpretable machine learning models
- clinically relevant candidate biomarkers
- reusable bioinformatics codebase

