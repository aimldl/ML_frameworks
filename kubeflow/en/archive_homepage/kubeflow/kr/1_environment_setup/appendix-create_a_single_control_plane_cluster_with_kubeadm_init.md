* Rev.1: 2020-07-07 (Tue)
* Draft: 2020-07-02 (Thu)

# 부록

* `kubeadm init` 명령어 실행 시 연관있는 항목
* `sudo kubeadm init`명령어의 전체 메세지
* `sudo kubeadm init` 출력 메세지 뒷부분 설명



## `kubeadm init` 명령어 실행 시 연관있는 항목

 `kubeadm init` 명령어는 아래의 복잡한 항목을 간단히 설치해줍니다.

```text
preflight                    Run pre-flight checks
kubelet-start                Write kubelet settings and (re)start the kubelet
certs                        Certificate generation
  /ca                          Generate the self-signed Kubernetes CA to provision identities for other Kubernetes components
  /apiserver                   Generate the certificate for serving the Kubernetes API
  /apiserver-kubelet-client    Generate the certificate for the API server to connect to kubelet
  /front-proxy-ca              Generate the self-signed CA to provision identities for front proxy
  /front-proxy-client          Generate the certificate for the front proxy client
  /etcd-ca                     Generate the self-signed CA to provision identities for etcd
  /etcd-server                 Generate the certificate for serving etcd
  /etcd-peer                   Generate the certificate for etcd nodes to communicate with each other
  /etcd-healthcheck-client     Generate the certificate for liveness probes to healthcheck etcd
  /apiserver-etcd-client       Generate the certificate the apiserver uses to access etcd
  /sa                          Generate a private key for signing service account tokens along with its public key
kubeconfig                   Generate all kubeconfig files necessary to establish the control plane and the admin kubeconfig file
  /admin                       Generate a kubeconfig file for the admin to use and for kubeadm itself
  /kubelet                     Generate a kubeconfig file for the kubelet to use *only* for cluster bootstrapping purposes
  /controller-manager          Generate a kubeconfig file for the controller manager to use
  /scheduler                   Generate a kubeconfig file for the scheduler to use
control-plane                Generate all static Pod manifest files necessary to establish the control plane
  /apiserver                   Generates the kube-apiserver static Pod manifest
  /controller-manager          Generates the kube-controller-manager static Pod manifest
  /scheduler                   Generates the kube-scheduler static Pod manifest
etcd                         Generate static Pod manifest file for local etcd
  /local                       Generate the static Pod manifest file for a local, single-node local etcd instance
upload-config                Upload the kubeadm and kubelet configuration to a ConfigMap
  /kubeadm                     Upload the kubeadm ClusterConfiguration to a ConfigMap
  /kubelet                     Upload the kubelet component config to a ConfigMap
upload-certs                 Upload certificates to kubeadm-certs
mark-control-plane           Mark a node as a control-plane
bootstrap-token              Generates bootstrap tokens used to join a node to a cluster
kubelet-finalize             Updates settings relevant to the kubelet after TLS bootstrap
  /experimental-cert-rotation  Enable kubelet client certificate rotation
addon                        Install required addons for passing Conformance tests
  /coredns                     Install the CoreDNS addon to a Kubernetes cluster
  /kube-proxy                  Install the kube-proxy addon to a Kubernetes cluster
```

참고로 이 중 컨트롤 플레인과 etcd에 해당하는 부분은 아래와 같습니다.

```text
control-plane
  /apiserver
  /controller-manager
  /scheduler
etcd
  /local
```

## `sudo kubeadm init`명령어의 전체 메세지

