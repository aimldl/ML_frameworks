* Rev.1: 2020-07-15 (Wed)
* Draft: 2020-07-01 (Wed)

# kubeadm 을 이용한 쿠버네티스 설치

<img src="images/kubeadm-stacked-color.png" height=200 align="left">

## kubeadm 개요

이 부분은 쿠버네티스 공식 문서의 [Overview of kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm/)에 해당합니다. 

kubeadm은 쿠버네티스 클러스터를 빨리 만들기 위한 도구입니다. 마스터 노드에서 `kubeadm init`을 실행해서 초기화하고, 워커 노드에서 `kubeadm join`을 실행해서 클러스터에 손쉽게 들어갈 수 있습니다.

kubeadm은 Bootstrapping 만 신경쓰고, 프로비져닝은 신경쓰지 않도록 설계되었습니다. 그러므로 쿠버네티스 클러스터를 이용할 때 있으면 좋은 add-on 또한 신경 쓰지 않습니다. 이런 add-on의 예로 쿠버네티스 대쉬보드 (Kubernetes Dashboard), 모니터링 솔루션즈 (Monitoring Solutions), 특정 클라우드를 위한 add-on 등이 있습니다.

### kubeadm의 하위 명령어

| kubeadm 하위 명령어                                          | 설명                                                         | 비고 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| [kubeadm init](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/) | 컨트롤 플레인 노드를 부트스트랩합니다                        |      |
| [kubeadm join](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-join) | 워커 노드를 부트스트랩하고 클러스터에 조인합니다             |      |
| [kubeadm upgrade](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-upgrade) | 클러스터를 새 버전으로 업그레이드 합니다                     |      |
| [kubeadm config](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-config) | kubeadm upgrade로 클러스터를 설정합니다 (kubeadm v1.7.x보다 낮은 버전에 해당) |      |
| [kubeadm token](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-token) | kubeadm join을 위한 토큰을 관리합니다                        |      |
| [kubeadm reset](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-reset) | kubeadm init이나 kubeadm join으로 생긴 변화를 원상복귀합니다 |      |
| [kubeadm version](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-version) | 버전정보를 보여줍니다                                        |      |
| [kubeadm alpha](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-alpha) | 비정식인 알파버전에 관한 정보를 보여줍니다                   |      |

## 쿠버네티스 공식 문서의 해당 부분

이 부분은 쿠버네티스 공식 문서의 [kubeadm으로 클러스터 구성하기](https://kubernetes.io/ko/docs/setup/production-environment/tools/kubeadm/) 혹은 [Bootstrapping clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/)에 해당합니다. 

* kubeadm 설치하기 / [Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)

* 클러스터 설정하기
  * kubeadm로 단일 컨트롤 플레인 클러스터 설정하기 / [Creating a single control-plane cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
  * [kubeadm로 컨트롤 플레인 사용자 정의하기](https://kubernetes.io/ko/docs/setup/production-environment/tools/kubeadm/control-plane-flags/) / [Customizing control plane configuration with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/control-plane-flags/)
  * kubeadm로 클러스터의 각 kubelet 설정하기 / [Configuring each kubelet in your cluster using kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/kubelet-integration/)

## 다음

* [kubeadm, kubelet, kubectl 설치하기](install_kubeadm_kubelet_kubectl.md)
