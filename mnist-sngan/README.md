# MNIST Generation with a Spectrally Normalized GAN

Coursework project, 2023.

## Problem

Generate images that look like MNIST handwritten digits.

## Method

A convolutional GAN: a generator that upsamples noise into 28x28 images and a
`Conv2D`-based discriminator, trained adversarially with Adam.

Spectral normalization is applied to constrain the discriminator's Lipschitz constant,
which is the usual remedy for mode collapse — without it the generator collapses onto
a handful of near-identical outputs.

An autoencoder over MNIST was built first, before the project settled on a GAN; that
code is still in the notebook.

## Libraries

`tensorflow` / `keras`, `numpy`, `pandas`, `matplotlib`, `Pillow`

## Result

`output.PNG` shows the last samples. They have digit-like stroke texture but most are
not recognizable digits — training was stopped well short of convergence, and the
generator/discriminator capacity was never properly balanced.