```bash
$ sudo kubeadm init
[sudo] password for k8smaster: 
W0703 14:55:49.388649   10153 configset.go:202] WARNING: kubeadm cannot validate component configs for API groups [kubelet.config.k8s.io kubeproxy.config.k8s.io]
[init] Using Kubernetes version: v1.18.5
[preflight] Running pre-flight checks
[preflight] Pulling images required for setting up a Kubernetes cluster
[preflight] This might take a minute or two, depending on the speed of your internet connection
[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Starting the kubelet
[certs] Using certificateDir folder "/etc/kubernetes/pki"
[certs] Generating "ca" certificate and key
[certs] Generating "apiserver" certificate and key
[certs] apiserver serving cert is signed for DNS names [k8smaster-gpu-desktop kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local] and IPs [10.96.0.1 192.168.0.109]
[certs] Generating "apiserver-kubelet-client" certificate and key
[certs] Generating "front-proxy-ca" certificate and key
[certs] Generating "front-proxy-client" certificate and key
[certs] Generating "etcd/ca" certificate and key
[certs] Generating "etcd/server" certificate and key
[certs] etcd/server serving cert is signed for DNS names [k8smaster-gpu-desktop localhost] and IPs [192.168.0.109 127.0.0.1 ::1]
[certs] Generating "etcd/peer" certificate and key
[certs] etcd/peer serving cert is signed for DNS names [k8smaster-gpu-desktop localhost] and IPs [192.168.0.109 127.0.0.1 ::1]
[certs] Generating "etcd/healthcheck-client" certificate and key
[certs] Generating "apiserver-etcd-client" certificate and key
[certs] Generating "sa" key and public key
[kubeconfig] Using kubeconfig folder "/etc/kubernetes"
[kubeconfig] Writing "admin.conf" kubeconfig file
[kubeconfig] Writing "kubelet.conf" kubeconfig file
[kubeconfig] Writing "controller-manager.conf" kubeconfig file
[kubeconfig] Writing "scheduler.conf" kubeconfig file
[control-plane] Using manifest folder "/etc/kubernetes/manifests"
[control-plane] Creating static Pod manifest for "kube-apiserver"
[control-plane] Creating static Pod manifest for "kube-controller-manager"
W0703 14:57:09.900821   10153 manifests.go:225] the default kube-apiserver authorization-mode is "Node,RBAC"; using "Node,RBAC"
[control-plane] Creating static Pod manifest for "kube-scheduler"
W0703 14:57:09.901429   10153 manifests.go:225] the default kube-apiserver authorization-mode is "Node,RBAC"; using "Node,RBAC"
[etcd] Creating static Pod manifest for local etcd in "/etc/kubernetes/manifests"
[wait-control-plane] Waiting for the kubelet to boot up the control plane as static Pods from directory "/etc/kubernetes/manifests". This can take up to 4m0s
[apiclient] All control plane components are healthy after 20.002615 seconds
[upload-config] Storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[kubelet] Creating a ConfigMap "kubelet-config-1.18" in namespace kube-system with the configuration for the kubelets in the cluster
[upload-certs] Skipping phase. Please see --upload-certs
[mark-control-plane] Marking the node k8smaster-gpu-desktop as control-plane by adding the label "node-role.kubernetes.io/master=''"
[mark-control-plane] Marking the node k8smaster-gpu-desktop as control-plane by adding the taints [node-role.kubernetes.io/master:NoSchedule]
[bootstrap-token] Using token: zqw1lb.tuhllf8m7zntibcq
[bootstrap-token] Configuring bootstrap tokens, cluster-info ConfigMap, RBAC Roles
[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to get nodes
[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to post CSRs in order for nodes to get long term certificate credentials
[bootstrap-token] configured RBAC rules to allow the csrapprover controller automatically approve CSRs from a Node Bootstrap Token
[bootstrap-token] configured RBAC rules to allow certificate rotation for all node client certificates in the cluster
[bootstrap-token] Creating the "cluster-info" ConfigMap in the "kube-public" namespace
[kubelet-finalize] Updating "/etc/kubernetes/kubelet.conf" to point to a rotatable kubelet client certificate and key
[addons] Applied essential addon: CoreDNS
[addons] Applied essential addon: kube-proxy

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.0.109:6443 --token zqw1lb.tuhllf8m7zntibcq \
    --discovery-token-ca-cert-hash sha256:e3f15962b0535847add930d0e16fe92dc3e7ed139f29e0093e0b0766ca615671
$
```

