# CancerOmics Design Document

## Project Overview

CancerOmics is a reproducible bioinformatics portfolio that demonstrates the complete workflow for analysing public cancer genomics and transcriptomics datasets. The repository is designed around reproducible research principles, where each analysis is self-contained while following a common project structure and coding standard.

The project combines computational biology, statistical analysis, machine learning, and data visualisation to investigate molecular mechanisms of cancer using publicly available datasets.

---

# Design Goals

The repository was designed to:

- Produce fully reproducible analyses
- Follow good software engineering practices
- Separate raw data, processed data, source code and results
- Allow each project to be executed independently
- Provide clear documentation for future users and collaborators

---

# Repository Structure

```
CancerOmics/

│
├── README.md
├── DESIGN.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── requirements.txt
├── pyproject.toml
│
├── Erastin_Ferrostatin_RNAseq_Analysis/
├── Ferroptosis_Biomarker_Discovery/
├── Immune_Microenvironment_Analysis/
└── Single_Cell_RNAseq_Analysis/
```

Each project directory contains:

- source code
- notebooks (where applicable)
- processed datasets
- figures
- outputs
- project-specific documentation

---

# Analysis Workflow

Each project follows the same workflow:

1. Data acquisition
2. Data preprocessing
3. Quality control
4. Statistical analysis
5. Biological interpretation
6. Visualisation
7. Reproducible reporting

Using the same workflow across projects improves consistency and reproducibility.

---

# Reproducibility

All analyses are intended to be reproducible from publicly available datasets.

The software environment is managed through:

- Python
- requirements.txt
- pyproject.toml

Dependencies are explicitly documented to ensure consistent execution across operating systems.

---

# Coding Principles

The project follows several software engineering principles:

- Modular scripts
- Descriptive variable names
- Version-controlled development
- Reproducible computational workflows
- Clear documentation
- Minimal code duplication

---

# Future Expansion

CancerOmics is designed as a growing portfolio.

Future analyses will follow the same repository structure, allowing new projects to be added without restructuring the repository.

Potential future projects include:

- Multi-omics integration
- Spatial transcriptomics
- ATAC-seq analysis
- Proteogenomics
- Cancer drug response modelling

---

# Intended Audience

This repository is intended for:

- Graduate admissions committees
- Research supervisors
- Bioinformatics researchers
- Computational biology collaborators
- Employers evaluating bioinformatics and data science skills
