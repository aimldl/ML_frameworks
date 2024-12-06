#!/usr/bin/env python
# coding: utf-8

# * Draft: 2020-11-24 (Tue)
# # Fashion MNIST Dataset Trained with CNN (Keras)
# 
# * Keras API reference > Built-in small datasets >
#   * [Fashion MNIST dataset, an alternative to MNIST](https://keras.io/api/datasets/fashion_mnist/)
# 
# * CNN
#   * [Simple MNIST convnet](https://keras.io/examples/vision/mnist_convnet/)
# ```
# Author: fchollet
# Date created: 2015/06/19
# Last modified: 2020/04/21
# Description: A simple convnet that achieves ~99% test accuracy on MNIST.
# ```
# * Google search: keras fashion mnist example
#   * [CNN with Tensorflow|Keras for Fashion MNIST](https://www.kaggle.com/gpreda/cnn-with-tensorflow-keras-for-fashion-mnist), Kaggle
#   * [Fashion MNIST with Keras and TPUs](https://colab.research.google.com/github/tensorflow/tpu/blob/master/tools/colab/fashion_mnist.ipynb#scrollTo=edfbxDDh2AEs), https://colab.research.google.com/
# 
# * (in Korean)
#   * [5.4.3. Fashion MNIST with Keras](https://sdc-james.gitbook.io/onebook/4.-and/5.4.-tensorflow/5.4.3.-fashion-mnist-with-keras)
#   * [딥러닝의 Hello World, Fashion-MNIST](https://tykimos.github.io/2018/09/30/Hello_Fashion_MNIST/), 블록과 함께 하는 파이선 딥러닝 케라스, 김태영

# Configuration
input_shape = (28, 28, 1)

# Hyperparameters
batch_size_per_replica = 128
#batch_size is defined after `Python module imports`
epochs = 15
validation_split = 0.1

# Python module imports
from tensorflow                import keras
from tensorflow.keras.models   import Sequential
from tensorflow.keras.layers   import Dense
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras          import layers

import numpy as np
import time
from datetime import timedelta

# Distributed Training
import tensorflow as tf

strategy = tf.distribute.MirroredStrategy()
print('Number of devices: {}'.format(strategy.num_replicas_in_sync))
batch_size = batch_size_per_replica * strategy.num_replicas_in_sync
print(f'batch_size_per_replica: {batch_size_per_replica}')
print(f'batch_size: {batch_size} = {batch_size_per_replica} * {strategy.num_replicas_in_sync}')

# Data acquisition
#(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
num_classes = 10

# Check the types of all the variables
print( type( x_train ), type( y_train ), type( x_test ), type( y_test ) )
[ type( x_train ), type( y_train ), type( x_test ), type( y_test ) ]

# Data Preparation
# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test  = x_test.astype("float32")  / 255

# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims( x_train, -1 )
x_test  = np.expand_dims( x_test,  -1 )

print( "x_train shape:", x_train.shape )
print( x_train.shape[0], "train samples" )
print( x_test.shape[0], "test samples" )

# Convert class vectors to binary class matrices
y_train = keras.utils.to_categorical( y_train, num_classes )
y_test = keras.utils.to_categorical( y_test, num_classes )

# Check the variable type
print( type(y_train), type(y_test) )

# Model Selection
# Model Preparation
model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
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
