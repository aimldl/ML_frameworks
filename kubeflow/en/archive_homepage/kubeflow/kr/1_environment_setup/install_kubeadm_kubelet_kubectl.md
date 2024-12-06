* Draft: 2020-07-02 (Thu)

# kubeadm, kubelet, kubectl 설치하기

이 부분은 쿠버네티스 공식 문서의 [Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/) > [Installing kubeadm, kubelet and kubectl](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-kubeadm-kubelet-and-kubectl)에 해당합니다.

## 개요

설치하게 될 각 패키지에 관한 간략할 설명입니다.

* kubeadm은 쿠버네티스 클러스터를 bootstrap하는 명령어입니다.
* kubelet은 모든 노드에 설치되어 포드와 컨테이너를 시작할 때 쓰입니다.
* kubectl은 클러스터와 통신할 때 쓰이는 명령어입니다.

**주의: 모든 패키지 버전이 일치해야 함**

이때 각 패키지의 버전이 일치해야 합니다. 버전이 틀리면 예상치 않은 동작을 할 수 있습니다. 그러므로 쿠버네티스 클러스터의 버전 업그레이드를 할 때에 각별한 주의가 필요합니다. 

자세한 내용은 

* Kubernetes [version and version-skew policy](https://kubernetes.io/docs/setup/release/version-skew-policy/)
* Kubeadm-specific [version skew policy](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#version-skew-policy)
* [Upgrading kubeadm clusters](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/) 

을 참고하세요.

## kubeadm, kubelet, kubectl 설치하기

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

### 마스터 노드

```bash
$ sudo apt-get update && sudo apt-get install -y apt-transport-https curl
  ...
apt-transport-https is already the newest version (1.6.12ubuntu0.1).
curl is already the newest version (7.58.0-2ubuntu3.9).
0 upgraded, 0 newly installed, 0 to remove and 3 not upgraded.
$ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
OK
$ cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
> deb https://apt.kubernetes.io/ kubernetes-xenial main
> EOF
deb https://apt.kubernetes.io/ kubernetes-xenial main
$ sudo apt-get update
  ...
Reading package lists... Done
$ sudo apt-get install -y kubelet kubeadm kubectl
  ...
Setting up kubelet (1.18.5-00) ...
Created symlink /etc/systemd/system/multi-user.target.wants/kubelet.service → /lib/systemd/system/kubelet.service.
Setting up kubeadm (1.18.5-00) ...
Processing triggers for systemd (237-3ubuntu10.38) ...
Processing triggers for ureadahead (0.100.0-20) ...
$ sudo apt-mark hold kubelet kubeadm kubectl
kubelet set on hold.
kubeadm set on hold.
kubectl set on hold.
$
```

### 워커 노드

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
deb https://apt.kubernetes.io/ kubernetes-xenial main
$ sudo apt-get update
  ...
Reading package lists... Done
$ sudo apt-get install -y kubelet kubeadm kubectl
  ...
Setting up kubectl (1.18.5-00) ...
Setting up ethtool (1:4.15-0ubuntu1) ...
Setting up kubelet (1.18.5-00) ...
Created symlink /etc/systemd/system/multi-user.target.wants/kubelet.service → /lib/systemd/system/kubelet.service.
Setting up kubeadm (1.18.5-00) ...
Processing triggers for systemd (237-3ubuntu10.41) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for ureadahead (0.100.0-21) ...
$ sudo apt-mark hold kubelet kubeadm kubectl
kubelet set on hold.
kubeadm set on hold.
kubectl set on hold.
$
```

## 다음

* [kubeadm으로 쿠버네티스 클러스터 생성하기](create_k8s_cluster_with_kubeadm.md)
