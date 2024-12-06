* Rev.3: 2020-07-07 (Tue)
* Rev.2: 2020-07-06 (Mon)
* Rev.1: 2020-07-03 (Fri)
* Draft: 2020-07-02 (Thu)

# kubeadm init으로  단일 구성 클러스터 생성하기

## 개요

앞서 마스터 노드 초기화의 목표에서 마스터 노드로 사용할 컴퓨터의 대수에 따라

* 단일 구성 클러스터(Single Control-Plane Kubernetes Cluster)
* 고가용성 클러스터  (High Availability Kubernetes Cluster)

중 하나를 선택할 수 있고, Pod Network로

* [Canal](https://github.com/tigera/canal/tree/master/k8s-install), [Calico](https://docs.projectcalico.org/latest/introduction/), [Cilium](https://github.com/cilium/cilium), [CNI-Genie](https://github.com/Huawei-PaaS/CNI-Genie), [Contiv](http://contiv.github.io), [Contrail](http://www.juniper.net/us/en/products-services/sdn/contrail/contrail-networking/), [Flannel](https://github.com/coreos/flannel/blob/master/Documentation/kubernetes.md), [Knitter](https://github.com/ZTE/Knitter/), [Multus](https://github.com/Intel-Corp/multus-cni), [OVN4NFV-K8S-Plugin](https://github.com/opnfv/ovn4nfv-k8s-plugin), [NSX-T](https://docs.vmware.com/en/VMware-NSX-T/2.0/nsxt_20_ncp_kubernetes.pdf), [Nuage](https://github.com/nuagenetworks/nuage-kubernetes/blob/v5.1.1-1/docs/kubernetes-1-installation.rst), [Romana](http://romana.io), [Weave Net](https://www.weave.works/docs/net/latest/kube-addon/)

중 하나를 선택할 수 있다고 설명했습니다.

이 부분에서는 단일 구성 클러스터를 생성하고, Calico Pod Network를 구성하는 명령어에 대해 알아봅니다. 그 전에 전제 조건 중 실행해야 하는 명령어를 먼저 요약해봅니다. [kubeadm 설치 전 사전 확인 작업](verify_before_installing_k8s.md) > 4. 스왑 메모리 (Swap Memory) 비활성화에서 이미 설명했지만, 중요하기 때문에 재확인한다는 느낌으로 명령어를 실행해봅니다. 클러스터에 쓸 모든 컴퓨터에서 스왑 메모리를 비활성화하는 두 개 명령어를 실행합니다.

## 전제 조건 (Prerequisites)

꼼꼼히 전제 조건을 재확인하려면, [kubeadm 설치 전 사전 확인 작업](verify_before_installing_k8s.md) > 4. 스왑 메모리 (Swap Memory) 비활성화를 참고하시면 됩니다. 하지만 새로 OS가 설치되었거나, 기존에 있는 OS에 신규 계정을 만든 상태로 네트워크가 잘 동작한다면, 일반적으로 한 가지 조건을 제외하고 나머지 조건은 만족됩니다.

나머지 하나의 조건을 만족시키기 위해서 스왑 메모리를 수동으로 비활성화합니다. 

#### 모든 컴퓨터에서 스왑 메모리 (Swap Memory)를 비활성화

##### Step 1. `swapoff` 명령어로 스왑 메모리를 모두 비활성화

```bash
$ sudo swapoff -a
[sudo] password for k8smaster: 
$
```

##### Step 2. `/etc/fstab`파일의 swap관련 부분을 비활성화

`/etc/fstab`파일을 텍스트 에디터로 열어서, `/swapfile`로 시작하는 swap 관련 부분을 제거하기 위해 줄의 제일 앞에 #를 붙여줍니다.

```bash
$ sudo nano /etc/fstab
```

#####  수정 전

```bash
/swapfile   none   swap   sw   0   0
```

##### 수정 후

```bash
#/swapfile   none   swap   sw   0   0
```

## 마스터 설정: `kubeadm init`의 기본값으로 초기화 하기

`kubeadm init`를 실행할 때는 주의가 필요합니다. 왜냐하면 다시 실행하기 위해선 먼저 클러스터를 해체해야 하기 때문입니다. 상세한 내용은 쿠버네티스 공식 문서의 [Creating a single control-plane cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) > [tear down the cluster](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#tear-down)를 참고하세요.

#### Step 1. `$ sudo kubeadm init` 명령어 실행

```bash
$ sudo kubeadm init
```

##### `$ sudo kubeadm init` 명령어의 출력 메세지에 대한 설명

명령어를 실행하면 아래와 같은 메세지가 출력됩니다.

```bash
  ...
Your Kubernetes control-plane has initialized successfully!
  ...
$
```

초기화 성공 메세지의 앞부분은

* 쿠버네티스 설치 가능 여부를 사전 체크하고,
* 컨트롤 플레인 요소를 다운로드하고 설치한

결과가 출력됩니다. 설치를 진행하기에 문제가 있을 경우, 사전 체크 과정에서 warning이나 error를 출력하고 exit 됩니다. 메세지가 나왔다는 것은 이 과정을 문제없이 통과했다는 것을 의미합니다.

초기화 성공 메세지의 뒷부분은 

* 남은 작업을 위해서 마스터와 노드에서 실행할 명령어를 보여줍니다.

#### Step 2. `$HOME/.kube/config`를 설정

마스터에서 아래의 명령어를 실행합니다. 이것은 `$ sudo kubeadm init` 의 출력 결과에 있는 명령어와 동일합니다.

```bash
$ mkdir -p $HOME/.kube
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

##### 명령어에 대한 설명

root 계정이 아닌 일반 사용자 계정으로 클러스터를 제어하기 위한 설정입니다. 제어를 위해선 `kubectl` 커맨드 명령어를 사용하게 됩니다.

일반 사용자 계정으로 `$HOME/.kube` 디렉토리를 만든 후, `/etc/kubernetes/admin.conf`의 내용을 `$HOME/.kube/config`으로 복사합니다. 마지막 명령어는 파일의 권한을 일반 사용자 계정으로 변경합니다. 이것이 없다면 파일을 쓰기 위해 루트 권한이 필요합니다.

```bash
$ cat config
cat: config: Permission denied
$
```

#### Step 3. Pod Network로 calico를 추가

```bash
$ kubectl apply -f [podnetwork].yaml
```

`podnetwork`로 기본인 calico를 선택할 경우에 아래 명령어를 실행합니다.

```bash
$ sudo kubectl apply -f https://docs.projectcalico.org/v3.14/manifests/calico.yaml
```

출력 메세지는 다음과 같습니다.

```bash
[sudo] password for k8smaster: 
configmap/calico-config created
customresourcedefinition.apiextensions.k8s.io/bgpconfigurations.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/bgppeers.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/blockaffinities.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/clusterinformations.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/felixconfigurations.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/globalnetworkpolicies.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/globalnetworksets.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/hostendpoints.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/ipamblocks.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/ipamconfigs.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/ipamhandles.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/ippools.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/kubecontrollersconfigurations.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/networkpolicies.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/networksets.crd.projectcalico.org created
clusterrole.rbac.authorization.k8s.io/calico-kube-controllers created
clusterrolebinding.rbac.authorization.k8s.io/calico-kube-controllers created
clusterrole.rbac.authorization.k8s.io/calico-node created
clusterrolebinding.rbac.authorization.k8s.io/calico-node created
daemonset.apps/calico-node created
serviceaccount/calico-node created
deployment.apps/calico-kube-controllers created
serviceaccount/calico-kube-controllers created
$
```

다른 `podnetwork`을 선택할 경우의 명령어는 다음 파트에서 설명합니다.

노드에서는 이 명령어를 실행하지 않습니다. 참고로 아래는 클러스터가 설정된 후에 실행한 결과입니다. 

```bash
$ sudo kubectl apply -f https://docs.projectcalico.org/v3.14/manifests/calico.yaml
[sudo] password for k8snode: 
The connection to the server localhost:8080 was refused - did you specify the right host or port?
$
```

어찌보면 당연한 얘기지만 클러스터 설정 과정의 불확실성을 명확해 덧붙입니다.

#### Step 4. 클러스터 노드 정보를 확인

`kubectl get nodes`명령어로 클러스터 노드 정보를 확인해봅니다.

```bash
$ kubectl get nodes
NAME                    STATUS   ROLES    AGE   VERSION
k8smaster-gpu-desktop   Ready    master   4h    v1.18.5
$
```

현재로썬 마스터 하나만 있습니다.

## 노드 설정:  `kubeadm join`명령어로 클러스터에 조인 (join)하기

앞서 생성된 클러스터에 노드를 조인 (join) 하기 위해,   `kubeadm join`명령어를 실행합니다. 상세한 내용은 쿠버네티스 공식 문서의 [Creating a single control-plane cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) > [join nodes to your cluster](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#join-nodes)를 참고하세요.

#### Step 1.  노드에서 `kubeadm join`명령어 실행

```bash
$ kubeadm join <control-plane-host>:<control-plane-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

에 해당하는 명령어를 실행합니다. 구체적인 파라미터 값은 마스터에서 `kubeadm init` 명령어 실행 시 출력됩니다. 예를 들면,

```bash
$ sudo kubeadm join 192.168.0.109:6443 --token zqw1lb.tuhllf8m7zntibcq \
    --discovery-token-ca-cert-hash sha256:e3f15962b0535847add930d0e16fe92dc3e7ed139f29e0093e0b0766ca615671
```

출력 메세지는

```bash
[sudo] password for k8snode: 
W0703 19:13:46.603764   24337 join.go:346] [preflight] WARNING: JoinControlPane.controlPlane settings will be ignored when control-plane flag is not set.
[preflight] Running pre-flight checks
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -oyaml'
[kubelet-start] Downloading configuration for the kubelet from the "kubelet-config-1.18" ConfigMap in the kube-system namespace
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Starting the kubelet
[kubelet-start] Waiting for the kubelet to perform the TLS Bootstrap...

This node has joined the cluster:
* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the control-plane to see this node join the cluster.
$
```

이 노드가 클러스터에 조인 (join) 했고, 확인하려면 컨트롤 플레인 (the control-plane), 즉 마스터에서 `kubectl get nodes`명령어를 실행하라는 메세지가 출력됐습니다. 이렇게 해서 단일 구성 클러스터의 생성을 완료했습니다. 

## (선택) 클러스터 상태 확인

아직 생성된 클러스터에 대한 감이 없으므로, 클러스터의 상태를 보는 것으로 클러스터가 잘 설정되었음을 확인합니다.

### 마스터에서 클러스터 정보를 확인

 `kubectl get nodes`명령어를 실행해보면 node가 추가되었음을 알 수 있습니다.

```bash
$ kubectl get nodes
NAME                     STATUS   ROLES    AGE     VERSION
k8smaster-gpu-desktop    Ready    master   3d22h   v1.18.5
k8snode-01-gpu-desktop   Ready    <none>   3d18h   v1.18.5
$
```

참고로 노드에서 같은 명령어를 실행하면 에러 메세지가 나옵니다.

```bash
$ kubectl get nodes
The connection to the server localhost:8080 was refused - did you specify the right host or port?
$
```

### 클러스터에 설치된 파드 (Pod)를 확인

쿠버네티스 클러스터의 아키텍쳐를 참고해서 설치된 파드를 확인해봅니다. 참고로 컨테이너를 실행시키는 최소 단위인 파드는 생성/소멸을 반복할 수 있고, 서로 통신할 수 있도록 Pod Network가 형성됩니다. Pod Network와 CNI Network는 동의어입니다.

<img src="images/kubernetes_architecture.jpg">

Source: [Kubernetes architecture and concepts tutorial - Kubernetes Administration for beginners(9:18)](https://www.youtube.com/watch?v=oFglQ50O_rU)

`kubectl get pod` 명령어로 설치된 파드 (Pod)를 확인했을 때의 출력입니다. 한 행이 한 줄에 보이도록 각 열의 간격을 조절했습니다.

```bash
$ kubectl get pod --namespace=kube-system -o wide
NAME                                          READY STATUS RESTARTS AGE    IP            NODE          NOMINATED NODE READINESS GATES
calico-kube-controllers-76d4774d89-wp8zx      1/1  Running  0       3d15h  172.16.37.65  k8smaster-gpu-desktop  <none>  <none>
calico-node-rcrvd                             1/1  Running  1       3d15h  192.168.0.118 k8snode-01-gpu-desktop <none>  <none>
calico-node-w5swf                             1/1  Running  0       3d15h  192.168.0.109 k8smaster-gpu-desktop  <none>  <none>
coredns-66bff467f8-dh65v                      1/1  Running  0       3d19h  172.16.37.66  k8smaster-gpu-desktop  <none>  <none>
coredns-66bff467f8-mb2mm                      1/1  Running  0       3d19h  172.16.37.67  k8smaster-gpu-desktop  <none>  <none>
etcd-k8smaster-gpu-desktop                    1/1  Running  0       3d19h  192.168.0.109 k8smaster-gpu-desktop  <none>  <none>
kube-apiserver-k8smaster-gpu-desktop          1/1  Running  0       3d19h  192.168.0.109 k8smaster-gpu-desktop  <none>  <none>
kube-controller-manager-k8smaster-gpu-desktop 1/1  Running  1       3d19h  192.168.0.109 k8smaster-gpu-desktop  <none>  <none>
kube-proxy-qmnxq                              1/1  Running  1       3d15h  192.168.0.118 k8snode-01-gpu-desktop <none>  <none>
kube-proxy-rx7sl                              1/1  Running  0       3d19h  192.168.0.109 k8smaster-gpu-desktop  <none>  <none>
kube-scheduler-k8smaster-gpu-desktop          1/1  Running  1       3d19h  192.168.0.109 k8smaster-gpu-desktop  <none>  <none>
$
```

노드에는 두 가지 파드가 있습니다.

* Pod Network를 위한 `calico-node-rcrvd`
* Service proxy를 위한 `kube-proxy-qmnxq`

[TODO: Kubelet이 보이지 않는 이유가 궁금하네요.]

```bash
$ kubectl get pod --namespace=kube-system -o wide | grep k8snode
calico-node-rcrvd                             1/1  Running  1       3d15h  192.168.0.118 k8snode-01-gpu-desktop <none>  <none>
kube-proxy-qmnxq                              1/1  Running  1       3d15h  192.168.0.118 k8snode-01-gpu-desktop <none>  <none>
$
```

마스터에는

* Pod Network를 위한 
  * `calico-kube-controllers-76d4774d89-wp8zx`
  * `calico-node-w5swf`
* Service proxy를 위한 `kube-proxy-rx7sl`

* DNS를 위한
  * `coredns-66bff467f8-dh65v`
  * `coredns-66bff467f8-mb2mm`

그리고 컨트롤 플레인 요소

* kubectl 명령어와 커뮤니케이션을 위해 쓰이는 API Server를 위한 `kube-apiserver-k8smaster-gpu-desktop`
* Controller Manager를 위한 `kube-controller-manager-k8smaster-gpu-desktop`
* 클러스터 데이터 베이스 etcd를 위한 `etcd-k8smaster-gpu-desktop`
* Scheduler를 위한 `kube-scheduler-k8smaster-gpu-desktop`

가 있습니다.

```bash
$ kubectl get pod --namespace=kube-system -o wide | grep k8smaster
NAME                                          READY STATUS RESTARTS AGE    IP            NODE          NOMINATED NODE READINESS GATES
calico-kube-controllers-76d4774d89-wp8zx      1/1  Running  0       3d15h  172.16.37.65  k8smaster-gpu-desktop  <none>  <none>
calico-node-w5swf                             1/1  Running  0       3d15h  192.168.0.109 k8smaster-gpu-desktop  <none>  <none>
coredns-66bff467f8-dh65v                      1/1  Running  0       3d19h  172.16.37.66  k8smaster-gpu-desktop  <none>  <none>
coredns-66bff467f8-mb2mm                      1/1  Running  0       3d19h  172.16.37.67  k8smaster-gpu-desktop  <none>  <none>
etcd-k8smaster-gpu-desktop                    1/1  Running  0       3d19h  192.168.0.109 k8smaster-gpu-desktop  <none>  <none>
kube-apiserver-k8smaster-gpu-desktop          1/1  Running  0       3d19h  192.168.0.109 k8smaster-gpu-desktop  <none>  <none>
kube-controller-manager-k8smaster-gpu-desktop 1/1  Running  1       3d19h  192.168.0.109 k8smaster-gpu-desktop  <none>  <none>
kube-proxy-rx7sl                              1/1  Running  0       3d19h  192.168.0.109 k8smaster-gpu-desktop  <none>  <none>
kube-scheduler-k8smaster-gpu-desktop          1/1  Running  1       3d19h  192.168.0.109 k8smaster-gpu-desktop  <none>  <none>
$
```

## 다음

* [클러스터에 붙은 노드 구성 검증하기](validate_node_setup.md)
* [부록: `kubeadm init` 명령어](appendix-create_a_single_control_plane_cluster_with_kubeadm_init.md)
  * `kubeadm init` 명령어 실행 시 연관있는 항목
  * `sudo kubeadm init`명령어의 전체 메세지
  * `sudo kubeadm init` 출력 메세지 뒷부분 설명

## 참고 문서

* [Set up a Bare Metal Kubernetes cluster with kubeadm](https://www.padok.fr/en/blog/kubeadm-kubernetes-cluster)
* [쿠버네티스(kubernetes) 설치 및 환경 구성하기](https://medium.com/finda-tech/overview-8d169b2a54ff)
* [우분투 Kubernetes 설치 방법](https://hiseon.me/linux/ubuntu/ubuntu-kubernetes-install/)