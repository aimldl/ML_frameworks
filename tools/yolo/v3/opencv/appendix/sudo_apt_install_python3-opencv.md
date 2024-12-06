* Draft: 2021-01-26 (Tue)

# `apt`를 이용해서 OpenCV 설치

## 개요

* 우분투 18.04에 APT패키지  관리툴을 이용해서 설치하고자 합니다.

```bash
$ sudo apt update
$ sudo apt install python3-opencv
```

* 아래 글에 나오는 것처럼 설치하면 OpenCV를 찾지 못하는 문제가 발생합니다.

```bash
$ python -c "import cv2; print(cv2.__version__)"
  ...
ModuleNotFoundError: No module named 'cv2'
$
```

환경은

* `(base) k8smaster@k8smaster-Alienware-Aurora-R7:~$`
  * 아나콘다 가상환경
  * Alienware-Aurora-R7에 NVIDIA GTX 1080 GPU카드가 장착
  * GPU 동작을 위해 CUDA Toolkit 등은 설치가 완료되어 정상 동작 중

## 참고 문서

Google search: ubuntu 18.04 how to install opencv

* [How to Install OpenCV on Ubuntu 18.04](https://linuxize.com/post/how-to-install-opencv-on-ubuntu-18-04/), Linuxize, 2020-01-12

> **Install OpenCV from the Ubuntu Repository**
>
> 1. Refresh the packages index and install the OpenCV package by typing:
>
> ```bash
> $ sudo apt update
> $ sudo apt install python3-opencv
> ```
>
> The command above will install all packages necessary to run OpenCV.
>
> 2. To verify the installation, import the `cv2` module and print the OpenCV version:
>
> ```bash
> $ python3 -c "import cv2; print(cv2.__version__)"
> 3.2.0
> $
> ```

## 문제

### ModuleNotFoundError: No module named 'cv2'

설치 후에 cv2 패키지를 찾지 못 합니다.

```bash
$ sudo apt update
$ sudo apt install python3-opencv
$ python -c "import cv2; print(cv2.__version__)"
  ...
ModuleNotFoundError: No module named 'cv2'
$
```

재설치하면 이미 설치되었다고 합니다.

```bash
$ sudo apt install -y python3-opencv
[sudo] k8smaster의 암호: 
패키지 목록을 읽는 중입니다... 완료
의존성 트리를 만드는 중입니다       
상태 정보를 읽는 중입니다... 완료
패키지 python3-opencv는 이미 최신 버전입니다 (3.2.0+dfsg-4ubuntu0.1).
다음 패키지가 자동으로 설치되었지만 더 이상 필요하지 않습니다:
  libllvm9
Use 'sudo apt autoremove' to remove it.
0개 업그레이드, 0개 새로 설치, 0개 제거 및 0개 업그레이드 안 함.
$
```

### `No package 'opencv' found`

`pkg-config`명령어로 확인해도 `No package 'opencv' found`라고 나옵니다.

```bash
$ pkg-config --modversion opencv
```

```bash
Package opencv was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opencv' found
$
```

## 힌트

TODO: 일단 여기서 중단하고 다른 방법으로 설치를 진행해봅니다.