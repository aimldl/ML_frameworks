* 
# 도커와 NVIDIA도커를 설치
## 도커와 NVIDIA 도커 설치 여부를 확인

설치가 되어 있다면 `docker` 및 `nvidia-docker`명령어가 실행됩니다.

```bash
$ docker --version
Docker version 19.03.6, build 369ce74a3c
$ nvidia-docker --version
Docker version 19.03.6, build 369ce74a3c
$
```

아니라면 각각의 설치를 진행합니다.

## 도커 설치하기

> [install_docker_on_ubuntu](../../../../environments/docker/en/bash_scripts/install_docker_on_ubuntu)
> 를 다운로드 받아서 실행하면 도커가 설치됩니다.

```bash
$ nano install_docker_on_ubuntu
$ chmod +x ./install_docker_on_ubuntu
$ ./install_docker_on_ubuntu
```
설치 과정에 대한 상세한 설명은 [How to Install Docker on Ubuntu](../../../../environments/docker/en/install/docker_on_ubuntu.md)를 참고하세요.

## NVIDIA 도커 설치하기

> [install_nvidia_docker_on_ubuntu](../../../../environments/docker/en/bash_scripts/install_nvidia_docker_on_ubuntu)
> 를 다운로드 받아서 실행하면 도커가 설치됩니다.
```bash
$ nano install_nvidia_docker_on_ubuntu
$ chmod +x install_nvidia_docker_on_ubuntu 
$ ./install_nvidia_docker_on_ubuntu 
```

설치 과정에 대한 상세한 설명은 [How to Install NVIDIA Docker on Ubuntu](../../../../environments/docker/en/install/nvidia-docker_on_Ubuntu.md)를 참고하세요.