* Rev.1: 2020-07-03 (Fri)
* Draft: 2020-07-02 (Thu)

# kubeadm으로 쿠버네티스 클러스터 생성하기

이 부분은 쿠버네티스 공식 문서의 [Creating a single control-plane cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)에 해당합니다. 한국어 페이지의 제목은 [kubeadm으로 컨트롤 플레인 사용자 정의하기](https://kubernetes.io/ko/docs/setup/production-environment/tools/kubeadm/control-plane-flags/) 입니다. 

## 큰 그림

쿠버네티스 클러스터는 개념적으로

* 컨트롤 플레인 노드 (Control Plane Node)와
* 여러개의 워커 노드 (Worker Node)

로 구성됩니다. 마스터 (Master) - 슬레이브 (Slave) 구조에서 컨트롤 플레인 노드가 마스터, 워커 노드가 슬레이브에 해당합니다. 줄여서 각각 마스터 (Master) - 노드 (Node)라고도 합니다.

| 마스터 - 슬레이브 구조 | 쿠버네티스                              | 단축어          |
| ---------------------- | --------------------------------------- | --------------- |
| 마스터 (Master)        | 컨트롤 플레인 노드 (Control Plane Node) | 마스터 (Master) |
| 슬레이브 (Slave)       | 워커 노드 (Worker Node)                 | 노드 (Node)     |

### 쿠버네티스 클러스터 아키텍쳐

컨트롤 플레인 노드 (Control Plane Node)는 컨트롤 플레인 요소 (Control Plane Components)가 실행되는 컴퓨터입니다. 워커 노드 (Worker Node)는 컨트롤 플레인 노드가 할당한 일 (Work 혹은 Task)을 수행하는 컴퓨터로 일반적으로 다수의 컴퓨터로 구성됩니다. 아래 그림은 마스터와 노드에 필요한 구성요소를 간략히 설명하는 쿠버네티스 클러스터 아키텍쳐의 한 예시입니다.

<img src="/home/k8smaster/github/aimldl.github.io/kubeflow/kr/1_environment_setup/images/kubernetes_architecture.jpg">

Source: [Kubernetes architecture and concepts tutorial - Kubernetes Administration for beginners(9:18)](https://www.youtube.com/watch?v=oFglQ50O_rU)

쿠버네티스 클러스터를 만들기 위해서는

* 마스터와 노드에 필요한 요소들을 설치해서 쿠버네티스 클러스터를 생성하고
* Pod Network 혹은 CNI Network로 각 노드를 연결하는 네트워크를 구성

하게 됩니다. 쿠버네티스 클러스터에서 컨테이너를 실행시키는 최소 단위가 파드 (Pod)입니다. 파드는 생성/소멸을 반복할 수 있는데, 여러 개의 파드가 있을 때 서로 통신할 수 있도록 Pod Network가 형성됩니다. 위의 그림에 `CNI Network: Wave Net, Calico`로 표기된 부분입니다. 

### 마스터 (노드)에서 실행되는 컨트롤 플레인 요소

| Component 이름     | 설명                                 | 비고                                    |
| ------------------ | ------------------------------------ | --------------------------------------- |
| API Server         | kubectl 명령어와 커뮤니케이션을 위함 | control-plane<br/>  /apiserver          |
| Controller Manager |                                      | control-plane<br/>  /controller-manager |
| Scheduler          |                                      | control-plane<br/>  /scheduler          |
| etcd               | 클러스터 데이터 베이스               | etcd<br/>  /local                       |

### (워커) 노드에서 실행되는 요소

| Component 이름 | 설명 | 비고 |
| -------------- | ---- | ---- |
| kubelet        |      |      |
| Service Proxy  |      |      |

### Pod Network 혹은 CNI (Container Network Interface) Network

CNI Network는 쿠버네티스가 네트워크 설명을 지휘하기 위한 방식입니다. 컨테이너를 기반으로 하는 파드가 생성되거나 소멸될 때 마다 기본 설정값을 기반으로 기본 CNI 플러그인을 불러오면서 자동으로 네트워크가 설정됩니다. 파드를 기반으로 하므로 Pod Network이라고도 합니다.

## 마스터 초기화

`kubeadm`의 초기화 명령어는 두 가지 옵션이 있습니다.

* `sudo kubeadm init` 기본값으로 초기화
* `sudo kubeadm init <args>` 옵션값을 주고 초기화

간단해 보이지만, 필요에 맞는 옵션을 선택하기 위해선 복잡한 구조와 절차에 대한 이해가 필요하므로 아래에 요약해서 설명해봅니다.

### 초기화 목표

마스터 노드 초기화는 두 가지 목표가 있습니다.

#### 쿠버네티스 클러스터 설정

쿠버네티스 클러스터를 기본 혹은 고가용성으로 설정합니다. 

* 단일 구성 클러스터(Single Control-Plane Kubernetes Cluster) 는 마스터 노드가 하나인 경우입니다. 즉, 컴퓨터 한 대만 마스터 노드로 쓰입니다.
* 고가용성 클러스터  (High Availability Kubernetes Cluster)를 설정하기 위해선 마스터 노드를 다중으로 구성합니다. 즉, 마스터 노드로 쓰이는 컴퓨터가 여러대 입니다.

#### Pod Network 생성

Pod Network으로 선택 가능한 옵션은

[Canal](https://github.com/tigera/canal/tree/master/k8s-install), [Calico](https://docs.projectcalico.org/latest/introduction/), [Cilium](https://github.com/cilium/cilium), [CNI-Genie](https://github.com/Huawei-PaaS/CNI-Genie), [Contiv](http://contiv.github.io), [Contrail](http://www.juniper.net/us/en/products-services/sdn/contrail/contrail-networking/), [Flannel](https://github.com/coreos/flannel/blob/master/Documentation/kubernetes.md), [Knitter](https://github.com/ZTE/Knitter/), [Multus](https://github.com/Intel-Corp/multus-cni), [OVN4NFV-K8S-Plugin](https://github.com/opnfv/ovn4nfv-k8s-plugin), [NSX-T](https://docs.vmware.com/en/VMware-NSX-T/2.0/nsxt_20_ncp_kubernetes.pdf), [Nuage](https://github.com/nuagenetworks/nuage-kubernetes/blob/v5.1.1-1/docs/kubernetes-1-installation.rst), [Romana](http://romana.io), [Weave Net](https://www.weave.works/docs/net/latest/kube-addon/)

이 있고, 선택에 따라 마스터 노드의 Pod Network 초기화 방식이 달라집니다. 기본값은 [Calico](https://docs.projectcalico.org/latest/introduction/)입니다. 각 옵션에 관한 보다 자세한 설명은 쿠버네티스 공식 문서의 [Installing Addons](https://kubernetes.io/docs/concepts/cluster-administration/addons/)을 참고하세요.

#### 내용 정리

<img src="/home/k8smaster/github/aimldl.github.io/kubeflow/kr/1_environment_setup/images/kubeadm_init-overview.png">

## 다음

* [kubeadm으로 단일 구성 클러스터 생성하기](create_a_single_control_plane_cluster_with_kubeadm_init.md)

## 참고 문서

* [Creating a single control-plane cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/), 쿠버네티스 공식 문서
* [Set up a Bare Metal Kubernetes cluster with kubeadm](https://www.padok.fr/en/blog/kubeadm-kubernetes-cluster)
* [쿠버네티스(kubernetes) 설치 및 환경 구성하기](https://medium.com/finda-tech/overview-8d169b2a54ff)
* [우분투 Kubernetes 설치 방법](https://hiseon.me/linux/ubuntu/ubuntu-kubernetes-install/)
* [11 Ways (Not) to Get Hacked](https://kubernetes.io/blog/2018/07/18/11-ways-not-to-get-hacked/), Kubernetes Blog