## `sudo kubeadm init` 출력 메세지 뒷부분 설명

출력 메세지는 초기화 성공 메세지의 앞부분과 뒷부분으로 나뉩니다.

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



### 마스터에서 실행할 명령어

`$HOME/.kube/config`를 설정하고

> To start using your cluster, you need to run the following as a regular user:
>   mkdir -p $HOME/.kube
>   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
>   sudo chown $(id -u):$(id -g) $HOME/.kube/config

Pod Network를 추가합니다.

> You should now deploy a pod network to the cluster.
> Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
>   https://kubernetes.io/docs/concepts/cluster-administration/addons/

### 노드에서 실행할 명령어

> Then you can join any number of worker nodes by running the following on each as root:
> kubeadm join <control-plane-host>:<control-plane-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash>

위의 예에서는

* `control-plane-host`가 `192.168.0.109`
* `control-plane-port`가 `6443`
* `token`이 `zqw1lb.tuhllf8m7zntibcq`
* `hash`가 `e3f15962b0535847add930d0e16fe92dc3e7ed139f29e0093e0b0766ca615671`

입니다. 이럴 경우에 노드에서 실행할 명령어는

```bash
kubeadm join 192.168.0.109:6443 --token zqw1lb.tuhllf8m7zntibcq \
    --discovery-token-ca-cert-hash sha256:e3f15962b0535847add930d0e16fe92dc3e7ed139f29e0093e0b0766ca615671
```

가 됩니다. 

**중요: 이 명령어를 안전하게 관리해야 합니다. 왜냐하면 이 명령어로 누구나 클러스터에 노드를 붙일 수 있기 때문입니다**

#### 각 항목에 대한 설명

##### `control-plane-host`

일반적으로 마스터의 IP주소 입니다. 

##### `control-plane-port`

* 6443포트는 쿠버네티스 API Server 프로세스의 기본 포트 입니다. 
* 만약 마스터에서 실행되는 API Server 프로세스의 포트가 6443이 아니라면, 해당 포트를 기입하면 됩니다.

##### `token`

* 마스터와 노드의 상호 인증을 위해서 토큰이 사용됩니다. 
* 토큰은 기본적으로 24시간 후에 만료됩니다. 

토큰은  `kubeadm token` 명령어로 조작할 수 있습니다.

* 기존 토큰 값 확인: `kubeadm token list`

```bash
$ kubeadm token list
```

* 토큰 신규 생성: `kubeadm token create`

```bash
$ kubeadm token create
W0707 10:53:45.962143    7158 configset.go:202] WARNING: kubeadm cannot validate component configs for API groups [kubelet.config.k8s.io kubeproxy.config.k8s.io]
99xb86.xwgaestxmg3ojlj6
$ sudo kubeadm token create
[sudo] password for k8smaster: 
W0707 10:54:19.640674    7869 configset.go:202] WARNING: kubeadm cannot validate component configs for API groups [kubelet.config.k8s.io kubeproxy.config.k8s.io]
msipgc.59zzy9z3jgfc6zzy
$
```

 상세한 내용은 쿠버네티스 공식 문서의 [kubeadm reference guide](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-token/)를 참고하세요.

##### `hash` 혹은 --discovery-token-ca-cert-hash

해쉬값은 아래 명령어로 확인할 수 있습니다.

```bash
$ openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'
```

출력 메세지는 해쉬값을 리턴합니다.

```bash
e3f15962b0535847add930d0e16fe92dc3e7ed139f29e0093e0b0766ca615671
$
```

## 참고 문서

* [쿠버네티스(kubernetes) 설치 및 환경 구성하기](https://medium.com/finda-tech/overview-8d169b2a54ff)