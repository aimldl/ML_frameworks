* Rev.1: 2020-10-16 (Fri)
* Draft: 2020-10-07 (Wed)

# How to Initialize Amazon SageMaker for AerialDetection

## Introduction

Currently, the default SageMaker is not suitable to run AerialDetection because the installation instructions at [AerialDetection](https://github.com/dacon-ai/AerialDetection)/[INSTALL.md](https://github.com/dacon-ai/AerialDetection/blob/master/INSTALL.md) fails in many steps. The problems during the installation has been fixed. [INSTALL.md](INSTALL.md) details the process and this article shows the step-by-step commands to initialize Amazon SageMaker for AerialDetection.

## Commands to initialize SageMaker

### Run a script `initialize_amazon_sagemaker`

Run a Bash script [bash_scripts/initialize_amazon_sagemaker](bash_scripts/initialize_amazon_sagemaker) to initialize SageMaker for AerialDetection. 

```bash
$ chmod +x initialize_amazon_sagemaker
$ ./initialize_amazon_sagemaker
```

After the initialization, you must be in the `pytorch_p36` virtual environment.

```bash
(base) [ec2-user@ip-123-45-67-89 SageMaker]$ source activate pytorch_p36
(pytorch_p36) [ec2-user@ip-123-45-67-89 SageMaker]$ 
```

Notice `(base)` has been changed to `(pytorch_p36)`.

This script is explained in the following sections more in detail. 

#### Get your AWS credentials ready

At the end of this script, the following message shows up.

```bash
  ...
Enter the credentials below
AWS Access Key ID [None]: 
```

Enter all the information for config & credentials. You may copy and paste the access key ID and press `Enter`.  The `Access Key ID` and `Secret Access Key` are changed to a series of aesterisk `*` . In the above example, `Region name` is `ap-northeast-2`, but enter the region name for your SageMaker instance. The output format is `json`.

```bash
AWS Access Key ID [None]: ********************
AWS Secret Access Key [None]: ****************************************
Default region name [ap-northeast-2]: ap-northeast-2
Default output format [None]: json
(base) [ec2-user@ip-123-45-67-89 SageMaker]$ 
```

If you don't have your AWS credentials ready, you may exit this part and enter the information later.

```bash
AWS Access Key ID [****************G7GU]: ^C
(base) [ec2-user@ip-123-45-67-89 SageMaker]$ 
```

To enter the credentials, run

```bash
$ aws configure
```

You may fix the information in the credentials by running the above command. For example, the typo `ap-notrheast-2` may be fixed to `ap-northeast-2` as follows.

```bash
$ aws configure
AWS Access Key ID [****************X9YZ]: 
AWS Secret Access Key [****************AbCd]: 
Default region name [ap-notrheast-2]: ap-northeast-2
Default output format [json]: 
```

### Summary

The content of the script `initialize_amazon_sagemaker` is below.

```bash
echo "Install AerialDetection"
# Meet requirements for AerialDetection
source activate pytorch_p36
sudo yum install -y gcc72 gcc72-c++
# Use a change name trick to swap gcc & gcc72
cd /usr/bin/
sudo mv gcc gcc_old
sudo mv gcc72 gcc

pip install mmcv-full
conda install -y cython

# If you haven't cloned AerialDetection repository, uncomment.
# cd ~/SageMaker
# git clone https://github.com/dingjiansw101/AerialDetection.git

cd ~/SageMaker/AerialDetection
chmod +x compile.sh
./compile.sh

pip install -r requirements.txt
python setup.py develop

echo "Install DOTA_devkit"
sudo yum install swig
cd DOTA_devkit/
swig -c++ -python polyiou.i
python setup.py build_ext --inplace

# Undo the change name trick to swap gcc72 and gcc
cd /usr/bin/
sudo mv gcc gcc_old
sudo mv gcc72 gcc

echo "Install some utility programs"
sudo yum install -y tree

echo "Configure Amazon IAM"
cat ~/SageMaker/.aws/config
cat ~/SageMaker/.aws/credentials
echo "config & credentials are displayed above."
echo "Enter the credentials below"
aws configure
```

The following part explains the set of commands presented above.

### Install AerialDetection

#### 1. Activate the Conda virtual environment

`pytorch_p36` satisfies most of AerialDetection's requirements.

```bash
sh-4.2$ source activate pytorch_p36
(pytorch_p36) sh-4.2$ 
```

#### 2. Upgrade the default gcc to a higher version

Install a higher version of gcc or `gcc72`.

```bash
$ sudo yum install -y gcc72 gcc72-c++
```

A trick to change the file name is used to use the higher version of gcc or `gcc72`

```bash
$ cd /usr/bin/
$ sudo mv gcc gcc_old
$ sudo mv gcc72 gcc
```

#### 3. Install MMCV

```bash
$ pip install mmcv-full
```

#### 4. Install Cython

```bash
$ conda install -y cython
```

#### 5. Clone the AerialDetection repository

If you have cloned the repository, skip this part.

```bash
$ cd ~/SageMaker
$ git clone https://github.com/dingjiansw101/AerialDetection.git
```

#### 6. Compile CUDA extensions.

```bash
$ cd ~/SageMaker/AerialDetection
$ chmod +x compile.sh
$ ./compile.sh
```

#### 7. Install AerialDetection and dependencies

```bash
$ pip install -r requirements.txt
$ python setup.py develop
# or "pip install -e ."
```

### Install DOTA_devkit

gcc is required for `python setup.py build_ext --inplace`. 

```bash
$ sudo yum install swig
$ cd DOTA_devkit/
$ swig -c++ -python polyiou.i
$ python setup.py build_ext --inplace
```

Change the file name back to `gcc` and `gcc77`

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

### Install some utility programs

```bash
$ sudo yum install -y tree
```

#### Configure Amazon IAM

To use other AWS services such as Amazon S3, A

It is assumed that the `config` and `credentials` are saved in the `~/SageMaker/.aws` directory.

```bash
$ cat ~/SageMaker/.aws/config
$ cat ~/SageMaker/.aws/credentials
echo "config & credentials are displayed above."
echo "Enter the credentials below"
$ aws configure
```

The AWS configuration is initialized to `None` at each time the SageMaker instance starts.

```bash
$ aws configure
AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [ap-northeast-2]: 
Default output format [None]: 
$
```

So a trick is to save the `config` and `credentials` under the `~/SageMaker` directory where the files under this directory is persistent. Refer to the displayed `config` and `credentials` and enter the credentials like below.

```bash
$ aws configure
AWS Access Key ID [None]: A*******************
AWS Secret Access Key [None]: a***************************************
Default region name [ap-northeast-2]: ap-notrheast-2
Default output format [None]: json
$
```

