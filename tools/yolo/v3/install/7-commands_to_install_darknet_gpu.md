$ ./install_docker_on_ubuntu 
$ ./install_nvidia_docker_on_ubuntu (double-check the name)

$ docker login

그런데 파일명이 다르네요. 

[cuDNN Library for Linux](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v7.4.2/prod/10.0_20181213/cudnn-10.0-linux-x64-v7.4.2.24.tgz)

를 클릭하니 동일한 파일인 `cudnn-10.0-linux-x64-v7.4.2.24.tgz`를 다운로드 받습니다.

$ docker pull nvidia/cuda:10.0-devel-ubuntu18.04
10.0-devel-ubuntu18.04: Pulling from nvidia/cuda
f22ccc0b8772: Pull complete 
3cf8fb62ba5f: Pull complete 
e80c964ece6a: Pull complete 
5d59c811e2af: Pull complete 
70a8c4b06826: Pull complete 
cd74940ce186: Pull complete 
3e2a00b42ba6: Pull complete 
ea92e080ed6c: Pull complete 
53ad5ada260f: Pull complete 
8342e80cbf2c: Pull complete 
Digest: sha256:473679cfce78d0f2ef9c21f46b7b80ac84029fb0aef4e2e616c217737a1d7e0a
Status: Downloaded newer image for nvidia/cuda:10.0-devel-ubuntu18.04
docker.io/nvidia/cuda:10.0-devel-ubuntu18.04
(base) aimldl@aimldl-home-desktop:~$ docker images
REPOSITORY          TAG                      IMAGE ID            CREATED             SIZE
nvidia/cuda         10.0-devel-ubuntu18.04   04156a673e4e        2 months ago        2.24GB
nvidia/cuda         11.0-base                2ec708416bb8        5 months ago        122MB
(base) aimldl@aimldl-home-desktop:~$ docker run -it --gpus all nvidia/cuda:10.0-devel-ubuntu18.04 bash
root@4f27c77943c0:/# 
root@4f27c77943c0:/# cat /usr/include/cudnn.h | egrep CUDNN_MAJOR -A 2

(base) aimldl@aimldl-home-desktop:~$ docker login
Authenticating with existing credentials...
WARNING! Your password will be stored unencrypted in /home/aimldl/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
(base) aimldl@aimldl-home-desktop:~$ docker pull nvidia/cuda:10.0-devel-ubuntu18.04
(base) aimldl@aimldl-home-desktop:~$ docker run -it --gpus all nvidia/cuda:10.0-devel-ubuntu18.04 bash
root@67315ceb667f:/# cd home/
root@67315ceb667f:/home# mkdir user
root@67315ceb667f:/home# cd user/
root@67315ceb667f:/home/user# mkdir downloads
root@67315ceb667f:/home/user# 

(base) aimldl@aimldl-home-desktop:~$ ls
AUTO_INSTALL  cuda-repo-ubuntu1804_10.0.130-1_amd64.deb  hello-kf-                             kubeflow_first_project                       yolov3    사진
Documents     cudnn-10.0-linux-x64-v7.4.2.24.tgz         install_atom-ubuntu_linux             libcudnn7-dev_7.4.2.24-1+cuda10.0_amd64.deb  공개      음악
Dropbox       darknet                                    install_docker_on_ubuntu              libcudnn7-doc_7.4.2.24-1+cuda10.0_amd64.deb  다운로드  템플릿
anaconda3     docker_with_yolov                          install_kubeflow                      libcudnn7_7.4.2.24-1+cuda10.0_amd64.deb      문서
bin           examples.desktop                           install_nvidia_docker_on_ubuntu       opencv_contrib-4.5.1                         바탕화면
build         github                                     kfctl_v1.0.1-0-gf3edb9b_linux.tar.gz  pipelines                                    비디오
(base) aimldl@aimldl-home-desktop:~$ docker cp cudnn-10.0-linux-x64-v7.4.2.24.tgz infallible_rhodes:/home/user/downloads
(base) aimldl@aimldl-home-desktop:~$ docker attach infallible_rhodes
root@67315ceb667f:/home/user/downloads# ls
cudnn-10.0-linux-x64-v7.4.2.24.tgz
root@67315ceb667f:/home/user/downloads# tar -xzvf cudnn-10.0-linux-x64-v7.4.2.24.tgz
cuda/include/cudnn.h
cuda/NVIDIA_SLA_cuDNN_Support.txt
cuda/lib64/libcudnn.so
cuda/lib64/libcudnn.so.7
cuda/lib64/libcudnn.so.7.4.2
cuda/lib64/libcudnn_static.a
root@67315ceb667f:/home/user/downloads# cp -P cuda/include/cudnn.h /usr/local/cuda-10.0/include
root@67315ceb667f:/home/user/downloads# cp -P cuda/lib64/libcudnn* /usr/local/cuda-10.0/lib64/
root@67315ceb667f:/home/user/downloads# chmod a+r /usr/local/cuda-10.0/lib64/libcudnn*
root@67315ceb667f:/home/user/downloads# cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
#define CUDNN_MAJOR 7
#define CUDNN_MINOR 4
#define CUDNN_PATCHLEVEL 2
--
#define CUDNN_VERSION (CUDNN_MAJOR * 1000 + CUDNN_MINOR * 100 + CUDNN_PATCHLEVEL)

