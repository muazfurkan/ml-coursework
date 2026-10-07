# Dimensionality Reduction and Clustering of Single-Cell RNA-seq Data

Coursework project, 2023.

## Problem

Single-cell RNA sequencing produces a genes x cells count matrix with thousands of
genes per cell. At that width, distance-based clustering is close to meaningless and
nothing can be plotted. The task: reduce the dimensionality first, then cluster, and
see what structure survives.

## Method

The notebook wraps the reduction methods in a small `reduction` class so they can be
swapped, and the clustering in a matching helper:

- **Reduction** — `PCA`, `KernelPCA`, `TruncatedSVD`, and `UMAP`
- **Clustering** — `KMeans` (`n_init=20`) and `DBSCAN`

The matrix is reduced to 3, 5, and 10 components, clustered separately at each width,
and the result plotted in both 2D and 3D. A few classifiers (SVM, decision tree,
random forest, Keras MLP) are also wired into the helper but are not part of the
reported results.

## Data

[Single Cell RNA Seq Nestorova2016 Mouse HSPC](https://www.kaggle.com/datasets/alexandervc/single-cell-rna-seq-nestorova2016-mouse-hspc)
from Kaggle — single-cell RNA-seq of mouse hematopoietic stem/progenitor cells,
collected by Nestorova et al. (2016).

## Libraries

`scikit-learn`, `umap-learn`, `numpy`, `pandas`, `matplotlib`, `tensorflow`

## Results

`results/` holds the plots. `PCA_0/1/2` and `SVD_0/1/2` are the 3-, 5-, and 10-component
runs; the `_02/_12/_22` files are the 3D views of the same runs.

PCA and SVD give nearly identical layouts here, which is expected — on a centered
matrix TruncatedSVD and PCA compute the same thing. Neither separates the cell
populations cleanly at any of the three widths.
