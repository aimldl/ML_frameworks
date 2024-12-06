* Draft: 2021-01-07 (Thu)

# TFX 설치하기

## 요약

TFX는 명령어 하나로 간단하게 설치됩니다.

```bash
pip install tfx
```

자세한 내용은 [The TFX User Guide > Installation](https://www.tensorflow.org/tfx/guide#installation)을 참고하세요.

## (옵션)

`tfx`라는 이름의 아나콘다 가상 환경 (Anaconda virtual environment)을 생성합니다.

```bash
(base) $ conda create -n tfx python=3 anaconda
  ...
Proceed ([y]/n)? y
#
# To activate this environment, use
#
#     $ conda activate tfx
#
# To deactivate an active environment, use
#
#     $ conda deactivate
$
(base) $
```

`tfx` 가상환경을 활성화합니다.

```bash
(base) $ conda activate tfx
(tfx) $
```

## TFX 설치하기

이상적으로는 아래 명령어를 실행하면 TFX의 설치가 완료됩니다.

```bash
(tfx) $ pip install tfx
```

## 설치 확인하기

확인을 위해 몇 가지 TFX 패키지와 TFX component를 import해봅니다.

```python
import tensorflow_data_validation as tfdv
import tensorflow_transform as tft
import tensorflow_transform.beam as tft_beam
from tfx.components import ExampleValidator
from tfx.components import Evaluator
from tfx.components import Transform
```

`python`인터프리터에서 

```bash
$ python
Python 3.8.5 (default, Sep  4 2020, 07:30:14) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

입력을 해서 에러가 발생하지 않으면 TFX 설치가 되었음을 확인할 수 있습니다.

```bash
>>> import tensorflow_data_validation as tfdv
2021-01-07 17:02:45.945332: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcudart.so.10.1'; dlerror: libcudart.so.10.1: cannot open shared object file: No such file or directory
2021-01-07 17:02:45.945354: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
>>> import tensorflow_transform as tft
>>> import tensorflow_transform.beam as tft_beam
>>> from tfx.components import ExampleValidator
>>> from tfx.components import Evaluator
>>> from tfx.components import Transform
>>>
```

