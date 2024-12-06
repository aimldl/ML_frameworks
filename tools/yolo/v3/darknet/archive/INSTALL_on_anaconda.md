* Draft: 2021-01-28 (Thu)

# 다크넷 설치하기 (쿡북 매뉴얼)

Anaconda를 다운로드 받아서 설치합니다.

```bash
$ wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
$ bash Anaconda3-2020.07-Linux-x86_64.sh

```

가상환경을 시작합니다.

```bash
$ bash
(base) $
```

새로운 가상환경을 생성합니다. 인터넷 연결이 없을 경우 `CondaHTTPError`가 발생합니다.

```bash
$ conda create -n darknet_with_opencv_and_cuda python=3 anaconda
```

* 이름을 `darknet_with_opencv_and_cuda`로 설정
* python3와 anaconda의 패키지를 가상환경에 같이 설치

> Tip: 사내망 등 보안이슈로 인터넷 연결이 없을 경우, 
>
> **Option 1. Docker로 환경을 생성한 후에 컨테이너를 복사해서 쓰는 방법이 있습니다.**
>
> 인터넷이 없을 경우 Anaconda 가상환경보다 Docker 컨테이너 환경을 쓰는데 더 깔끔하고 나은 방법일 수 있습니다.
>
> **Option 2. 다운로드 받은 설치파일을 설치하면 `(base)`가상환경을 만들 수 있습니다.** `darknet_with_opencv_and_cuda`라는 가상환경을 만들지 않고, `(base)` 도 가상환경을 제공한다는 것에 주목하세요.
>
> 기본 환경으로 돌아가려면
>
> ```bash
> (base) $ conda deactivate
> $
> ```
>
> `(base)`가상환경을 다시 활성화하려면
>
> ```bash
> $
> $ conda activate base
> (base) $
> ```
>
> 라고 명령어를 실행하면 됩니다.

생성된 환경을 확인합니다.

```bash
$ conda info -e
# conda environments:
#
base                  *  /home/aimldl/anaconda3
darknet_with_opencv_and_cuda     /home/aimldl/anaconda3/envs/darknet_with_opencv_and_cuda

$
```

가상환경을 활성화합니다.

```bash
(base) $ conda activate darknet_with_opencv_and_cuda
(darknet_with_opencv_and_cuda) $ 
```

