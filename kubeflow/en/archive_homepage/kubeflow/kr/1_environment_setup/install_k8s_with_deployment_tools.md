* Draft: 2020-07-01 (Wed)

## 배포 도구을 이용해서 쿠버네티스 설치하기

쿠버네티스 아래의 배포 도구 (Deployment Tool) 중 하나를 선택해서 설치합니다.

* [kubeadm](https://github.com/kubernetes/kubeadm)
* [kops](https://github.com/kubernetes/kops)
* [kubespray](https://github.com/kubernetes-sigs/kubespray)
* [kubicorn](https://github.com/kubicorn/kubicorn)

이 문서에서는 kubeadm을 이용해서 로컬 머신에 쿠버네티스를 설치하는 과정을 설명합니다. 가장 쉽고 많이 사용되는 배포 도구로 알려져 있기 때문입니다. 참고로

* kops는 공식적으로 AWS에 쿠버네티스를 설치하는 것만 지원합니다. 
* kubespray는 AWS, GCE, Azure, OpenStack, vSphere, Packet (bare metal), Oracle Cloud Infrastructure (베타 버전), Bare Metal에 고가용성 클러스터 생성을 지원합니다.
* kubicorn은 비공식적인 프로젝트로 쿠버네티스 공식 문서에는 언급되어 있지 않습니다.

### 한국어 번역된 쿠버네티스 설치 관련 공식 문서

참고로 쿠버네티스 공식 문서의 [Installing Kubernetes with deployment tools](https://kubernetes.io/ko/docs/setup/production-environment/tools/) 메뉴의 하위 문서를 정리하면 아래 표와 같습니다. 열에는 배포 툴 (kubeadm, kops, kubespray)이 있고, 행에는 영어 문서 제목 (English), 한국어 문서 제목 (Korean), 설치 환경 타입 (Host Type)이 있습니다.

|           | kubeadm                                                      | kops                                                         | kubespray                                                    |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| English   | [Bootstrapping clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/) (9) | [Installing Kubernetes with kops](https://kubernetes.io/docs/setup/production-environment/tools/kops/) | [Installing Kubernetes with Kubespray](https://kubernetes.io/docs/setup/production-environment/tools/kubespray/) |
| Korean    | [kubeadm으로 클러스터 구성하기](https://kubernetes.io/ko/docs/setup/production-environment/tools/kubeadm/) (2) | [Kops로 쿠버네티스 설치하기](https://kubernetes.io/ko/docs/setup/production-environment/tools/kops/) |                                                              |
| Host Type | Any(?)                                                       | AWS                                                          | GCE, Azure, OpenStack, AWS, vSphere, Packet (bare metal), Oracle Cloud Infrastructure (Experimental) or Baremetal |

복수의 하위 문서가 있을 경우 개수를 괄호 () 안에 표시했습니다. 2020년 7월 현재 kubeadm의 9개의 영어 문서 중 2개만 한국어로 번역되어 있습니다.

## 다음

* [kubeadm 을 이용한 쿠버네티스 설치](install_k8s_with_kubeadm.md)