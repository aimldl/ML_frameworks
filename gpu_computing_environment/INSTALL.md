* Rev.2: 2021-01-09 (Sat)
* Rev.1: 2020-06-24 (Wed)
* Draft: 2019-03-03 (Sun)

# GPU 연산 환경 구축하기 (Setting up GPU Computing Environments)

## 큰 그림 (Big Picture)

GPU 연산 환경은 예산에 맞게 다양하게 구축할 수 있습니다.

* 소형 임베디드 보드 (Embedded board)
  * 경량 컴퓨터에 경량 GPU가 내장된 NVIDIA J (Graphics Processing Unit)etson Nano를 구입해서 사용
* 개인용 데스크탑 (Desktop)
  * 개인 컴퓨터에서 게임용으로 쓰이기도 하는 NVIDIA GeForce 시리즈의 GPU카드 한 개를 몇 십만원대에 구입해서 장착
* 기업용 서버 (Workstation/Server)
  * 서버용 컴퓨터 하나에 NVIDIA Quadro 시리즈의 GPU카드 여러개를 구입해서 장착 (Multi-GPU 환경)
  * 이렇게 멀티 GPU카드가 꽂힌 서버 여러 대로 클러스터를 구성 (Multi-Node Multi-GPU 환경)
* 슈퍼 컴퓨터 (High Performance Computer)
  * 고성능 연산을 위한 NVIDIA DGX 시스템을 여러 대로 고성능 클러스터를 구성 (고성능 Multi-Node Multi-GPU 환경)
  * 예: NVIDIA V-100카드 8장이 내장된 NVIDIA DGX 시스템 수십 대를 광케이블로 연결한 클러스터

그 외에도 모바일 용 (Mobile GPUs, Mobile Workstation GPUs)도 있습니다만 여기서는 다루지 않습니다.



직접 구축하지 않고 이미 구축되어 잘 관리되고 있는, 퍼블릭 클라우드에서 GPU를 원하는 만큼 대여할 수도 있습니다.

* 퍼블릭 클라우드 서비스: Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure 등

## `set_up` 디렉토리 vs. `INSTALL.md`

* (모든 경우를 다룰 수는 없지만) 환경에 따라 조금씩 설정이 미묘하게 달라지는 등의 어려움이 있습니다. 여러 가지 경우를 [INSTALL.md](INSTALL.md)에서 정리합니다.
* 각 경우를 진행하면서 `set_up` 디렉토리에 파일로 저장합니다. (다양한 연산 환경을 [INSTALL.md](INSTALL.md) 파일 하나에 담을 수 없습니다.)

## 개인용 데스크탑 컴퓨터에 GPU 연산 환경 구축하기

#### [텐서플로를 위한 GPU 연산 환경 설정하기 (Setting up the GPU Computing Environments for TensorFlow)](set_up/gpu_computing_environments_for_tensorflow.md)

* 예기치 않는 에러를 피하려면 우분투 20.04대신 한 버전 오래된 18.04를 선택하세요.
* 이유는 텐스플로 2.x가 CUDA 10.1를 지원하고, CUDA10.1이 우분투 18.10과 18.04까지 지원하기 때문입니다.
  * 우분투 홈페이지의 메인 다운로드 페이지에는 18.04를 다운로드 받을 수 있지만 18.10는 받을 수 없습니다.

* [우분투 18.04에 NVIDIA GeForce 1080를 설정하는 방법](set_up/nvidia_geforce1080_on_ubuntu18_04.md)
* [우분투 20.04에 NVIDIA GeForce 1080Ti를  설정하는 방법 ](set_up/nvidia_geforce1080ti_on_ubuntu20_04.md)

### 버전 다운그레이드해서 성공적으로 GPU 환경을 설치한 경우

[GPU 환경 설정하기](set_up/gpu_computing_environment-downgrade-sucess.md)를 참고하세요.
