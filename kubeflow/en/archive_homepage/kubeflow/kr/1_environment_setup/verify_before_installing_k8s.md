* Rev.2: 2020-07-15 (Wed)
* Rev.1: 2020-07-02 (Thu)
* Draft: 2020-07-01 (Wed)

# 쿠버네티스 설치 전 확인 작업

아래는  [Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)에서 해당하는 내용입니다.

## OS 설치

- Ubuntu 16.04+
- Debian 9+
- CentOS 7
- Red Hat Enterprise Linux (RHEL) 7
- Fedora 25+
- HypriotOS v1.0.1+
- Container Linux (tested with 1800.6.0)

## 최소 요건

* 각 컴퓨터 혹은 노드의
  * CPU가 2개 이상 이다.
  * RAM이 2 GB 이상 이다.
  * hostname, MAC주소, product_uuid가 고유하다. ([here](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#verify-mac-address) 참조)
  * 특정 포트가 개방되야 한다. ([here](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#check-required-ports) 참조)
  * **swap의 기능이 꺼져있다.**
* 클러스터의 컴퓨터 혹은 노드가 모두 네트워크로 연결될 수 있어야 한다.
  * public network 혹은 private network 상관 없음.

**중요: 각 컴퓨터에 설치될 kubelet이 정상 동작하려면 swap의 기능이 꺼져있어야만 합니다**

## 1. hostname, MAC주소, product_uuid의 고유성

각 노드의 hostname, MAC주소, product_uuid이 고유한지 확인합니다.

마스터로 사용할 컴퓨터

```bash
$ hostname
GPU-Desktop
$ ip link | grep "link"
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    link/ether 14:b3:1f:22:ef:e3 brd ff:ff:ff:ff:ff:ff
    link/ether 9c:b6:d0:ea:33:89 brd ff:ff:ff:ff:ff:ff
    link/ether 02:42:fb:71:1f:45 brd ff:ff:ff:ff:ff:ff
$ sudo cat /sys/class/dmi/id/product_uuid
[sudo] password for k8smaster: 
4C4C4544-0053-3910-8030-C3C04F314C32
$
```

워커 노드로 사용할 컴퓨터

```bash
$ hostname
k8snode-01-gpu-desktop
$ ip link | grep "link"
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    link/ether d8:9e:f3:7b:49:2e brd ff:ff:ff:ff:ff:ff
    link/ether 9c:b6:d0:f5:7e:21 brd ff:ff:ff:ff:ff:ff
$ sudo cat /sys/class/dmi/id/product_uuid
[sudo] password for k8snode: 
4C4C4544-004B-3110-8059-C4C04F504D32
$
```

## 2. 네트워크 어댑터 (Network Adapter) 확인

쿠버네티스 클러스터 주소가 적합한 네트워크 어댑터를 지나갈 수 있도록 IP루트 (IP route)를 추가하기를 추천합니다. 만약 컴퓨터에 꽂힌 네크워크 카드가 한 개 이상일 경우, 쿠버네티스 구성요소들 (Kubernetes Components)이 디폴트 경로 (default route)로 데이터를 주고 받을 수 없을 수 있습니다.

TODO: 공식 문서의 설명이 부족하므로 필요 시 내용 추가.

### 2.1. Linux노드의 iptables이 bridged traffic을 볼 수 있도록 설정되었는지 확인

#### 2.1.1. `br_netfilter` 모듈이 로딩되었는지 확인

```bash
$ lsmod | grep br_netfilter
br_netfilter           24576  0
bridge                155648  1 br_netfilter
$
```

로딩이 안 되었다면, 아래 명령어로 로딩합니다.

```bash
$ sudo modprobe br_netfilter 
```

더 상세한 내용은 [Network Plugin Requirements](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/#network-plugin-requirements)를 참고하세요

#### 2.1.2. `net.bridge.bridge-nf-call-iptables`이 1로 설정되었는지 확인

아래 명령어를 실행하기 전에 `br_netfilter` 모듈이 로딩되어 있어야 합니다.

```bash
$ cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
$ sudo sysctl --system
```

위의 명령어는 `/etc/sysctl.d/k8s.conf` 을 생성합니다. 파일 내용은 아래와 같습니다.

```bash
$ cat /etc/sysctl.d/k8s.conf 
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
$
```

`sysctl`명령어을 실행하면  `/etc/sysctl.d/k8s.conf` 의 설정파일이 적용된 것을 확인할 수 있습니다.

```bash
$ sudo sysctl --system
  ...
* Applying /etc/sysctl.d/k8s.conf ...
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
* Applying /etc/sysctl.conf ...
$
```

## 3. 필요한 필수 포트의 개방 여부를 확인

* 마스터 노드는 6443, 2379-2380, 10250-10252 포트가 필요
* 워커 노드는 10250, 30000-23767 포트가 필요



마스터 노트 (Master Node or Control-Plane Node)

| Protocol | Direction | Port Range | Purpose                 | Used By              |
| -------- | --------- | ---------- | ----------------------- | -------------------- |
| TCP      | Inbound   | 6443*      | Kubernetes API server   | All                  |
| TCP      | Inbound   | 2379-2380  | etcd server client API  | kube-apiserver, etcd |
| TCP      | Inbound   | 10250      | Kubelet API             | Self, Control plane  |
| TCP      | Inbound   | 10251      | kube-scheduler          | Self                 |
| TCP      | Inbound   | 10252      | kube-controller-manager | Self                 |

*가 붙은 포트 (6443)는 덮어쓸 수 있으므로, 이 포트를 쓸 수 있는지 확인해야 합니다.

TODO: 확인하는 명령어가 공식 문서에 없으므로 추가해야 함

워커 노드 (Worker Node)

| Protocol | Direction | Port Range  | Purpose            | Used By             |
| -------- | --------- | ----------- | ------------------ | ------------------- |
| TCP      | Inbound   | 10250       | Kubelet API        | Self, Control plane |
| TCP      | Inbound   | 30000-32767 | NodePort Services† | All                 |

## 4. 스왑 메모리 (Swap Memory) 비활성화

쿠버네티스의 주요 구성 요소 중의 하나인 kubelet은 스왑 메모리를 지원하지 않도록 개발되었습니다. 그러므로 스왑 메모리를 비활성화해야 합니다. 

### Step 1. 스왑 메모리를 모두 비활성화합니다.

```bash
$ sudo swapoff -a
[sudo] password for k8smaster: 
$
```

> swapon, swapoff - enable/disable devices and files for paging and swapping
>
> Enable/disable all:
>
> $ swapon -a [-e] [-f] [-v]
> $ swapoff -a [-v]
>
> **-a, --all**
>
> All devices marked as ''swap'' in */etc/fstab* are made available, except for those with the ''noauto'' option. Devices that are already being used as swap are silently skipped.
>
> Source: [swapoff(8) - Linux man page](https://linux.die.net/man/8/swapoff)

### Step 2. `/etc/fstab`파일의 swap관련 부분을 비활성화합니다.

`/etc/fstab`파일을 텍스트 에디터로 열면

```bash
$ sudo nano /etc/fstab
```

 아래와 같습니다.

```bash
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/nvme0n1p1 during installation
UUID=68661764-1b74-4ecb-971a-c92568eb8282 /               ext4    errors=remount-ro 0       1
/swapfile                                 none            swap    sw              0       0
```

두번째 줄의 `/swapfile`로 시작되는 하는 곳이 swap 관련 부분입니다. 이 부분을 제거하기 위해 줄의 제일 앞에 #를 붙여줍니다.

```bash
#/swapfile                                 none            swap    sw              0       0
```

#### 주의:  `/etc/fstab`파일을 수동으로 비활성화하는 것을 권장합니다.

아래처럼 `sed`명령어를 이용해서 `/etc/fstab`파일의 열번째 줄의 제일 앞부분에 #를 붙여줄 수도 있지만, 위처럼 수동으로 비활성화하는 것을 권장합니다. 왜냐하면 만약 두번째 줄에 `/swapfile`이 아닌 루트 파티션에 관한 내용이 있다면 아주 위험한 결과를 초래할 수 있기 때문입니다.

```bash
$ sudo sed -i '10s/^/#/' /etc/fstab
```

[다른 블로그](https://medium.com/finda-tech/overview-8d169b2a54ff)의 명령어를 참고하다가  `sed`명령어를 이용하는 경우만 설명하는 경우를 본 적이 있습니다. 이 블로그에는 열번째 줄이 아닌 두번째 줄에 #을 붙이도록 되어 있습니다.  

```bash
$ sudo sed -i '2s/^/#/' /etc/fstab
```

Ubuntu 18.04 LTS버전임에도 `/etc/fstab`에서 `/swapfile`이 있는 줄의 수가 달라진 경우가 있다는 것으로 유추할 수 있습니다. 이렇게 줄이 틀리면 스왑메모리 비활성화가 되지 않아, 나중에 쿠버네티스 클러스터를 사용할 때 오동작을 할 수 있습니다. 그러므로 어차피 텍스트 에디터로 `/etc/fstab`파일을 열어서 확인해야 하기 때문에 그냥 수동으로 비활성화하는 것을 권장합니다.

## 5. 노드 간의 네트워크 연결 확인

네트워크 연결은 (완벽하게 잘 연결되었는지 확인할 수는 없지만) ping 테스트로 확인할 수 있습니다. 클러스터에 들어올 각 컴퓨터에서 인터넷 접속이 접속이 되면, 일반적으로 문제가 없으므로 이 과정은 생략할 수 있습니다.

## 다음

* [컨테이너 런타임 (Container Runtime) 설치하기](install_container_runtime.md)