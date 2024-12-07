* 2021-01-08 (Fri)

# TensorFlow Extended (TFX) 설치하는 방법

# (How to Install TensorFlow Extended)

이 페이지는 TFX 설치의 핸즈온을 보여줍니다.

## OS = Ubuntu 20.04

시스템에는 Ubuntu 20.04가 설치되어 있습니다.

```bash
$ cat /etc/os-release
NAME="Ubuntu"
VERSION="20.04.1 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.1 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
$
```

## Python3

Python3는 이미 Ubuntu 20.04에 설치되어 있습니다.

```bash
$ python3 --version
Python 3.8.5
$ which python3
/usr/bin/python3
$
```

> 하지만 `python`은 없으니 유의하세요.
>
> ```bash
> $ python --version
> 
> Command 'python' not found, did you mean:
> 
>   command 'python3' from deb python3
>   command 'python' from deb python-is-python3
> 
> $ which python
> $
> ```
>
> 그러므로 `pip`도 없습니다.
>
> ```bash
> $ pip install tfx
> 
> Command 'pip' not found, but there are 18 similar ones.
> 
> $
> ```

## PIP3

Ubuntu 20.04에 `pip3`는 설치되어 있지 않습니다.

```bash
$ pip3 install [target_package]
Command 'pip3' not found, but can be installed with:

sudo apt install python3-pip

$
```

아래의 명령어로 설치합니다.

```bash
$ sudo apt install python3-pip
  ...
계속 하시겠습니까? [Y/n] y
  ...
$
```

## TFX

TFX를 설치합니다.

```bash
$ pip3 install tfx
```

실행 결과는 [부록. INSTALL-TFX](appendix/INSTALL-TFX.md)를 참고하세요.

> 부록 A. `pip3 install tfx` 실행 결과
>
> * `$ pip3 install tfx` 실행 시 주요 출력 메세지
> * 성공적으로 설치된 패키지의 전체 리스트
> * `$ pip3 install tfx` 실행 시 전체 출력 메세지

설치 확인을 위해 파이썬 인터프리터를 실행시킨 후,

```bash
$ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

 파이썬 패키지를 몇 가지 임포트 해봅니다.

```bash
>>> import apache_beam as beam
>>> exit()
```

에러가 발생하지 않으면 잘 설치된 것으로 여길 수 있습니다.

## 참고

설치에 관한 자세한 내용은 아래를 참고하세요. 각 참고사항의 중요내용을 간략하게 요약했습니다.

* Building Machine Learning Pipelines (책) > 2. Introduction to TensorFlow Extended > Installing TFX

> ```bash
> $ pip install tfx
> ```

* [tfx 0.26.0](https://pypi.org/project/tfx/)

> ```bash
> pip install tfx
> ```

* [TFX User Guide](https://github.com/tensorflow/tfx/blob/master/docs/guide/index.md)

> **Installation**
>
> Python 3.6 | 3.6 | 3.8, PyPI 0.26.0
>
> ```bash
> pip install tfx
> ```