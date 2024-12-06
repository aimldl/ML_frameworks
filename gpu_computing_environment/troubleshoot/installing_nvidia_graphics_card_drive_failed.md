

* Draft: 2021-01-10 (Sun)

# 우분투 20.04에서 NVIDIA GeForce 1080Ti GPU카드 설정하는 방법

## 개요 + 문제

GPGPU를 사용을 위한 GPU카드 설정을 하기 위해서 

1. NVIDIA 그래픽 카드 드라이버 설치하기
2. CUDA toolkit 설치하기
3. model    : GP104 [GeForce GTX 1080]cuDNN 설치하기

이 3가지 과정을 진행 하기 위해서 2까지 실행했는데, 문제가 발생했습니다.

1에서 자동으로 설치된 패키지의 일부를 2에서 지워서 그런지 아래처럼 패키지 의존성 이슈가 발생합니다.

```bash
다음 패키지의 의존성이 맞지 않습니다:
 cuda : 의존: cuda-11-2 (>= 11.2.0) 하지만 %s 패키지를 설치하지 않을 것입니다
E: 문제를 바로잡을 수 없습니다. 망가진 고정 패키지가 있습니다.
```

1을 실행한 후에 NVIDIA 그래픽 카드가 설치되어 있었지만, 재부팅 후에 `설정 > 정보`에서 확인하면 `NV134`로 돌아가 있습니다.

<img src="/home/aimldl/github/environments/gpu_computing_environment/set_up/images/ubuntu20-04-settings-about-aimldl_desktop-vn134.png">

뭔가 잘못 된 것이 확실하네요. 문제를 돌리지 위해서 1의 명령어를 실행해도

```bash
$ sudo ubuntu-drivers autoinstall
[sudo] aimldl의 암호: 
패키지 목록을 읽는 중입니다... 완료
의존성 트리를 만드는 중입니다       
상태 정보를 읽는 중입니다... 완료
몇몇 패키지를 설치할 수 없습니다. 요청한 상황이 불가능할 수도 있고,
불안정 배포판을 사용해서 일부 필요한 패키지를 아직 만들지 않았거나,
아직 Incoming에서 나오지 않은 경우일 수도 있습니다.
이 상황을 해결하는데 다음 정보가 도움이 될 수도 있습니다:

다음 패키지의 의존성이 맞지 않습니다:
 linux-modules-nvidia-460-generic-hwe-20.04-edge : 의존: nvidia-kernel-common-460 (>= 460.32.03) 하지만 460.27.04-0ubuntu1 패키지를 설치할 것입니다
 nvidia-driver-460 : 의존: libnvidia-compute-460 (= 460.27.04-0ubuntu1) 하지만 460.32.03-0ubuntu0.20.04.1 패키지를 설치할 것입니다
                     의존: libnvidia-decode-460 (= 460.27.04-0ubuntu1) 하지만 %s 패키지를 설치하지 않을 것입니다
                     의존: libnvidia-encode-460 (= 460.27.04-0ubuntu1) 하지만 %s 패키지를 설치하지 않을 것입니다
                     추천: nvidia-settings 하지만 %s 패키지를 설치하지 않을 것입니다
                     추천: nvidia-prime (>= 0.8) 하지만 %s 패키지를 설치하지 않을 것입니다
                     추천: libnvidia-compute-460:i386 (= 460.27.04-0ubuntu1)
                     추천: libnvidia-decode-460:i386 (= 460.27.04-0ubuntu1)
                     추천: libnvidia-encode-460:i386 (= 460.27.04-0ubuntu1)
                     추천: libnvidia-ifr1-460:i386 (= 460.27.04-0ubuntu1)
                     추천: libnvidia-fbc1-460:i386 (= 460.27.04-0ubuntu1)
                     추천: libnvidia-gl-460:i386 (= 460.27.04-0ubuntu1)
E: 문제를 바로잡을 수 없습니다. 망가진 고정 패키지가 있습니다.
$
```

