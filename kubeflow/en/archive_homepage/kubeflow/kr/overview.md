* Draft: 2020-06-30 (Wed)



# Kubeflow = Kubernetes+ML Flow

## 환경설정

쿠버네티스는 콘테이너 오케스트레이션 기술의 실질적인 표준 (De Facto Standard)입니다.

[쿠버네티스 클러스터 설치하기](1_environment_setup/install_k8s_cluster.html)

* [쿠버네티스 설치 전 확인 작업](1_environment_setup/verify_before_installing_k8s.md)

  * (클러스터에 붙을 모든 컴퓨터가 쿠버네티스 설치를 취한 최소 스펙을 만족하는지 확인)

  * (모든 컴퓨터에서 인터넷 접속이 가능한지 확인)

  * 스왑 메모리 (Swap Memory)를 비활성화

    ```bash
    $ sudo swapoff -a
    $ sudo nano /etc/fstab
    ```

    텍스트 에디터로 열어서 두번째 줄의 `/swapfile`로 시작되는 하는 곳을 제거

    ```bash
    #/swapfile   none   swap   sw   0   0
    ```

* [컨테이너 런타임 (Container Runtime) 설치하기](1_environment_setup/install_container_runtime.md)

  * [컨테이너 런타임 설치하기: kubeadm편](1_environment_setup/install_container_runtime_with_kubeadm.md)

  버전 19.03.11이 추천된다.

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

$ sudo systemctl enable docker
```

* [배포 툴을 이용해서 쿠버네티스 설치하기](1_environment_setup/install_k8s_with_deployment_tools.md)
  * [kubeadm 을 이용한 쿠버네티스 설치](1_environment_setup/install_k8s_with_kubeadm.md)
  * [kubeadm, kubelet, kubectl 설치하기](1_environment_setup/install_kubeadm_kubelet_kubectl.md)
    * 모든 컴퓨터에 kubeadm, kubelet, kubectl를 설치합니다. 

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

* [kubeadm으로 쿠버네티스 클러스터 생성하기](1_environment_setup/create_k8s_cluster_with_kubeadm.md)
  *  마스터 노드로 사용할 컴퓨터의 대수에 따라 하나를 선택 
    * 단일 구성 클러스터(Single Control-Plane Kubernetes Cluster)
    * 고가용성 클러스터  (High Availability Kubernetes Cluster)
  * Pod Network로 하나를 선택
    * [Canal](https://github.com/tigera/canal/tree/master/k8s-install), [Calico](https://docs.projectcalico.org/latest/introduction/), [Cilium](https://github.com/cilium/cilium), [CNI-Genie](https://github.com/Huawei-PaaS/CNI-Genie), [Contiv](http://contiv.github.io), [Contrail](http://www.juniper.net/us/en/products-services/sdn/contrail/contrail-networking/), [Flannel](https://github.com/coreos/flannel/blob/master/Documentation/kubernetes.md), [Knitter](https://github.com/ZTE/Knitter/), [Multus](https://github.com/Intel-Corp/multus-cni), [OVN4NFV-K8S-Plugin](https://github.com/opnfv/ovn4nfv-k8s-plugin), [NSX-T](https://docs.vmware.com/en/VMware-NSX-T/2.0/nsxt_20_ncp_kubernetes.pdf), [Nuage](https://github.com/nuagenetworks/nuage-kubernetes/blob/v5.1.1-1/docs/kubernetes-1-installation.rst), [Romana](http://romana.io), [Weave Net](https://www.weave.works/docs/net/latest/kube-addon/)
  * [kubeadm으로 단일 구성 클러스터 생성하기](1_environment_setup/create_a_single_control_plane_cluster_with_kubeadm_init.md)
    * [부록: `kubeadm init` 명령어](1_environment_setup/appendix-create_a_single_control_plane_cluster_with_kubeadm_init.md)
      * `kubeadm init` 명령어 실행 시 연관있는 항목
      * `sudo kubeadm init`명령어의 전체 메세지
      * `sudo kubeadm init` 출력 메세지 뒷부분 설명

`podnetwork`로 기본인 calico를 선택

마스터 설정: `kubeadm init`의 기본값으로 초기화 하기

```bash
$ sudo kubeadm init
$ mkdir -p $HOME/.kube
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config
$ sudo kubectl apply -f https://docs.projectcalico.org/v3.14/manifests/calico.yaml
$ kubectl get nodes
```

노드 설정:  `kubeadm join`명령어로 클러스터에 조인 (join)하기

```bash
$ kubeadm join <control-plane-host>:<control-plane-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash>

```



* [클러스터에 붙은 노드 구성 검증하기](1_environment_setup/validate_node_setup.md)
  * 노드 적합성 테스트는 그냥 넘어가기로 합니다.
* 
* [쿠버네티스 대쉬보드 (Kubernetes Dashboard) 설치하기](1_environment_setup/deploy_k8s_dashboard.md)
* [클러스터에 신규 노드 조인 (Join)하기](1_environment_setup/add_a_new_node_to_the_existing_cluster.md)

* [Match the versions of Docker-Kubernetes-Kubeflow Chain](1_environment_setup/match_the_versions_of_docker-kubernetes-kubeflow_chain.md)

Kubeflow 1.0
k8s      1.14
Docker   1.13.1, 17.03, 17.06, 17.09, 18.06, 18.09

1.15 is said to be compatible, but it wasn't for my case. I struggles days until I reached a conclusion that 1.15 is the problem. After switching to 1.14, everything worked magically without much effort.

[kubeadm init args로  단일 구성 클러스터 생성하기](1_environment_setup/create_a_single_control_plane_cluster_with_kubeadm_init_args.md)



1_environment_setup/
