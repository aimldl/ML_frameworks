* Rev.1: 2020-10-22 (Thu)
* Draft: 2020-10-03 (Sat)

# Install & Configure the Computing Environment

## References

* [AerialDetection](https://github.com/dacon-ai/AerialDetection)/[INSTALL.md](https://github.com/dacon-ai/AerialDetection/blob/master/INSTALL.md)
  * This is the main tutorial I've used.

* [[힐링]Baseline Aerial Detection 설치 for Ubuntu](https://dacon.io/competitions/official/235644/codeshare/1710?page=1&dtype=recent&ptype=pub)
  * I found this later article writtein in Korean.
  * I keep this in case I may reference it in the future.

## Summary

```bash
#!/bin/bash
# install_aerialdetection
# Usage:
#   $ chmod +x install_aerialdetection 
#   $ ./install_aerialdetection

# Install Aerialdetection
# a. Create a conda virtual environment and activate it. Then install Cython.
conda create --name AerialDetection --clone pytorch_p36
source activate AerialDetection
conda install -y cython

# b. Install PyTorch stable or nightly and torchvision following the official instructions.
# c. Clone the AerialDetection repository.
cd SageMaker/
# if folder AerialDetection doesn't exist
# git clone https://github.com/dingjiansw101/AerialDetection.git
cd AerialDetection

# d. Compile cuda extensions.
chmod +x compile.sh
./compile.sh

# e. Install AerialDetection (other dependencies will be installed automatically).
pip install -r requirements.txt
python setup.py develop
# or "pip install -e ."
```

> ### Requirements
>
> - Linux
> - Python 3.5+ ([Say goodbye to Python2](https://python3statement.org/))
> - PyTorch 1.1
> - CUDA 9.0+
> - NCCL 2+
> - GCC 4.9+
> - [mmcv](https://github.com/open-mmlab/mmcv)
>
> are tested on:
>
> - OS: Ubuntu 16.04/18.04 and CentOS 7.2
> - CUDA: 9.0/9.2/10.0
> - NCCL: 2.1.15/2.2.13/2.3.7/2.4.2
> - GCC: 4.9/5.3/5.4/7.3

## Checking the requirements

### Linux

```bash
$ cat /etc/os-release
```

On Amazon SageMaker, the output looks like below.

```bash
NAME="Amazon Linux AMI"
VERSION="2018.03"
ID="amzn"
ID_LIKE="rhel fedora"
VERSION_ID="2018.03"
PRETTY_NAME="Amazon Linux AMI 2018.03"
ANSI_COLOR="0;33"
CPE_NAME="cpe:/o:amazon:linux:2018.03:ga"
HOME_URL="http://aws.amazon.com/amazon-linux-ami/"
```

### Python 3.5+

The `python --version` command shows the version.

```bash
$ python --version
Python 3.6.10 :: Anaconda, Inc.
$
```

### PyTorch 1.1

On Amazon SageMaker, there are three Conda virtual environments for PyTorch. 

* pytorch_p27
* pytorch_latest_p36 
* pytorch_p36

`pytorch_p27` is for Python 2.7 which does not satisfy the requirements. Let's check the PyTorch versions of either `pytorch_latest_p36` or `pytorch_p36`. 

```
(pytorch_latest_p36) sh-4.2$ python -c "import torch; print( torch.__version__ )"
1.6.0
(pytorch_latest_p36) sh-4.2$
```

As of 2020-10-06 (Tue),  `pytorch_latest_p36` has PyTorch 1.6.0. 

```bash
sh-4.2. $ source activate pytorch_p36
(pytorch_p36) sh-4.2$ python -c "import torch; print( torch.__version__ )"
1.4.0
(pytorch_p36) sh-4.2$
```

`pytorch_p36` has PyTorch 1.4.0. There is a report saying AerialDetection didn't work on PyTorch 1.5, 1.6, but worked on 1.4.  So the selected Conda virtual environment is `pytorch_p36`. 

### CUDA 9.0+

The `nvidia-smi` command shows the CUDA version. In the next example, `CUDA Version: 11.0` shows that CUDA 11.0 is installed.

```bash
$ nvidia-smi | grep CUDA
| NVIDIA-SMI 450.51.05    Driver Version: 450.51.05    CUDA Version: 11.0     |
$
```

### NCCL 2+

```bash
$ locate nccl| grep "libnccl.so" | tail -n1 | sed -r 's/^.*\.so\.//'
2.7.6.
$
```

### GCC 4.9+

```bash
$ gcc --version
gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-28)
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
$
```

Unfortunately, gcc version is lower than 4.9. This will cause an error in the next step. The installation of MMCV fails with the following error.

```bash
$ pip install mmcv-full
  ...
Index.h:31:2: error: #error "You're running a too old version of GCC. We need GCC 5 or later."
     #error "You're running a too old version of GCC. We need GCC 5 or later."
      ^
    error: command '/usr/local/cuda-10.1/bin/nvcc' failed with exit status 1
  ...
$
```

So gcc version must be upgraded. But the challenge is upgrading the preinstalled packages are not supported due to potential issues imposed by the upgrade. For details, refer to "AWS > Documentation > Amazon SageMaker > Developer Guide > [Install External Libraries and Kernels in Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-add-external.html)". 

> ### Unsupported
> SageMaker aims to support as many package installation operations as possible. However, if the packages were installed by SageMaker or DLAMI, and you use the following operations on these packages, it might make your notebook instance unstable:
>
> * Uninstalling
> * Downgrading
> * Upgrading
>
> We do not provide support for installing packages via yum install or installing R packages from CRAN. Due to potential issues with network conditions or configurations, or the availability of Conda 

### A trick to use gcc

The reason why gcc is necessary is to compile source codes such as `Index.h`. A trick is to install, say, `gcc72` and use it temporarily instead of `gcc`.

First, install `gcc72`. 

```bash
$ sudo yum install -y gcc72 gcc72-c++
```

For details, refer to [Installing g++ 5 on Amazon Linux](https://stackoverflow.com/questions/38188896/installing-g-5-on-amazon-linux).

Secondly, change the file name of `gcc72` to `gcc`.

Currently, there exists `gcc` and `gcc72` in the `/usr/bin` directory.

```bash
$ gcc --version
gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-28)
  ...
$ gcc72 --version
gcc72 (GCC) 7.2.1 20170915 (Red Hat 7.2.1-2)
  ...
$ which gcc
/usr/bin/gcc
$
```

Change the file names as follows.

```bash
$ cd /usr/bin
$ sudo mv gcc gcc_old
$ sudo mv gcc72 gcc
$ which gcc
/usr/bin/gcc
$
```

 `gcc` will be used when the `pip` command installs MMCA. 

### [mmcv](https://github.com/open-mmlab/mmcv)

MMCV is a foundational python library for computer vision research and supports many research project. There are two versions of MMCV: `mmcv` and `mmcv-full`.

* `mmcv` is the light version without CUDA ops, but all other features.
* `mmcv-full` is the full version with CUDA ops.

Note: installing both versions in the same environment causes errors like `ModuleNotFound`.

##### Install `mmcv-full` instead of `mmcv` to use the computational power of GPU which requires CUDA.

The name change trick works and `pip install mmcv-full` built `mmcv-full` successfully!

```bash
$ pip install mmcv-full
Collecting mmcv-full
  ...
Building wheels for collected packages: mmcv-full
  Building wheel for mmcv-full (setup.py) ... done
  ...
Successfully built mmcv-full
Installing collected packages: mmcv-full
Successfully installed mmcv-full-1.1.4
$ 
```

So far installation of `mmcv-full` is smooth. But there were several challenges to overcome. As a future reference, some failed attempts are given below.

##### A trick to use alias

Aliasing `gcc72` to `gcc` failed.

```bash
$ gcc --version
gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-28)
  ...
$ gcc72 --version
gcc72 (GCC) 7.2.1 20170915 (Red Hat 7.2.1-2)
  ...
$ alias gcc='gcc72'
$ gcc --version
gcc72 (GCC) 7.2.1 20170915 (Red Hat 7.2.1-2)
  ...
$
```

Notice the first `gcc --version` returns 4.8.5. while the second `gcc --version` after the alias returns 7.2.1. The `alias` command is valid only within this terminal. So closing the terminal reverts to the original `gcc` command.

When `pip install mmcv-full` was actually ran. An error occurred because gcc version is too old. While `gcc` was aliased successfully, which indicates the original `gcc`.

```bash
$ alias
gcc='gcc72'
$ which gcc
/usr/bin/gcc
$
```

Anyways, the name change trick worked just fine.

##### Installing `mmcv`

Even with the old `gcc` version,`mmcv` is successfully installed with `pip` on Amazon SageMaker. This implies `gcc` is used to compile the part necessary for CUDA.

```bash
$ pip install mmcv
Collecting mmcv
  Downloading mmcv-1.1.4.tar.gz (239 kB)
     |████████████████████████████████| 239 kB 891 kB/s 
  ...
Successfully built mmcv
Installing collected packages: mmcv
Successfully installed mmcv-1.1.4
$
```

To uninstall `mmcv`, run:

```bash
$ pip uninstall mmcv
Found existing installation: mmcv 1.1.4
Uninstalling mmcv-1.1.4:
  Would remove:
    /home/ec2-user/anaconda3/envs/pytorch_latest_p36/lib/python3.6/site-packages/mmcv-1.1.4.dist-info/*
    /home/ec2-user/anaconda3/envs/pytorch_latest_p36/lib/python3.6/site-packages/mmcv/*
Proceed (y/n)? y
  Successfully uninstalled mmcv-1.1.4
$
```

## Install AerialDetection

> a. Create a conda virtual environment and activate it. Then install Cython.
>
> ```bash
> $ conda create -n AerialDetection python=3.7 -y
> $ source activate AerialDetection
> (AerialDetection)$ conda install cython
> ```
>
> b. Install PyTorch stable or nightly and torchvision following the [official instructions](https://pytorch.org/).
>
> c. Clone the AerialDetection repository.
>
> ```bash
> $ git clone https://github.com/dingjiansw101/AerialDetection.git
> ```
>
> d. Compile cuda extensions.
>
> ```bash
> $ cd AerialDetection
> $ ./compile.sh
> ```
>
> e. Install AerialDetection (other dependencies will be installed automatically).
>
> ```bash
> $ pip install -r requirements.txt
> $ python setup.py develop
> # or "pip install -e ."
> ```

As you are already in Conda virtual environment `pytorch_p36`, the two commands in step a is not necessary. If you prefer using `AerialDetection`, you may clone `pytorch_p36` and create a new virtual environment.

### Cloning `pytorch_p36` to `AerialDetection`

The `--clone` option allows to clone an existing Conda environment.

> ```bash
> $ conda create --name mydestination --clone mysource
> ```
>
> Source: [How can you “clone” a conda environment into the root environment?](https://stackoverflow.com/questions/40700039/how-can-you-clone-a-conda-environment-into-the-root-environment)

`pytorch_p36` is cloned to a new Conda environment `AerialDetection`. 

```bash
sh-4.2$ conda create --name AerialDetection --clone pytorch_p36
Source:      /home/ec2-user/anaconda3/envs/pytorch_p36
Destination: /home/ec2-user/anaconda3/envs/AerialDetection
  ...
sh-4.2$
```

To activate the virtual environment, run:

```bash
sh-4.2$ source activate pytorch_p36
(pytorch_p36) sh-4.2$
```

For simplicity, `(pytorch_p36) sh-4.2$` is denoted to `$` below. All the commands must be run in Conda virtual environment `pytorch_p36`.

Now install `cython`.

```bash
$ conda install cython
  ...
  added / updated specs:
    - cython
  ...
The following NEW packages will be INSTALLED:

  docutils           pkgs/main/linux-64::docutils-0.16-py36_1
  pip                pkgs/main/linux-64::pip-20.2.3-py36_0

The following packages will be UPDATED:

  ca-certificates                               2020.6.24-0 --> 2020.7.22-0
  openssl                                 1.1.1g-h7b6447c_0 --> 1.1.1h-h7b6447c_0
  ...
$ cd SageMaker
$ git clone https://github.com/dingjiansw101/AerialDetection.git
$ cd AerialDetection
$ chmod +x compile.sh 
$ ./compile.sh
```

Note the errors will occur when a too old version of GCC is used. Refer to [compile.sh Fails to Compile](troubleshooting/compile_sh_fails_to_compile.md). 

```bash
error: #error "You're trying to build PyTorch with a too old version of GCC. We need GCC 5 or later."
```

```bash
$ pip install -r requirements.txt
  ...
Installing collected packages: mmcv, shapely
Successfully installed mmcv-1.1.4 shapely-1.7.1
$ python setup.py develop
  ...
Installing yapf script to /home/ec2-user/anaconda3/envs/pytorch_p36/bin

Using /home/ec2-user/anaconda3/envs/pytorch_p36/lib/python3.6/site-packages
Finished processing dependencies for mmdet==0.6.0+19eac33
$
```

You may add ` > /dev/null` to suppress the output.

## Install DOTA_devkit

The instructions are as follows.

```bash
$ sudo apt-get install swig
$ cd DOTA_devkit
$ swig -c++ -python polyiou.i
$ python setup.py build_ext --inplace
```

But SageMaker doesn't have either `apt-get` or `apt`.

```bash
$ sudo apt-get install swig
sudo: apt-get: command not found
$ sudo apt install swig
sudo: apt: command not found
$
```

Instead, use the `yum` command.

```bash
$ sudo yum install swig
$ cd DOTA_devkit/
$ ls
DOTA2COCO.py               nms.py                  prepare_dota1_5.py            rotate.py
DOTA.py                    polyiou.cpp             prepare_dota1_aug.py          rotate_test.py
dota_utils.py              polyiou.h               prepare_dota1.py              setup.py
geojson2coco.py            polyiou.i               readme.md                     SplitOnlyImage_multi_process.py
HRSC2COCO.py               polyiou.py              ResultMerge_multi_process.py  SplitOnlyImage.py
ImgSplit_multi_process.py  poly_overlaps_test.py   ResultMerge.py                utils.py
ImgSplit.py                prepare_dota1_5_aug.py  results_obb2hbb.py
$ swig -c++ -python polyiou.i
$ python setup.py build_ext --inplace
$
```

### Change the file name back to `gcc` and `gcc77`

```bash
$ sudo mv gcc gcc_old
$ sudo mv gcc72 gcc
$ which gcc
/usr/bin/gcc
$ cd /usr/bin
$ which gcc72
/usr/bin/gcc72
$
```