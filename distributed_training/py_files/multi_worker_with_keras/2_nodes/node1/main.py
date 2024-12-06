#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# main.py

import os
import json

import tensorflow as tf
import mnist

per_worker_batch_size = 64

#batch_size = 64
#epochs = 3
#steps_per_epoch = 70

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
   #'task': {'type': 'worker', 'index': 0}  # first node
   'task': {'type': 'worker', 'index': 1}  # second node
}

# To actually use the dictionary to configure training, 
#   serialize it as JSON, and placed in the TF_CONFIG environment variable.
os.environ['TF_CONFIG'] = json.dumps(tf_config)
print( 'TF_CONFIG:', os.environ.get('TF_CONFIG') )

#tf_config = json.loads(os.environ['TF_CONFIG'])
num_workers = len(tf_config['cluster']['worker'])
print(f'num_workers = {num_workers}')
global_batch_size = per_worker_batch_size * num_workers

# To actually run with MultiWorkerMirroredStrategy you'll need to run worker processes and pass a TF_CONFIG to them.
# Prerequisite:
#   TF_CONFIG must be set before a tf.distribute.Strategy instance is created
#     because MultiWorkerMirroredStrategy() 
#       * parses TF_CONFIG and
#       * starts TensorFlow's GRPC servers.

#os.environ['CUDA_VISIBLE_DEVICES']='0'
#os.environ['CUDA_VISIBLE_DEVICES']='0,1'

strategy = tf.distribute.MultiWorkerMirroredStrategy()
multi_worker_dataset = mnist.mnist_dataset(global_batch_size)

with strategy.scope():
  # Model building/compiling need to be within `strategy.scope()`.
  multi_worker_model = mnist.build_and_compile_cnn_model()

multi_worker_model.fit(multi_worker_dataset, epochs=3, steps_per_epoch=70)
