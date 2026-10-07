# Alzheimer's Prediction with Autoencoder Embeddings

Coursework project, 2023.

## Problem

Same genetic dataset as [`../alzheimer-genetic-ml`](../alzheimer-genetic-ml), with two
issues taken on directly: the classes are imbalanced, and the input is 9881 features
wide.

## Method

**Class balancing.** The minority class is oversampled by drawing with replacement
(`pandas.sample(replace=True)`) until both classes match. Cheap, and it duplicates
rather than synthesizes — so it risks overfitting to the repeated samples, where
something like SMOTE would interpolate instead.

**Autoencoder.** A symmetric fully-connected autoencoder compresses the input:

```
9881  ->  Dense(2000, relu)  ->  Dense(100, relu)  ->  Dense(2000, relu)  ->  Dense(9881, relu)
```

Trained with MSE and Adam for 200 epochs. The 100-unit bottleneck is then used as a
learned feature representation, and a `RandomForestClassifier` is trained on those
embeddings instead of on the raw features.

**Reconstruction-loss inference.** The more interesting variant: train an autoencoder
on positive samples *only*, freeze it, then push unseen samples through it and read the
reconstruction loss. A sample the model reconstructs well is likely to belong to the
class it was trained on. This turns the classifier into a one-class / novelty detector,
which is a reasonable fit for an imbalanced problem. Separate autoencoders were trained
per class so both directions could be compared.

## Libraries

`tensorflow` / `keras`, `scikit-learn`, `numpy`, `pandas`, `matplotlib`

## Caveat

The train/test split is done first and the oversampling is applied only to the training
half, which is the right order. But the masks that separate the two classes
(`X_train[label == 1]`) are built from the full `label` series rather than from
`y_train`, so features and labels are aligned by index across mismatched lengths. That
is fragile at best — worth re-checking before trusting the reported numbers.
