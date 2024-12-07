* Draft: 2020-07-13 (Mon)

# Kubeflow 설정 

## Kubernetes Cluster 생성

Docker Kubernetes1.14 Kubeflow 1.0

쿠버네티스 버전 1.18이 설치 되어 있습니다.

```bash
Client Version: version.Info{Major:"1", Minor:"18"
Server Version: version.Info{Major:"1", Minor:"18"
```

하지만 이 버전은 Kubeflow와 호환이 되지 않습니다. 쿠버네티스와 쿠브플로우의 버전은 아래 표에 정리되어 있습니다. 

> The recommended Kubernetes version is 1.14. Kubeflow has been validated and tested on Kubernetes 1.14.
>
> - Your cluster must run at least Kubernetes version 1.11.
> - Kubeflow **does not work** on Kubernetes 1.16.
> - Older versions of Kubernetes may not be compatible with the latest Kubeflow versions. The following matrix provides information about compatibility between Kubeflow and Kubernetes versions.

> | Kubernetes Versions | Kubeflow 0.4   | Kubeflow 0.5   | Kubeflow 0.6   | Kubeflow 0.7   | Kubeflow 1.0        |
> | ------------------- | -------------- | -------------- | -------------- | -------------- | ------------------- |
> | 1.11                | **compatible** | **compatible** | incompatible   | incompatible   | incompatible        |
> | 1.12                | **compatible** | **compatible** | incompatible   | incompatible   | incompatible        |
> | 1.13                | **compatible** | **compatible** | incompatible   | incompatible   | incompatible        |
> | 1.14                | **compatible** | **compatible** | **compatible** | **compatible** | **compatible**      |
> | 1.15                | incompatible   | **compatible** | **compatible** | **compatible** | **compatible**      |
> | 1.16                | incompatible   | incompatible   | incompatible   | incompatible   | **no known issues** |
> | 1.17                | incompatible   | incompatible   | incompatible   | incompatible   | **no known issues** |
> | 1.18                | incompatible   | incompatible   | incompatible   | incompatible   | **no known issues** |
>
> - **incompatible**: the combination does not work at all
> - **compatible**: all Kubeflow features have been tested and verified for the Kubernetes version
> - **no known issues**: the combination has not been fully tested but there are no repoted issues
>
> 출처: [ Overview of Deployment on Existing Clusters > Minimum system requirements](https://www.kubeflow.org/docs/started/k8s/overview/#minimum-system-requirements)

쿠버네티스 1.14를 추천하므로 쿠버네티스 재설치를 진행합니다.



### 마스터 설정

마스터로 사용할 컴퓨터를 설정해봅니다.

#### 신규 계정 만들기

쿠버네티스 전용으로 사용할 계정과 패스워드를 생성합니다. 

##### Step 1. 새로운 컴퓨터의 기존 계정에 로그인합니다.

##### Step 2. 신규 계정을 생성합니다.

터미널을 열고, `adduser` 명령어에 신규 계정의 이름을 입력합니다. 여기에선 k8smaster를 계정 이름으로 씁니다. k8s는 Kubernetes의 축약어입니다.

```bash
$ sudo adduser k8smaster
```

현재 계정의 패스워드를 입력하고

```bash
[sudo] password for aimldl: 
Adding user `k8smaster' ...
Adding new group `k8smaster' (1002) ...
Adding new user `k8smaster' (1002) with group `k8smaster' ...
Creating home directory `/home/k8smaster' ...
Copying files from `/etc/skel' ...
```

 신규 생성할 계정의 패스워드를 입력합니다.

```bash
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
Changing the user information for k8smaster
Enter the new value, or press ENTER for the default
	Full Name []: 
	Room Number []: 
	Work Phone []: 
	Home Phone []: 
	Other []: 
Is the information correct? [Y/n] y
$
```

##### Step 3. 기존 계정을 로그 아웃합니다.

##### Step 4. 새로 만들 계정과 패스워드를 써서 다시 로그인합니다.

새로운 계정으로 로그인하여 깨끗한 환경이 만들어졌습니다.



#### 신규 OS의 환경 설정

[install_ubuntu_basic_packages](../../../technical_skills/computing_environments/linux_ubuntu/bash_scripts/install_ubuntu_basic_packages)

[install_ubuntu_productivity_packages](../../../technical_skills/computing_environments/linux_ubuntu/bash_scripts/install_ubuntu_productivity_packages)





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

## 





컨테이너 런타임 (Container Runtime) 설치하기


## 1. Docker 설치 여부 확인하기

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

## 2. Docker 설치하기

여기까지는 앞에 sudo 를 붙이는 경우도 설명을 합니다만, 앞으로는 root계정으로 명령어를 실행할 것을 권장합니다. 앞으로는 root계정으로 로그인한 것을 가정합니다.

### `root` 계정으로 로그인 하기

`sudo -i` 혹은 `sudo -s` 명령어로 `root` 계정으로 로그인할 수 있습니다.

$ sudo -i
[sudo] password for k8smaster: 
$

# 