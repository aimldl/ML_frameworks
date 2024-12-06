* Draft: 2020-07-02 (Thu)

# 컨테이너 런타임 설치하기: kubeadm편

이 부분은 쿠버네티스 공식 문서의 [Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/) > [Installing runtime](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-runtime)에 해당합니다. 컨테이너 런타임의 설치에 관해서는 앞부분의 [컨테이너 런타임 (Container Runtime) 설치하기](install_container_runtime.md)에 있는데, 이 부분은 배포 도구 중 하나인 kubeadm을 경우로 한정된 경우입니다.

쿠버네티스는 

* 컨테이너를 파드 (Pod) 안에서 실행하기 위해 컨테이너 런타임을 사용
* 선택된 컨테이너 런타임을 인터페이스하기 위해 컨테이너 런타임 인터페이스(CRI)를 사용

합니다.

다음 표는 컨테이너 런타임과 관련된 소켓 경로입니다. 

| Runtime    | Path to Unix domain socket        |
| ---------- | --------------------------------- |
| Docker     | `/var/run/docker.sock`            |
| containerd | `/run/containerd/containerd.sock` |
| CRI-O      | `/var/run/crio/crio.sock`         |

별도로 지정하지 않으면 kubeadm이 이 경로를 스캔하며 설치된 컨테이너 런타임를 자동으로 찾아냅니다. 

## 복수의 컨테이너 런타임이 설치되었을 경우

* Docker와 containerd가 모두 있을 경우,
  * Docker가 우선적으로 선택합니다.
  * Docker만 설치하더라도 Docker18.09는 containerd도 설치하므로 이런 절차가 필요합니다.
* 그 외에 복수의 런타임이 설치된 경우,
  * 에러가 발생합니다.

### 마스터 노트의 예

앞에서 마스터 노드에는 Docker만 설치했습니다. 현재 버전은 19.03.12입니다.

```bash
$ hostname
k8smaster-gpu-desktop
$ docker --version
Docker version 19.03.12, build 48a66213fe
$
```

`/var/run` 디렉토리에서 Docker 혹은 containerd와 관련된 파일을 보면 

```bash
$ cd /var/run
$ ls | egrep "docker|containerd"
containerd
docker
docker.pid
docker.sock
$
```

Docker뿐만 아니라 containerd도 같이 있음을 알 수 있습니다.

### 워커 노트의 예

앞에서 워커 노드에도 Docker만 설치했습니다. 현재 버전은 19.03.11입니다.

```bash
$ hostname
k8snode-01-gpu-desktop
$ docker --version
Docker version 19.03.11, build 42e35e61f3
$
```

`/var/run` 디렉토리에서 Docker 혹은 containerd와 관련된 파일을 보면 

```bash
$ cd /var/run
$ ls | egrep "docker|containerd"
containerd
docker
docker.pid
docker.sock
$
```

워커 노드 역시 Docker뿐만 아니라 containerd도 같이 있음을 알 수 있습니다.

## 다음

* [배포 툴을 이용해서 쿠버네티스 설치하기](install_k8s_with_deployment_tools.md)