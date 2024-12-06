#!/usr/bin/env python
# coding: utf-8

'''
  * Rev.2: 2021-06-04 (Fri)

# Training the MNIST Dataset with MLP on Keras
* Google search: keras mnist example with mlp
  * [How to create an MLP classifier with TensorFlow 2.0 and Keras](https://www.machinecurve.com/index.php/2019/07/27/how-to-create-a-basic-mlp-classifier-with-the-keras-sequential-api/)
 
* The following Keras code is similar to the above reference, but not equal.
* Read the reference to understand the details.
'''

'''
## Multi-worker Configuration
Two components of TF_CONFIG exist: cluster and task.
  * cluster is the same for all workers
  * task provides information of the current task
         is different on each worker.
    * worker
      The worker with index 0 is appointed as the chief worker.
    * chief is a worker with a little more responsibility such as 
      * saving checkpoint and writing summary file for TensorBoard.

## References
* [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)
* [Multi-worker Configuration](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras#multi-worker_configuration)
'''

# Python module imports
import os
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--worker_index', help='index of this node', type=int)
args = parser.parse_args()
print( f'worker_index: {args.worker_index}' )

# Reset the TF_CONFIG environment variable
os.environ.pop('TF_CONFIG', None)

# tf_config is just a local variable in python. 
tf_config = {
    'cluster': {
        'worker': ['52.78.103.158:6006', '52.79.164.25:6006']
    },
    'task': {'type': 'worker', 'index': args.worker_index}  # first node
}
print(tf_config)

# To actually use the dictionary to configure training, 
#   serialize it as JSON, and placed in the TF_CONFIG environment variable.
os.environ['TF_CONFIG'] = json.dumps(tf_config)
print( 'TF_CONFIG:', os.environ.get('TF_CONFIG') )

'''
## TensorFlow2 code
'''

# Python module imports
import tensorflow as tf
from tensorflow 	      import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras        import layers

import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import timedelta

# Configuration
verbose = 0

# Hyperparameters
epochs = 20
validation_split = 0.2
per_worker_batch_size = 250

## Multi-node part: automatically computed assuming tf_config is set correctly.
num_workers = len(tf_config['cluster']['worker'])
global_batch_size = per_worker_batch_size * num_workers
print(f'global_batch_size = per_worker_batch_size * num_workers: {global_batch_size} = {per_worker_batch_size} * {num_workers}')

'''
To actually run with MultiWorkerMirroredStrategy you'll need to run worker $
Prerequisite:
  TF_CONFIG must be set before a tf.distribute.Strategy instance is created
    because MultiWorkerMirroredStrategy() 
      * parses TF_CONFIG and
      * starts TensorFlow's GRPC servers.
'''
strategy = tf.distribute.MultiWorkerMirroredStrategy()

# The only change you will make to distribute the training to multiple-workers is 
#   enclosing the model building and model.compile() call inside strategy.scope()

# Data acquisition
#multi_worker_dataset = mnist.mnist_dataset(global_batch_size)
#(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
multi_worker_dataset = keras.datasets.mnist.load_data(global_batch_size)

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
def build_model():
  model = keras.Sequential(
      [Dense(350, input_shape=input_shape, activation='relu'),
       Dense(50, activation='relu'),
       Dense(number_of_classes, activation='softmax'),
      ]
  )
  return model

with strategy.scope():
  # Model building/compiling need to be within `strategy.scope()`
  model = build_model()
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Model Training
# Configure the hyper-parameters.
# Recall
# ```text
# (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# ```

# TODO: Adjust the time calculation more accurately for the multi-node case.
start_time = time.perf_counter()

model.fit(multi_worker_dataset, epochs=epochs, batch_size=global_batch_size)
#model.fit(x_train_prepared, y_train_prepared, epochs=epochs, batch_size=batch_size, validation_split=validation_split)

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

