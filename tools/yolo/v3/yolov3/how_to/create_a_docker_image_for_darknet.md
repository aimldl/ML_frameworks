* Draft: 2021-02-03 (Wed)

# 다크넷용 도커 이미지 만드는 방법



### 베이스 도커 이미지 

도커 이미지입니다.

```bash
$ docker images
REPOSITORY           TAG                         IMAGE ID      CREATED      SIZE
nvcr.io/nvidia/cuda  11.2.0-runtime-ubuntu18.04  5b3bfc967c6d  2 weeks ago  2.01GB
$
```

도커 이미지에서 컨테이너를 실행합니다.

```bash
pkg-config: not found$ docker run -it nvcr.io/nvidia/cuda:11.2.0-runtime-ubuntu18.04 bash
root@0f849469a8df:/# 
```

### 필요한 기본 패키지 설치

에디터 `nano`를 설치합니다.

```bash
# apt update
  ...
# apt install -y nano git pkg-cfg
  ...
# 
```

docker python3 ubuntu



```bash
# which python
#
```

### OpenCV 설치

에디터 `nano`로 opencv 설치용 스크립트를 작성합니다.

```bash
# nano install_opencv_in_linux
```

[../bash_scripts/install_opencv_in_linux_without_sudo](../bash_scripts/install_opencv_in_linux_without_sudo)의 내용을 복사해서 저장해서 실행합니다. 설치에 관한 자세한 내용은 [../install/opencv.md](../install/opencv.md)를 참고하세요.

소스코드를 직접 컴파일하기 때문에 시간이 꽤 걸립니다.

```bash
# chmod +x install_opencv_in_linux 
# ./install_opencv_in_linux
  ...
-- Installing: /usr/local/bin/opencv_version
-- Set runtime path of "/usr/local/bin/opencv_version" to "/usr/local/lib"
#
```

지금까지 설치된 파일의 목록입니다.

```bash
# ls
build  install_opencv_in_linux  opencv-master  opencv.zip  opencv_contrib-master  opencv_contrib.zip
#
```

### Darknet 설치

* 다크넷은 오픈소스 인공신경망 프레임워크로 C언어와 CUDA로 구현되었습니다.
* CPU와 GPU 연산 모두 지원하고, 속도가 빠릅니다.
* 설치가 간단합니다.
  * 소스코드를 GitHub 저장소 [pjreddie /
    darknet](https://github.com/pjreddie/darknet)에서 다운로드 받아서 컴파일하면 됩니다.

#### CPU only일 경우

```bash
# git clone https://github.com/pjreddie/darknet
# cd darknet
# make
```

#### OpenCV와 GPU를 사용할 경우

소스를 다운로드 받고

```bash
# git clone https://github.com/pjreddie/darknet
# cd darknet
```

`pkg-config: not foundMakefile`을 텍스트 에디터로 열어서 

```bash
# nano Makefile
```

기본 옵션을 

```makefile
GPU=0
CUDNN=0
OPENCV=0
```

아래처럼 변경한 후

```makefile
GPU=1
CUDNN=0
OPENCV=1
```

`make`명령어로 컴파일합니다.

```bash
# make
```

참고로 디렉토리 위치는 `Makefile`이 있는 `darknet`디렉토리에서 `make`명령어를 실행해야 합니다.

컴파일해서 `darknet` 실행파일을 만드는 과정에서 다양한 에러가 발생할 수 있습니다. 에러를 제거하고 마지막까지 성공적으로 컴파일하는데 있어, 어려움을 겪는 경우가 많이 있습니다.

#### YOLOv3 웨이트 파일을 다운로드

```bash
# wget https://pjreddie.com/media/files/yolov3.weights
  ...
#
```



