* 2020-07-09 (Thu)
# 클러스터에 붙은 노드 구성 검증하기

## 개요

노드 적합성 테스트는 그냥 넘어가기로 합니다.

## 상세 내용

> Google search: validate kubernetes Node Conformance Test
>
> Couple of thing I can suggest you to run Conformance Test:
> 1) Forget about https://kubernetes.io/docs/setup/node-conformance/
> 2) Install [kubetest](https://github.com/kubernetes/test-infra/tree/master/kubetest) and follow [Conformance Testing in Kubernetes](https://github.com/kubernetes/community/blob/master/contributors/devel/conformance-tests.md) instruction
> 3) Use [sonobuoy](https://github.com/heptio/sonobuoy) solution from Heptio. More information you can find here: [Conformance Testing - 1.11+](https://github.com/heptio/sonobuoy/blob/master/docs/conformance-testing.md)
> Good Luck!
>
> 출처: [Kubernetes Node Conformance Test](https://stackoverflow.com/questions/54129836/kubernetes-node-conformance-test)
Kubetest를 설치해봅니다.

> ## Kubetest > Installation
>
> Please clone this repo and then run `GO111MODULE=on go install ./kubetest` from the clone.
>
> Common alternatives:
>
> ```text
> go install k8s.io/test-infra/kubetest  # if you check out test-infra
> bazel run //kubetest  # use bazel to build and run
> ```
>
> 출처: [test-infra](https://github.com/kubernetes/test-infra)/[kubetest](https://github.com/kubernetes/test-infra/tree/master/kubetest)/

```bash
$ git clone https://github.com/kubernetes/test-infra.git
$ cd test-infra/
# Go is necessary.
$ sudo apt install gccgo-go
  ...
$ GO111MODULE=on go install ./kubetest
kubetest/aksengine_helpers.go:30:2: cannot find package "github.com/Azure/azure-sdk-for-go/services/authorization/mgmt/2015-07-01/authorization" in any of:
  ...
$ go install ./kubetest
kubetest/aksengine_helpers.go:30:2: cannot find package "github.com/Azure/azure-sdk-for-go/services/authorization/mgmt/2015-07-01/authorization" in any of:
  ...
$
```

설치가 안 되고 에러 메세지가 발생합니다. Azure 관련 메세지가 나오는 걸 보면, Azure 상의 쿠버네티스를 테스트하는 명령어 일지도 모르겠네요. Azure와는 상관이 없으므로 이 명령어도 무시하기로 합니다.

노드 적합성 테스트는 그냥 넘어가기로 합니다.

## 다음

[쿠버네티스 대쉬보드 (Kubernetes Dashboard) 설치하기](deploy_k8s_dashboard.md)

## 부록: 공식 문서의 노드 적합성 테스트의 명령어를 쓰지 않는 이유

쿠버네티스 공식 문서에는

* [노드 구성 검증하기](https://kubernetes.io/ko/docs/setup/best-practices/node-conformance/) (한국어), [Validate node setup](https://kubernetes.io/docs/setup/best-practices/node-conformance/) (영어)

에 관한 문서가 있습니다. 이 문서에 나오는 명령어는 무시해도 좋다는 결론이 났습니다.

[노드 구성 검증하기](https://kubernetes.io/ko/docs/setup/best-practices/node-conformance/)의 노드 적합성 테스트의 명령어

```bash
$ sudo docker run -it --rm --privileged --net=host -v /:/rootfs -v $CONFIG_DIR:$CONFIG_DIR -v $LOG_DIR:/var/result k8s.gcr.io/node-test:0.2
```

를 실행하면 테스트가 실패합니다. 실패 원인을 제거하기 위해 구글 검색해봅니다.

> Google search: kubernetes Node Conformance Test system validation failed: unsupported docker version: 19.03.11
>
>  이 글을 보면 모든 Docker 버전에 대해 테스트 했지만 실패했다고 되어 있습니다.
>
> 출처: [Node conformance test NodeProblemDetector failed against all docker ce and ee versions from 17.06.--19.03](https://github.com/kubernetes/kubernetes/issues/78186)

> 검색 결과가 몇 개 나오지 않아서 검색 범위를 넖혀 봅니다.
>  Google search: kubernetes Node Conformance Test system validation failed: unsupported docker version: 19.03.11
>
> 실패원인 제거를 위해 찾아본 다른 문서에서도 공식 문서의 명령어가 안 된다는 "신호"를 많이 봤습니다. 

> Google search: validate kubernetes Node Conformance Test
>
> Couple of thing I can suggest you to run Conformance Test:
> 1) Forget about https://kubernetes.io/docs/setup/node-conformance/
> 2) Install [kubetest](https://github.com/kubernetes/test-infra/tree/master/kubetest) and follow [Conformance Testing in Kubernetes](https://github.com/kubernetes/community/blob/master/contributors/devel/conformance-tests.md) instruction
> 3) Use [sonobuoy](https://github.com/heptio/sonobuoy) solution from Heptio. More information you can find here: [Conformance Testing - 1.11+](https://github.com/heptio/sonobuoy/blob/master/docs/conformance-testing.md)
> Good Luck!
>
> 출처: [Kubernetes Node Conformance Test](https://stackoverflow.com/questions/54129836/kubernetes-node-conformance-test)

이 문서는 노드 적합성 테스트 명령어 잊어버리라는 조언합니다. 그래서 잊기로 합니다.

## 부록: 노드 적합성 테스트의 명령어 실행 과정

### Problem: system validation failed: unsupported docker version: 19.03.12

```bash
$ sudo docker run -it --rm --privileged --net=host -v /:/rootfs -v $CONFIG_DIR:$CONFIG_DIR -v $LOG_DIR:/var/result k8s.gcr.io/node-test:0.2
  ...
Running in parallel across 8 nodes

OS: Linux
KERNEL_VERSION: 4.15.0-108-generic
CONFIG_NAMESPACES: enabled
CONFIG_NET_NS: enabled
CONFIG_PID_NS: enabled
CONFIG_IPC_NS: enabled
CONFIG_UTS_NS: enabled
CONFIG_CGROUPS: enabled
CONFIG_CGROUP_CPUACCT: enabled
CONFIG_CGROUP_DEVICE: enabled
CONFIG_CGROUP_FREEZER: enabled
CONFIG_CGROUP_SCHED: enabled
CONFIG_CPUSETS: enabled
CONFIG_MEMCG: enabled
CONFIG_INET: enabled
CONFIG_EXT4_FS: enabled
CONFIG_PROC_FS: enabled
CONFIG_NETFILTER_XT_TARGET_REDIRECT: enabled (as module)
CONFIG_NETFILTER_XT_MATCH_COMMENT: enabled (as module)
CONFIG_OVERLAY_FS: enabled (as module)
CONFIG_AUFS_FS: enabled (as module)
CONFIG_BLK_DEV_DM: enabled
CGROUPS_CPU: enabled
CGROUPS_CPUACCT: enabled
CGROUPS_CPUSET: enabled
CGROUPS_DEVICES: enabled
CGROUPS_FREEZER: enabled
CGROUPS_MEMORY: enabled
DOCKER_VERSION: 19.03.12
F0709 16:23:05.757598     155 e2e_node_suite_test.go:96] system validation failed: unsupported docker version: 19.03.12

Failure [0.135 seconds]
[BeforeSuite] BeforeSuite 
/go/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/test/e2e_node/e2e_node_suite_test.go:157

  system validation
  Expected success, but got an error:
      <*errors.errorString | 0xc420292050>: {
          s: "system validation failed: exit status 1",
      }
      system validation failed: exit status 1

  /go/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/test/e2e_node/e2e_node_suite_test.go:122
  ...
Ran 88 of 162 Specs in 0.239 seconds
FAIL! -- 0 Passed | 88 Failed | 0 Pending | 74 Skipped 

Ginkgo ran 1 suite in 403.927172ms
Test Suite Failed
$
```

### Hint: system validation failed: unsupported docker version: 19.03.12

에러 메세지: `system validation failed: unsupported docker version: 19.03.12`

> Google search: kubernetes system validation failed: unsupported docker version
>
> You need to downgrade docker to 18.06, until 18.09 is validated and supported by kubeadm

> Version 19.03.11 is recommended, but 1.13.1, 17.03, 17.06, 17.09, 18.06 and 18.09 are known to work as well. 
>
> 출처:
>
> * [v1.18  릴리스 노트](https://kubernetes.io/ko/docs/setup/release/notes/)
>
> * [Kubernetes version and version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/)
>
> * [Container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)

현재 설치된 도커 버전을 확인합니다.

```bash
$ docker version
Client: Docker Engine - Community
 Version:           19.03.12
  ...
$
```

현 시점에 도커 최신 버전인`19.03.12`가 설치되어 있습니다. 쿠버네티스가 지원하는 최신 버전은 19.03.11입니다. 버전이 하나 높은 19.03.12이므로 19.03.11로 다운 그레이드 해야합니다.

우선 Docker를 제거합니다. 자세한 내용은 [Install docker on Ubuntu](https://github.com/aimldl/technical_skills/blob/master/computing_environments/docker/how_to_install/docker_on_ubuntu.md)의 마지막에 있는 `Uninstall Docker`를 참고하세요.

#### Uninstall

```bash
$ sudo apt-get purge docker-ce docker-ce-cli containerd.io
$ sudo rm -rf /var/lib/docker
```

#### 제거 확인

```bash
$ docker version
-bash: /usr/bin/docker: No such file or directory
$
```

제거를 위해 아래 명령어가 쓰였는 데 모두 제거 되지 않아 위의 명령어를 썼습니다.

```bash
$ dpkg -l | grep -i docker
ii  docker-ce      5:19.03.12~3-0~ubuntu-bionic  amd64  Docker:     the open-source application container engine
ii  docker-ce-cli  5:19.03.12~3-0~ubuntu-bionic  amd64  Docker CLI: the open-source application container engine
$
```

```bash
$ sudo apt-get purge -y docker-engine docker docker.io docker-ce
  ...
Package 'docker' is not installed, so not removed
Package 'docker.io' is not installed, so not removed
Package 'docker-engine' is not installed, so not removed
The following packages were automatically installed and are no longer required:
  aufs-tools cgroupfs-mount pigz
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  ...
$ sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce
  ...
Package 'docker' is not installed, so not removed
Package 'docker.io' is not installed, so not removed
Package 'docker-ce' is not installed, so not removed
Package 'docker-engine' is not installed, so not removed
The following packages will be REMOVED:
  aufs-tools* cgroupfs-mount* pigz*
  ...
$
```

### 다운 그레이드 버전 설치하기

설치 시 원하는 버전을 `VERSION_STRING`으로 지정해서 설치합니다. 설치 전반에 관한 내용은 [ Container runtimes > Docker](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#docker)를 참고하세요.

```bash
$ sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
```

설치하려는 버전인 19.03.11의 `VERSION_STRING`은 `5:19.03.11~3-0~ubuntu-bionic`이고, `containerd.io` 버전은 `1.2.13-2`입니다. 그러므로 실행할 명령어는

```bash
$ apt-get install docker-ce=5:19.03.11~3-0~ubuntu-bionic docker-ce-cli=5:19.03.11~3-0~ubuntu-bionic containerd.io=1.2.13-2
```

입니다.

버전을 확인합니다. Docker와 containerd 모두 원하는 버전이 설치되었습니다

```bash
$ sudo docker version
Client: Docker Engine - Community
 Version:           19.03.11
  ...
Server: Docker Engine - Community
 Engine:
  Version:          19.03.11
  ...
containerd:
  Version:          1.2.13
  ...
$
```

## 부록: `VERSION_STRING` 정보 확인하기

다른 버전에 대한 `VERSION_STRING` 정보는 다음 명령어로 가능합니다. 두 번째 열이  `VERSION_STRING` 정보입니다.

```bash
# apt-cache madison docker-ce
 docker-ce | 5:19.03.12~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.11~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.10~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.9~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.8~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.7~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.6~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.5~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.4~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.3~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.2~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.1~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.0~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.9~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.8~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.7~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.6~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.5~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.4~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.3~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.2~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.1~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.0~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 18.06.3~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 18.06.2~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 18.06.1~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 18.06.0~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 18.03.1~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
#
```

쿠버네티스에서 호환 확인된 버전인 19.03.11와 1.13.1, 17.03, 17.06, 17.09, 18.06, 18.09 에 해당하는 것은가 있습니다. 19.03.11, 18.09, 18.06 만 보여지고 1.13.1, 17.03, 17.06, 17.09는 없네요.

docker-ce | 5:19.03.11~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
  ...
docker-ce | 5:18.09.9~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 5:18.09.8~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 5:18.09.7~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 5:18.09.6~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 5:18.09.5~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 5:18.09.4~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 5:18.09.3~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 5:18.09.2~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 5:18.09.1~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 5:18.09.0~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 18.06.3~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 18.06.2~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 18.06.1~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
docker-ce | 18.06.0~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages