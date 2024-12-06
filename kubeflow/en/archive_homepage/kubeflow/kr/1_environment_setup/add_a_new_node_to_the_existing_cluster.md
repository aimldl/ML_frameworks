* Rev.1: 2020-07-21 (Tue)
* Draft: 2020-07-07 (Tue)

# 클러스터에 신규 노드 조인 (Join)하기
기존에 생성된 클러스터에 노드를 새로 조인 (Join) 해봅니다.

## Executive Summary
### 1. Install the common parts
```bash
install_common_parts() {  # used both for master and worker ndoes
  printf "\nInstalling the common parts...\n"
  deactivate_swap_memory
  safe_install_docker
  install_kubeadm_kubelet_kubectl
}
```
### 2. Join a workder node to the Kubernetec Cluster
```bash
$ sudo kubeadm join 123.456.7.890:6443 --token 511z8u.52isecvhqz3zut7b \
    --discovery-token-ca-cert-hash sha256:2b1881f6ce22a61bca221b5482421b41b268eb08d43a7667bcf81696bd90d50b 
```

## 신규 계정 만들기

쿠버네티스 전용으로 사용할 계정과 패스워드를 생성합니다. 

Step 1. 새로운 컴퓨터의 기존 계정에 로그인합니다.

Step 2. 터미널을 열고, `adduser` 명령어에 신규 계정의 이름을 입력합니다. 

```bash
$ sudo adduser k8snode
```

여기에선 k8snode를 계정 이름으로 씁니다. k8s는 Kubernetes의 축약어입니다.

패스워드도 입력합니다.

Step 3. 기존 계정을 로그 아웃합니다.

Step 4. 새로 만들 계정과 패스워드를 써서 다시 로그인합니다.

새로운 환경이 만들어졌습니다.



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
/swapfile                                 none            swap    sw              0       0
```

##### 수정 후

```bash
#/swapfile                                 none            swap    sw              0       0
```

## 컨테이너 런타임 (Container Runtime) 설치하기

### 1. Docker 설치 여부 확인하기

$ hostname
k8snode-01-gpu-desktop
$ docker --version
Docker version 19.03.11, build 42e35e61f3
$

$ sudo docker run hello-world


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

### 2. Docker 설치하기

여기까지는 앞에 sudo 를 붙이는 경우도 설명을 합니다만, 앞으로는 root계정으로 명령어를 실행할 것을 권장합니다. 앞으로는 root계정으로 로그인한 것을 가정합니다.

### `root` 계정으로 로그인 하기

`sudo -i` 혹은 `sudo -s` 명령어로 `root` 계정으로 로그인할 수 있습니다.

```bash
$ sudo -i
[sudo] password for k8smaster: 
$

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

### kubeadm, kubelet, kubectl 설치하기

모든 컴퓨터에 kubeadm, kubelet, kubectl를 설치합니다. 

```bash
$ sudo apt-get update && sudo apt-get install -y apt-transport-https curl
$ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
$ cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
$ sudo apt-get update
$ sudo apt-get install -y kubelet kubeadm kubectl
$ sudo apt-mark hold kubelet kubeadm kubectl
```

The kubelet is now restarting every few seconds, as it waits in a crashloop for kubeadm to tell it what to do.

워커 노드
```bash
$ sudo apt-get update && sudo apt-get install -y apt-transport-https curl
  ...
curl is already the newest version (7.58.0-2ubuntu3.9).
apt-transport-https is already the newest version (1.6.12ubuntu0.1).
0 upgraded, 0 newly installed, 0 to remove and 11 not upgraded.
$ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
OK
$ cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
> deb https://apt.kubernetes.io/ kubernetes-xenial main
> EOF
> deb https://apt.kubernetes.io/ kubernetes-xenial main
> $ sudo apt-get update
> ...
> Reading package lists... Done
> $ sudo apt-get install -y kubelet kubeadm kubectl
> ...
> Setting up kubectl (1.18.5-00) ...
> Setting up ethtool (1:4.15-0ubuntu1) ...
> Setting up kubelet (1.18.5-00) ...
> Created symlink /etc/systemd/system/multi-user.target.wants/kubelet.service → /lib/systemd/system/kubelet.service.
> Setting up kubeadm (1.18.5-00) ...
> Processing triggers for systemd (237-3ubuntu10.41) ...
> Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
> Processing triggers for ureadahead (0.100.0-21) ...
> $ sudo apt-mark hold kubelet kubeadm kubectl
> kubelet set on hold.
> kubeadm set on hold.
> kubectl set on hold.
> $
```

## 설정값 확인

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
TOKEN                     TTL         EXPIRES                     USAGES                   DESCRIPTION                                                EXTRA GROUPS
99xb86.xwgaestxmg3ojlj6   16h         2020-07-08T10:53:45+09:00   authentication,signing   <none>                                                     system:bootstrappers:kubeadm:default-node-token
msipgc.59zzy9z3jgfc6zzy   16h         2020-07-08T10:54:19+09:00   authentication,signing   <none>                                                     system:bootstrappers:kubeadm:default-node-token
te578q.hqpe7yaby5ikdxav   17h         2020-07-08T10:54:52+09:00   authentication,signing   <none>                                                     system:bootstrappers:kubeadm:default-node-token
$
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

```bash
$ sudo kubectl get nodes
[sudo] password for k8smaster: 
NAME                     STATUS     ROLES    AGE     VERSION
atckevin                 NotReady   <none>   54s     v1.18.5
k8smaster-gpu-desktop    Ready      master   4d3h    v1.18.5
k8snode-01-gpu-desktop   Ready      <none>   3d22h   v1.18.5
$
```

<img src="images/kubernetes-dashboard-cluster_nodes-atc_kevin-not_ready.png">

## Next
* [Match the versions of Docker-Kubernetes-Kubeflow Chain](match_the_versions_of_docker-kubernetes-kubeflow_chain.md)
