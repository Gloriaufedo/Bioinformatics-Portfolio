# 🧬 Single-Cell RNA-seq Analysis of Human PBMCs

[cite_start]This repository contains an end-to-end Python pipeline using **Scanpy** to preprocess, cluster, and annotate a single-cell RNA sequencing (scRNA-seq) dataset of Human Peripheral Blood Mononuclear Cells (PBMCs)[cite: 24, 25, 26].

---

## 🎯 Objective
[cite_start]To analyze scRNA-seq data from human PBMCs and identify distinct immune cell populations through quality control filtering, dimensionality reduction, unsupervised clustering, marker gene expression profiling, and cell-type annotation[cite: 25, 26, 33, 46, 96, 136, 137, 202].

---

## 📊 Dataset
* [cite_start]**Source:** Publicly available 10x Genomics PBMC 3K single-cell dataset[cite: 25, 26].
* [cite_start]**Dimensions:** 2,700 individual cells $\times$ 32,738 genes[cite: 31, 32].
* [cite_start]**Composition:** Multiple circulating immune cell populations[cite: 202, 222, 223, 224, 225].

---

## 🛠️ Tools & Dependencies
[cite_start]The pipeline relies on the following Python libraries[cite: 1]:
* [cite_start]**Single-Cell Analysis:** `scanpy` [cite: 2][cite_start], `anndata` [cite: 2]
* [cite_start]**Data Science & ML:** `numpy` [cite: 12][cite_start], `pandas` [cite: 12][cite_start], `scikit-learn` [cite: 12]
* [cite_start]**Visualization:** `matplotlib` [cite: 2][cite_start], `seaborn` [cite: 2]
* [cite_start]**Clustering Engine:** `leidenalg` [cite: 135, 138][cite_start], `igraph` [cite: 137, 139]

---

## 🔄 Pipeline Workflow & Methods

### 1. Data Preprocessing & Quality Control
* [cite_start]Loaded the raw count matrix into an `AnnData` structure[cite: 25, 26, 27].
* [cite_start]Flagged mitochondrial genes using the `"MT-"` prefix to track dying or stressed cells[cite: 33].
* [cite_start]Calculated comprehensive quality control (QC) metrics via `sc.pp.calculate_qc_metrics`[cite: 34].
* [cite_start]Removed low-quality cells and doublets using strict threshold filtering[cite: 46, 48]:
  * [cite_start]**Gene counts:** Subsampled cells expressing $< 2,500$ genes[cite: 46].
  * [cite_start]**Mitochondrial fraction:** Excluded cells with $\ge 5\%$ mitochondrial read counts[cite: 48].

### 2. Normalization & Feature Selection
* [cite_start]Scaled library sizes to a target sum of $10^4$ reads per cell and log-transformed counts ($ln(counts + 1)$) to stabilize variance[cite: 68].
* [cite_start]Saved the normalized raw expression state to `adata.raw` for cleaner downstream marker testing[cite: 70].
* [cite_start]Subsampled the dataset to the top **2,000 highly variable genes (HVGs)** to focus on structurally informative biological variation[cite: 81, 82].
* [cite_start]Regressed out unwanted variation and scaled expression matrix values to a maximum threshold of 10[cite: 83].

### 3. Dimensionality Reduction & Unsupervised Clustering
* [cite_start]Performed **Principal Component Analysis (PCA)** on the scaled HVG matrix to reduce data noise[cite: 96].
* [cite_start]Computed a neighborhood graph based on the top 40 principal components ($n_{\text{neighbors}} = 10$)[cite: 136].
* [cite_start]Generated a two-dimensional **UMAP embedding** for low-dimensional layout visualization[cite: 136].
* [cite_start]Applied the **Leiden community detection algorithm** (resolution = 0.5) to capture transcriptionally distinct cell clusters[cite: 137].

### 4. Marker Gene Validation & Cell-Type Annotation
[cite_start]Clusters were mapped to explicit biological lineages using known canonical immune marker expression profiles[cite: 149, 202]:

| Cell Type | Canonical Marker Genes | Assigned Leiden Clusters |
| :--- | :--- | :--- |
| **T Cells** | `CD3D`, `CD8A` | [cite_start]Cluster 0 [cite: 204] |
| **NK Cells** | `NKG7` | [cite_start]Cluster 1 [cite: 205] |
| **B Cells** | `MS4A1` | [cite_start]Cluster 2 [cite: 206] |
| **Monocytes** | `LYZ` | [cite_start]Cluster 3 [cite: 207] |

### 5. Differential Marker Analysis
* [cite_start]Conducted a **Wilcoxon Rank-Sum test** comparing each cluster against all remaining cells to pinpoint cluster-specific signatures[cite: 219, 230].
* [cite_start]Generated a hierarchical dendrogram and deep-dive expression **heatmap** for the top 5 differentially expressed markers per group to assess global cluster relationships[cite: 287, 291, 293, 294].

---

## 📈 Key Code Snippets

### Preprocessing & Normalization
```
import scanpy as sc

# Load and annotate mitochondrial genes
adata = sc.datasets.pbmc3k()
adata.var["mt"] = adata.var_names.str.startswith("MT-")
sc.pp.calculate_qc_metrics(adata, qc_vars=["mt"], inplace=True)
```
### Filter, scale, and log-transform
```
adata = adata[adata.obs.n_genes_by_counts < 2500, :]
adata = adata[adata.obs.pct_counts_mt < 5, :]
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
adata.raw = adata.copy()
```

### Highly Variable Genes selection and Scaling
```
sc.pp.highly_variable_genes(adata, n_top_genes=2000)
adata = adata[:, adata.var.highly_variable]
sc.pp.scale(adata, max_value=10)
```

### PCA, Neighbors, and UMAP
```
sc.tl.pca(adata, svd_solver="arpack")
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
sc.tl.umap(adata)
sc.tl.leiden(adata, resolution=0.5, flavor='igraph')
```

### Mapping clusters to immune types
```
celltype_map = {
    "0": "T Cells",
    "1": "NK Cells",
    "2": "B Cells",
    "3": "Monocytes"
}
adata.obs["cell_type"] = adata.obs["leiden"].map(celltype_map)
```

### Export processed object
```
adata.write("pbmc_scRNA_processed.h5ad")
```
---

# 📌 Results Summary

- Immune Cell Landscape: The unsupervised pipeline split the PBMC population into highly isolated, clean clusters representing standard circulating human immune cell subsets.

- Separation Quality: The UMAP layout showed strong partitioning between lymphoid (T, NK, B cells) and myeloid (Monocyte) lineages.

- Marker Fidelity: Cell-type mapping was directly corroborated by intense target localized expression of CD3D (T Cells), NKG7 (NK Cells), MS4A1 (B Cells), and LYZ (Monocytes) across the corresponding coordinates.

- Expression Specificity: Differential expression testing verified robust statistical enrichment for structural markers, showcasing clean data profiles matching contemporary single-cell reference atlases.
