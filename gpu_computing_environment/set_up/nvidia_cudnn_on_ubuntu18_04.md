* Rev.1: 2021-02-15 (Mon)
* Draft: 2021-01-10 (Sun)

# 우분투 18.04에서 NVIDIA cuDNN을 설정하는 방법

* 테스트 환경

  * (base) k8smaster@k8smaster-Alienware-Aurora-R7


## 현재 상황

NVIDIA Graphics driver와 CUDA11.0이 설치된 상태입니다. 

* CUDA 10.0으로 다운그레이드해서 cuDNN을 설치하지 않고 11.0버전을 유지한채 cuDNN을 설치해보겠습니다.
* 목적은 darknet을 돌리기 위함입니다.

```bash
$ ubuntu-drivers devices== /sys/devices/pci0000:00/0000:00:01.1/0000:02:00.0 ==
modalias : pci:v000010DEd00001B80sv00001028sd00003366bc03sc00i00
vendor   : NVIDIA Corporation
model    : GP104 [GeForce GTX 1080]
driver   : nvidia-driver-390 - distro non-free
driver   : nvidia-driver-418 - third-party free
driver   : nvidia-driver-418-server - distro non-free
driver   : nvidia-driver-455 - third-party free
driver   : nvidia-driver-450-server - distro non-free
driver   : nvidia-driver-460 - third-party free recommended
driver   : nvidia-driver-450 - third-party free
driver   : xserver-xorg-video-nouveau - distro free builtin

$
```

```bash
$ tail -n 2 ~/.bash_custom
export PATH=/usr/local/cuda/bin:/$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
$
```

```bash
$ ls -al /usr/local/cuda 
lrwxrwxrwx 1 root root 9  1월 25 13:37 /usr/local/cuda -> cuda-11.0
$
```

### cuDNN 다운로드 및 설치

#### 다운로드

https://developer.nvidia.com/rdp/cudnn-archive

너무 많은 것이 있습니다. 

<img src="images/nvidia-homepage-cudnn_download-cudnn_archive-2021-02-10.png">

웹브라우저의 찾기 기능으로 `11.0`을 찾습니다.

<img src='images/nvidia-homepage-cudnn_download-cudnn_archive-2021-02-15-11_0.png'>

위에 보이는 것이 11.0을 지원하는 모든 경우입니다. 모두 `cuDNN v8`이므로 가장 최신 버전인 `v8.0.5`를 설치해보겠습니다.

이 중 

[cuDNN Library for Linux (x86_64)](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.0.5/11.0_20201106/cudnn-11.0-linux-x64-v8.0.5.39.tgz)

를 다운로드 받습니다.

<img src='images/nvidia_cudnn-download-cudnnv8_0_5-cudnn_library_for_linux_x86_64-chrome_downloading.png'>

다운로드 받기 위해서는 원하는 버전을 클릭한 후 로그인이 필요합니다.

### 로그인 하기

<img src="/home/k8smaster/github/environments/gpu_computing_environment/install/images/nvidia-homepage-cudnn-nvidia_developer_program_membership_required.png">

계정이 있다면 `Login` 아니라면 `Join now`에서 계정을 만든 후에 로그인 합니다.

<img src="/home/k8smaster/github/environments/gpu_computing_environment/install/images/nvidia-homepage-log_in_or_sign_up_for_an_nvidia_account.png">

로그인 입력을 누른 다음  캡챠로 태깅을 해야합니다.

<img src="/home/k8smaster/github/environments/gpu_computing_environment/install/images/nvidia-homepage-log_in-captcha.png">

자세한 내용은 [NVIDIA cuDNN 설치하기](../install/cudnn.md)를 참고하세요.

