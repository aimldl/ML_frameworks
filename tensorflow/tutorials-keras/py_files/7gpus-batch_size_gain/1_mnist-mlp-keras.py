#!/usr/bin/env python
# coding: utf-8

#   * Rev.2: 2021-06-04 (Fri)

# # Training the MNIST Dataset with MLP on Keras
# * Google search: keras mnist example with mlp
#   * [How to create an MLP classifier with TensorFlow 2.0 and Keras](https://www.machinecurve.com/index.php/2019/07/27/how-to-create-a-basic-mlp-classifier-with-the-keras-sequential-api/)
# 
# * The following Keras code is similar to the above reference, but not equal.
# * Read the reference to understand the details.

# Hyperparameters
batch_size_per_replica = 250
#batch_size is defined after `Python module imports`
epochs = 20
validation_split = 0.2
verbose = 0

# Python module imports
from tensorflow 	      import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras        import layers

import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import timedelta

# Distributed Training
import tensorflow as tf

strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
print('Number of devices: {}'.format(strategy.num_replicas_in_sync))
batch_size = batch_size_per_replica * strategy.num_replicas_in_sync
print(f'batch_size_per_replica: {batch_size_per_replica}')
print(f'batch_size: {batch_size} = {batch_size_per_replica} * {strategy.num_replicas_in_sync}')

# Data acquisition
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Data exploration
print(type(x_train), type(y_train), type(x_test), type(y_test))
print( x_train.shape, y_train.shape, x_test.shape, y_test.shape )

if verbose:
  plt.imshow(x_train[0])
  plt.show()

  y_train.shape, y_train, 
  plt.imshow(x_train[1])
  plt.show()

  plt.imshow(x_train[2])
  plt.show()

# Data Preparation
#   pixel value ranges from 0 to 255. (256)
#   scaling the max value to 1
x_train_normalized = x_train.astype('float32') / 255
x_test_normalized = x_test.astype('float32') / 255
plt.imshow(x_train_normalized[0], cmap='Greys')

# Make sure the shape
x_train_normalized = np.expand_dims( x_train_normalized, -1 )
x_test_normalized = np.expand_dims( x_test_normalized, -1 )
print( x_train_normalized.shape[0], x_test_normalized.shape[0] )

# Reshape the data
#   by flattening the 2D (28x28) to 1D (784)
# input_shape = (28, 28, 1)
input_shape = (784, )

x_train_prepared = x_train.reshape(x_train_normalized.shape[0], input_shape[0])
x_test_prepared = x_test.reshape(x_test_normalized.shape[0], input_shape[0])
x_train_normalized.shape[0], input_shape[0]

# One-hot encoding
number_of_classes = 10  # because 0-9
y_train_prepared = keras.utils.to_categorical(y_train, number_of_classes)
y_test_prepared  = keras.utils.to_categorical(y_test, number_of_classes)

# Double-check
y_train_prepared[0]
y_train_prepared[1]
y_train_prepared[2]

y_test.shape, y_test
y_test_prepared[0]
y_test_prepared[1]

# Feature Engineering
# is skipped

# Model Selection
#   MLP with
#     * input layer of 350 neurons
#     * hidden layer of 50 neurons
#     * output layer of 10 neurons

# Model Preparation
with strategy.scope():
  model = keras.Sequential(
      [Dense(350, input_shape=input_shape, activation='relu'),
       Dense(50, activation='relu'),
       Dense(number_of_classes, activation='softmax'),
      ]
  )
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Model Training
# Configure the hyper-parameters.
# Recall
# ```text
# (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# ```
start_time = time.perf_counter()

model.fit(x_train_prepared, y_train_prepared, epochs=epochs, batch_size=batch_size, validation_split=validation_split)

elapsed_time = time.perf_counter() - start_time  # in seconds
elapsed_time_hms = str(timedelta(seconds=elapsed_time))
#print('training_time: %.3f' % elapsed_time)
print(f'training_time: {elapsed_time_hms}')

# ValueError: Shapes (250, 10) and (250, 28, 28, 10) are incompatible
# ValueError: Shapes (32, 10) and (32, 28, 28, 10) are incompatible
# -> input_shape = (28, 28, 1) => input_shape = (784, )
# ValueError: Input 0 of layer sequential_1 is incompatible with the layer: 
#              expected axis -1 of input shape to have value 784 but received input with shape (32, 28, 28, 1)
# -> x_train = x_train.reshape(x_train.shape[0], input_shape[0])
# -> x_test = x_test.reshape(x_test.shape[0], input_shape[0])

# Evaluation
predictions = model.evaluate(x_test_prepared, y_test_prepared)

# MLP can achieve the accuracy of 0.9803
print(f'Test results: Loss = {predictions[0]}, Accuracy = {predictions[1]}')