자동으로 문제를 바로 잡을 수 없다고 합니다. 

## 힌트

그래서 수동으로 의존하는 각 패키지를 설치하려고 했지만

```bash
$ sudo apt install nvidia-kernel-common-460 libnvidia-compute-460 ...
```

 실패했습니다.

## 해결

가장 확실한 방법으로 우분투를 재설치했습니다. 



## 설치 과정 요약

### 1. NVIDIA 그래픽 카드 드라이버 설치하기

(1) 그래픽 카드에 대한 정보 알아내기

```
$ ubuntu-drivers devices
  ...
model    : GP104 [GeForce GTX 1080]
  ...
$
```

(2) `설정 > 정보`에서 시스템에 설치된 그래픽 카드 확인하기. 

<img src="/home/aimldl/github/environments/gpu_computing_environment/set_up/images/ubuntu20-04-settings-about-aimldl_desktop-vn134.png">

`그래픽`이 `NV134`로 되어있습니다. NVIDIA사의 그래픽 카드 드라이버로 설치해야 합니다.

(NVIDIA의 그래픽 카드 드라이버가 아닐 경우)

(3) 다음 명령어로  드라이버를 자동으로 설치하기

```bash
$ sudo ubuntu-drivers autoinstall
[sudo] aimldl의 암호: 
  ...
완료되었습니다
Processing triggers for initramfs-tools (0.136ubuntu6.3) ...
update-initramfs: Generating /boot/initrd.img-5.8.0-36-generic
$
```

(4) 시스템 재부팅

```bash
$ reboot
```

(5) `설정 > 정보`에서 시스템에 설치된 그래픽 카드 확인하기

빙고! `그래픽`이 `NVIDIA Corporation GP 104 [GeForce GTX 1080]`으로 인식되었습니다.

<img src="/home/aimldl/github/environments/gpu_computing_environment/set_up/images/ubuntu20-04-settings-about-aimldl_desktop-nvidia_corporation_gp104-geforce_gtx_1080.png">

(6) 드라이버 버전 등을 `nvidia-smi`명령어로 확인하기

```bash
$ nvidia-smi
```

출력 메세지는 아래와 같습니다.

```bash
Sun Jan 10 23:53:02 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.32.03    Driver Version: 460.32.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 1080    Off  | 00000000:01:00.0  On |                  N/A |
|  0%   38C    P8    13W / 200W |    384MiB /  8118MiB |      2%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1009      G   /usr/lib/xorg/Xorg                182MiB |
|    0   N/A  N/A      1266      G   /usr/bin/gnome-shell              120MiB |
|    0   N/A  N/A      4302      G   ...AAAAAAAAA= --shared-files       77MiB |
+-----------------------------------------------------------------------------+
$
```

이번에 설치된 

* 드라이버 버전은 `460.32.03`
* CUDA 버전은 `11.2`

입니다.

### 주의 사항

* GPU환경을 구축할 때 텐서프로가 지원하는 `CUDA 버전`은 항상 오래된 것이기 때문에 작은 문제가 발생하기 마련이므로 주의가 필요합니다.
  * 텐서플로는 오래된 `CUDA 버전`인 `10.1`을 지원합니다.
  * 이 문서가 작성된 시점에서 `CUDA 버전`은 `11.2`입니다. 

### 2. CUDA toolkit 설치하기

