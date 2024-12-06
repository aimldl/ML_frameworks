* Rev.2: 2022-04-27 (Wed)
* Rev.1: 2021-01-20 (Wed)
* Draft: 2020-11-12 (Thu)

# 텐서플로우 설치하기 (Installing TensorFlow)

## 개요

[Install TensorFlow 2](https://www.tensorflow.org/install)의 내용을 정리했습니다. 설치 가이드의 한국어판은 [TensorFlow 2 설치](https://www.tensorflow.org/install)입니다. 한국어 설치 가이드보다 원본인 영어를 참고하시길 권장합니다. 이유는 [왜 영어 설치 가이드를 참고해야 하는가?](translated_tensorflow_installation_guide_can_be_wrong.md)를 참고하세요.

> ### [Install TensorFlow 2](https://www.tensorflow.org/install)
>
> TensorFlow is tested and supported on the following 64-bit systems:
>
> * Python 3.5–3.8
> * Ubuntu 16.04 or later
> * Windows 7 or later (with [C++ redistributable](https://support.microsoft.com/help/2977003/the-latest-supported-visual-c-downloads)) 
> * macOS 10.12.6 (Sierra) or later (no GPU support)
> * Raspbian 9.0 or later
>
> **[Download a package](https://www.tensorflow.org/install/pip)**
>
> Install TensorFlow with Python's *pip* package manager.
>
> >  TensorFlow 2 packages require a `pip` version >19.0.
>
> Official packages available for Ubuntu, Windows, macOS, and the Raspberry Pi.
>
> See the [GPU guide](https://www.tensorflow.org/install/gpu) for CUDA®-enabled cards.
>
> ```bash
> # Requires the latest pip
> pip install --upgrade pip
> 
> # Current stable release for CPU and GPU
> pip install tensorflow
> 
> # Or try the preview build (unstable)
> pip install tf-nightly
> ```
>
> 출처: https://www.tensorflow.org/install

## 설치 과정

### Step 1. GPU를 사용하기 위해 설정

> TensorFlow GPU 지원에는 다양한 드라이버와 라이브러리가 필요합니다. 설치를 단순화하고 라이브러리 충돌을 방지하려면 [GPU를 지원하는 TensorFlow Docker 이미지](https://www.tensorflow.org/install/docker)를 사용하는 것이 좋습니다(Linux만 해당). 이 설정에는 [NVIDIA® GPU 드라이버](https://www.nvidia.com/drivers)만 있으면 됩니다.

> **소프트웨어 요구사항**
>
> 다음 NVIDIA® 소프트웨어가 시스템에 설치되어 있어야 합니다.
>
> - [NVIDIA® GPU 드라이버](https://www.nvidia.com/drivers) - CUDA® 10.1에는 418.x 이상이 필요합니다.
> - [CUDA® Toolkit](https://developer.nvidia.com/cuda-toolkit-archive) - TensorFlow는 CUDA® 10.1을 지원합니다(TensorFlow 2.1.0 이상).
> - [CUPTI](http://docs.nvidia.com/cuda/cupti/)는 CUDA® Toolkit과 함께 제공됩니다.
> - [cuDNN SDK 7.6](https://developer.nvidia.com/cudnn)
> - *(선택사항)* [TensorRT 6.0](https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html) - 일부 모델에서 추론 처리량과 지연 시간을 향상합니다.
>
> 출처: [GPU지원](https://www.tensorflow.org/install/gpu)

> **apt를 사용하여 CUDA 설치**
>
> 이 섹션에서는 Ubuntu 16.04 및 18.04에 CUDA® 10(TensorFlow 1.13.0 이상)을 설치하는 방법을 보여줍니다. 아래의 명령어는 다른 Debian 기반 배포판에도 적용될 수 있습니다.



### Step 2-1. NVIDIA 소프트웨어가 설치되어 있는지 확인

```bash
$ nvidia-smi

Command 'nvidia-smi' not found, but can be installed with:

sudo apt install nvidia-340      
sudo apt install nvidia-utils-390

$
```

설치가 안 되어 있습니다.

### Step 2-2. 터미널에서 아래 명령어로 설치
아래의 명령어를 실행합니다.

출처: [TensorFlow](https://www.tensorflow.org/) > [TensorFlow 2 설치](https://www.tensorflow.org/install) > [GPU 지원](https://www.tensorflow.org/install/gpu)의 [Linux 설정 > apt를 사용하여 CUDA 설치](https://www.tensorflow.org/install/gpu#install_cuda_with_apt)

```bash
# Add NVIDIA package repositories
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.1.243-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo dpkg -i cuda-repo-ubuntu1804_10.1.243-1_amd64.deb
sudo apt-get update
wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt-get update

# Install NVIDIA driver
sudo apt-get install --no-install-recommends nvidia-driver-450
# Reboot. Check that GPUs are visible using the command: nvidia-smi

# Install development and runtime libraries (~4GB)
sudo apt-get install --no-install-recommends \
    cuda-10-1 \
    libcudnn7=7.6.5.32-1+cuda10.1  \
    libcudnn7-dev=7.6.5.32-1+cuda10.1


# Install TensorRT. Requires that libcudnn7 is installed above.
sudo apt-get install -y --no-install-recommends libnvinfer6=6.0.1-1+cuda10.1 \
    libnvinfer-dev=6.0.1-1+cuda10.1 \
    libnvinfer-plugin6=6.0.1-1+cuda10.1
```

### Step 2-3. 설치 완료 후에 확인

```bash
Welcome to ubuntu18.04, Python 3.6.9,
aimldl@aimldl-home-desktop:~$ nvidia-smi
Thu Jan 21 18:33:14 2021
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 450.102.04   Driver Version: 450.102.04   CUDA Version: 11.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 1080    On   | 00000000:01:00.0 Off |                  N/A |
|  0%   32C    P8     6W / 200W |    309MiB /  8118MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1105      G   /usr/lib/xorg/Xorg                168MiB |
|    0   N/A  N/A      1236      G   /usr/bin/gnome-shell              137MiB |
+-----------------------------------------------------------------------------+
aimldl@aimldl-home-desktop:~$ nvcc --version

Command 'nvcc' not found, but can be installed with:

sudo apt install nvidia-cuda-toolkit

aimldl@aimldl-home-desktop:~$
```

### Step 2. 패키지 다운로드

`pip`을 최신 버전으로 업데이트/설치하고, 텐서플로우를 CPU와 GPU가 지원되는 안정적인 최신 버전 (current stable release)으로 설치합니다.  

> ```bash
> # Requires the latest pip
> pip install --upgrade pip
> 
> # Current stable release for CPU and GPU
> pip install tensorflow
> 
> # Or try the preview build (unstable)
> pip install tf-nightly
> ```

```bash
$ pip install --upgrade pip
$ pip install tensorflow
```

### Step 3. 설치 확인하기

```bash
$ python -c "import tensorflow as tf; print(tf.__version__)"
2.8.0
$
```

