# ML Coursework

Machine learning coursework and experiments, 2022-2023. **Archived.**

These are university assignments and self-study projects from my undergraduate years,
collected here from eight separate repositories so they stop cluttering my profile
while staying available to read. Nothing here is maintained, and none of it is meant
as production code — the notebooks are as they were when the assignment was handed in,
including the dead ends.

I have kept the honest results rather than the flattering ones. Several of these
models don't work well, and where I understand why, the folder README says so.

## Contents

| Project | What it does | Main tools |
|---|---|---|
| [song-generator-gru](song-generator-gru) | Generates Turkish lyrics with a GRU language model, trained on a corpus I scraped | Keras, BeautifulSoup |
| [stock-price-gru](stock-price-gru) | Predicts Microsoft's closing share price from a 90-day window | Keras, plotly |
| [mnist-sngan](mnist-sngan) | Generates MNIST-like digits with a spectrally normalized GAN | Keras |
| [lung-ct-cancer-classification](lung-ct-cancer-classification) | Classifies chest CT scans as cancer / no cancer | scikit-learn, OpenCV |
| [sentiment-word2vec-rf](sentiment-word2vec-rf) | Tweet sentiment from averaged Word2Vec vectors | gensim, scikit-learn |
| [scrna-dimensionality-reduction](scrna-dimensionality-reduction) | Reduces and clusters single-cell RNA-seq data from mouse HSPCs | scikit-learn, UMAP |
| [alzheimer-genetic-ml](alzheimer-genetic-ml) | Compares classical ML algorithms on wide genetic sequence data | scikit-learn, UMAP |
| [alzheimer-autoencoder](alzheimer-autoencoder) | Same problem, using autoencoder embeddings and class balancing | Keras, scikit-learn |

## The projects

### [song-generator-gru](song-generator-gru)

A GRU language model that generates Turkish song lyrics. The interesting half was
building the corpus: I scraped roughly 94k lines of song lyrics and poetry off two
Turkish sites with `requests` and `BeautifulSoup`. The model learns Turkish syllable
rhythm convincingly and meaning not at all, which is what a corpus this size buys you.

### [stock-price-gru](stock-price-gru)

A single `GRU(64)` regressor over a 90-day sliding window of Microsoft closing prices.
It tracks the shape of the curve and nothing more. The ceiling here is structural
rather than architectural — the drivers of a share price are not in its own price
history — which was the useful thing to learn from it.

### [mnist-sngan](mnist-sngan)

A convolutional GAN with spectral normalization on the discriminator to hold off mode
collapse. The samples have digit-like stroke texture but mostly aren't digits;
training was stopped short of convergence and the two networks were never balanced
against each other properly.

### [lung-ct-cancer-classification](lung-ct-cancer-classification)

Chest CT scans preprocessed with OpenCV, flattened, and fed to `LinearSVC`, random
forests, and a small Keras MLP. Flattening throws away all spatial structure, so this
is the baseline a CNN should have been measured against rather than a serious attempt.

### [sentiment-word2vec-rf](sentiment-word2vec-rf)

Word2Vec vectors trained on the tweet corpus with gensim, averaged per tweet into one
fixed-length vector, then classified with a random forest. Averaging discards word
order entirely, which is fine for coarse sentiment and hopeless for negation.

### [scrna-dimensionality-reduction](scrna-dimensionality-reduction)

A genes x cells count matrix reduced to 3, 5, and 10 components with PCA, kernel PCA,
truncated SVD, and UMAP, then clustered with k-means and DBSCAN at each width and
plotted in 2D and 3D. PCA and SVD produce near-identical layouts, which is expected on
centered data; neither separates the cell populations cleanly.

### [alzheimer-genetic-ml](alzheimer-genetic-ml)

A survey of classical algorithms — random forest, SVM, decision tree, Keras MLP,
k-means, DBSCAN — on a genetic dataset far wider than it is tall, with RFE and
sequential feature selection to cut it down. The result I kept is a negative one:
retraining on the decision tree's top 20 features by Gini importance made accuracy
*worse*, because greedy per-split importance doesn't identify a feature subset that
works together.

### [alzheimer-autoencoder](alzheimer-autoencoder)

The same dataset, approached with deep learning: oversample the minority class, squeeze
9881 features through a 100-unit autoencoder bottleneck, and classify the embeddings.
The variant I still like is training an autoencoder on one class only, freezing it, and
classifying unseen samples by reconstruction loss — a one-class framing that suits an
imbalanced problem better than the straightforward one.

## A note on the data

The datasets are not included. Most were public Kaggle datasets and each folder README
links the original. The one exception is the scraped Turkish lyrics corpus in
`song-generator-gru`, which is third-party lyrics text — the scraping code that built
it is included, the corpus itself is not.
