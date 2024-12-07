# Lab: Distributed training with Keras

- 2 hours
- https://www.coursera.org/learn/gcp-production-ml-systems/gradedLti/pD2ns/lab-distributed-training-with-keras


## Purpose

This lab uses

- tf.distribute.Strategy API > tf.distribute.MirroredStrategy which
  - copy, essentially, all of the model's variables to each processor.
  - use [all-reduce](http://mpitutorial.com/tutorials/mpi-reduce-and-allreduce/) to combine the gradients from all processors
  - apply the combined value to all copies of the model.

## Objectives

- Define a distribution strategy and set an input pipeline.
- Create the Keras model.
- Define the callbacks.
- Train and evaluate the model.

## Tasks

1. Prepare the JupyterLab environment with Vertex Workbench
2. Open the Jupyter notebook
3. Do the hands-on lab

For details, refer to [Lab: Distributed Training with Keras](https://docs.google.com/document/d/1PZowLJ0lk-Uc5rAnwu71hlC6LVpeiFVkFZLUUQb9fDU/edit#) (Google docs).

My mirror

- [keras.ipynb](ipynb_files/keras.ipynb) has no output.

- [keras-working_code.ipynb](ipynb_files/keras-working_code.ipynb)

  - This notebook failed on Vertex Workbench Notebook on TF2.6 without GPU.
  - Running the notebook on TF2.10 without GPU worked just fine.

  

- Running the first code resulted in an error.

```python
import tensorflow_datasets as tfds
import tensorflow as tf

import os
```

```python
AttributeError: module 'tensorflow_datasets.core' has no attribute 'utils
```
