* Draft: 2020-07-01 (Wed)

# 컨테이너 런타임 (Container Runtime) 설치하기

쿠버네티스는 컨테이너 오케스트레이션 툴 (Container Orchestration Tool)이므로, 컨테이너를 다루기 위해 필요한 컨테이너 런타임 (프로그램)의 설치가 선행되어야 합니다. 현재 사용 가능한 컨테이너 런타임은

* [Docker](https://www.docker.com/)
* [CRI-O](https://cri-o.io/) (Container Runtime Interface-Open Container Initiative)
* [rkt](https://coreos.com/rkt/)
* [containerd](https://containerd.io/)

가 있습니다. 

쿠버네티스 공식 문서 ([컨테이너 런타임](https://kubernetes.io/ko/docs/setup/production-environment/container-runtimes/))에서는 Docker와 CRI-O 의 설치 방법을 설명합니다. 쿠버네티스는 개발 초기에는 런타임 프로그램으로 Docker를 사용했고, CRI-O는 Docker의 단점을 극복하여 인기가 상승하고 있는 컨테이너 런타임입니다. 

여기서는 Docker의 설치만 다룹니다. 쿠버네티스 개발 초창기부터 Docker를 고려했기 때문입니다. 쿠버네티스 공식 문서의 [노드 구성 검증하기](https://kubernetes.io/ko/docs/setup/best-practices/node-conformance/)를 보면, 노드가 쿠버네티스를 위한 최소 요구조건을 만족하지는 검증하는 [노드 적합성 테스트](https://kubernetes.io/ko/docs/setup/best-practices/node-conformance/#%EB%85%B8%EB%93%9C-%EC%A0%81%ED%95%A9%EC%84%B1-%ED%85%8C%EC%8A%A4%ED%8A%B8)는 컨테이너 런타임으로 Docker인 경우만 지원합니다.

설치 과정은 일반적인 Docker 설치 과정과 동일합니다. 쿠버네티스를 설치하고자 하는 모든 컴퓨터 (마스터와 모든 워커 노드)에 먼저 설치해야 합니다.

## 1. Docker 설치하기

### 1.1. root 계정으로 명령어를 실행할 경우

```bash
# apt-get update && apt-get install -y apt-transport-https ca-certificates curl software-properties-common gnupg2
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg |  apt-key add -
# add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
# apt-get update &&  apt-get install -y \
  containerd.io=1.2.13-2 \
  docker-ce=5:19.03.11~3-0~ubuntu-$(lsb_release -cs) \
  docker-ce-cli=5:19.03.11~3-0~ubuntu-$(lsb_release -cs)
# cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF
# mkdir -p /etc/systemd/system/docker.service.d
# systemctl daemon-reload
# systemctl restart docker
```

부팅 후 Docker 서비스를 시작하려면

```bash
# systemctl enable docker
```

### 1. 2. 앞에 sudo 를 붙이고 명령어를 실행할 경우

```bash
$ sudo apt-get update && sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common gnupg2
$ sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
$ sudo apt-get update && sudo apt-get install -y \
  containerd.io=1.2.13-2 \
  docker-ce=5:19.03.11~3-0~ubuntu-$(lsb_release -cs) \
  docker-ce-cli=5:19.03.11~3-0~ubuntu-$(lsb_release -cs)
$ cat > daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF
$ sudo mv daemon.json /etc/docker/
$ sudo mkdir -p /etc/systemd/system/docker.service.d
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```

부팅 후 Docker 서비스를 시작하려면

```bash
$ sudo systemctl enable docker
```

##### `cat > daemon.json <<EOF ...`의 sudo용 명령어 변환

일반적으로 명령어 앞에 sudo 만 붙이면 되지만, 그것보다 조금 까다로운 상황이 발생하기도 합니다. 일례로 root계정에서 실행한 아래 명령어 하나는 

```bash
# cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF
```

sudo를 쓰는 경우로 변환할 때, 두 개의 명령어로 나누었습니다.

```bash
$ cat > daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF
$ sudo mv daemon.json /etc/docker/
```

## 2. Docker 설치 여부 확인하기

마스터에서 확인하기

```bash
$ hostname
k8smaster-gpu-desktop
$ docker --version
Docker version 19.03.12, build 48a66213fe
$
```

```bash
$ sudo docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
$
```

워커 노드에서 확인하기

```bash
$ hostname
k8snode-01-gpu-desktop
$ docker --version
Docker version 19.03.11, build 42e35e61f3
$
```

거의 같은 시간에 설치했지만 워커 노트에 설치한 Docker 의 마이너 버전이 하나 낮네요. 큰 문제는 없으므로 일단 넘어갑니다.

## 다음

* [컨테이너 런타임 설치하기: kubeadm편](install_container_runtime_with_kubeadm.md)