#include "driver_types.h"
root@67315ceb667f:/home/user/downloads# 


# apt update
# apt install -y git

https://github.com/aimldl/tools/blob/main/yolo/v3/install/2-prepare_darknet_on_baseimage.md

CPU Only version
# git clone https://github.com/pjreddie/darknet.git
# cd darknet/
# make

yolov3.weights 파일을 복사
# read escape sequence
(base) aimldl@aimldl-home-desktop:~$ docker ps
CONTAINER ID        IMAGE                                COMMAND             CREATED             STATUS              PORTS               NAMES
67315ceb667f        nvidia/cuda:10.0-devel-ubuntu18.04   "bash"              7 minutes ago       Up 7 minutes                            infallible_rhodes
(base) aimldl@aimldl-home-desktop:~$ docker cp yolov3.weights infallible_rhodes:/home/user/darknet
(base) aimldl@aimldl-home-desktop:~$ docker attach infallible_rhodes
root@67315ceb667f:/home/user/darknet# 


# ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg

Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 20.008677 seconds.
dog: 100%
truck: 92%
bicycle: 99%
root@67315ceb667f:/home/user/darknet# 


# apt install -y nano


# nano Makefile  
GPU=1
CUDNN=0
OPENCV=0
OPENMP=0
DEBUG=0

# make
#

# # ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 0.178809 seconds.
dog: 100%
truck: 92%
bicycle: 99%
root@67315ceb667f:/home/user/darknet# 



https://github.com/aimldl/tools/blob/main/yolo/v3/install/5-prepare_cudnn_for_darknet.md


# nano Makefile  
GPU=1
CUDNN=1
OPENCV=0
OPENMP=0
DEBUG=0

# make
#

# ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
CUDA Error: out of memory
darknet: ./src/cuda.c:36: check_error: Assertion `0' failed.
Aborted (core dumped)
#

Google search: darknet cudnn CUDA Error: out of memory
* [run yolov3 with GPU:CUDA Error: out of memory #791](https://github.com/pjreddie/darknet/issues/791)
> I maked the darknet with "GPU=1,CUDNN=1,OPENCV=1" successfully，however，when I use the command "sudo ./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights data/dog.jpg
",it shows:
CUDA Error: out of memory
darknet: ./src/cuda.c:36: check_error: Assertion `0' failed.
But if I use the command"sudo ./darknet detector test cfg/coco.data cfg/yolov2.cfg yolov2.weights data/dog.jpg",it can detect targets successfully.
It seems that the problem is the yolov3.What can I do to solve the problem?


> hjchai commented on 18 May 2018
@dayn9t I think your gpu is low in memory. when Yolov3 fully loaded to gpu, it takes about 1600MB memory by default setting(416*416) on my computer, plus 300ish MiB from display and other applications, it is very like it will throw out OOM error. Try to run on a gpu with larger memory or reduce the width and height setting in your cfg file(Note: reducing the size might impact your detection results.).

> aryus96 commented on 16 Sep 2018 • 
edited 
I had the same problem with a GT740M with 4096Mo GDDR4 memory. Nvidia 384.130, Cuda 9, CUDNN, OpenCV 3.3.
>
>My solution to run Yolov3 perfectly was to : modify the cfg/yolov3.cfg :
>
>batch=1
>subdivisions=1
>width=416
>height=416

> SonaHarutyunyan commented on 11 Dec 2018
> Here https://github.com/AlexeyAB/darknet you can find this note:
> Note: if error Out of memory occurs then in .cfg-file you should increase subdivisions=16, 32 or 64


https://www.nvidia.com/en-sg/geforce/products/10series/geforce-gtx-1080/
1080
GPU Engine Specs:
2560NVIDIA CUDA® Cores
1607Base Clock (MHz)
1733Boost Clock (MHz)
Memory Specs:
10 GbpsMemory Speed
8 GB GDDR5XStandard Memory Config
256-bitMemory Interface Width
320

