#!/usr/bin/env python
# coding: utf-8

'''
0-multi-worker_configuration-keras.py
  * Rev.3: 2021-06-17 (Thu)
  * Rev.3: 2021-06-10 (Thu)
  * Rev.2: 2021-06-04 (Fri)

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
