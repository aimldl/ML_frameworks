# Lab: Distributed training using GPUs on Google Cloud’s AI Platform (Multi-Worker)

Equivalently,

- Distributed Training using GPUs on Cloud AI Platform 

- 2 hours

- https://www.coursera.org/learn/gcp-production-ml-systems/gradedLti/mLKRf/lab-distributed-training-using-gpus-on-google-clouds-ai-platform-multi-worker

  ## Purpose

  - Perform distributed training using the `MirroredStrategy` 
  - This strategy will allow to use the synchronous AllReduce strategy on a VM with multiple GPUs.

  ## Objectives

  - Setting up the environment

  - Create a model to train locally
  - Train on multiple GPUs/CPUs with MultiWorkerMirrored Strategy

  ## Tasks

  1. Prepare the JupyterLab environment with Vertex Workbench
  2. Create a Cloud Storage bucket
  3. Open the Jupyter notebook
  4. Do the hands-on with the notebook

  For details, refer to [Lab: Distributed training using GPUs on Google Cloud’s AI Platform (Multi-Worker)](https://docs.google.com/document/d/1gRwEtBfpngeZQ-NOxKlwPs53mo7PTtPdL7MKc25i818/edit#) (Google docs).

  My mirror

  - distributed_training.ipynb
  - distributed_training-failed_to_run.ipynb
    - TODO: I encountered the following error for all the `config.yaml` I used.

  ```bash
  CalledProcessError: Command 'b'\nnow=$(date +"%Y%m%d_%H%M%S")\nJOB_NAME="multi_gpu_fashion_minst_4gpu_$now"\n\ngcloud ai-platform jobs submit training $JOB_NAME \\\n  --staging-bucket=gs://$BUCKET \\\n  --package-path=train \\\n  --module-name=train.train_mult_worker_mirrored \\\n  --runtime-version=2.3 \\\n  --python-version=3.7 \\\n  --region=us-west1 \\\n  --config config.yaml\n'' returned non-zero exit status 1.
  ```

  

  - distributed_training-works.ipynb
