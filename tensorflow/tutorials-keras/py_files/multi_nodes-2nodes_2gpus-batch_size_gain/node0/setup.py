#!/usr/bin/env python
# coding: utf-8

# Multi-worker Configuration
#   https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras#multi-worker_configuration

# FOR DISTRIBUTED TRAINING
import json
import os
import sys

import subprocess

# Before importing TensorFlow, make a few changes to the environment.
# Disable all GPUs. This prevents errors caused by the workers all trying to use the same GPU.
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Environment variables and subprocesses in notebooks
os.environ['GREETINGS'] = 'Hello TensorFlow!'
# To test it, run "echo ${GREETINGS}"
# Caution: running the above echo command in a terminal returns NOTHING.
cmd = 'echo ${GREETINGS}'
subprocess.call(cmd, shell=True)

# Reset the TF_CONFIG environment variable
os.environ.pop('TF_CONFIG', None)

# Ensure the current directory is on python's path
if '.' not in sys.path:
  sys.path.insert(0, '.')

TF_CONFIG = '{"cluster": {"worker": ["3.36.146.88:6006", "3.36.218.39:6006"]}, "task": {"type": "worker", "index": 0}}'


