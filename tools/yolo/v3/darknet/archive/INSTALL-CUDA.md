

[Toward a Containerized Nvidia CUDA, TensorFlow and OpenCV](https://www.datamachines.io/blog/toward-a-containerized-nvidia-cuda-tensorflow-and-opencv)

* Dockerfile
* [datamachines/cuda_tensorflow_opencv](datamachines/cuda_tensorflow_opencv)

Tag in the bottom

10.2_2.3.1_4.5.0-20201204

```bash
$ sudo docker pull datamachines/cuda_tensorflow_opencv:10.2_2.3.1_4.5.0-20201204
$
```

```bash
[sudo] k8smaster의 암호: 
10.2_2.3.1_4.5.0-20201204: Pulling from datamachines/cuda_tensorflow_opencv
171857c49d0f: Pull complete 
419640447d26: Pull complete 
61e52f862619: Pull complete 
c118dad7e37a: Pull complete 
29c091e4be16: Pull complete 
d85c81a4428d: Pull complete 
e6ba6b94dd40: Pull complete 
1f77d844ce7b: Pull complete 
2aaf2e015c84: Pull complete 
1dfb7b1bfd8d: Pull complete 
f032c3eb3f17: Pull complete 
39e90a291a61: Pull complete 
6045f1534700: Pull complete 
33ebfe690d9b: Pull complete 
1ff1008dbb4d: Pull complete 
6d1a36e6bda6: Pull complete 
56cf6971baaf: Pull complete 
3dfe87fa5f8e: Pull complete 
62b6e6a80ac0: Pull complete 
4d9228d57bba: Pull complete 
8c62cf8dd659: Pull complete 
e04cab1db723: Pull complete 
a72a7157f273: Pull complete 
ece753e6ce93: Pull complete 
0c899f550f90: Pull complete 
5fc24f5831bd: Pull complete 
9bdc3b48d36f: Pull complete 
c2c0de5b4cbb: Pull complete 
715cdba36870: Pull complete 
Digest: sha256:038f5c1201eef95a30a1e3fbf089949762fac9cb7696a9bd4f405016fce7ac74
Status: Downloaded newer image for datamachines/cuda_tensorflow_opencv:10.2_2.3.1_4.5.0-20201204
docker.io/datamachines/cuda_tensorflow_opencv:10.2_2.3.1_4.5.0-20201204
$
```

```bash
$ sudo docker images
REPOSITORY                            TAG                          IMAGE ID            CREATED             SIZE
<none>                                <none>                       67532306e1b6        41 minutes ago      4.23GB
nvcr.io/nvidia/cuda                   11.2.0-runtime-ubuntu18.04   5b3bfc967c6d        2 weeks ago         2.01GB
datamachines/cuda_tensorflow_opencv   10.2_2.3.1_4.5.0-20201204    88ee926b4281        7 weeks ago         8.32GB
$
```



```bash
$ sudo docker run -it 88ee926b4281 bash
root@81aae2fef9ac:/dmc# 
```



```bash
root@81aae2fef9ac:/dmc# nvidia-smi
bash: nvidia-smi: command not found
root@81aae2fef9ac:/dmc#

# sudo apt install -y nano 
```

Makefile

```bash
GPU=1
CUDNN=1
OPENCV=1
OPENMP=1
DEBUG=0

```

```bash
# make
mkdir -p obj
mkdir -p backup
mkdir -p results
gcc -Iinclude/ -Isrc/ -DOPENCV `pkg-config --cflags opencv`  -DGPU -I/usr/local/cuda/include/ -DCUDNN  -Wall -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -fPIC -fopenmp -Ofast -DOPENCV -DGPU -DCUDNN -c ./src/gemm.c -o obj/gemm.o
Package opencv was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opencv' found
In file included from ./src/utils.h:5:0,
                 from ./src/gemm.c:2:
include/darknet.h:16:14: fatal error: cudnn.h: No such file or directory
     #include "cudnn.h"
              ^~~~~~~~~
compilation terminated.
Makefile:89: recipe for target 'obj/gemm.o' failed
make: *** [obj/gemm.o] Error 1
root@81aae2fef9ac:/dmc/darknet# 
```

```makefile
GPU=0
CUDNN=0
OPENCV=0
OPENMP=0
DEBUG=0
```



$ sudo docker cp yolov3.weights trusting_rosalind:/dmc/darknet 

$ sudo docker attach trusting_rosalind

* [DockerFile with Nvidia GPU support for TensorFlow and OpenCV](https://github.com/datamachines/cuda_tensorflow_opencv)

root@81aae2fef9ac:/dmc/darknet# ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg

  ...

Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 15.533322 seconds.
dog: 100%
truck: 92%
bicycle: 99%