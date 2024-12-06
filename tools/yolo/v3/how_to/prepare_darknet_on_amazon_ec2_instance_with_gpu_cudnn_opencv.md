* Draft: 2021-02-17 (Wed)

# How to Prepare Darknet on Amazon EC2 Instance (with GPU, cuDNN, and OpenCV)

## Create an Amazon EC2 instance


## Check the computing environment
run
```bashvices/en
Add new stuff by batch_git_push
last month
$ nvidia-smi
Wed Feb 17 04:23:29 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 450.80.02    Driver Version: 450.80.02    CUDA Version: 11.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  On   | 00000000:00:1E.0 Off |                    0 |
| N/A   29C    P0    24W / 300W |      0MiB / 16160MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
$ docker --version
Docker version 20.10.3, build 48d30b5
$ nvidia-docker --version
Docker version 20.10.3, build 48d30b5
$ cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
#define CUDNN_MAJOR 7
#define CUDNN_MINOR 5
#define CUDNN_PATCHLEVEL 1
--
#define CUDNN_VERSION (CUDNN_MAJOR * 1000 + CUDNN_MINOR * 100 + CUDNN_PATCHLEVEL)

#include "driver_types.h"
$ 
```
## Prepare the installation Bash scripts
On EC2

```bash
$ ls
Nvidia_Cloud_EULA.pdf  README  src  tools
$
```

```bash
$ cd
$ nano install_darknet-cpu_only
$ chmod +x install_darknet-cpu_only 
$ ./install_darknet-cpu_only 
```
It takes `1m1.571s` on EC2 p3.2xlarge.

`install_darknet-cpu_only`
```bash
$ git clone https://github.com/pjreddie/darknet.git
$ cd darknet/
$ wget https://pjreddie.com/media/files/yolov3.weights &
$ make
```
For details, refer to https://pjreddie.com/darknet/yolo/

## CPU Only

```bash
$ ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 20.962725 seconds.
dog: 100%
truck: 92%
bicycle: 99%
$
```

```bash
$ cp darknet darknet.cpu
```

## Makefile

```bash
$ cd darknet
$ nano Makefile
```
```makefile
GPU=0
CUDNN=0
OPENCV=0
OPENMP=0
DEBUG=0

ARCH= -gencode arch=compute_30,code=sm_30 \
      -gencode arch=compute_35,code=sm_35 \
  ...
```

## Enable GPU
```bash
$ nano Makefile
```

```makefile
GPU=1
```

```bash
$ make
  ...
$
```
It takes `0m47.825s` on EC2 p3.2xlarge.
### Verify
```bash
$ ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 10.958885 seconds.
dog: 100%
truck: 92%
bicycle: 99%
$
```
The accuracy remains identical, but darknet runs a lot faster.
Reducing time from 20.96 to 10.95 seconds.

```bash
$ cp darknet darknet.gpu
```

# Enable GPU and cuDNN
```bash
$ nano Makefile
```

```makefile
GPU=1
CUDNN=1
```

```bash
$ make
```

It takes `0m37.838s` on EC2 p3.2xlarge.

### Verify
```bash
$ ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 0.028911 seconds.
dog: 100%
truck: 92%
bicycle: 99%
$
```
The accuracy remains identical, but darknet runs a lot faster.
Reducing time from 10.95 to 0.02 seconds.

Unit seconds
```
CPU: 20.962725
GPU: 10.958885
GPU+cuDNN: 0.028911
```

```bash
$ cp darknet darknet.gpu_cudnn
```

## Running a video

According to [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/), the command to run a video is:

```bash
$ ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights <video file>
```

`OpenCV` is required to run a video. Darknet does not run without `OpenCV`. For example,

```bash
$ ./darknet.gpu_cudnn detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights ../videos/downtown.mp4
Demo needs OpenCV for webcam images.
$
```
The following part shows how to install/compile OpenCV which takes hours.

## Install OpenCV

```bash
$ nano install_opencv_in_linux
$ chmod +x install_opencv_in_linux 
$ ./install_opencv_in_linux
```
The next step is to compile OpenCV. This takes hours depending on machine.
```bash
$ nano install_opencv_contrib
$ chmod +x install_opencv_contrib
$ ./install_opencv_contrib
```

It takes 87 minutes on EC2 p3.2xlarge instance.
```bash
$ time cmake --build .
  ...
(wd now: ~/darknet/build)

real	87m5.041s
user	81m37.946s
sys	5m8.719s
$

## Enable GPU and cuDNN

```bash
$ nano Makefile
```

```makefile
GPU=1
CUDNN=1
OPENCV=1
```

```bash
$ make
```

```bash
$ cp darknet darknet.gpu_cudnn_opencv
```


## Enable X11 to use GUI
To display GUI, X11 is required. 
```bash
$ sudo apt install -y x11-apps
$ sudo apt install -y xorg openbox
```

### Verify
```bash
$ ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 0.028416 seconds.
dog: 100%
truck: 92%
bicycle: 99%
Gtk-Message: 08:01:41.182: Failed to load module "canberra-gtk-module"
Gtk-Message: 08:01:41.206: Failed to load module "canberra-gtk-module"
$
```
The accuracy remains identical, but darknet runs a lot faster.
Reducing time from 0.028911 to 0.028416 seconds.

```
(in seconds)
CPU: 20.962725
GPU: 10.958885
GPU+cuDNN: 0.028911
GPU+cuDNN+OpenCV: 0.028416
```
A pop-up window will show the detected result.

## Run a video
```bash
$ ./darknet.gpu_cudnn detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights ../videos/downtown.mp4
```

```bash
FPS:29.9
Objects:

car: 97%
car: 100%
car: 100%
car: 99%
truck: 97%
person: 99%
person: 98%
person: 96%
truck: 85%
truck: 94%
person: 94%
person: 90%
person: 90%
person: 90%
car: 86%
```
To save FPSs, 
