* Draft: 2020-07-01 (Wed)

# 쿠버네티스 클러스터 설치하기

## 이전

* [Kubeflow = Kubernetes+ML Flow](../../overview.md)

## 개요

쿠버네티스 클러스터 (Kuternetes Cluster)를 두 가지 환경에 만들 수 있습니다.

* 학습 환경
* 운영 환경

여기에선 운영 환경에 쿠버네티스 클러스터를 설치하는 경우를 다룹니다. [쿠버네티스 공식 문서](https://kubernetes.io/ko/docs/home/)의 [시작하기](https://kubernetes.io/ko/docs/setup/) > [운영 환경](https://kubernetes.io/ko/docs/setup/production-environment/)에 해당합니다.

## 운영 환경을 위한 쿠버네티스 클러스터 설치하기

운영 환경 설치를 위한 대부분의 명령어는 `root` 권한으로 실행해야 합니다. `root` 계정으로 로그인 하거나 명령어 앞에 `sudo`를 붙이면 됩니다.

### `root` 계정으로 로그인 하기

`sudo -i` 혹은 `sudo -s` 명령어로 `root` 계정으로 로그인할 수 있습니다.

```bash
$ sudo -i
[sudo] password for k8smaster: 
# 
```

```bash
# exit
logout
$
```

프롬프트가 $에서 #으로 바뀌었음에 주의하세요. root 계정의 프롬프트는 #입니다. 현재 $에서는 k8smaster라는 계정을 쓰고 있습니다.

아래에선 위의 명령어가 실행되는 과정을 `whoami` 명령어을 이용해서 상세히 설명합니다.

```bash
$ whoami
k8smaster
$ sudo -i
[sudo] password for k8smaster: 
#
# whoami
root
# exit
logout
$
$ whoami
k8smaster
$
```

$ 프롬프트에서 `whoami` 명령어로 누구의 계정이였는 확인해보니 `k8smaster`입니다. `sudo -i` 명령어와 패스워드를 입력했더니, 프롬프트가 #로 바뀌었습니다. `whoami` 명령어를 실행하니 `root` 계정이라는 것을 알 수 있습니다. `exit` 명령어를 실행하니 프롬르트가 다시 $로 돌아왔습니다. `whoami` 명령어로 누구의 계정인지 재확인하니 역시나 `k8smaster`였습니다.

### root 권한으로 명령어를 실행하는 예: `apt update`

`apt update` 명령어를 실행하라고 하면, 아래 두 가지 중 한가지 방식으로 명령어를 실행해야 합니다. 여러 개의 명령어를 입력해야 하므로 가능하다면 root 계정으로 로그인하는게 더 편리합니다.

1. #### root 로 로그인 해서 명령어를 실행

```bash
# apt update
```

2. #### 앞에 `sudo`를 붙이고 명령어를 실행

```bash
$ sudo apt update
```

## 다음

* [쿠버네티스 설치 전 확인 작업](verify_before_installing_k8s.md)
