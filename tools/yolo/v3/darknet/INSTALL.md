* Draft: 2021-01-25 (Mon)

# 다크넷 설치하기 (Installing Darknet) 

## 개요
* 두 개의 dependancies가 있지만, 설치하지 않아도 동작합니다.
  > Darknet is easy to install with only two optional dependancies:
  
  * [OpenCV](https://opencv.org/)
  * [CUDA](https://developer.nvidia.com/cuda-downloads)
  
## 설치 과정

### 다크넷 홈페이지의 설치 가이드

> Installing The Base System
> 
> First clone the Darknet git repository here. This can be accomplished by:
> 
> git clone https://github.com/pjreddie/darknet.git
> cd darknet
> make
>
> If you have any errors, try to fix them? If everything seems to have compiled correctly, try running it!
> ./darknet

### 설치 과정 

`$`는 `k8smaster@k8smaster-Alienware-Aurora-R7:~`를 생략한 표현입니다.

CUDA를 설치한 콘다 가상환경인 `tf2`를 활성화합니다.
```bash
(base) $ conda activate tf2
```

`tf2` 환경에서 다크넷 베이스 시스템을 설치합니다.
```bash
(tf2) $ git clone https://github.com/pjreddie/darknet.git
  ...
(tf2) $ cd darknet
(tf2) $ make 
```

컴파일이 성공적이면 `darknet` 실행파일이 생성됩니다. 

컴파일 전의 파일
```bash
$ ls
LICENSE       LICENSE.gen  LICENSE.meta  LICENSE.v1  README.md  data      include  scripts
LICENSE.fuck  LICENSE.gpl  LICENSE.mit   Makefile    cfg        examples  python   src
$
```

``` bash
$ ls
LICENSE       LICENSE.gpl   LICENSE.v1  backup   data      libdarknet.a   python   src
LICENSE.fuck  LICENSE.meta  Makefile    cfg      examples  libdarknet.so  results
LICENSE.gen   LICENSE.mit   README.md   darknet  include   obj            script
$
```

성공적인지 아래 명령어로 확인합니다.
```bash
$ ./darknet
```
아래와 같은 출력이 예상됩니다.
```bash
usage: ./darknet <function>
```

### OpenCV

### 문제

다크넷을 컴파일할 때 OpenCV이 없으면, 다크넷을 실행할 때 `Not compiled with OpenCV`라는 메세지가 출력됩니다.

```bash
$ cd ~/darknet
$ ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
data/dog.jpg: Predicted in 7056.965000 milli-seconds.
bicycle: 99%
dog: 100%
truck: 93%
Not compiled with OpenCV, saving to predictions.png instead
$
```

### 설치하기

(아나콘다가 설치되었고 darknet_with_opencv라는 가상환경이 만들어졌다고 가정)

#### Step 1. 먼저 OpenCV를 설치합니다.

```bash
$ conda activate darknet_with_opencv
$ conda install -c conda-forge -y opencv
$ python -c 'import cv2; print(cv2.__version__)'
$ pkg-config --modversion opencv
```

#### Step 2. 다크넷을 설치합니다.

```bash
$ git clone https://github.com/pjreddie/darknet
$ wget https://pjreddie.com/media/files/yolov3.weights
```

#### Step 3. 다크넷을 실행해서 확인해봅니다.

```bash
$ ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 18.021478 seconds.
dog: 100%
truck: 92%
bicycle: 99%
$
```

* `Not compiled with OpenCV, saving to predictions.png instead`라는 메세지가 나오지 않습니다.
* 그런데 `predictions.png`가 생성되었습니다.

```bash
$ ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights
Demo needs OpenCV for webcam images.
$
```

