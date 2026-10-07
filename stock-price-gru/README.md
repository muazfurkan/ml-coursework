# Microsoft Stock Price Prediction with a GRU

Coursework project, 2023.

## Problem

Predict Microsoft's closing share price from its historical price time series.

## Method

A single GRU regressor built with Keras:

```
InputLayer((90, 1))  ->  GRU(64)  ->  Dense(1, activation='tanh')
```

The input is a sliding window of 90 days of scaled closing prices; the model predicts
the next value. Trained with mean squared error, Adam at `lr=1e-4`, and RMSE as the
reported metric.

> The original repository description mentioned a Transformer variant. There isn't one
> in the notebook — only the GRU above was actually built and trained.

## Data

[Microsoft stock time series](https://www.kaggle.com/datasets/vijayvvenkitesh/microsoft-stock-time-series-analysis/)
from Kaggle. `dataset.PNG` shows the series.

## Libraries

`tensorflow` / `keras`, `numpy`, `pandas`, `scikit-learn`, `plotly`

## Result

`predictions.PNG` shows predicted against actual prices. The model tracks the general
shape of the curve and little else. A longer series and a larger model would help some,
but share prices are driven by things absent from the input — earnings, policy,
macro news — so a univariate model on past prices has a low ceiling by construction.
