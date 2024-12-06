* Draft: 2021-01-26 (Tue)

# OpenCV 설치하기

## 개요

* Ubuntu 18.04에서 3가지 방식으로 설치한 경험을 요약했습니다. 

* 최종적으로 3번째 방법 Anaconda를 이용해서 설치했습니다.

## 요약

1. `apt`를 이용해서 설치
   * Dependencies 설치 후
   * OpenCV를 설치 --> 설치는 완료했으나, cv2모듈을 찾을 수 없었음
   * 자세한 내용은 [`apt`를 이용해서 OpenCV 설치](appendix/sudo_apt_install_python3-opencv.md)를 참고하세요.

```bash
$ sudo apt install -y python3-opencv
```

```bash
$ python -c "import cv2; print(cv2.__version__)"
  ...
ModuleNotFoundError: No module named 'cv2'
$
```

2. `pip`을 이용해서 설치

```bash
$ pip install opencv-python
```

* [opencv-python 4.5.1.48](https://pypi.org/project/opencv-python/)를 pip으로 설치할 수 있습니다.
* pre-built지만 CPU-only라서 속도가 GPU를 사용했을 때보다 느립니다.
* CPU-only와 GPU사용했을 때의 성능을 비교할 때 사용될 수 있습니다.

> **Unofficial** pre-built CPU-only OpenCV packages for Python.
>
> Check the manual build section if you wish to compile the bindings from source to enable additional modules such as CUDA.

3. OpenCV만 소스코드로 설치

* OpenCV를 설치 명령어 모음 [bash_scripts/install_opencv](bash_scripts/install_opencv)

* 설치 완료 전 Anaconda를 이용한 방법이 더 쉽다는 것을 알고 이 방법은 중단
   * 자세한 내용은 [OpenCV Dependencies를 `apt`로 & OpenCV를 소스코드로 설치하기](appendix/installing_opencv_dependencies_with_apt_and_opencv_from_source_code.md)를 참고하세요.

4. `Anaconda`를 이용해서 설치

* Anaconda 설치 완료 후, 아래 명령어로 opencv를 설치합니다.

```bash
$ conda install -c conda-forge -y opencv
```

`-c` 혹은 `--channel`옵션으로 `conda-forge`를 통해 설치하라고 지정했습니다. 전체 메세지는 [`conda-forge`를 통해 OpenCV 설치하기](appendix/conda_install_-c_conda-forge_-y_opencv-full_message.md)를 참고하세요.

* 설치 확인
  * 파이썬 환경: 파이썬에서 설치가 잘 되었는지 확인해봅니다.

```bash
$ python -c 'import cv2; print(cv2.__version__)'
4.2.0
$
```

파이썬에서 cv2 모듈을 import할 수 있어서 설치가 잘 되었음을 알 수 있습니다.

* `pkg-config` 명령어를 이용했을 땐 `opencv`를 찾을 수 없었습니다.

```bash
$ pkg-config --modversion opencv
Package opencv was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opencv' found
$
```

