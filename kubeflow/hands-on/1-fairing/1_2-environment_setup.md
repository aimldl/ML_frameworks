* Draft: 2021-05-18 (Tue)

# Environment Setup

## Conda virtual environment on a local machine

* Prerequisite: Anaconda is installed on your local machine.
  * If not, refer to [Anaconda](https://github.com/aimldl/environments/tree/master/anaconda/en).

* Create a new virtual environment named `kf`.
  * You may use a name that you like.

```bash
(base) $ conda create -n kf python=3 anaconda
```

 Enter `y` 

```bash
  ...
Proceed ([y]/n)? y
  ...
# To activate this environment, use
#
#     $ conda activate kf
#
# To deactivate an active environment, use
#
#     $ conda deactivate
(base) $
```

* From now on, this Conda environment will be used.
* Activate the `kf` environment.

```bash
(base) $ conda activate kf
(kf) $
```

## Install Kubeflow Fairing SDK

```bash
(kf) $ pip install kubeflow-fairing
```

## Clone the `kubeflow/fairing` git repository

```bash
$ cd && mkdir kubeflow
$ git clone https://github.com/kubeflow/fairing.git
$
```

Let's take a quick look at the directory structure.

```bash
$ cd ~/kubeflow
$ tree -d -L 2
.
├── containerregistry
│   ├── client
│   ├── transform
│   └── transport
├── docs
│   └── source
├── examples
│   ├── aws
│   ├── distributed-training
│   ├── gcp
│   ├── kubeflow
│   ├── kubeflow-gke
│   ├── kubernetes
│   ├── kubernetes-in-cluster-builder
│   ├── lightgbm
│   ├── mnist
│   ├── notebook
│   ├── prediction
│   ├── pytorch
│   ├── simple
│   └── train_job_api
├── integration
├── kubeflow
│   └── fairing
└── tests
    ├── integration
    ├── unit
    └── workflows

28 directories
$
```

