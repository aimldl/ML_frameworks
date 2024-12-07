* Draft: 2020-07-28 (Tue)

# [한국어 쿠버네티스 문서](https://kubernetes.io/ko/docs/home/) (Kubernetes Tutorial in Korean)
문서의 펼친 목차를 제공. 아직 미완성임.

##  펼친 목차 (Unfolded Table of Contents)
### [문서 / 시작하기](https://kubernetes.io/ko/docs/setup/)
* [릴리스 노트와 버전 차이 지원(skew)](https://kubernetes.io/ko/docs/setup/release/)
  * [v1.18 릴리스 노트](https://kubernetes.io/ko/docs/setup/release/notes/)
* [학습 환경](https://kubernetes.io/ko/docs/setup/learning-environment/)
  * [Minikube로 쿠버네티스 설치](https://kubernetes.io/ko/docs/setup/learning-environment/minikube/)
* [운영 환경](https://kubernetes.io/ko/docs/setup/production-environment/)
  * [컨테이너 런타임](https://kubernetes.io/ko/docs/setup/production-environment/container-runtimes/)
  * [Installing Kubernetes with deployment tools](https://kubernetes.io/ko/docs/setup/production-environment/tools/)
    * [kubeadm으로 클러스터 구성하기](https://kubernetes.io/ko/docs/setup/production-environment/tools/kubeadm/)
      * [kubeadm으로 컨트롤 플레인 사용자 정의하기](https://kubernetes.io/ko/docs/setup/production-environment/tools/kubeadm/control-plane-flags/)
      * [고가용성 토폴로지 선택](https://kubernetes.io/ko/docs/setup/production-environment/tools/kubeadm/ha-topology/)
    * [Kops로 쿠버네티스 설치하기](https://kubernetes.io/ko/docs/setup/production-environment/tools/kops/)
  * [턴키 클라우드 솔루션](https://kubernetes.io/ko/docs/setup/production-environment/turnkey/) (내용 무)
  * [온-프레미스 VM](https://kubernetes.io/ko/docs/setup/production-environment/on-premises-vm/) (내용 무)
  * [쿠버네티스에서 윈도우](https://kubernetes.io/ko/docs/setup/production-environment/windows/)
    * [쿠버네티스에서 윈도우 컨테이너 스케줄링을 위한 가이드](https://kubernetes.io/ko/docs/setup/production-environment/windows/user-guide-windows-containers/)
* [kubeadm으로 컨트롤 플레인 사용자 정의하기](https://kubernetes.io/ko/docs/setup/production-environment/tools/kubeadm/control-plane-flags/)
* [Kops로 쿠버네티스 설치하기](https://kubernetes.io/ko/docs/setup/production-environment/tools/kops/)
* [쿠버네티스에서 윈도우 컨테이너 스케줄링을 위한 가이드](https://kubernetes.io/ko/docs/setup/production-environment/windows/user-guide-windows-containers/)
* [모범 사례](https://kubernetes.io/ko/docs/setup/best-practices/)
  * [여러 영역에서 구동](https://kubernetes.io/ko/docs/setup/best-practices/multiple-zones/)
  * [대형 클러스터 구축](https://kubernetes.io/ko/docs/setup/best-practices/cluster-large/)
  * [PKI 인증서 및 요구 조건](https://kubernetes.io/ko/docs/setup/best-practices/certificates/)

### [문서 / 개념](https://kubernetes.io/ko/docs/concepts/)
* [개요](https://kubernetes.io/ko/docs/concepts/overview/) 쿠버네티스와 그 컴포넌트에 대한 하이-레벨(high-level) 개요를 제공한다.
  * [쿠버네티스란 무엇인가?](https://kubernetes.io/ko/docs/concepts/overview/what-is-kubernetes/)
  * [쿠버네티스 컴포넌트](https://kubernetes.io/ko/docs/concepts/overview/components/)
  * [쿠버네티스 API](https://kubernetes.io/ko/docs/concepts/overview/kubernetes-api/) (Done, [The Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/))
  * [쿠버네티스 오브젝트로 작업하기](https://kubernetes.io/ko/docs/concepts/overview/working-with-objects/)
    * [쿠버네티스 오브젝트 이해하기](https://kubernetes.io/ko/docs/concepts/overview/working-with-objects/kubernetes-objects/)
    * [쿠버네티스 오브젝트 관리](https://kubernetes.io/ko/docs/concepts/overview/working-with-objects/object-management/)
    * [오브젝트 이름과 ID](https://kubernetes.io/ko/docs/concepts/overview/working-with-objects/names/)
    * [네임스페이스](https://kubernetes.io/ko/docs/concepts/overview/working-with-objects/namespaces/)
    * [레이블과 셀렉터](https://kubernetes.io/ko/docs/concepts/overview/working-with-objects/labels/)
    * [어노테이션](https://kubernetes.io/ko/docs/concepts/overview/working-with-objects/annotations/)
    * [필드 셀렉터](https://kubernetes.io/ko/docs/concepts/overview/working-with-objects/field-selectors/)
    * [권장 레이블](https://kubernetes.io/ko/docs/concepts/overview/working-with-objects/common-labels/)
* [클러스터 아키텍처](https://kubernetes.io/ko/docs/concepts/architecture/)  쿠버네티스 뒤편의 구조와 설계 개념들
  * [노드](https://kubernetes.io/ko/docs/concepts/architecture/nodes/)
  * [컨트롤 플레인-노드 간 통신](https://kubernetes.io/ko/docs/concepts/architecture/control-plane-node-communication/)
  * [컨트롤러](https://kubernetes.io/ko/docs/concepts/architecture/controller/)
  * [클라우드 컨트롤러 매니저](https://kubernetes.io/ko/docs/concepts/architecture/cloud-controller/)
* [컨테이너](https://kubernetes.io/ko/docs/concepts/containers/) 런타임 의존성과 함께 애플리케이션을 패키징하는 기술
  * [이미지](https://kubernetes.io/ko/docs/concepts/containers/images/)
  * [런타임클래스(RuntimeClass)](https://kubernetes.io/ko/docs/concepts/containers/runtime-class/)
  * [컨테이너 환경 변수](https://kubernetes.io/ko/docs/concepts/containers/container-environment/)
  * [컨테이너 라이프사이클 훅(Hook)](https://kubernetes.io/ko/docs/concepts/containers/container-lifecycle-hooks/)
* [워크로드](https://kubernetes.io/ko/docs/concepts/workloads/)  쿠버네티스에서 배포할 수 있는 가장 작은 컴퓨트 오브젝트인 파드와, 이를 실행하는 데 도움이 되는 하이-레벨(higher-level) 추상화
  * [파드](https://kubernetes.io/ko/docs/concepts/workloads/pods/)
    * [파드(Pod) 개요](https://kubernetes.io/ko/docs/concepts/workloads/pods/pod-overview/)
    * [파드](https://kubernetes.io/ko/docs/concepts/workloads/pods/pod/)
    * [파드 라이프사이클](https://kubernetes.io/ko/docs/concepts/workloads/pods/pod-lifecycle/)
    * [초기화 컨테이너](https://kubernetes.io/ko/docs/concepts/workloads/pods/init-containers/)
    * [파드 토폴로지 분배 제약 조건](https://kubernetes.io/ko/docs/concepts/workloads/pods/pod-topology-spread-constraints/)
    * [파드 프리셋](https://kubernetes.io/ko/docs/concepts/workloads/pods/podpreset/)
    * [중단(disruption)](https://kubernetes.io/ko/docs/concepts/workloads/pods/disruptions/)
    * [임시(Ephemeral) 컨테이너](https://kubernetes.io/ko/docs/concepts/workloads/pods/ephemeral-containers/)
  * [컨트롤러](https://kubernetes.io/ko/docs/concepts/workloads/controllers/)
    * [레플리카셋](https://kubernetes.io/ko/docs/concepts/workloads/controllers/replicaset/)
    * [레플리케이션 컨트롤러](https://kubernetes.io/ko/docs/concepts/workloads/controllers/replicationcontroller/)
    * [디플로이먼트](https://kubernetes.io/ko/docs/concepts/workloads/controllers/deployment/)
    * [스테이트풀셋](https://kubernetes.io/ko/docs/concepts/workloads/controllers/statefulset/)
    * [데몬셋](https://kubernetes.io/ko/docs/concepts/workloads/controllers/daemonset/)
    * [가비지(Garbage) 수집](https://kubernetes.io/ko/docs/concepts/workloads/controllers/garbage-collection/)
    * [완료된 리소스를 위한 TTL 컨트롤러](https://kubernetes.io/ko/docs/concepts/workloads/controllers/ttlafterfinished/)
    * [잡 - 실행부터 완료까지](https://kubernetes.io/ko/docs/concepts/workloads/controllers/job/)
    * [크론잡](https://kubernetes.io/ko/docs/concepts/workloads/controllers/cron-jobs/)
* [서비스, 로드밸런싱, 네트워킹](https://kubernetes.io/ko/docs/concepts/services-networking/) 쿠버네티스의 네트워킹에 대한 개념과 리소스에 대해 설명한다.
  * [서비스](https://kubernetes.io/ko/docs/concepts/services-networking/service/)
  * [서비스 토폴로지](https://kubernetes.io/ko/docs/concepts/services-networking/service-topology/)
  * [엔드포인트슬라이스](https://kubernetes.io/ko/docs/concepts/services-networking/endpoint-slices/)
  * [서비스 및 파드용 DNS](https://kubernetes.io/ko/docs/concepts/services-networking/dns-pod-service/)
  * [서비스와 애플리케이션 연결하기](https://kubernetes.io/ko/docs/concepts/services-networking/connect-applications-service/)
  * [인그레스 컨트롤러](https://kubernetes.io/ko/docs/concepts/services-networking/ingress-controllers/)
  * [인그레스(Ingress)](https://kubernetes.io/ko/docs/concepts/services-networking/ingress/)
  * [네트워크 정책](https://kubernetes.io/ko/docs/concepts/services-networking/network-policies/)
  * [HostAliases로 파드의 /etc/hosts 항목 추가하기](https://kubernetes.io/ko/docs/concepts/services-networking/add-entries-to-pod-etc-hosts-with-host-aliases/)
  * [IPv4/IPv6 이중 스택](https://kubernetes.io/ko/docs/concepts/services-networking/dual-stack/)
* [스토리지](https://kubernetes.io/ko/docs/concepts/storage/) 클러스터의 파드에 장기(long-term) 및 임시 스토리지를 모두 제공하는 방법
TODO: 하위 메뉴를 생성하고, 각 메뉴의 내용을 빠르게 스캔한다.
* [구성](https://kubernetes.io/ko/docs/concepts/configuration/) 쿠버네티스가 파드 구성을 위해 제공하는 리소스
TODO: 하위 메뉴를 생성하고, 각 메뉴의 내용을 빠르게 스캔한다.
* [보안](https://kubernetes.io/ko/docs/concepts/security/) 클라우드 네이티브 워크로드를 안전하게 유지하기 위한 개념
  * [클라우드 네이티브 보안 개요](https://kubernetes.io/ko/docs/concepts/security/overview/)
* [스케줄링과 축출(eviction)](https://kubernetes.io/ko/docs/concepts/scheduling-eviction/) 쿠버네티스에서, 스케줄링은 kubelet이 파드를 실행할 수 있도록 파드가 노드와 일치하는지 확인하는 것을 말한다. 축출은 리소스가 부족한 노드에서 하나 이상의 파드를 사전에 장애로 처리하는 프로세스이다.
TODO: 하위 메뉴를 생성하고, 각 메뉴의 내용을 빠르게 스캔한다.
* [정책](https://kubernetes.io/ko/docs/concepts/policy/) 리소스의 그룹에 적용되도록 구성할 수 있는 정책
TODO: 하위 메뉴를 생성하고, 각 메뉴의 내용을 빠르게 스캔한다.
* [클러스터 관리](https://kubernetes.io/ko/docs/concepts/cluster-administration/) 쿠버네티스 클러스터 생성 또는 관리에 관련된 로우-레벨(lower-level)의 세부 정보를 설명한다.
TODO: 하위 메뉴를 생성하고, 각 메뉴의 내용을 빠르게 스캔한다.
* [쿠버네티스 확장](https://kubernetes.io/ko/docs/concepts/extend-kubernetes/) 쿠버네티스 클러스터의 동작을 변경하는 다양한 방법
TODO: 하위 메뉴를 생성하고, 각 메뉴의 내용을 빠르게 스캔한다.

### [문서 / 태스크](https://kubernetes.io/ko/docs/tasks/)
* [도구 설치](https://kubernetes.io/ko/docs/tasks/tools/) 컴퓨터에서 쿠버네티스 도구를 설정한다.
  * [kubectl 설치 및 설정](https://kubernetes.io/ko/docs/tasks/tools/install-kubectl/)
  * [Minikube 설치](https://kubernetes.io/ko/docs/tasks/tools/install-minikube/)
* [클러스터 운영](https://kubernetes.io/ko/docs/tasks/administer-cluster/) 클러스터를 운영하기 위한 공통 태스크를 배운다.
  * [kubeadm으로 관리하기](https://kubernetes.io/ko/docs/tasks/administer-cluster/kubeadm/)
    * [kubeadm을 사용한 인증서 관리](https://kubernetes.io/ko/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/)
    * [kubeadm 클러스터 업그레이드](https://kubernetes.io/ko/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
    * [윈도우 노드 추가](https://kubernetes.io/ko/docs/tasks/administer-cluster/kubeadm/adding-windows-nodes/)
    * [윈도우 노드 업그레이드](https://kubernetes.io/ko/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/)
  * [메모리, CPU 와 API 리소스 관리](https://kubernetes.io/ko/docs/tasks/administer-cluster/manage-resources/)
    * [네임스페이스에 대한 기본 메모리 요청량과 상한 구성](https://kubernetes.io/ko/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)
    * [네임스페이스에 대한 기본 CPU 요청량과 상한 구성](https://kubernetes.io/ko/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)
    * [네임스페이스에 대한 메모리의 최소 및 최대 제약 조건 구성](https://kubernetes.io/ko/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)
    * [네임스페이스에 대한 CPU의 최소 및 최대 제약 조건 구성](https://kubernetes.io/ko/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)
    * [네임스페이스에 대한 메모리 및 CPU 쿼터 구성](https://kubernetes.io/ko/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)
    * [네임스페이스에 대한 파드 쿼터 구성](https://kubernetes.io/ko/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)
  * [네트워크 폴리시 제공자(Network Policy Provider) 설치](https://kubernetes.io/ko/docs/tasks/administer-cluster/network-policy-provider/)
    * [네트워크 폴리시로 캘리코(Calico) 사용하기](https://kubernetes.io/ko/docs/tasks/administer-cluster/network-policy-provider/calico-network-policy/)
    * [네트워크 폴리시로 실리움(Cilium) 사용하기](https://kubernetes.io/ko/docs/tasks/administer-cluster/network-policy-provider/cilium-network-policy/)
    * [네트워크 폴리시로 큐브 라우터(Kube-router) 사용하기](https://kubernetes.io/ko/docs/tasks/administer-cluster/network-policy-provider/kube-router-network-policy/)
    * [네트워크 폴리시로 로마나(Romana)](https://kubernetes.io/ko/docs/tasks/administer-cluster/network-policy-provider/romana-network-policy/)
    * [네트워크 폴리시로 위브넷(Weave Net) 사용하기](https://kubernetes.io/ko/docs/tasks/administer-cluster/network-policy-provider/weave-network-policy/)
  * [DNS 서비스 사용자 정의하기](https://kubernetes.io/ko/docs/tasks/administer-cluster/dns-custom-nameservers/)
  * [고가용성 쿠버네티스 클러스터 마스터 설정하기](https://kubernetes.io/ko/docs/tasks/administer-cluster/highly-available-master/)
  * [기본 스토리지클래스(StorageClass) 변경하기](https://kubernetes.io/ko/docs/tasks/administer-cluster/change-default-storage-class/)
  * [네트워크 폴리시(Network Policy) 선언하기](https://kubernetes.io/ko/docs/tasks/administer-cluster/declare-network-policy/)
  * [노드에 대한 확장 리소스 알리기](https://kubernetes.io/ko/docs/tasks/administer-cluster/extended-resource-node/)
  * [서비스 디스커버리를 위해 CoreDNS 사용하기](https://kubernetes.io/ko/docs/tasks/administer-cluster/coredns/)
  * [쿠버네티스 API를 사용하여 클러스터에 접근하기](https://kubernetes.io/ko/docs/tasks/administer-cluster/access-cluster-api/)
  * [클러스터 관리](https://kubernetes.io/ko/docs/tasks/administer-cluster/cluster-management/)
  * [클러스터에서 실행되는 서비스에 접근](https://kubernetes.io/ko/docs/tasks/administer-cluster/access-cluster-services/)
  * [퍼시스턴트볼륨 반환 정책 변경하기](https://kubernetes.io/ko/docs/tasks/administer-cluster/change-pv-reclaim-policy/)
* [파드와 컨테이너 설정](https://kubernetes.io/ko/docs/tasks/configure-pod-container/) 파드와 컨테이너에 대한 공통 구성 태스크들을 수행한다.
  * [컨테이너 및 파드 메모리 리소스 할당](https://kubernetes.io/ko/docs/tasks/configure-pod-container/assign-memory-resource/)
  * [파드에 대한 서비스 품질(QoS) 구성](https://kubernetes.io/ko/docs/tasks/configure-pod-container/quality-service-pod/)
  * [스토리지의 볼륨을 사용하는 파드 구성](https://kubernetes.io/ko/docs/tasks/configure-pod-container/configure-volume-storage/)
  * [프라이빗 레지스트리에서 이미지 받아오기](https://kubernetes.io/ko/docs/tasks/configure-pod-container/pull-image-private-registry/)
  * [노드 어피니티를 사용해 노드에 파드 할당](https://kubernetes.io/ko/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)
  * [노드에 파드 할당](https://kubernetes.io/ko/docs/tasks/configure-pod-container/assign-pods-nodes/)
  * [초기화 컨테이너에 대한 구성](https://kubernetes.io/ko/docs/tasks/configure-pod-container/configure-pod-initialization/)
  * [스태틱(static) 파드 생성하기](https://kubernetes.io/ko/docs/tasks/configure-pod-container/static-pod/)
* [쿠버네티스 오브젝트 관리](https://kubernetes.io/ko/docs/tasks/manage-kubernetes-objects/) 쿠버네티스 API와 상호 작용하기 위한 선언적이고 명령적인 패러다임
  * [구성 파일을 이용한 쿠버네티스 오브젝트의 선언형 관리](https://kubernetes.io/ko/docs/tasks/manage-kubernetes-objects/declarative-config/)
  * [Kustomize를 이용한 쿠버네티스 오브젝트의 선언형 관리](https://kubernetes.io/ko/docs/tasks/manage-kubernetes-objects/kustomization/)
  * [명령형 커맨드를 이용한 쿠버네티스 오브젝트 관리하기](https://kubernetes.io/ko/docs/tasks/manage-kubernetes-objects/imperative-command/)
  * [구성파일을 이용한 명령형 쿠버네티스 오브젝트 관리](https://kubernetes.io/ko/docs/tasks/manage-kubernetes-objects/imperative-config/)
* [애플리케이션에 데이터 주입하기](https://kubernetes.io/ko/docs/tasks/inject-data-application/) 워크로드를 실행하는 파드에 대한 구성과 기타 데이터를 지정한다.
  * [컨테이너를 위한 커맨드와 인자 정의하기](https://kubernetes.io/ko/docs/tasks/inject-data-application/define-command-argument-container/)
  * [컨테이너를 위한 환경 변수 정의하기](https://kubernetes.io/ko/docs/tasks/inject-data-application/define-environment-variable-container/)
* [애플리케이션 실행](https://kubernetes.io/ko/docs/tasks/run-application/) 스테이트리스와 스테이트풀 애플리케이션 모두를 실행하고 관리한다.
  * [단일 인스턴스 스테이트풀 애플리케이션 실행하기](https://kubernetes.io/ko/docs/tasks/run-application/run-single-instance-stateful-application/)
  * [스테이트풀셋(StatefulSet) 삭제하기](https://kubernetes.io/ko/docs/tasks/run-application/delete-stateful-set/)
  * [Horizontal Pod Autoscaler](https://kubernetes.io/ko/docs/tasks/run-application/horizontal-pod-autoscale/)
  * [Horizontal Pod Autoscaler 연습](https://kubernetes.io/ko/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
* [클러스터 내 어플리케이션 액세스](https://kubernetes.io/ko/docs/tasks/access-application-cluster/) 클러스터의 애플리케이션에 접근하기 위해 로드 밸런싱, 포트 포워딩, 방화벽 설정 또는 DNS 구성을 설정한다
  * [웹 UI (대시보드)](https://kubernetes.io/ko/docs/tasks/access-application-cluster/web-ui-dashboard/)
  * [클러스터 액세스](https://kubernetes.io/ko/docs/tasks/access-application-cluster/access-cluster/)
  * [다중 클러스터 접근 구성](https://kubernetes.io/ko/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
  * [포트 포워딩을 사용해서 클러스터 내 애플리케이션에 접근하기](https://kubernetes.io/ko/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)
  * [공유 볼륨을 이용하여 동일한 파드의 컨테이너 간에 통신하기](https://kubernetes.io/ko/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/)
  * [클러스터의 DNS 구성하기](https://kubernetes.io/ko/docs/tasks/access-application-cluster/configure-dns-cluster/)
* [모니터링, 로깅, 그리고 디버깅](https://kubernetes.io/ko/docs/tasks/debug-application-cluster/) 모니터링 및 로깅을 설정하여 클러스터 문제를 해결하거나, 컨테이너화된 애플리케이션을 디버깅한다.
  * [리소스 메트릭 파이프라인](https://kubernetes.io/ko/docs/tasks/debug-application-cluster/resource-metrics-pipeline/)
  * [리소스 모니터링 도구](https://kubernetes.io/ko/docs/tasks/debug-application-cluster/resource-usage-monitoring/)
  * [엘라스틱서치(Elasticsearch) 및 키바나(Kibana)를 사용한 로깅](https://kubernetes.io/ko/docs/tasks/debug-application-cluster/logging-elasticsearch-kibana/)
  * [초기화 컨테이너(Init Containers) 디버그하기](https://kubernetes.io/ko/docs/tasks/debug-application-cluster/debug-init-containers/)
  * [파드 실패의 원인 검증하기](https://kubernetes.io/ko/docs/tasks/debug-application-cluster/determine-reason-pod-failure/)
* [TLS](https://kubernetes.io/ko/docs/tasks/tls/) TLS(Transport Layer Security)를 사용하여 클러스터 내 트래픽을 보호하는 방법을 이해한다.
  * [Kubelet의 인증서 갱신 구성](https://kubernetes.io/ko/docs/tasks/tls/certificate-rotation/)
* [클러스터 데몬 관리](https://kubernetes.io/ko/docs/tasks/manage-daemon/) 롤링 업데이트 수행과 같은 데몬셋 관리를 위한 일반적인 작업을 수행한다.
  * [데몬셋(DaemonSet)에서 롤링 업데이트 수행](https://kubernetes.io/ko/docs/tasks/manage-daemon/update-daemon-set/)
  * [데몬셋(DaemonSet)에서 롤백 수행](https://kubernetes.io/ko/docs/tasks/manage-daemon/rollback-daemon-set/)
* [네트워킹](https://kubernetes.io/ko/docs/tasks/network/) 클러스터에 대한 네트워킹 설정 방법에 대해 배운다.
  * [IPv4/IPv6 이중 스택 검증](https://kubernetes.io/ko/docs/tasks/network/validate-dual-stack/)
* [GPU 스케줄링](https://kubernetes.io/ko/docs/tasks/manage-gpus/scheduling-gpus/) 클러스터의 노드별로 리소스로 사용할 GPU를 구성하고 스케줄링한다.
* [HugePages 관리](https://kubernetes.io/ko/docs/tasks/manage-hugepages/scheduling-hugepages/) 클러스터에서 huge page를 스케줄할 수 있는 리소스로 구성하고 관리한다.
* [플러그인으로 kubectl 확장](https://kubernetes.io/ko/docs/tasks/extend-kubectl/kubectl-plugins/) kubectl 플러그인을 작성하고 설치해서 kubectl을 확장한다.

### [문서 / 튜토리얼](https://kubernetes.io/ko/docs/tutorials/)
TODO: 하위 메뉴를 생성하고, 각 메뉴의 내용을 빠르게 스캔한다.
    * [
    * [
    * [


### [문서 / 레퍼런스](https://kubernetes.io/ko/docs/reference/)
* [표준 용어집](https://kubernetes.io/ko/docs/reference/glossary/?fundamental=true)
* [쿠버네티스 API 사용하기](https://kubernetes.io/ko/docs/reference/using-api/)
  * [쿠버네티스 API 개요](https://kubernetes.io/ko/docs/reference/using-api/api-overview/)
  * [클라이언트 라이브러리](https://kubernetes.io/ko/docs/reference/using-api/client-libraries/)
* [쿠버네티스 이슈와 보안](https://kubernetes.io/ko/docs/reference/issues-security/)
  * [쿠버네티스 이슈 트래커](https://kubernetes.io/ko/docs/reference/issues-security/issues/)
  * [쿠버네티스 보안과 공개 정보](https://kubernetes.io/ko/docs/reference/issues-security/security/)
* [Accessing the API](https://kubernetes.io/docs/reference/access-authn-authz/)
  * 다수의 영문 문서가 있음
* [API Reference](https://kubernetes.io/docs/reference/kubernetes-api/)
  * [v1.18](https://kubernetes.io/docs/reference/kubernetes-api/api-index/)
    * [Kubernetes API v1.18](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/)
  * [Well-Known Labels, Annotations and Taints](https://kubernetes.io/docs/reference/kubernetes-api/labels-annotations-taints/)
* [Setup tools reference](https://kubernetes.io/docs/reference/setup-tools/)
  * [Kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/)
    * 다수의 영문 문서가 있음    
* [kubectl CLI](https://kubernetes.io/ko/docs/reference/kubectl/)
  * [kubectl 개요](https://kubernetes.io/ko/docs/reference/kubectl/overview/)
  * [kubectl 치트 시트](https://kubernetes.io/ko/docs/reference/kubectl/cheatsheet/)
* [커맨드 라인 도구 레퍼런스](https://kubernetes.io/ko/docs/reference/command-line-tools-reference/)
  * [기능 게이트](https://kubernetes.io/ko/docs/reference/command-line-tools-reference/feature-gates/)
* [Scheduling](https://kubernetes.io/docs/reference/scheduling/)
  * [Scheduling Policies](https://kubernetes.io/docs/reference/scheduling/policies/)
  * [Scheduling Profiles](https://kubernetes.io/docs/reference/scheduling/profiles/)
* [도구](https://kubernetes.io/ko/docs/reference/tools/) (Kubectl, Kubeadm, Minikube, 대시보드, Helm, Kompose에 관한 링크)

## [문서 / 쿠버네티스 문서에 기여하기](https://kubernetes.io/ko/docs/contribute/)

## 읽을 부분
[쿠버네티스 문서](https://kubernetes.io/ko/docs/home/)
* [문서 / 시작하기](https://kubernetes.io/ko/docs/setup/)
  * [kubeadm으로 컨트롤 플레인 사용자 정의하기](https://kubernetes.io/ko/docs/setup/production-environment/tools/kubeadm/control-plane-flags/)
  * [Kops로 쿠버네티스 설치하기](https://kubernetes.io/ko/docs/setup/production-environment/tools/kops/)
  * [쿠버네티스에서 윈도우 컨테이너 스케줄링을 위한 가이드](https://kubernetes.io/ko/docs/setup/production-environment/windows/user-guide-windows-containers/)
  * [모범 사례](https://kubernetes.io/ko/docs/setup/best-practices/)
    * [여러 영역에서 구동](https://kubernetes.io/ko/docs/setup/best-practices/multiple-zones/)
    * [대형 클러스터 구축](https://kubernetes.io/ko/docs/setup/best-practices/cluster-large/)
    * [PKI 인증서 및 요구 조건](https://kubernetes.io/ko/docs/setup/best-practices/certificates/)
