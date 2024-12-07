* Rev.1: 2020-07-03 (Fri)
* Draft: 2020-07-02 (Thu)

# kubeadm init args로  단일 구성 클러스터 생성하기

TODO:

$ sudo kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

### 옵션 값을 주고 초기화 하기

```bash
$ sudo kubeadm init <args>
```

`<args>`에 들어가는 적절한 옵션을 선택하기 위해서 초기화 과정에 대한 이해가 필요합니다. 몇 가지 항목에 대해 소개합니다.

##### --pod-network-cidr로 Pod Network 설정

 [Calico](https://docs.projectcalico.org/latest/introduction/) 외에 필요에 맞는 다른 옵션을 `--pod-network-cidr`을 써서 선택할 수 있습니다. CIDR (Classless Inter-Domain Routing)은 IP주소를 자동으로 할당하고 IP 라우팅을 하는 네트워크 프로토콜입니다. Pod Network에서 신규 생성되는 파드 (Pod)에 IP주소를 할당하게 되는데, Pod Network에서 쓰일 IP주소의 범위를 지정하기 위해 CIDR이 쓰일 수 있습니다. CIDR로 설정이 되면 마스터 노드가 모든 노드의 IP주소를 할당하게 됩니다. 

IP주소의 범위를 지정하는 예로  `Flannel`을 사용할 때 쓰이는 옵션인 `10.244.0.0/16`가 쓰일 수 있습니다.

```bash
$ sudo kubeadm init --pod-network-cidr=10.244.0.0/16
```

`10.244.0.0/16`은 호스트 네트워크로 잘 사용되지 않는 대역으로 `Flannel`에서 권장합니다. 만약 호스트 네트워크에서 `10.244.0.0/16`를 사용하고 있다면, 다른 네트워크 대역 `--pod-network-cidr=v.w.x.y/z`을 지정해야 합니다.

Pod Network과 호스트 네트워크가  겹치면 문제가 발생할 수 있으므로 재확인이 필요합니다. 이 예제에서 마스터 노드로 사용할 컴퓨터의 IP주소를 확인해보면

```bash
$ ifconfig | grep inet
  ...
        inet 192.168.0.xyz  netmask 255.255.255.0  broadcast 192.168.0.255
$
```

`192.168.0.xyz`로  `Flannel` 권장 네트워크 대역과 다름을 알수 있습니다. 

방화벽을 사용할 경우, 방화벽 규칙이 UDP 8285, 8472 포트를 허용해야 합니다. `Flannel`은  캡슐화된 패킷을 

* UDP 백엔드로 보내기 위해 UDP 8285 포트를
* (커널이) vxlan 백엔드로 보내기 위해 UDP 8472 포트를 

사용합니다.

`--pod-network-cidr`에 관한 자세한 내용은 아래를 참고하세요.

* [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
* [Installing Addons](https://kubernetes.io/docs/concepts/cluster-administration/addons/)
* [Creating a single control-plane cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)의 [Installing a Pod network add-on](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#pod-network)

##### Container 관련: --cri-socket option로 컨테이너 런타임 인터페이스 (CRI) 설정

컨테이너 런타임의 기본값은 Docker입니다. 그 외에 [CRI-O](https://cri-o.io/), [rkt](https://coreos.com/rkt/), [containerd](https://containerd.io/)를 선택할 수 있습니다. 일반적으로 Docker를 쓰기 때문에 옵션을 변경할 필요는 없습니다.

##### API Server 관련: --apiserver-advertise-address로 마스터 노드의 API Server 주소 설정 

기본적으로 마스터 노드의 IP주소를 API Server의 advertise address로 설정합니다. 이 옵션은 마스터 노드의 IP주소가 아닌 다른 IP주소를  API Server의 advertise address로 설정할 때 쓰입니다. 일반적으로 기본값을 쓰기 때문에 옵션을 변경할 필요는 없습니다.

##### Scheduler 관련

기본적으로 `kubeadm init`을 실행하면 `node-role.kubernetes.io/master:NoSchedule`로 설정됩니다. 마스터를 노드 역할로 쓰지 않겠다는 의미로, 마스터는 작업을 수행하는데 쓰이지 않습니다. 다수의 워커노드를 사용할 경우는 마스터의 안정성을 위해서 좋지만, 마스터 1대와 노드 1대만 있을 경우에는 문제가 될 수 있습니다. 

##### --control-plane-endpoint로 컨트롤 플레인 엔드포인트 설정

컨트롤 플레인 노드는 마스터 노드의 동의어입니다.  고가용성 클러스터 설정할 때 마스터 노드를 다중화하게 됩니다. 이 옵션은 하나의 IP주소 혹은 DNS명으로 모든 마스터 노드의 공유 엔드포인트를 설정할 때 쓰입니다. 만약 하나의 마스터 노드만 가지는 클러스터를 형성할 때는 쓰이지 않습니다.

## <img src="/home/k8smaster/github/aimldl.github.io/kubeflow/kr/1_environment_setup/images/kubernetes_architecture.jpg">

Source: [Kubernetes architecture and concepts tutorial - Kubernetes Administration for beginners(9:18)](https://www.youtube.com/watch?v=oFglQ50O_rU)

##### 별도의 네트워크 플러그인을 위한 Add-on 설치에 관해서

쿠버네티스에서 기본으로 제공하는 kubenet을 써도 되지만, 간단한 기능을 제공하는 네트워크 플러그인으로 네트워크 정책 설정 등 고급 기능이 필요할 경우엔 별도의 Add-on을 설치해야 합니다. 고급 기능 설정까지 이 단계에서 알아보면 복잡해지므로 일단은 kubenet을 사용해서 클러스터 설정을 진행합니다.

자세한 내용은 쿠버네티스 공식 문서의 [Creating a single control-plane cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) > [Installing a Pod network add-on](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)을 참고하세요.

### `kubeadm init`와 `kubeadm init <args>`의 비교

설정을 기본값을 쓸 수도, 옵션을 써서 변경할 수도 있습니다. 앞서 나온 몇 가지 변경 옵션을 정리해봅니다.  나머지 모든 옵션에 대해서는 [kubeadm init](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/)을 참고하세요.

| 항목                                                    | 기본값: kubeadm init                | 변경 옵션: kubeadm init <args>             | 일반적인 선택                |
| ------------------------------------------------------- | ----------------------------------- | ------------------------------------------ | ---------------------------- |
| CRI 컨테이너 런타임 인터페이스                          | Docker                              | --cri-socket option                        | 기본값                       |
| Pod Network 설정                                        | Calico                              | --pod-network-cidr                         | 기본값, Flannel, Weave Net   |
| API Server의 Advertise Address                          | 노드로 쓰이는 컴퓨터의 기본 IP주소  | --apiserver-advertise-address=<ip-address> | 기본값                       |
| 고가용성 클러스터 설정 시 컨트롤 플레인 엔드포인트 설정 | (하나의 마스터 노트 사용 시 미사용) | --control-plane-endpoint                   | 테스트용: 미사용, 상용: 사용 |

1. (Recommended) If you have plans to upgrade this single control-plane `kubeadm` cluster to high availability you should specify the `--control-plane-endpoint` to set the shared endpoint for all control-plane nodes. Such an endpoint can be either a DNS name or an IP address of a load-balancer.

   Later you can modify `cluster-endpoint` to point to the address of your load-balancer in an high availability scenario.

2. Choose a Pod network add-on, and verify whether it requires any arguments to be passed to `kubeadm init`. Depending on which third-party provider you choose, you might need to set the `--pod-network-cidr` to a provider-specific value. See [Installing a Pod network add-on](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#pod-network).

3. (Optional) Since version 1.14, `kubeadm` tries to detect the container runtime on Linux by using a list of well known domain socket paths. To use different container runtime or if there are more than one installed on the provisioned node, specify the `--cri-socket` argument to `kubeadm init`. See [Installing runtime](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-runtime).

4. (Optional) Unless otherwise specified, `kubeadm` uses the network interface associated with the default gateway to set the advertise address for this particular control-plane node's API server. To use a different network interface, specify the `--apiserver-advertise-address=<ip-address>` argument to `kubeadm init`. To deploy an IPv6 Kubernetes cluster using IPv6 addressing, you must specify an IPv6 address, for example `--apiserver-advertise-address=fd00::101`

5. (Optional) Run `kubeadm config images pull` prior to `kubeadm init` to verify connectivity to the gcr.io container image registry.