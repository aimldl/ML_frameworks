#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# main.py


per_worker_batch_size = 64

#batch_size = 64
#epochs = 3
#steps_per_epoch = 70

import os
import json

import tensorflow as tf
import numpy as np

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--worker_index', help='index of this node', type=int)
args = parser.parse_args()
print( f'worker_index: {args.worker_index}' )

def mnist_dataset(batch_size):
  (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
  # The `x` arrays are in uint8 and have values in the range [0, 255].
  # You need to convert them to float32 with values in the range [0, 1]
  x_train = x_train / np.float32(255)
  y_train = y_train.astype(np.int64)
  train_dataset = tf.data.Dataset.from_tensor_slices(
      (x_train, y_train)).shuffle(60000).repeat().batch(batch_size)
  return train_dataset

def build_and_compile_cnn_model():
  model = tf.keras.Sequential([
      tf.keras.Input(shape=(28, 28)),
      tf.keras.layers.Reshape(target_shape=(28, 28, 1)),
      tf.keras.layers.Conv2D(32, 3, activation='relu'),
      tf.keras.layers.Flatten(),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dense(10)
  ])
  model.compile(
      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
      optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
      metrics=['accuracy'])
  return model

# Multi-worker Configuration
#   Two components of TF_CONFIG exist: cluster and task.
#     * cluster is the same for all workers
#     * task provides information of the current task
#            is different on each worker.
#       * worker
#         The worker with index 0 is appointed as the chief worker.
#       * chief is a worker with a little more responsibility such as 
#         * saving checkpoint and writing summary file for TensorBoard.

# Reset the TF_CONFIG environment variable
os.environ.pop('TF_CONFIG', None)

# tf_config is just a local variable in python. 
tf_config = {
    'cluster': {
        'worker': ['13.124.124.59:6006', '54.180.160.159:6006']
    },
    'task': {'type': 'worker', 'index': args.worker_index}  # first node
}

print(tf_config)

# To actually use the dictionary to configure training, 
#   serialize it as JSON, and placed in the TF_CONFIG environment variable.
os.environ['TF_CONFIG'] = json.dumps(tf_config)
print( 'TF_CONFIG:', os.environ.get('TF_CONFIG') )

num_workers = len(tf_config['cluster']['worker'])
print(f'num_workers = {num_workers}')
global_batch_size = per_worker_batch_size * num_workers

# To actually run with MultiWorkerMirroredStrategy you'll need to run worker processes and pass a TF_CONFIG to them.
# Prerequisite:
#   TF_CONFIG must be set before a tf.distribute.Strategy instance is created
#     because MultiWorkerMirroredStrategy() 
#       * parses TF_CONFIG and
#       * starts TensorFlow's GRPC servers.
#strategy = tf.distribute.MultiWorkerMirroredStrategy()
strategy = tf.distribute.MultiWorkerMirroredStrategy()
multi_worker_dataset = mnist.mnist_dataset(global_batch_size)

with strategy.scope():
  # Model building/compiling need to be within `strategy.scope()`.
  multi_worker_model = mnist.build_and_compile_cnn_model()

multi_worker_model.fit(multi_worker_dataset, epochs=epochs, steps_per_epoch=steps_per_epoch)
