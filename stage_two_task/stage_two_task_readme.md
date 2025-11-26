# **Single-Cell RNA-seq Analysis of Human Bone Marrow**

This project performs a complete single-cell RNA-sequencing (scRNA-seq) analysis workflow on human bone marrow. The pipeline includes quality control, normalization, dimensionality reduction, clustering, and automated cell-type annotation using marker-based scoring (decoupler). The analysis follows standard Scanpy procedures and integrates external resources such as Ensembl BioMart and PanglaoDB.

The accompanying Jupyter Notebook (`.ipynb`) contains all code used in the analysis.

---

## **1\. Data Loading and Initial Setup**

The analysis begins by importing all required libraries (Scanpy, Pandas, Decoupler, Matplotlib, Seaborn).  
The raw dataset is loaded into an `AnnData` object. Gene names are checked and made unique to ensure compatibility with Scanpy functions.

---

## **2\. Identification of Gene Categories (MT, RIBO, HB)**

Before QC, key gene categories are identified:

* **Mitochondrial genes (MT)**  
   Identified based on the “MT-” prefix or appropriate Ensembl IDs.

* **Ribosomal genes (RIBO)**  
   Identified using well-known ribosomal markers (“RPL”, “RPS”).

* **Hemoglobin genes (HB)**  
   Identified using “HBB”, “HBA1”, “HBA2”, etc.

These are later used to evaluate cell quality and detect potentially stressed or dying cells.

---

## **3\. Calculation of QC Metrics**

Scanpy’s built-in QC functions are used to compute:

* Number of genes detected per cell

* Total UMI counts per cell

* Percent mitochondrial content

* Percent ribosomal content

* Percent hemoglobin content

These metrics are visualized using violin plots to assess variability and potential quality issues across the dataset.

---

## **4\. QC Filtering**

Cells and genes are filtered using standard scRNA-seq thresholds:

* **Cells with fewer than 400 detected genes are removed.**

* **Genes expressed in fewer than 3 cells are removed.**

* **Cells with mitochondrial percentage above 5% are excluded.**

Ribosomal and hemoglobin percentages are inspected, but not used as strict filtering thresholds unless signs of biologically unrealistic expression levels are observed.

A scatter plot of total counts vs. gene counts helps identify potential doublets or low-quality cells.

---

## **5\. Doublet Detection**

Scrublet is used to identify and score potential doublets. Doublet scores are visualized and flagged cells may be removed depending on quality criteria.

---

## **6\. Normalization and Highly Variable Genes**

After filtering:

* Counts are normalized to the median total counts per cell.

* Data is log-transformed.

* Highly variable genes (HVGs) are selected (top 1,000).

These HVGs drive downstream dimensionality reduction and clustering.

---

## **7\. Dimensionality Reduction**

To visualize and interpret structure in the data:

* PCA is computed on HVGs.

* A neighborhood graph is built.

* UMAP is used for low-dimensional visualization across clusters and QC metrics.

---

## **8\. Clustering**

Leiden clustering is performed at multiple resolutions to explore cluster granularity:

* Resolution 0.02

* Resolution 0.5

* Resolution 2.0

UMAP plots are generated for each resolution to visually inspect the cluster structure.

---

## **9\. Gene Annotation and Integration with External Databases**

### **9.1. Mapping Ensembl IDs to Gene Names**

Ensembl BioMart is queried to retrieve mappings between Ensembl gene IDs and gene symbols.

### **9.2. Loading PanglaoDB Cell-Type Markers**

PanglaoDB marker tables are retrieved using decoupler’s Omnipath interface.

Markers are cleaned, deduplicated, and mapped to Ensembl IDs to match the dataset.

---

## **10\. Automated Cell-Type Scoring Using decoupler**

Marker-based scoring is performed using ULM (univariate linear model):

* The dataset is scored based on marker enrichment.

* Only markers with sufficient overlap with the dataset are retained (`tmin=3`).

Scores for each cell type are added to the AnnData object and visualized on UMAP.

---

## **11\. Ranking Markers per Cluster**

Using the small-resolution clusters (e.g., resolution 0.02):

* Groups are compared against the rest of the dataset.

* Marker genes are ranked using a t-test-based method.

* Top markers for each cluster are used to match clusters to cell identities.

---

## **12\. Cell-Type Assignment**

Cluster labels (Leiden) are mapped to biological cell types based on:

* decoupler cell-type scores

* PanglaoDB marker matching

* ranked cluster markers

* visual inspection of marker expression (dotplots, heatmaps, violin plots)

These annotations are stored in `bone_marrow_adata.obs["cell_type"]`.

---

## **13\. Additional Visualization**

Multiple visualization methods are used to confirm cluster identity:

* Dotplot

* Stacked violin plot

* Matrix plot

* Heatmap

* Tracks plot

Key markers for B cells, NK cells, and T cells are shown across clusters.

---

## **14\. Output**

The final output includes:

* A fully annotated `AnnData` object

* UMAP plots showing QC metrics, cluster labels, and cell types

* Marker-based visualizations

* Ranked marker gene tables

* decoupler cell-type scoring matrices

All visualizations and analysis steps are contained in the accompanying `.ipynb` notebook.

