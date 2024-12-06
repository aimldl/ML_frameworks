* Draft: 2021-01-08 (Fri)

# Could not load dynamic library 'libcudart.so.10.1'

[hands-on/1-test-tfrecord.md](../hands-on/1-test-tfrecord.md)의 `test-tfrecord.py`를 실행했을 때 에러가 발생했습니다. 

최신 CUDA 버전을 설치했지만, 텐서플로는 예전 버전인 10.1을 요구합니다. 이런 버전 이슈로 코드가 동작하지 않은 것입니다.

일차적인 해결책으로 심볼릭링크를 만들어서 최신 버전인 `libcudart.so.11.0`를  `libcudart.so.10.1`에 연결해서 파일이 있는 것처럼 인식해줬습니다. 다행이 backward compatibility가 적용되서 코드가 작동은 합니다. 

아래의 명령어를 실행해서 해결했습니다. 자세한 것은 Solution1에 있습니다.

```bash
$ sudo ln -s /usr/local/cuda-11.2/targets/x86_64-linux/lib/libcudart.so.11.0 /usr/lib/x86_64-linux-gnu/libcudart.so.10.1
```

TODO: CUDA 버전을 낮추는 것을 고려해야 합니다. 제일 밑의 Considerdation 참고.

### 소스 코드

```python
# test-tfrecord.py
import tensorflow as tf

with tf.io.TFRecordWriter('test.tfrecord') as w:# test-tfrecord.py
import tensorflow as tf

with tf.io.TFRecordWriter('test.tfrecord') as w:
    w.write(b'First record')
    w.write(b'Second record')
    
for record in tf.data.TFRecordDataset('test.tfrecord'):
    print(record)
    w.write(b'First record')
    w.write(b'Second record')
    
for record in tf.data.TFRecordDataset('test.tfrecord'):
    print(record)
```

```bash
~/github/projects/automl/hands-on$ python3 test-tfrecord.py
```

## 문제

발생한 에러 메세지입니다. 

* `libcudart.so.10.1`가 없어서 문제가 생겼습니다.
* NVIDIA CUDA Library가 설치 되어 있지 않아서 발생하는 문제로 예상됩니다.

```bash
2021-01-08 15:48:31.553710: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcudart.so.10.1'; dlerror: libcudart.so.10.1: cannot open shared object file: No such file or directory
2021-01-08 15:48:31.553732: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
2021-01-08 15:48:32.600869: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcuda.so.1
2021-01-08 15:48:32.658486: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:982] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-01-08 15:48:32.658904: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1716] Found device 0 with properties: 
pciBusID: 0000:01:00.0 name: GeForce GTX 1080 computeCapability: 6.1
coreClock: 1.7335GHz coreCount: 20 deviceMemorySize: 7.93GiB deviceMemoryBandwidth: 298.32GiB/s
2021-01-08 15:48:32.658961: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:982] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-01-08 15:48:32.659567: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1716] Found device 1 with properties: 
pciBusID: 0000:02:00.0 name: GeForce GTX 1080 computeCapability: 6.1
coreClock: 1.7335GHz coreCount: 20 deviceMemorySize: 7.93GiB deviceMemoryBandwidth: 298.32GiB/s
2021-01-08 15:48:32.659634: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcudart.so.10.1'; dlerror: libcudart.so.10.1: cannot open shared object file: No such file or directory
2021-01-08 15:48:32.659692: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcublas.so.10'; dlerror: libcublas.so.10: cannot open shared object file: No such file or directory
2021-01-08 15:48:32.659736: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcufft.so.10'; dlerror: libcufft.so.10: cannot open shared object file: No such file or directory
2021-01-08 15:48:32.659776: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcurand.so.10'; dlerror: libcurand.so.10: cannot open shared object file: No such file or directory
2021-01-08 15:48:32.659816: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcusolver.so.10'; dlerror: libcusolver.so.10: cannot open shared object file: No such file or directory
2021-01-08 15:48:32.659864: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcusparse.so.10'; dlerror: libcusparse.so.10: cannot open shared object file: No such file or directory
2021-01-08 15:48:32.659910: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcudnn.so.7'; dlerror: libcudnn.so.7: cannot open shared object file: No such file or directory
2021-01-08 15:48:32.659918: W tensorflow/core/common_runtime/gpu/gpu_device.cc:1753] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devicelibcudart.so.10.1s...
2021-01-08 15:48:32.660119: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2021-01-08 15:48:32.664356: I tensorflow/core/platform/profile_utils/cpu_utils.cc:104] CPU Frequency: 3699850000 Hz
2021-01-08 15:48:32.664622: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5a12bb0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2021-01-08 15:48:32.664635: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2021-01-08 15:48:32.665535: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1257] Device interconnect StreamExecutor with strength 1 edge matrix:
2021-01-08 15:48:32.665546: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1263]      
tf.Tensor(b'First record', shape=(), dtype=string)
tf.Tensor(b'Second record', shape=(), dtype=string)
$
```

