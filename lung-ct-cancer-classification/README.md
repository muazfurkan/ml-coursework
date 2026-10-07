# Lung Cancer Classification from Chest Scans

Coursework project, 2023.

## Problem

Binary classification of chest scan images into cancer / no cancer.

## Method

Images are loaded and preprocessed with OpenCV and scikit-image (resize, grayscale,
normalize), then flattened into feature vectors. Three model families are trained on
those features and compared:

- `LinearSVC`, with L1 and L2 penalties
- `RandomForestClassifier`, with gini and entropy criteria (100 trees, `max_depth=6`)
- a Keras MLP: `Dense(400, relu) -> Dense(1, sigmoid)`, 10 epochs

> `Conv2D` and `MaxPooling2D` are imported in the notebook, but no CNN is actually
> trained — the neural model is the fully-connected MLP above. Flattening the images
> throws away spatial structure, which is the obvious thing to fix here.

## Data

[Chest CT-Scan images](https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images)
from Kaggle. Note these are **CT scans**, not X-rays, despite how the original
repository was named.

## Libraries

`opencv-python`, `scikit-image`, `scikit-learn`, `tensorflow` / `keras`, `numpy`
