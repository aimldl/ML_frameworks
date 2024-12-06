* Draft: 2020-12-31 (Thu)

# Installation

## Conda Virtual Environment

### Prerequisite

```bash
(base) aimldl@aimldl-desktop:~$
```

Notice the prompt starts from `(base)` which implies Anaconda has already been installed.

### Create a new virtual environment

The name of the new virtual environment is `yolo_tensorflow2`. The following command 

* not only creates the new environment, 
* but also installs Python3 along with Anaconda's basic packages.

```bash
(base) aimldl@aimldl-desktop:~$ conda create -n yolo_tensorflow2 python=3 anaconda
  ...
Proceed ([y]/n)? y
  ...
# To activate this environment, use
#
#     $ conda activate yolo_tensorflow2
#
# To deactivate an active environment, use
#
#     $ conda deactivate
(base) aimldl@aimldl-desktop:~$
```

Anaconda's basic packages include `conda`, `jupyter`,`numpy`, `pandas`, `pip`, `spyder`, and so on. For details, refer to [Anaconda package lists](https://docs.anaconda.com/anaconda/packages/pkg-docs/). In my case, the machine has 64-bit Linux and Python 3.8. The list of support packages can be seen at [Packages for 64-bit Linux with Python 3.8](https://docs.anaconda.com/anaconda/packages/py3.8_linux-64/).

### Activate the new virtual environment

To activate the new virtual environment, run `conda activate` followed by the name.

```bash
(base) aimldl@aimldl-desktop:~$ conda activate yolo_tensorflow2
(yolo_tensorflow2) aimldl@aimldl-desktop:~$ 
```

Notice the prompt is changed from `(base)` to the new name `(yolo_tensorflow`)`. A shortened notation will be used as follows to focus on the Linux commands.

```bash
(base) $ conda activate yolo_tensorflow2
(yolo_tensorflow2) $ 
```

## Machine Learning Frameworks

ML frameworks such as `keras`, `keras-gpu`, `pytorch`, `pytorch-gpu`, `scikit-image`, `scikit-learn`, `tensorflow`, `tensorflow-gpu`, `tensorflow-tensorboard`, `torchvision` are supported by Anaconda. In general, you may use the `conda install` command to install a ML framework. Doing so installs a stable version for the virtual environment from conda-forge.

Note certain versions may not exist in conda-forge. If so, you may use the `pip install` command. For details, refer to [Install TensorFlow 2](https://www.tensorflow.org/install) > [Install TensorFlow with pip](https://www.tensorflow.org/install/pip#virtual-environment-install).

### When Tensorflow is not installed,

importing Tensorflow fails with `ModuleNotFoundError`.

```bash
(yolo_tensorflow2) $  python -c 'import tensorflow as tf'
  ...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'tensorflow'
(yolo_tensorflow2) $
```

### Installing Tensorflow2

#### with `conda install`

```bash
(yolo_tensorflow2) $ conda install tensorflow
   ...
Proceed ([y]/n)? y
  ...
(yolo_tensorflow2) $
```

#### with `pip install`

```
$ sudo apt update
$ pip install --upgrade pip
$ pip install --upgrade tensorflow
```

### Uninstalling Tensorflow2

When something went wrong and Tensorflow has be removed, uninstall it:

#### with `conda uninstall`

```bash
(yolo_tensorflow2) $ conda uninstall tensorflow
  ...
Proceed ([y]/n)? 
  ...
(yolo_tensorflow2) $
```

#### with `pip uninstall`

```bash
(yolo_tensorflow2) $ pip uninstall tensorflow
  ...
Proceed (y/n)? y
  Successfully uninstalled tensorflow-2.4.0
(yolo_tensorflow2) $
```

TODO: delete the virtual environment

(yolo_tensorflow2) aimldl@aimldl-desktop:~$ 

https://stackoverflow.com/questions/55392100/install-tensorflow-2-0-in-conda-enviroment