## 힌트1

Google search: `Could not load dynamic library 'libcudart.so.10.1'; dlerror: libcudart.so.10.1: cannot open shared object file: No such file or directory`

* [tensorflow-gpu: Could not load dynamic library 'libcudart.so.10.1' #39132](https://github.com/tensorflow/tensorflow/issues/39132)

> ```python
> import tensorflow as tf
> print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
> ```



`import tensorflow as tf`를 했을 때 경고 메세지가 나옵니다. NVIDIA CUDA 라이브러리 문제인 것이 강력히 의심됩니다.

```bash
$ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
2021-01-08 15:53:41.760649: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcudart.so.10.1'; dlerror: libcudart.so.10.1: cannot open shared object file: No such file or directory
2021-01-08 15:53:41.760670: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
>>> 
```

NVIDIA의 그래픽카드 드라이버, CUDA toolkit, cuDNN를 설치합니다.

* [nvidia_graphics_card_driver_automatically-ubuntu20_04.md](https://github.com/aimldl/environments/blob/master/gpgpu/install/nvidia_graphics_card_driver_automatically-ubuntu20_04.md)
* [nvidia_cuda_toolkit-ubuntu20_04.md](https://github.com/aimldl/environments/blob/master/gpgpu/install/nvidia_cuda_toolkit-ubuntu20_04.md)

* [nvidia_cudnn-ubuntu20_04.md](https://github.com/aimldl/environments/blob/master/gpgpu/install/nvidia_cudnn-ubuntu20_04.md)

```bash
$ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
2021-01-08 19:00:05.001561: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcudart.so.10.1'; dlerror: libcudart.so.10.1: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /usr/local/cuda-11.2/lib64
2021-01-08 19:00:05.001653: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
>>> 
$
```

설치 후에도 동일한 에러가 발생합니다. 

```bash
$ echo $LD_LIBRARY_PATH
/usr/local/cuda-11.2/lib64
$
```

라는 디렉토리가 없다는 메세지 입니다. 확인해봅니다.

```bash
$ ls /usr/local/cuda-11.2/
DOCS      README  compute-sanitizer  include  libnvvp           nvml  nvvm-prev  share  targets
EULA.txt  bin     extras             lib64    nsightee_plugins  nvvm  samples    src    tools
$
```

`/usr/local/cuda-11.2/lib64`는 존재합니다. 파일이 있는지 확인해봅니다.

```bash
$ sudo ls /usr/local/cuda-11.2/lib64/libcudart.so.10.1
ls: '/usr/local/cuda-11.2/lib64/libcudart.so.10.1'에 접근할 수 없습니다: 그런 파일이나 디렉터리가 없습니다
$
```

실제로 이런 파일이 없다고 나오네요. 다른 파일들을 확인해보면 CUDA에서 필요한 무엇인가 설치가 안 됐음을 알 수 있습니다.

```bash
$ ls /usr/local/cuda-11.2/lib64/
libOpenCL.so                  libcurand_static.a          libnppim.so.11.2.1.68
  ...
libcurand.so.10.2.3.68        libnppim.so.11              stubs
$
```

## 힌트 2

Google search: libcudart.so.10.1

[Could not load dynamic library 'libcudart.so.10.1'; dlerror: libcudart.so.10.1: cannot open shared object file: No such file or directory #38578](https://github.com/tensorflow/tensorflow/issues/38578)

> [@domindominik](https://github.com/domindominik),
> As the error says Could not load dynamic library 'libcudart.so.10.1, you may have to install CUDA 10.1.
> Similar issue [#34759](https://github.com/tensorflow/tensorflow/issues/34759).
>
> [@gadagashwini](https://github.com/gadagashwini) how to fix it without install oldest Cuda version? When Tensorflow will start supporting Cuda 10.2?
>
> [@domindominik](https://github.com/domindominik), To use CUDA 10.2 with Tensorflow 2.2. Please build the Tensorflow from source.
> Follow the instructions mentioned [here](https://www.tensorflow.org/install/source). And also take a look at this [comment.](https://github.com/tensorflow/tensorflow/issues/38194#issuecomment-609922803)Thanks

[https://github.com/tensorflow/tensorflow/issues/39132](https://github.com/tensorflow/tensorflow/issues/39132)

> **Describe the problem**
>
> ```python
> import tensorflow as tf
> print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
> ```
>
> TensorFlow doesn't use my GPU because there is a bug while trying to load "libcudart.so.10.1". 
>
> My system has libcudart.so.10.2 installed. All the other libraries load fine since they look for libcu***.so.10 and not 10.1
>
> Here is the CUDA lib I have installed:
>
> ```bash
> /opt/cuda/doc/man/man7/libcudart.7
> /opt/cuda/doc/man/man7/libcudart.so.7
> /opt/cuda/targets/x86_64-linux/lib/libcudart.so
> /opt/cuda/targets/x86_64-linux/lib/libcudart.so.10
> /opt/cuda/targets/x86_64-linux/lib/libcudart.so.10.2
> /opt/cuda/targets/x86_64-linux/lib/libcudart.so.10.2.89
> /opt/cuda/targets/x86_64-linux/lib/libcudart_static.a
> ```

> **Suggested solutions**
>
> ### **[ravikyram](https://github.com/ravikyram)** commented [on 4 May 2020](https://github.com/tensorflow/tensorflow/issues/39132#issuecomment-623352457)
>
> [@gillouche](https://github.com/gillouche) To use CUDA 10.2 with Tensorflow 2.2. Please build the Tensorflow from source. Follbashow the instructions mentioned [here](https://www.tensorflow.org/install/source). And also take a look at this [comment.](https://github.com/tensorflow/tensorflow/issues/38194#issuecomment-609922803)Thanks!
>
> ### **[petervandenabeele](https://github.com/petervandenabeele)** commented [on 17 May 2020](https://github.com/tensorflow/tensorflow/issues/39132#issuecomment-629804400)
>
> It seems that libcudart 10.1 and 10.2 are compatible. I was able to hack this on Ubuntu 20.04 by providing a symlink as mentioned by others and run tensorflow 2.2 with libcudart 10.2 (without building from source, just the symlink from a fake library). This may help: [#38194 (comment)](https://github.com/tensorflow/tensorflow/issues/38194#issuecomment-629801937)
>
> ### **[stdcoutzyx](https://github.com/stdcoutzyx)** commented [on 27 Jun 2020](https://github.com/tensorflow/tensorflow/issues/39132#issuecomment-650565521)
>
> meet this problem when using tensorflo# test-tfrecord.py
> import tensorflow as tf
>
> with tf.io.TFRecordWriter('test.tfrecord') as w:
>     w.write(b'First record')
>     w.write(b'Second record')
>     
> for record in tf.data.TFRecordDataset('test.tfrecord'):
>     print(record)w2.2 with cuda10.2. Solved by ln -s
>
> ```bash
> sudo ln -s /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudart.so.10.2 /usr/lib/x86_64-linux-gnu/libcudart.so.10.1
> ```

## Action1

힌트에서 얻은 명령어를 실행해봅니다.

```bash
$ sudo ln -s /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudart.so.10.2 /usr/lib/x86_64-linux-gnu/libcudart.so.10.1
$
```

결과는 여전히 에러가 발생합니다.

```bash
$ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
2021-01-08 19:15:15.890067: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcudart.so.10.1'; dlerror: libcudart.so.10.1: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /usr/local/cuda-11.2/lib64
2021-01-08 19:15:15.890087: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
>>> 
```

여전히 틀립니다.

```bash
$ cd /usr/local/cuda-10.2/targets/x86_64-linux/lib/
bash: cd: /usr/local/cuda-10.2/targets/x86_64-linux/lib/: 그런 파일이나 디렉터리가 없습니다
$
```

10.2를 11.2로 변경했습니다.

```bash
$ cd /usr/local/cuda-11.2/targets/x86_64-linux/lib/

```

디렉토리가 있으므로 파일명을 확인해봅니다.

```bash
$ ls libcudart.so*
libcudart.so  libcudart.so.11.0  libcudart.so.11.2.72
$
```

# test-tfrecord.py
import tensorflow as tf

with tf.io.TFRecordWriter('test.tfrecord') as w:
    w.write(b'First record')
    w.write(b'Second record')
    
for record in tf.data.TFRecordDataset('test.tfrecord'):
    print(record)디렉토리 명과 파일명을 변경해봅니다.

```bash
$ sudo ln -s /usr/local/cuda-11.2/targets/x86_64-linux/lib/libcudart.so.11.0 /usr/lib/x86_64-linux-gnu/libcudart.so.10.1
$
```

Hope this works!

```bash
$ sudo ln -s /usr/local/cuda-11.2/targets/x86_64-linux/lib/libcudart.so.11.0 /usr/lib/x86_64-linux-gnu/libcudart.so.10.1
ln: failed to create symbolic link '/usr/lib/x86_64-linux-gnu/libcudart.so.10.1': 파일이 있습니다
$
```

마지막 단계일지도? 파이팅!

```bash
$ cd /usr/lib/x86_64-linux-gnu/
$ ls -al libcudart*
lrwxrwxrwx 1 root root 63  1월  8 19:14 libcudart.so.10.1 -> /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudart.so.10.2
$
```

이 파일은 조금 전에 만든 심폴릭 링크입니다. 그러므로 지워도 됩니다. 하지만 혹시나 모르니 백업해놓습니다.

```bash
$ sudo mv libcudart.so.10.1 libcudart.so.10.1.old
[sudo] k3sserver의 암호: 
$
```

## Solution1

다시 실행합니다.

```bash
$ sudo ln -s /usr/local/cuda-11.2/targets/x86_64-linux/lib/libcudart.so.11.0 /usr/lib/x86_64-linux-gnu/libcudart.so.10.1
$
```

이번에는 에러가 없으므로 무사히 넘어갔습니다. 잘 됐는지 확인해봅니다.

```python
$ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
2021-01-08 19:25:33.332966: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcudart.so.10.1
>>> 
```

성공입니다!

## Solution2

그런데 이게 최종 문제는 아닙니다.

```bash
$ python3 test-tfrecord.py
```

를 실행해봅니다. 출력 메세지입니다.

```bash
$ python3 test-tfrecord.py 
2021-01-08 19:27:16.617567: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcudart.so.10.1
2021-01-08 19:27:17.615516: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcuda.so.1
2021-01-08 19:27:17.696574: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:982] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-01-08 19:27:17.697362: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1716] Found device 0 with properties: 
pciBusID: 0000:01:00.0 name: GeForce GTX 1080 computeCapability: 6.1
coreClock: 1.7335GHz coreCount: 20 deviceMemorySize: 7.93GiB deviceMemoryBandwidth: 298.32GiB/s
2021-01-08 19:27:17.697439: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:982] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-01-08 19:27:17.698155: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1716] Found device 1 with properties: 
pciBusID: 0000:02:00.0 name: GeForce GTX 1080 computeCapability: 6.1
coreClock: 1.7335GHz coreCount: 20 deviceMemorySize: 7.93GiB deviceMemoryBandwidth: 298.32GiB/s
2021-01-08 19:27:17.698180: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcudart.so.10.1
2021-01-08 19:27:17.698310: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcublas.so.10'; dlerror: libcublas.so.10: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /usr/local/cuda-11.2/lib64
2021-01-08 19:27:17.699235: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcufft.so.10
2021-01-08 19:27:17.699454: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcurand.so.10
2021-01-08 19:27:17.699523: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcusolver.so.10'; dlerror: libcusolver.so.10: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /usr/local/cuda-11.2/lib64
2021-01-08 19:27:17.699582: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcusparse.so.10'; dlerror: libcusparse.so.10: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /usr/local/cuda-11.2/lib64
2021-01-08 19:27:17.699636: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcudnn.so.7'; dlerror: libcudnn.so.7: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /usr/local/cuda-11.2/lib64
2021-01-08 19:27:17.699647: W tensorflow/core/common_runtime/gpu/gpu_device.cc:1753] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/in# test-tfrecord.py
import tensorflow as tf

with tf.io.TFRecordWriter('test.tfrecord') as w:
    w.write(b'First record')
    w.write(b'Second record')
    
for record in tf.data.TFRecordDataset('test.tfrecord'):
    print(record)stall/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2021-01-08 19:27:17.699910: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2021-01-08 19:27:17.705837: I tensorflow/core/platform/profile_utils/cpu_utils.cc:104] CPU Frequency: 3699850000 Hz
2021-01-08 19:27:17.706263: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x62bf130 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2021-01-08 19:27:17.706285: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2021-01-08 19:27:17.707388: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1257] Device interconnect StreamExecutor with strength 1 edge matrix:
2021-01-08 19:27:17.707401: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1263]      
tf.Tensor(b'First record', shape=(), dtype=string)
tf.Tensor(b'Second record', shape=(), dtype=string)
$
```

일단 결과는 나왔습니다.

```python
# test-tfrecord.py
import tensorflow as tf

with tf.io.TFRecordWriter('test.tfrecord') as w:
    w.write(b'First record')
    w.write(b'Second record')
    
for record in tf.data.TFRecordDataset('test.tfrecord'):
    print(record)
```

`print(record)`에 대한 결과로

```python
tf.Tensor(b'First record', shape=(), dtype=string)
tf.Tensor(b'Second record', shape=(), dtype=string)
```

를 얻을 수 있었습니다.

## Consideration

하지만 아래와 같이 유사한 형태의 에러가 발생했습니다.

```bash
2021-01-08 19:27:17.698310: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcublas.so.10'; dlerror: libcublas.so.10: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /usr/local/cuda-11.2/lib64
2021-01-08 19:27:17.699235: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcufft.so.10
2021-01-08 19:27:17.699454: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcurand.so.10
2021-01-08 19:27:17.699523: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcusolver.so.10'; dlerror: libcusolver.so.10: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /usr/local/cuda-11.2/lib64
2021-01-08 19:27:17.699582: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcusparse.so.10'; dlerror: libcusparse.so.10: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /usr/local/cuda-11.2/lib64
2021-01-08 19:27:17.699636: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcudnn.so.7'; dlerror: libcudnn.so.7: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /usr/local/cuda-11.2/lib64
```

일단 문제는 해결했지만 매번 심볼릭 링크로 문제를 해결할 수는 없습니다. CUDA 버전을 낮추는 것을 고려해야겠습니다.