* 자동 설치: Bash 스크립트 [install_nvidia_cuda_libraries-ubuntu20_04](https://github.com/aimldl/coding/blob/main/bash_scripting/bash_scripts/install_nvidia_cuda_libraries-ubuntu20_04)를 실행하면 자동으로 설치할 수 있습니다.

스크립트의 내용을 로컬 컴퓨터의 텍스트 파일에 복사한 후

```bash
$ nano install_nvidia_cuda_libraries-ubuntu20_04
```

위의 명령어는 `nano`텍스트 에디터를 `install_nvidia_cuda_libraries-ubuntu20_04`라는 파일명으로 오픈하는 것입니다. 스크립트의 내용을 복사 & 붙여넣기 한 후에, 파일을 저장하고 (Ctrl+o), 에디터를 나가시면 (Ctrl+x)됩니다.

그리고 스크립트를 실행하세요.

```bash
$ bash install_nvidia_cuda_libraries-ubuntu20_04
  ...
[sudo] aimldl의 암호:
  ...
```

만약 메세지에 다음 처럼 메세지가 나오더라도 

```bash
  ...
다음 패키지가 자동으로 설치되었지만 더 이상 필요하지 않습니다:
  libatomic1:i386 libbsd0:i386 libdrm-amdgpu1:i386 libdrm-intel1:i386 libdrm-nouveau2:i386 
  ...
  screen-resolution-extra xserver-xorg-video-nvidia-460
'sudo apt autoremove'를 이용하여 제거하십시오.
```

 `sudo apt autoremove`를 실행하지 않아도 괜찮습니다. 왜냐하면 스크립트의 다음 명령어가  `sudo apt autoremove`이기 때문에 자동으로 실행됩니다.

```bash
다음 패키지를 지울 것입니다:
  linux-modules-nvidia-460-generic-hwe-20.04-edge* nvidia-compute-utils-460* nvidia-driver-460* nvidia-kernel-common-460* nvidia-kernel-source-460* nvidia-prime* nvidia-settings*
  nvidia-utils-460*
  ...
```

이미 자동으로 설치된 패키지의 일부를 지워서 그런지 아래처럼 패키지 의존성 이슈가 발생합니다.

```bash
다음 패키지의 의존성이 맞지 않습니다:
 cuda : 의존: cuda-11-2 (>= 11.2.0) 하지만 %s 패키지를 설치하지 않을 것입니다
E: 문제를 바로잡을 수 없습니다. 망가진 고정 패키지가 있습니다.
```

재부팅 전에 NVIDIA 그래픽 카드가 설치되어 있었지만, 재부팅 후에 `설정 > 정보`에서 확인하면 `NV134`로 돌아가 있습니다.

<img src="/home/aimldl/github/environments/gpu_computing_environment/set_up/images/ubuntu20-04-settings-about-aimldl_desktop-vn134.png">

뭔가 잘못 된 것이 확실하네요.

설치 후에 취해야 하는 액션을 안내하는 문구가 출력됩니다. 

```bash
  ...
Take the following post-installation actions.
Take a note of the following part.
$ ls /usr/local/ | grep cuda-
$ ls /usr/local/
Add the PATH variable at the end of `.bashrc`
$ echo 'export PATH=/usr/local/cuda-11.0/bin${PATH:+:${PATH}}' >> ~/.bashrc
$ echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
# Reload the bash
$ source ~/.bashrc
# Check 
$ sudo ldconfig
$ nvidia-smi
$ echo $PATH

Reboot? (y/n): 
```

여기까지 오면 스크립트는 끝까지 실행된 것입니다. 재부팅을 원하면 y를 아니면 n를 입력합니다.

### 자동 설치: Bash 스크립트 [install_nvidia_cuda_libraries-ubuntu20_04](https://github.com/aimldl/coding/blob/main/bash_scripting/bash_scripts/install_nvidia_cuda_libraries-ubuntu20_04)의 상세 내용

Step 1. Pre-installation actions

```bash
$ lspci | grep -i nvidia
$ uname -m && cat /etc/*release
$ gcc --version
```

Step 2. Update/upgrade the system and install dependencies

```bash
$ sudo apt-get update && sudo apt-get upgrade -y
$ sudo apt install -y build-essential
$ sudo apt-get install -y python-dev python3-dev python-pip python3-pip
#$ sudo apt-get install linux-headers-$(uname -r)
```

Step 3. Clean the existing NVIDIA driver.

```bash
# TODO: include -y to remove automatically
$ sudo apt-get purge nvidia*
$ sudo apt-get autoremove
$ sudo apt-get autoclean
$ sudo rm -rf /usr/local/cuda*
```

Step 4. Install the latest NVIDIA CUDA

* cuda 11.2 is the latest version (as of 2021-01-08). 
* You may change the version name in the following command.
* These commands are from ***Installation instructions: deb (network)*** below. 

```bash
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
$ sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ wget https://developer.download.nvidia.com/compute/cuda/11.2.0/local_installers/cuda-repo-ubuntu2004-11-2-local_11.2.0-460.27.04-1_amd64.deb
$ sudo dpkg -i cuda-repo-ubuntu2004-11-2-local_11.2.0-460.27.04-1_amd64.deb
$ sudo apt-key add /var/cuda-repo-ubuntu2004-11-2-local/7fa2af80.pub
$ sudo apt-get update -y
$ sudo apt-get -y install cuda
```

Step 5. Reboot the system

```bash
$ reboot
```

For the full detail of this document, refer to [NVIDIA CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#abstract). A more general guideline is available at [NVIDIA CUDA GETTING STARTED GUIDE FOR LINUX](http://developer.download.nvidia.com/compute/cuda/7_0/Prod/doc/CUDA_Getting_Started_Linux.pdf). [Verify CUDA Installation](https://xcat-docs.readthedocs.io/en/stable/advanced/gpu/nvidia/verify_cuda_install.html)

Step 6. Post-installation actions

TODO: check the command & update the output at the bottom.

```bash
# Double-check the directory name
$ ls /usr/local/ | grep "cuda-"
$ ls /usr/local/

# Add the PATH variable at the end of `.bashrc`
$ echo 'export PATH=/usr/local/cuda-11.0/bin${PATH:+:${PATH}}' >> ~/.bashrc
$ echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc

# Reload the bash
$ source ~/.bashrc

# Check 
$ sudo ldconfig
$ nvidia-smi
$ echo $PATH
/usr/local/cuda-11.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
$
```

The above commands are explained more in detail below.

자동으로 문제를 바로 잡을 수 없다고 합니다. 

## 힌트

```bash
다음 패키지의 의존성이 맞지 않습니다:
 linux-modules-nvidia-460-generic-hwe-20.04-edge : 의존: nvidia-kernel-common-460 (>= 460.32.03) 하지만 460.27.04-0ubuntu1 패키지를 설치할 것입니다
 nvidia-driver-460 : 의존: libnvidia-compute-460 (= 460.27.04-0ubuntu1) 하지만 460.32.03-0ubuntu0.20.04.1 패키지를 설치할 것입니다
                     의존: libnvidia-decode-460 (= 460.27.04-0ubuntu1) 하지만 %s 패키지를 설치하지 않을 것입니다
                     의존: libnvidia-encode-460 (= 460.27.04-0ubuntu1) 하지만 %s 패키지를 설치하지 않을 것입니다
                     추천: nvidia-settings 하지만 %s 패키지를 설치하지 않을 것입니다
                     추천: nvidia-prime (>= 0.8) 하지만 %s 패키지를 설치하지 않을 것입니다
                     추천: libnvidia-compute-460:i386 (= 460.27.04-0ubuntu1)
                     추천: libnvidia-decode-460:i386 (= 460.27.04-0ubuntu1)
                     추천: libnvidia-encode-460:i386 (= 460.27.04-0ubuntu1)
                     추천: libnvidia-ifr1-460:i386 (= 460.27.04-0ubuntu1)
                     추천: libnvidia-fbc1-460:i386 (= 460.27.04-0ubuntu1)
                     추천: libnvidia-gl-460:i386 (= 460.27.04-0ubuntu1)
E: 문제를 바로잡을 수 없습니다. 망가진 고정 패키지가 있습니다.
$
```

그래서 수동으로 의존하는 각 패키지를 설치하려고 했지만

```bash
$ sudo apt install nvidia-kernel-common-460 libnvidia-compute-460 ...
```

 실패했습니다.

## 해결

가장 확실한 방법으로 우분투를 재설치했습니다. 

