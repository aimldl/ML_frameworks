# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 20:42:51 2018

@author: the.kim
"""

from __future__ import absolute_import, division, print_function

import os
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow.contrib.eager as tfe

tf.enable_eager_execution()

print("TensorFlow version: {}".format(tf.VERSION))
print("Eager executionL {}".format(tf.executing_eagerly()))