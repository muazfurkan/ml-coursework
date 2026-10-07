# Tweet Sentiment Analysis with Word2Vec + Random Forest

Coursework project, 2023.

## Problem

Classify the sentiment of tweets from their text.

## Method

A Word2Vec model is trained on the tweet corpus with gensim to get word vectors. Each
tweet is then represented by averaging the vectors of its words into a single
fixed-length vector, and a `RandomForestClassifier` is trained on those. A `LinearSVC`
is trained on the same features for comparison.

Averaging word vectors discards word order entirely, so the representation is a bag of
meanings — it works acceptably for coarse sentiment and would not for anything needing
syntax or negation handling.

## Data

[Twitter dataset for sentiment analysis](https://www.kaggle.com/datasets/dunyajasim/twitter-dataset-for-sentiment-analysis)
from Kaggle: tweet text plus a sentiment label per row, as CSV.

## Libraries

`gensim`, `scikit-learn`, `numpy`, `pandas`, `matplotlib`
