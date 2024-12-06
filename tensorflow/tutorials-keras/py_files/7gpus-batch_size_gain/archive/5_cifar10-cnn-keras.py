#!/usr/bin/env python
# coding: utf-8

# # CIFAR10 Dataset Trained & Evaluated with Convolutional Neural Networks (Keras)
# * Rev.1: 2021-05-27 (Thu)
# * Draft: 2020-11-23 (Mon)

# ## CIFAR10 Dataset
# * 32x32 color images (or 32x32 pixels with 3 channels)
# * labeled over 10 categories
# * 50,000 training data; 10,000 test data

# ## Related Documents
# * Keras API reference > Built-in small datasets >
#   * [CIFAR10 small images classification dataset](https://keras.io/api/datasets/cifar10/)
#   * [CIFAR100 small images classification dataset](https://keras.io/api/datasets/cifar100/)
# 
# * [CIFAR homepage](https://www.cs.toronto.edu/~kriz/cifar.html), Alex Krizhevsky, U of Toronto
#   * See the technical paper for details on the dataset
#     * [Learning Multiple Layers of Features from Tiny Images](https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf), Alex Krizhevsky, 2009.
# 
# * Google search: keras cifar10 example
#   * [Train a simple deep CNN on the CIFAR10 small images dataset using augmentation](https://keras.io/zh/examples/cifar10_cnn_tfaugment2d/)
#   * [CIFAR-10 이미지 분류를 위한 CNN을 구성해보자! (Keras)](https://gruuuuu.github.io/machine-learning/cifar10-cnn/#)


# TODO: Fix the bug

# Configuration
input_shape = (32, 32, 3)

# Hyperparameters
batch_size = 128
epochs = 15
validation_split = 0.1

# Python module imports
from tensorflow              import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras        import layers

import numpy as np

# Data acquisition
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
num_classes = 10

#from keras.datasets import cifar10
#(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Data Preparation

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test  = x_test.astype("float32")  / 255

# Make sure images have shape (32, 32, 1)
x_train = np.expand_dims( x_train, -1 )
x_test = np.expand_dims( x_test, -1 )

print( "x_train shape:", x_train.shape )
print( x_train.shape[0], "train samples" )
print( x_test.shape[0], "test samples" )

# Convert class vectors to binary class matrices
y_train = keras.utils.to_categorical( y_train, num_classes )
y_test = keras.utils.to_categorical( y_test, num_classes )

# ValueError: Input 0 of layer sequential_3 is incompatible with the layer: expected axis -1 of input shape to have value 3 but received input with shape [None, 32, 32, 3, 1]

# Model
model = keras.Sequential(
    [
        keras.Input( shape=input_shape ),
        layers.Conv2D(32, kernel_size=(3, 3), padding='same', activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), padding='same', activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense( 512, activation='relu' ),
        layers.Dropout(0.5),
        layers.Dense( num_classes, activation="softmax" )
    ]
)
model.summary()
model.compile( loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"] )

# Training
model.fit( x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=validation_split )

# Evaluation
score = model.evaluate( x_test, y_test, verbose=0 )
print("Test loss:", score[0])
print("Test accuracy:", score[1])
