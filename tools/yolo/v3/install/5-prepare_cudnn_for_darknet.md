

## 신규 컨테이너 생성하기 

OpenCV가 컴파일 되고 있는 동안 같은 도커 이미지의 다른 컨테이너를 생성합니다.

먼저 다른 컨테이너가 생성된 것을 확인하기 위해서 현재 상태를 봅니다.

```bash
$ docker ps
CONTAINER ID  IMAGE                     COMMAND  CREATED            ...  NAMES
b865d9c1f5da  baseimage-darknet:ver0.2  "bash"   15 minutes ago     ...  quirky_engelbart
f508e9cee903  baseimage-darknet         "bash"   About an hour ago  ...  vibrant_jang
  ...
$
```

새로 컨테이너를 실행한 다음

```bash
$ docker run -it --gpus all baseimage-darknet:ver0.2 bash
root@1e6bdeec1030:/# 
```

확인해보면 제일 위에 `vibrant_bartik`라는 이름의 컨테이너가 새로 생성되었음을 알 수 있습니다.

```bash
$ docker ps
CONTAINER ID  IMAGE                     COMMAND  CREATED            ...  NAMES
1e6bdeec1030  baseimage-darknet:ver0.2  "bash"   55 seconds ago     ...  vibrant_bartik
b865d9c1f5da  baseimage-darknet:ver0.2  "bash"   15 minutes ago     ...  quirky_engelbart
f508e9cee903  baseimage-darknet         "bash"   About an hour ago  ...  vibrant_jang
  ...
$
```

> 컨테이너를 빠져나가고 다시 들어가려면
>
> `Ctrl+p+q`를 눌러서 빠져나갔다가, `docker attach` 명령어로 다시 들어갑니다.
>
> ```bash
> $ docker attach vibrant_bartik
> root@1e6bdeec1030:/# 
> ```

 현 상태를 확인해보면

```bash
root@1e6bdeec1030:/# cd /home/user/darknet/
root@1e6bdeec1030:/home/user/darknet# ls
LICENSE       LICENSE.meta  README.md  data          libdarknet.so    results
LICENSE.fuck  LICENSE.mit   backup     examples      obj              scripts
LICENSE.gen   LICENSE.v1    cfg        include       predictions.jpg  src
LICENSE.gpl   Makefile      darknet    libdarknet.a  python           yolov3.weights
root@1e6bdeec1030:/home/user/darknet# head -n 8 Makefile 
GPU=1
CUDNN=0
OPENCV=0
OPENMP=0
DEBUG=0

#ARCH= -gencode arch=compute_30,code=sm_30 \
ARCH= -gencode arch=compute_35,code=sm_35 \
root@1e6bdeec1030:/home/user/darknet# 
```

`Makefile`을 변경한 부분이 그대로 남아있음을 알 수 있습니다.

## CUDNN 설정 변경하기

### OpenCV와 CUDNN의 진행 및 계획

이제부터는 OpenCV와 독립적인 별도의 환경에서 `CUDNN`설정 변경을 해봅니다. 그런 다음 `OpenCV`의 컴파일이 끝나고 나서 `CUDNN`설정 변경을 그대로 적용하면 될 것입니다.

참고 삼아 OpenCV의 컴파일 상태를 확인해봅니다. 제 경우는 아직 31%네요. (문서로 기록하면서 진행하다 보니 조금 느립니다.)

```bash
# make
   ...
[ 31%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_intrin256.avx2.cpp.o
[ 31%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_intrin128.avx512_skx.cpp.o
[ 31%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_intrin256.avx512_skx.cpp.o
```

### CUDNN 설정 변경 시작하기

이제 본격적으로 시작해봅니다.

`darknet` 디렉토리의 `Makefile`에서 

```makefile
GPU=1
CUDNN=0
OPENCV=0
```

을

```makefile
GPU=1
CUDNN=1
OPENCV=0
```

으로 변경합니다.

```bash
root@1e6bdeec1030:/home/user/darknet# nano Makefile 
root@1e6bdeec1030:/home/user/darknet#
```

