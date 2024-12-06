* Draft: 2021-02-03 (Wed)

# GPU=1로 다크넷 컴파일 하기

[opencv.md](opencv.md)를 참고해서 OpenCV를 설치합니다.

컴파일할 때 문제가 발생해서

* [darknet_with_opencv_1.md](darknet_with_opencv_1.md)와
* [darknet_with_gpu_1.md](darknet_with_gpu_1.md)

문제해결을 한 다음, 두 옵션을 모두 켜서 컴파일했습니다.

* 다운로드 되어 있는 `darknet` 디렉토리의 `Makefile`에서 

```bash
$ cd ~/darknet
$ nano Makefile
```

* `OPENCV`를 `0`에서 `1`로,`GPU`를 `0`에서 `1`로 변경한 후

```makefile
GPU=1
CUDNN=0
OPENCV=1
  ...
```

* 컴파일합니다.

```bash
$ make
  ...
usr/local/cuda/lib64 -lcuda -lcudart -lcublas -lcurand -lstdc++  libdarknet.a
$
```

이미 문제가 해결된 상태에서 컴파일하므로 과정은 스무즈하게 진행됩니다.

```bash
$ ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 0.208754 seconds.
dog: 100%
truck: 92%
bicycle: 99%
$
```

실행 후 결과를 확인해보면 `~/darknet`디렉토리에 `predictions.png`가 생성되었습니다.

실행속도가 빨라졌음을 알 수 있습니다.

| 값       | GPU=0             | GPU=1            |
| -------- | ----------------- | ---------------- |
| OPENCV=0 | 15.382767 seconds | 0.859870 seconds |
| OPENCV=1 | 15.382767 seconds | 0.208754 seconds |

이에 더해 실행 후 잠깐 결과를 보여줍니다. 아주 빨리 지나가기 때문에 주의가 필요합니다.

<img src="/home/k8smaster/github/tools/darknet/install/images/darknet-detection-result-dog-with_opencv.png">

