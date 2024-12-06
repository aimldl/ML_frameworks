* Draft: 2021-01-25 (Mon)

# 다크넷 설치하기 (Installing Darknet) 

## 개요
* 두 개의 dependancies가 있지만, 설치하지 않아도 동작합니다.
  > Darknet is easy to install with only two optional dependancies:
  
  * [OpenCV](https://opencv.org/)
  * [CUDA](https://developer.nvidia.com/cuda-downloads)
  
## 설치 과정

### 다크넷 홈페이지의 설치 가이드

> Installing The Base System
> 
> First clone the Darknet git repository here. This can be accomplished by:
> 
> git clone https://github.com/pjreddie/darknet.git
> cd darknet
> make
>
> If you have any errors, try to fix them? If everything seems to have compiled correctly, try running it!
> ./darknet

### 설치 과정 

`$`는 `k8smaster@k8smaster-Alienware-Aurora-R7:~`를 생략한 표현입니다.

CUDA를 설치한 콘다 가상환경인 `tf2`를 활성화합니다.
```bash
(base) $ conda activate tf2
```

`tf2` 환경에서 다크넷 베이스 시스템을 설치합니다.
```bash
(tf2) $ git clone https://github.com/pjreddie/darknet.git
(tf2) $ cd darknet
(tf2) $ make 
```

컴파일이 성공적이면 `darknet` 실행파일이 생성됩니다. 성공적인지 아래 명령어로 확인합니다.
```bash
$ ./darknet
```
아래와 같은 출력이 예상됩니다.
```bash
usage: ./darknet <function>
```