컴파일할 경우 에러가 발생합니다.

### Problem

```bash
root@1e6bdeec1030:/home/user/darknet# make
gcc -Iinclude/ -Isrc/ -DGPU -I/usr/local/cuda/include/ -DCUDNN  -Wall -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -fPIC -Ofast -DGPU -DCUDNN -c ./src/gemm.c -o obj/gemm.o
  ...
./src/convolutional_layer.c:153:13: error: 'CUDNN_CONVOLUTION_FWD_SPECIFY_WORKSPACE_LIMIT' undeclared (first use in this function); dCompile Darknet with CUDNNid you mean 'CUDNN_CONVOLUTION_FWD_ALGO_DIRECT'?
             CUDNN_CONVOLUTION_FWD_SPECIFY_WORKSPACE_LIMIT,
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             CUDNN_CONVOLUTION_FWD_ALGO_DIRECT
compilation terminated due to -Wfatal-errors.
Makefile:89: recipe for target 'obj/convolutional_layer.o' failed
make: *** [obj/convolutional_layer.o] Error 1
root@1e6bdeec1030:/home/user/darknet# 
```

### Hint

#### CUDA 설치를 확인

CUDA 설치는 두 개의 명령어 중 하나만으로도 가능합니다.

```bash
root@1e6bdeec1030:/home/user/darknet# nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2020 NVIDIA Corporation
Built on Mon_Nov_30_19:08:53_PST_2020
Cuda compilation tools, release 11.2, V11.2.67
Build cuda_11.2.r11.2/compiler.29373293_0
root@1e6bdeec1030:/home/user/darknet#
```

```bash
root@1e6bdeec1030:/home/user/darknet# nvidia-smi
Tue Feb  9 10:43:04 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.32.03    Driver Version: 460.32.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 1080    On   | 00000000:01:00.0  On |                  N/A |
| 28%   37C    P8    11W /root@1e6bdeec1030:/home/user/darknet# nvidia-smi
Tue Feb  9 10:43:04 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.32.03    Driver Version: 460.32.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|     합니다.    Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 1080    On   | 00000000:01:00.0  On |                  N/A |
| 28%   37C    P8    11W / 180W |    289MiB /  8118MiB |     14%      Default |
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
root@1e6bdeec1030:/home/user/darknet# 
 180W |    289MiB /  8118MiB |     14%      Default |
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
root@1e6bdeec1030:/home/user/darknet# 
```

> 주의: 도커 컨테이너를 실행할 때 `--gpus all `옵션이 없을 경우, 다음 같은 에러가 발생합니다. 꼭 `--gpus all ` 옵션을 사용하세요.
>
> ```bash
> # nvcc --version
> bash: nvcc: command not found
> # nvidia-smi
> bash: nvidia-smi: command not found
> #
> ```
>

#### cuDNN 설치를 확인

NVIDIA 드라이버, CUDA 및 cuDNN이 설치되어야 하는데, 앞에서 드라이버와 CUDA가 설치되었음이 확인되었습니다. 

#### Problem

그런데 

```bash
root@1e6bdeec1030:/home/user/darknet# cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
cat: /usr/local/cuda/include/cudnn.h: No such file or directory
root@1e6bdeec1030:/home/user/darknet#
```

cuDNN 설치가 안 되었나봅니다.

#### Action

```bash
export PATH=/usr/local/cuda/bin:/$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```

의 `PATH` 및 `LD_LIBRARY_PATH`정보를 임시로 업데이트 해보겠습니다.

```bash
root@1e6bdeec1030:/home/user/darknet# export PATH=/usr/local/cuda/bin:/$PATH
root@1e6bdeec1030:/home/user/darknet#export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
root@1e6bdeec1030:/home/user/darknet#

```

