





## 새 컴퓨터에서 도커 컨테이너환경을 실행

`docker pull` 명령어도 도커 이미지를 다운로드 받습니다.

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

도커 환경을 실행합니다. 

```bash
$ docker run --gpus all -it aimldl/darknet:gpu_cudnn_opencv_version bash
root@228b2e12fee0:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@228b2e12fee0:/#
```

`darknet` 디렉토리로 이동합니다.

```bash
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

## 이미지로 다크넷의 성능을 테스트

우선 `GPU`와 `OPENCV`를 설정하고 

```bash
root@228b2e12fee0:/home/user/darknet# head -n 5 Makefile 
GPU=1
CUDNN=0
OPENCV=1
OPENMP=0
DEBUG=0
root@228b2e12fee0:/home/user/darknet#
```

다크넷의 성능을 테스트 합니다.

```bash
root@228b2e12fee0:/home/user/darknet# ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 0.052934 seconds.
dog: 100%
truck: 92%
bicycle: 99%
$
```

`cuDNN`을 추가해서 설정하고

```bash
root@228b2e12fee0:/home/user/darknet# head -n 5 Makefile 
GPU=1
CUDNN=1
OPENCV=1
OPENMP=0
DEBUG=0
root@228b2e12fee0:/home/user/darknet#
```

`darknet`을 컴파일 합니다.

 yolov3를 테스트합니다.



## 비디오로 다크넷 성능을 테스트

```bash
$ ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights <video file>
```



```bash
$ ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights kt_data/seoul.mp4 
```

동작하지 않습니다.

```bash
Demo needs OpenCV for webcam images.
$
```

`OpenCV`가 있는지 확인해보겠습니다.





### 실패한 명령어

```bash
$ asdf
  ...
Loading weights from yolov3.weights...Done!
Cannot load image "../etri_videos/seoul.mp4"
STB Reason: unknown image type
$
```



```bash
# ./darknet.gpu_opencv detector cfg/yolov3.cfg yolov3.weights ../etri_videos/seoul.mp4 

```

```bash
# ./darknet.gpu_opencv detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights ../etri_videos/seoul.mp4 
Demo needs OpenCV for webcam images.
#
```

> ## Real-Time Detection on a Webcam
>
> Running YOLO on test data isn't very interesting if you can't see the result. Instead of running it on a bunch of images let's run it on the input from a webcam!
>
> To run this demo you will need to compile [Darknet with CUDA and OpenCV](https://pjreddie.com/darknet/install/#cuda). Then run the command:
>
> ```
> ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights
> ```
>
> YOLO will display the current FPS and predicted classes as well as the image with bounding boxes drawn on top of it.
>
> You will need a webcam connected to the computer that OpenCV can connect to or it won't work. If you have multiple webcams connected and want to select which one to use you can pass the flag `-c <num>` to pick (OpenCV uses webcam `0` by default).
>
> You can also run it on a video file if OpenCV can read the video:
>
> ```
> ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights <video file>
> ```
>
> That's how we made the YouTube video above.
>
> Source: https://pjreddie.com/darknet/yolo/



[run_with_gui.md](../../../../how_to/run_with_gui.md)

```basj
$ xhost +local:docker
non-network local connections being added to access control list
$ docker run -it --gpus all -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:ro aimldl/darknet:gpu_cudnn_opencv_ver0.2 bash
# xclock
```



```bash
$ ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights ../etri_videos/seoul.mp4 > darknet-2021-02-15_mon.log
```

cuDNN을 컴파일해서

```bash
root@228b2e12fee0:/home/user/darknet# head -n 5 Makefile 
GPU=1
CUDNN=1
OPENCV=1
OPENMP=0
DEBUG=0
```

```bash
# make
#
```

```bash
root@041a6653113d:/home/user/darknet# ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights ../etri_videos/seoul.mp4 > darknet-2021-02-15_mon.log

...
Loading weights from yolov3.weights...Done!

(Demo:15787): dbind-WARNING **: 19:27:17.391: Couldn't connect to accessibility bus: Failed to connect to socket /tmp/dbus-CGk1tCxcEO: Connection refused
Gtk-Message: 19:27:17.410: Failed to load module "canberra-gtk-module"
Gtk-Message: 19:27:17.411: Failed to load module "canberra-gtk-module"
Floating point exception (core dumped)
$
```

