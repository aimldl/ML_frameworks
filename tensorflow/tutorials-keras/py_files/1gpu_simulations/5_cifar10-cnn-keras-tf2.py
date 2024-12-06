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
# * Kaggle
#   * [TensorFlow: CIFAR10 CNN Tutorial](https://www.kaggle.com/amyjang/tensorflow-cifar10-cnn-tutorial)
# 
# * [CIFAR homepage](https://www.cs.toronto.edu/~kriz/cifar.html), Alex Krizhevsky, U of Toronto
#   * See the technical paper for details on the dataset
#     * [Learning Multiple Layers of Features from Tiny Images](https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf), Alex Krizhevsky, 2009.
# 
# * Google search: keras cifar10 example
#   * [Train a simple deep CNN on the CIFAR10 small images dataset using augmentation](https://keras.io/zh/examples/cifar10_cnn_tfaugment2d/)
#   * [CIFAR-10 이미지 분류를 위한 CNN을 구성해보자! (Keras)](https://gruuuuu.github.io/machine-learning/cifar10-cnn/#)
#
# Bug fix
# Problem
# $ python 5_cifar10-cnn-keras-tf2.py
#   ...
# Epoch 1/15
# Traceback (most recent call last):
#   File "5_cifar10-cnn-keras-tf2.py", line 95, in <module>
#     model.fit( x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=validation_split )
#   ...
#   ValueError: Input 0 of layer sequential is incompatible with the layer: expected axis -1 of input shape to have value 3 but received input with shape (None, 32, 32, 3, 1)
# $
#
# Hint
#     x_train shape: (50000, 32, 32, 3, 1)
#   Like above, the shape has trailing ",1"
#   The input shape is supposed to be
#     x_train shape: (50000, 32, 32, 3)
#   as defined in
#     input_shape = (32, 32, 3)
#
# Solution
#   x_train is reshaped as follows:
#     x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 3)
#     x_test  = x_test.reshape( x_test.shape[0],  x_test.shape[1],  x_test.shape[2],  3)

# Configuration
input_shape = (32, 32, 3)

# Hyperparameters
batch_size = 128
epochs = 15
validation_split = 0.1

# Python module imports
#from keras.datasets import    cifar10
#   https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data

from tensorflow                import keras
from tensorflow.keras          import models
from tensorflow.keras          import layers
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils    import to_categorical

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from datetime import timedelta

# Data acquisition
#(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
num_classes = 10
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Exploratory Data Analysis
plt.figure(figsize = (10,7))
p = sns.countplot(y_train.flatten())
p.set(xticklabels=classes)

# Any NaN values?
#   Expecting `False` for both cases
np.isnan(x_train).any()
np.isnan(x_test).any()

# Data Preparation
# Normalize
#   Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test  = x_test.astype("float32")  / 255

# Make sure images have shape (32, 32, 3)
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], input_shape[2])
x_test  = x_test.reshape( x_test.shape[0],  x_test.shape[1],  x_test.shape[2],  input_shape[2])
#x_train = np.expand_dims( x_train, -1 )
#x_test  = np.expand_dims( x_test,  -1 )

print( "x_train shape:", x_train.shape )
print( x_train.shape[0], "train samples" )
print( x_test.shape[0], "test samples" )

# plot first few images
#   https://machinelearningmastery.com/how-to-develop-a-cnn-from-scratch-for-cifar-10-photo-classification/
#for i in range(9):
	# define subplot
#	pyplot.subplot(330 + 1 + i)
	# plot raw pixel data
#	pyplot.imshow(x_train[i])
# show the figure
#pyplot.show()

# Convert class vectors to binary class matrices
#y_train = keras.utils.to_categorical( y_train, num_classes )
#y_test = keras.utils.to_categorical( y_test, num_classes )
y_train = to_categorical( y_train, num_classes )
y_test  = to_categorical( y_test,  num_classes )
# Equivalently
#import tensorflow as tf
#y_train = tf.one_hot(y_train.astype(np.int32), depth=10)
#y_test = tf.one_hot(y_test.astype(np.int32), depth=10)

# Check the variable type
print( type(y_train), type(y_test) )

# Model Selection
# Model Preparation
model = models.Sequential(
    [
        keras.Input(shape=input_shape),
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

# Model Training
start_time = time.perf_counter()

model.fit( x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=validation_split )

elapsed_time = time.perf_counter() - start_time  # in seconds
elapsed_time_hms = str(timedelta(seconds=elapsed_time))
#print('training_time: %.3f' % elapsed_time)
print(f'training_time: {elapsed_time_hms}')

# Model Evaluation
score = model.evaluate( x_test, y_test, verbose=0 )
print("Test loss:", score[0])
print("Test accuracy:", score[1])