> 주의: `export LD_LIBRARY_PATH=/usr/local/cuda-11.0/lib64:$LD_LIBRARY_PATH`와 같이 버전 명이 명시된 경우에 CUDA 버전이 맞지 않으면 찾지 못하는 경우가 있습니다.  가령 `/usr/local/cuda` 디렉토리는 심볼릭 링크로 현재 설치된 버전을 가리킵니다.
>
> ```bash
> # cd /usr/local
> # ll cuda
> lrwxrwxrwx 1 root root 9 Jan 13 01:50 cuda -> cuda-11.2/
> # ls
> nvToolsExt.h  nvToolsExtCuda.h  nvToolsExtCudaRt.h  nvToolsExtOpenCL.h  nvToolsExtSync.h  nvtx3
> #
> ```
>
> 위의 경우는 현재 설치된 버전이 11.2인데 11.0의 디렉토리를 `LD_LIBRARY_PATH`로 지정하고 있으니 문제입니다.
>
> 나는 업데이트 했는데, 동작하지 않는 "논리적인 오류"인 셈이죠. 찾기 힘든 오류가 될 수 있으므로 주의합니다.

`/usr/local/cuda/bin/`에는 다음과 같은 파일이 있습니다.

```bash
root@1e6bdeec1030:/home/user/darknet# cd /usr/local/cuda/bin/
root@1e6bdeec1030:/usr/local/cuda/bin# ls
bin2c              cu++filt        cuda-memcheck  fatbinary     nvdisasm  nvprune
compute-sanitizer  cuda-gdb        cudafe++       nvcc          nvlink    ptxas
crt                cuda-gdbserver  cuobjdump      nvcc.profile  nvprof
root@1e6bdeec1030:/usr/local/cuda/bin# 
```

`/usr/local/cuda/lib64` 에는 다음과 같은 파일이 있습니다.

```bash
root@1e6bdeec1030:/usr/local/cuda/bin# cd /usr/local/cuda/lib64
root@1e6bdeec1030:/usr/local/cuda/lib64# ls
libOpenCL.so                  libcurand_static.a          libnppim.so.11.2.1.68
libOpenCL.so.1                libcusolver.so              libnppim_static.a
libOpenCL.so.1.0              libcusolver.so.11           libnppist.so
libOpenCL.so.1.0.0            libcusolver.so.11.0.2.68    libnppist.so.11
libaccinj64.so                libcusolverMg.so            libnppist.so.11.2.1.68
libaccinj64.so.11.2           libcusolverMg.so.11         libnppist_static.a
libaccinj64.so.11.2.67        libcusolverMg.so.11.0.2.68  libnppisu.so
libcublas.so                  libcusolver_static.a        libnppisu.so.11
libcublas.so.11               libcusparse.so              libnppisu.so.11.2.1.68
libcublas.so.11.3.1.68        libcusparse.so.11           libnppisu_static.a
libcublasLt.so                libcusparse.so.11.3.1.68    libnppitc.so
libcublasLt.so.11             libcusparse_static.a        libnppitc.so.11
libcublasLt.so.11.3.1.68      liblapack_static.a          libnppitc.so.11.2.1.68
libcublasLt_static.a          libmetis_static.a           libnppitc_static.a
libcublas_static.a            libnppc.so                  libnpps.so
libcudadevrt.a                libnppc.so.11               libnpps.so.11
libcudart.so                  libnppc.so.11.2.1.68        libnpps.so.11.2.1.68
libcudart.so.11.0             libnppc_static.a            libnpps_static.a
libcudart.so.11.2.72          libnppial.so                libnvToolsExt.so
libcudart_static.a            libnppial.so.11             libnvToolsExt.so.1
libcufft.so                   libnppial.so.11.2.1.68      libnvToolsExt.so.1.0.0
libcufft.so.10                libnppial_static.a          libnvblas.socat: /usr/local/cuda/include/cudnn.h: No such file or directory
libcufft.so.10.4.0.72         libnppicc.so                libnvblas.so.11
libcufft_static.a             libnppicc.so.11             libnvblas.so.11.3.1.68
libcufft_static_nocallback.a  libnppicc.so.11.2.1.68      libnvjpeg.so
libcufftw.so                  libnppicc_static.a          libnvjpeg.so.11
libcufftw.so.10               libnppidei.so               libnvjpeg.so.11.3.1.68
libcufftw.so.10.4.0.72        libnppidei.so.11            libnvjpeg_static.a
libcufftw_static.a            libnppidei.so.11.2.1.68     libnvperf_host.so
libcuinj64.so                 libnppidei_static.a         libnvperf_host_static.a
libcuinj64.so.11.2            libnppif.so                 libnvperf_target.so
libcuinj64.so.11.2.67         libnppif.so.11              libnvptxcompiler_static.a
libculibos.a                  libnppif.so.11.2.1.68       libnvrtc-builtins.so
libcupti.so                   libnppif_static.a           libnvrtc-builtins.so.11.2
libcupti.so.11.2              libnppig.so                 libnvrtc-builtins.so.11.2.67
libcupti.so.2020.3.0          libnppig.so.11              libnvrtc.so
libcupti_static.a             libnppig.so.11.2.1.68       libnvrtc.so.11.2
libcurand.so                  libnppig_static.a           libnvrtc.so.11.2.67
libcurand.so.10               libnppim.so              cat: /usr/local/cuda/include/cudnn.h: No such file or directory
root@1e6bdeec1030:/usr/local/cuda/lib64# 
   nvrtc-prev
libcurand.so.10.2.3.68        libnppim.so.11              stubs
root@1e6bdeec1030:/usr/local/cuda/lib64# 
```

