* Draft: 2021-02-03 (Wed)

# GPU=1로 다크넷 컴파일 하기

[opencv.md](opencv.md)를 참고해서 OpenCV를 설치합니다.

다크넷을 컴파일하기 위해

* 다운로드 되어 있는 `darknet` 디렉토리의 `Makefile`에서 

```bash
$ cd ~/darknet
$ nano Makefile
```

* `GPU`를 `0`에서 `1`로 변경한 후

```makefile
GPU=1
CUDNN=0
OPENCV=0
  ...
```

* 컴파일합니다.

```bash
$ make
  ...
usr/local/cuda/lib64 -lcuda -lcudart -lcublas -lcurand -lstdc++  libdarknet.a
$
```

에러가 발생해서 수정했습니다. 자세한 내용은 [$ make ... nvcc: not found](../troubleshoot/makefile_nvcc_not_found.md)을 참고하세요.

```bash
$ ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 0.859870 seconds.
dog: 100%
truck: 92%
bicycle: 99%
$
```

실행 후 결과를 확인해보면 `~/darknet`디렉토리에 `predictions.png`가 생성되었습니다.
