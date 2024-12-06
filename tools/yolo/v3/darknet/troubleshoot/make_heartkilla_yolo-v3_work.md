* Draft: 2021-02-02 (Tue)

# Git Repo [heartkilla](https://github.com/heartkilla)/[yolo-v3](https://github.com/heartkilla/yolo-v3)의 오류를 수정해서 동작하도록 만드는 과정

## 개요

* [../install/as_heartkilla_suggests.md](../install/as_heartkilla_suggests.md)의 부록입니다.
  * [heartkilla](https://github.com/heartkilla)/[yolo-v3](https://github.com/heartkilla/yolo-v3)의 내용을 그대로 따라하면 동작하지 않습니다.
  * 발생하는 오류를 수정해서 동작하도록 만드는 과정을 기록합니다.

## 문제 & 변경 사항

* `git clone`을 해도 텐서플로 버전 이슈로 동작하지 않습니다.
* Anaconda환경으로 변경했습니다.
* 이 과정에서 최신 텐서플로 버전이 아닌 예전 버전을 설치하도록 설정을 변경했습니다.

## 문제 해결 과정

```bash
$ git clone https://github.com/heartkilla/yolo-v3.git
```

`pip`명령어에서 쓰이는 `requirements.txt`를 아나콘다용으로 변경합니다.

```yaml
name: yolov3-heartkilla-tensorflow

dependencies:
  - python==3.6.6
  - pip
  - matplotlib
  - numpy
  - pip:
    - tensorflow
    - seaborn
    - pillow
    - opencv-python
```

가상환경을 생성합니다.

```bash
(base) $ conda env create -f conda_by_aimldl.yml 
Collecting package metadata (repodata.json): done
Solving environment: done
  ...
done
#
# To activate this environment, use
#
#     $ conda activate yolov3-heartkilla-tensorflow
#
# To deactivate an active environment, use
#
#     $ conda deactivate
(base) $
```

가상환경을 활성화 하고

```bash
(base) $ conda activate yolov3-heartkilla-tensorflow
(yolov3-heartkilla-tensorflow) $
```

설치된 텐서플로 버전을 확인합니다.

```bash
(yolov3-heartkilla-tensorflow) $ python -c 'import tensorflow as tf; print(tf.__version__)'
2021-02-02 10:12:28.742332: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
2.4.1
$
```

현재 Anaconda가 지원하는 최신 버전인 `2.4.1`이 설치되었습니다.

## Problem

Git clone 후 테스트를 위해 `load_weights.py`를 실행했을 때 에러가 발생했는데, 

```bash
(yolov3-gpu) $ python load_weights.py
2021-02-02 09:58:21.443575: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libnvinfer.so.6
2021-02-02 09:58:21.443805: W
  ...
Traceback (most recent call last):
  File "load_weights.py", line 117, in <module>
    main()
  File "load_weights.py", line 101, in main
    inputs = tf.placeholder(tf.float32, [1, 416, 416, 3])
AttributeError: module 'tensorflow' has no attribute 'placeholder'
(yolov3-gpu) $
```

새로 생성한 가상환경에서도 동일한 에러가 발생합니다.

```bash
(yolov3-heartkilla-tensorflow) $ python load_weights.py
  ...
AttributeError: module 'tensorflow' has no attribute 'placeholder'
(yolov3-heartkilla-tensorflow) $
```

## Hint

Google search: tensorflow version issue 'AttributeError: module 'tensorflow' has no attribute 'placeholder' anaconda

* [AttributeError: module 'tensorflow' has no attribute 'placeholder' #14](https://github.com/theislab/scgen/issues/14)

> The solution provided by the Tensorflow team on their website:
>
> ```python
> import tensorflow.compat.v1 as tf
> tf.disable_v2_behavior() 
> ```

```python
import tensorflow as tf
# aimldl
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
# aimldl
```

코드 변경 후 실행해도 기존 에러는 해결됐지만 다른 에러가 발생합니다.

```bash
(yolov3-heartkilla-tensorflow) $ python load_weights.py
  ...
AttributeError: module 'tensorflow' has no attribute 'variable_scope'
(yolov3-heartkilla-tensorflow) $
```

> **[M0hammadL](https://github.com/M0hammadL)** commented [on 25 Oct 2019](https://github.com/theislab/scgen/issues/14#issuecomment-546337391)
>
> The current and safest option is to use tf <2.0 for now. 
>
> **[mikeyEcology](https://github.com/mikeyEcology)** commented [on 11 Dec 2019](https://github.com/theislab/scgen/issues/14#issuecomment-564210550)
>
> I solved this and several other incompatibilities in my code by going back to tensorflow version 1:
> `pip install tensorflow==1.4`
>
> **[Djokovicxw](https://github.com/Djokovicxw)** commented [on 15 Dec 2019](https://github.com/theislab/scgen/issues/14#issuecomment-565780521)
>
> ```
> import tensorflow.compat.v1 as tf
> tf.disable_v2_behavior() 
> ```
>
> works.
> I am using Python 3.7 and tensorflow 2.0.
>
> **[yannis1962](https://github.com/yannis1962)** commented [on 25 Feb 2020](https://github.com/theislab/scgen/issues/14#issuecomment-590581988)
>
> I re-installed tensorflow==1.15.2 and it worked (otherwise rasa-nlu wouldn't work)
>
> **[moschjoon](https://github.com/moschjoon)** commented [on 12 Apr 2020](https://github.com/theislab/scgen/issues/14#issuecomment-612600647) • edited 
>
> just remove the current version of tensorflow (using command: 
>
> $ conda remove tensorflow
>
> , then install 1.15.0 using command: 
>
> $ conda install tensorflow=1.15.0
>
> it works

## Solution

저는 pip으로 tensorflow를 설치했기 때문에 `conda remove tensorflow`가 동작하지 않습니다. 대신

```bash
$ pip uninstall tensorflow
  ...
Proceed (y/n)? y
  Successfully uninstalled tensorflow-2.4.1
$
```

으로 제거한 후

```bash
(yolov3-heartkilla-tensorflow) $ conda install -y tensorflow=1.15.0
```

로 재설치했습니다.



를 변경합니다.

```yaml
name: yolov3-heartkilla-tensorflow-1_15

dependencies:
  - python==3.6.6
  - pip
  - matplotlib
  - numpy
  - tensorflow=1.15.0
  - pip:
    - seaborn
    - pillow
    - opencv-python
```

`python load_weights.py` 명령어를 확인해보면 에러가 사라졌습니다.

```bash
(yolov3-heartkilla-tensorflow) $ python load_weights.py
```

대신 소스코드에서 다른 에러가 발생했지만

```bash
  ...
FileNotFoundError: [Errno 2] No such file or directory: './weights/yolov3.weights'
(yolov3-heartkilla-tensorflow) $
```

`weights` 디렉토리에 웨이트 파일을 다운로드하면 동작합니다.

```bash
# yolov3
$ wget https://pjreddie.com/media/files/yolov3.weights -O weights/yolov3.weights

# yolov3-tiny
$ wget https://pjreddie.com/media/files/yolov3-tiny.weights -O weights/yolov3-tiny.weights
```

다시 한번 출력 메세지를 정리하면 다음과 같습니다.

```bash
(yolov3-heartkilla-tensorflow) $ python load_weights.py
  ...
ry is optimized with Intel(R) MKL-DNN to use the following CPU instructions in performance critical operations:  SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in non-MKL-DNN operations, rebuild TensorFlow with the appropriate compiler flags.
2021-02-02 11:20:26.955228: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 3699850000 Hz
2021-02-02 11:20:26.955758: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55d804fa8db0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2021-02-02 11:20:26.955771: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
OMP: Info #154: KMP_AFFINITY: Initial OS proc set respected: 0-11
OMP: Info #214: KMP_AFFINITY: decoding x2APIC ids.
OMP: Info #156: KMP_AFFINITY: 12 available OS procs
OMP: Info #157: KMP_AFFINITY: Uniform topology
OMP: Info #285: KMP_AFFINITY: topology layer "LL cache" is equivalent to "socket".
OMP: Info #285: KMP_AFFINITY: topology layer "L3 cache" is equivalent to "socket".
OMP: Info #285: KMP_AFFINITY: topology layer "L2 cache" is equivalent to "core".
OMP: Info #285: KMP_AFFINITY: topology layer "L1 cache" is equivalent to "core".
OMP: Info #191: KMP_AFFINITY: 1 socket x 6 cores/socket x 2 threads/core (6 total cores)
OMP: Info #216: KMP_AFFINITY: OS proc to physical thread map:
OMP: Info #171: KMP_AFFINITY: OS proc 0 maps to socket 0 core 0 thread 0 
OMP: Info #171: KMP_AFFINITY: OS proc 6 maps to socket 0 core 0 thread 1 
OMP: Info #171: KMP_AFFINITY: OS proc 1 maps to socket 0 core 1 thread 0 
OMP: Info #171: KMP_AFFINITY: OS proc 7 maps to socket 0 core 1 thread 1 
OMP: Info #171: KMP_AFFINITY: OS proc 2 maps to socket 0 core 2 thread 0 
OMP: Info #171: KMP_AFFINITY: OS proc 8 maps to socket 0 core 2 thread 1 
OMP: Info #171: KMP_AFFINITY: OS proc 3 maps to socket 0 core 3 thread 0 
OMP: Info #171: KMP_AFFINITY: OS proc 9 maps to socket 0 core 3 thread 1 
OMP: Info #171: KMP_AFFINITY: OS proc 4 maps to socket 0 core 4 thread 0 
OMP: Info #171: KMP_AFFINITY: OS proc 10 maps to socket 0 core 4 thread 1 
OMP: Info #171: KMP_AFFINITY: OS proc 5 maps to socket 0 core 5 thread 0 
OMP: Info #171: KMP_AFFINITY: OS proc 11 maps to socket 0 core 5 thread 1 
OMP: Info #252: KMP_AFFINITY: pid 5514 tid 5514 thread 0 bound to OS proc set 0
2021-02-02 11:20:26.959434: I tensorflow/core/common_runtime/process_util.cc:115] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.
Model has been saved successfully.
(yolov3-heartkilla-tensorflow) $
```