#### Result

다시 확인을 해봤지만

```bash
root@1e6bdeec1030:/home/user/darknet# cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
cat: /usr/local/cuda/include/cudnn.h: No such file or directory
root@1e6bdeec1030:/usr/local/cuda/lib64# 
```

 위의 적용한 것으로 문제해결이 되지 않았습니다.

#### Hint

Google search: cat: /usr/local/cuda/include/cudnn.h: No such file or directory

* [How to verify CuDNN installation?](https://stackoverflow.com/questions/31326015/how-to-verify-cudnn-installation)

> I have searched many places but ALL I get is HOW to install it, not how to verify that it is installed. I can verify my NVIDIA driver is installed, and that CUDA is installed, but I don't know how to verify CuDNN is installed.
>
> Installing CuDNN just involves placing the files in the CUDA directory. If you have specified the routes and the CuDNN option correctly while installing caffe it will be compiled with CuDNN.
>
> Is there a way to find if cuDNN is installed without using Caffe. Something like the examples you get with CUDA? – gokul_uf Feb 28 '16 at 18:41
>
> @gokul_uf you can use the following (assuming you've symlinked /usr/local/cuda to /usr/local/cuda-#.#): 
>
> ```bash
> $ cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2 
> ```
>
> – matt Oct 25 '17 at 3:11
>
> @Boooooooooms He's simply taking the contents of a "header file" for the programming language C, and using the program "grep" to read out a specific variable for us – Greg Hilston Jun 15 '19 at 6:10

> The installation of CuDNN is just copying some files. Hence to check if CuDNN is installed (and which version you have), you only need to check those files.
>



```bash
$ docker ps
CONTAINER ID  IMAGE                     COMMAND  ...  NAMES
1e6bdeec1030  baseimage-darknet:ver0.2  "bash"   ...  vibrant_bartik
b865d9c1f5da  baseimage-darknet:ver0.2  "bash"   ...  quirky_engelbart
  ...
$ docker export 1e6bdeec1030 > baseimage-darknet_ver0_4.tar
```



```bash
$ docker commit 1e6bdeec1030 baseimage-darknet:ver0.4
sha256:3a48bd8567fdb44ad550a89782db9deb3db7a602c06516432adf03d1078826e8
$ docker images
REPOSITORY         TAG     IMAGE ID      CREATED         SIZE
baseimage-darknet  ver0.4  3a48bd8567fd  32 seconds ago  8.36GB
baseimage-darknet  ver0.3  9ed3aa90a41c  26 minutes ago  10.2GB
baseimage-darknet  ver0.2  40b7c6a87c86  3 hours ago     8.36GB
  ...
$
```

