

`Makefile`의 옵션을 변경합니다.

```makefile
GPU=0
CUDNN=0
OPENCV=0
```

을

```makefile
GPU=1
CUDNN=0
OPENCV=0
```

로 바꿉니다. 3가지 모두 1로 변경해야 하지만 하나씩 문제를 해결해서 마지막에 3개 모두 1로 변경해서 컴파일할 예정입니다.

```bash
root@f508e9cee903:/home/user/darknet# make
gcc -Iinclude/ -Isrc/ -DGPU -I/usr/local/cuda/include/ -Wall -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -fPIC -Ofast -DGPU -c ./src/gemm.c -o obj/gemm.o
  ...
nvcc  -gencode arch=compute_30,code=sm_30 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_50,code=[sm_50,compute_50] -gencode arch=compute_52,code=[sm_52,compute_52] -Iinclude/ -Isrc/ -DGPU -I/usr/local/cuda/include/ --compiler-options "-Wall -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -fPIC -Ofast -DGPU" -c ./src/convolutional_kernels.cu -o obj/convolutional_kernels.o
nvcc fatal   : Unsupported gpu architecture 'compute_30'
Makefile:92: recipe for target 'obj/convolutional_kernels.o' failed
make: *** [obj/convolutional_kernels.o] Error 1
$

```

문제해결은 https://github.com/aimldl/tools/blob/0d2388f849d61d6f5ad149de0aebc9c9ffd5140a/darknet/troubleshoot/makefile_nvcc_not_found.md

를 참고하세요.

`Makefile`의

```makefile
GPU=1
CUDNN=0
OPENCV=0
OPENMP=0
DEBUG=0

ARCH= -gencode arch=compute_30,code=sm_30 \
      -gencode arch=compute_35,code=sm_35 \
      -gencode arch=compute_50,code=[sm_50,compute_50] \
      -gencode arch=compute_52,code=[sm_52,compute_52]
```

를 

```makefile
GPU=1
CUDNN=0
OPENCV=0
OPENMP=0
DEBUG=0

#ARCH= -gencode arch=compute_30,code=sm_30 \
ARCH= -gencode arch=compute_35,code=sm_35 \
      -gencode arch=compute_50,code=[sm_50,compute_50] \
      -gencode arch=compute_52,code=[sm_52,compute_52]
```

로 변경합니다.

## Problem

도커 컨테이너 안에서는 보지 못 했던 에러가 발생합니다.

```bash
root@f508e9cee903:/home/user/darknet# ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
CUDA Error: CUDA driver version is insufficient for CUDA runtime version
darknet: ./src/cuda.c:36: check_error: Assertion `0' failed.
Aborted (core dumped)
root@f508e9cee903:/home/user/darknet#
```

버전 확인을 위해 `nvidia-smi`명령어를 실행했는데 보이지 않습니다.

```bash
root@f508e9cee903:/home/user/darknet# nvidia-smi
bash: nvidia-smi: command not found
root@f508e9cee903:/home/user/darknet# 
```

## Solution

아!  `docker run`을 할 때 `--gpus all`옵션이 필요합니다.

```bash
$ docker run -it --gpus all baseimage-darknet:latest bash
$
```

지금까지 한 것을 저장하기 위해서 `Ctrl+p+q`로 빠져나갑니다.

```bash
$ docker ps
CONTAINER ID  IMAGE              COMMAND  ...  NAMES
f508e9cee903  baseimage-darknet  "bash"   ...  vibrant_jang
$
```

컨테이너를 이미지로 저장합니다.

```bash
$ docker commit vibrant_jang baseimage-darknet:ver0.2
sha256:40b7c6a87c86c814302c3a8c5702917bd27dd5845ebcaa71aa74677d80b9173d
$
```

새로운 이미지가 생성되었음을 확인합니다.

```bash
$ docker images
REPOSITORY         TAG     IMAGE ID      CREATED         SIZE
baseimage-darknet  ver0.2  40b7c6a87c86  31 seconds ago  8.36GB
baseimage-darknet  latest  3d0a19184aa9  48 minutes ago  7.27GB
  ...
$
```

이미지에서 새로운 컨테이너를 생성합니다.

```bash
$ docker run -it --gpus all baseimage-darknet:ver0.2 bash
root@b865d9c1f5da:/# 
```

`nvidia-smi` 명령어를 실행해봅니다.

```bash
root@b865d9c1f5da:/# nvidia-smi
Tue Feb  9 10:09:48 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.32.03    Driver Version: 460.32.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 1080    On   | 00000000:01:00.0  On |                  N/A |
| 27%   44C    P0    41W / 180W |    305MiB /  8118MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX 1080    On   | 00000000:02:00.0 Off |                  N/A |
| 27%   27C    P8     5W / 180W |      2MiB /  8119MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+
root@b865d9c1f5da:/# 

```

`CUDA Error: CUDA driver version is insufficient for CUDA runtime version`이라는 에러가 발생했지만 옵션을 바꾸는 것 만으로 해결됐습니다.

```bash
root@b865d9c1f5da:/# cd /home/user/darknet/
root@b865d9c1f5da:/home/user/darknet# ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 0.237820 seconds.
dog: 100%
truck: 92%
bicycle: 99%
root@b865d9c1f5da:/home/user/darknet#
```

CPU only에서 15.46초 정도가 걸렸던 것이 `0.24`초로 줄었습니다.