$ nano cfg/yolov3.cfg
[net]
# Testing
# batch=1
# subdivisions=1
# Training
batch=64


batch=32

Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 0.053748 seconds.
dog: 100%
truck: 92%
bicycle: 99%
(base) aimldl@aimldl-home-desktop:~/darknet$ 

It works just fine!

https://github.com/aimldl/tools/blob/main/yolo/v3/install/4-prepare_opencv_for_darknet.md


install_opencv_contrib_without_sudo


# nano Makefile 
GPU=1
CUDNN=0
OPENCV=1
OPENMP=0
DEBUG=0

https://github.com/aimldl/tools/blob/main/yolo/v3/bash_scripts/install_opencv_contrib_without_sudo#L10

root@67315ceb667f:/home/user/darknet# nano install_opencv_contrib_without_sudo
root@67315ceb667f:/home/user/darknet# chmod +x install_opencv_contrib_without_sudo 
root@67315ceb667f:/home/user/darknet# ./install_opencv_contrib_without_sudo 


https://github.com/aimldl/tools/blob/main/yolo/v3/bash_scripts/install_opencv_dependencies_without_sudo

# nano install_opencv_dependencies_without_sudo
# chmod +x install_opencv_dependencies_without_sudo
# ./install_opencv_dependencies_without_sudo


https://github.com/aimldl/tools/blob/main/yolo/v3/install/4-prepare_opencv_for_darknet.md

# python3 -c 'import cv2; print(cv2.__version__)'
# pkg-config --modversion op(base) k8smaster@k8smaster-Alienware-Aurora-R7:~$ docker export aimldl/darknet:gpu_cudnn_opencv_version > darknet_gpu_cudnn_opencv_version.tar
Error response from daemon: No such container: aimldl/darknet:gpu_cudnn_opencv_version
(base) k8smaster@k8smaster-Alienware-Aurora-R7:~$ docker save aimldl/darknet:gpu_cudnn_opencv_version > darknet_gpu_cudnn_opencv_version.tarencv



### 새 컴퓨터로 옮긴 다음 성능 확인



```bash
$ docker login
Authenticating with existing credentials...
WARNING! Your password will be stored unencrypted in /home/k8smaster/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
$ docker pull aimldl/darknet:gpu_cudnn_opencv_versiongpu_cudnn_opencv_version: Pulling from aimldl/darknet
f22ccc0b8772: Already exists 
3cf8fb62ba5f: Already exists 
e80c964ece6a: Already exists 
5d59c811e2af: Pull complete 
70a8c4b06826: Pull complete 
cd74940ce186: Pull complete 
3e2a00b42ba6: Pull complete 
ea92e080ed6c: Pull complete 
53ad5ada260f: Pull complete 
8342e80cbf2c: Pull complete 
42b4ccb63866: Pull complete 
Digest: sha256:a2addb2f0b8516e26b3a4ab06d3a56441203a646525ac2e5723bad51d54be3c6
Status: Downloaded newer image for aimldl/darknet:gpu_cudnn_opencv_version
docker.io/aimldl/darknet:gpu_cudnn_opencv_version
$ docker images
REPOSITORY      TAG                       IMAGE ID      CREATED            SIZE
aimldl/darknet  gpu_cudnn_opencv_version  4b159247967d  About an hour ago  6.51GB
  ...
$
```









새로 만든 도커 환경을 실행하고 `darknet` 디렉토리로 이동합니다.

```bash
$ docker run --gpus all -it aimldl/darknet:gpu_cudnn_opencv_version bash
root@228b2e12fee0:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@228b2e12fee0:/# cd home/user/
root@228b2e12fee0:/home/user# ls
darknet  downloads
root@228b2e12fee0:/home/user# cd darknet/
root@228b2e12fee0:/home/user/darknet# ls
LICENSE       cfg                                       obj
LICENSE.fuck  darknet                                   opencv-master
  ...
build         libdarknet.so                             yolov3.weights
root@228b2e12fee0:/home/user/darknet#
```



다크넷으로 yolov3를 테스트합니다.

```bash
$ docker images
REPOSITORY      TAG                       IMAGE ID      CREATED            SIZE
aimldl/darknet  gpu_cudnn_opencv_version  4b159247967d  About an hour ago  6.51GB
  ...
$root@228b2e12fee0:/home/user/darknet# ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 0.052934 seconds.
dog: 100%
truck: 92%
bicycle: 99%
$
```

