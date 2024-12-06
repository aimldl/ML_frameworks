#!/usr/bin/env python
# coding: utf-8

#   * Rev.2: 2021-06-04 (Fri)

# Hyperparameters
batch_size_per_replica = 128
#batch_size is defined after `Python module imports`
epochs = 20
validation_split = 0.2

# Python module imports
from tensorflow              import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras        import layers

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
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
number_of_classes = 10  # because 0-9

# Data Preparation
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Make sure the shape
x_train = np.expand_dims( x_train, -1 )
x_test = np.expand_dims( x_test, -1 )

# One-hot encoding
y_train = keras.utils.to_categorical(y_train, number_of_classes)
y_test = keras.utils.to_categorical(y_test, number_of_classes)

# Double-check
input_shape = (28, 28, 1)
#input_shape = (784, )
input_shape

# Model Selection
# Model Preparation
with strategy.scope():
  model = keras.Sequential(
      [
       keras.Input(shape=input_shape),
       layers.Conv2D(32, kernel_size=(3,3), activation='relu'),
       layers.MaxPooling2D(pool_size=(2,2)),
       layers.Conv2D(64, kernel_size=(3,3), activation='relu'),
       layers.MaxPooling2D(pool_size=(2,2)),
       layers.Flatten(),
       layers.Dropout(0.5),
       Dense(number_of_classes, activation='softmax')
      ]
  )
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

# Model Training
start_time = time.perf_counter()

model.fit(x_train, y_train, epochs=epochs, validation_split=validation_split)

elapsed_time = time.perf_counter() - start_time  # in seconds
elapsed_time_hms = str(timedelta(seconds=elapsed_time))
#print('training_time: %.3f' % elapsed_time)
print(f'training_time: {elapsed_time_hms}')

# Evaluation
predictions = model.evaluate(x_test, y_test)
