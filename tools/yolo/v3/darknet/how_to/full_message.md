* Draft: 2021-01-28 (Thu)

# 다크넷을 위한 도커 환경 만드는 방법 (전체 출력 메세지 포함 버전)

## 요약

### Step 1. 도커 (Docker)를 설치합니다.

```bash
$ sudo apt-get update
$ sudo apt-get remove docker docker-engine docker.io
$ sudo apt install -y docker.io
$ docker --version
$ sudo docker run hello-worldUnable to find image 'hello-world:latest' locally
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ sudo systemctl enable docker
$ 
```

로그아웃 후 재로그인

### Step 2. NVIDIA Docker를 설치합니다.



## 전체 출력 메세지 포함 버전

`(darknet_with_opencv_and_cuda) k8smaster@k8smaster-Alienware-Aurora-R7:~$`를 `$`로 생략했습니다.

### Step 1. 도커 (Docker)를 설치합니다.

```bash
$ sudo apt-get update
[sudo] k8smaster의 암호: 
받기:1 http://dl.google.com/linux/chrome/deb stable InRelease [1,811 B]
무시:2 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  InRelease        
무시:3 http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  InRelease
받기:4 http://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,062 B]                   
받기:5 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  Release [697 B]  
받기:6 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  Release.gpg [836 B]
기존:7 http://ppa.launchpad.net/nomacs/stable/ubuntu bionic InRelease                               
받기:8 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]                        
기존:9 http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release
기존:10 https://typora.io/linux ./ InRelease                                                        
기존:11 http://kr.archive.ubuntu.com/ubuntu bionic InRelease                                        
무시:13 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  Packages        
받기:13 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  Packages [549 kB]
받기:14 http://kr.archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]                      
기존:15 http://ppa.launchpad.net/otto-kesselgulasch/gimp/ubuntu bionic InRelease                    
받기:16 http://security.ubuntu.com/ubuntu bionic-security/main amd64 DEP-11 Metadata [48.9 kB]      
받기:17 http://kr.archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]                    
받기:18 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 DEP-11 Metadata [59.8 kB]
받기:19 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 DEP-11 Metadata [2,464 B]
받기:20 http://kr.archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [1,862 kB]           
받기:21 http://kr.archive.ubuntu.com/ubuntu bionic-updates/main i386 Packages [1,210 kB]
받기:22 http://kr.archive.ubuntu.com/ubuntu bionic-updates/main amd64 DEP-11 Metadata [295 kB]
받기:23 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [1,710 kB]
받기:24 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe i386 Packages [1,558 kB]
받기:25 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 DEP-11 Metadata [289 kB]  
받기:26 http://kr.archive.ubuntu.com/ubuntu bionic-updates/multiverse i386 Packages [14.3 kB]       
받기:27 http://kr.archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 Packages [31.8 kB]      
받기:28 http://kr.archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 DEP-11 Metadata [2,468 B]
받기:29 http://kr.archive.ubuntu.com/ubuntu bionic-backports/universe amd64 DEP-11 Metadata [9,288 B]
내려받기 7,897 k바이트, 소요시간 11초 (709 k바이트/초)                                              
패키지 목록을 읽는 중입니다... 완료
W: Target Packages (Packages) is configured multiple times in /etc/apt/sources.list:52 and /etc/apt/sources.list.d/cuda.list:1
W: Target Translations (ko_KR) is configured multiple times in /etc/apt/sources.list:52 and /etc/apt/sources.list.d/cuda.list:1
W: Target Translations (ko) is configured multiple times in /etc/apt/sources.list:52 and /etc/apt/sources.list.d/cuda.list:1
W: Target Translations (en) is configured multiple times in /etc/apt/sources.list:52 and /etc/apt/sources.list.d/cuda.list:1
W: Target Packages (Packages) is configured multiple times in /etc/apt/sources.list:52 and /etc/apt/sources.list.d/cuda.list:1
W: Target Translations (ko_KR) is configured multiple times in /etc/apt/sources.list:52 and /etc/apt/sources.list.d/cuda.list:1
W: Target Translations (ko) is configured multiple times in /etc/apt/sources.list:52 and /etc/apt/sources.list.d/cuda.list:1
W: Target Translations (en) is configured multiple times in /etc/apt/sources.list:52 and /etc/apt/sources.list.d/cuda.list:1
$ sudo apt-get remove docker docker-engine docker.io
패키지 목록을 읽는 중입니다... 완료
의존성 트리를 만드는 중입니다       
상태 정보를 읽는 중입니다... 완료
패키지 'docker-engine'는 설치되어 있지 않아, 지우지 않았습니다.
패키지 'docker'는 설치되어 있지 않아, 지우지 않았습니다.
패키지 'docker.io'는 설치되어 있지 않아, 지우지 않았습니다.
다음 패키지가 자동으로 설치되었지만 더 이상 필요하지 않습니다:
  linux-headers-4.15.0-132 linux-headers-4.15.0-132-generic linux-image-4.15.0-132-generic
  linux-modules-4.15.0-132-generic linux-modules-extra-4.15.0-132-generic
Use 'sudo apt autoremove' to remove them.
0개 업그레이드, 0개 새로 설치, 0개 제거 및 6개 업그레이드 안 함.
$ sudo apt install -y docker.io
패키지 목록을 읽는 중입니다... 완료
의존성 트리를 만드는 중입니다       
상태 정보를 읽는 중입니다... 완료
다음 패키지가 자동으로 설치되었지만 더 이상 필요하지 않습니다:
  linux-headers-4.15.0-132 linux-headers-4.15.0-132-generic linux-image-4.15.0-132-generic
  linux-modules-4.15.0-132-generic linux-modules-extra-4.15.0-132-generic
Use 'sudo apt autoremove' to remove them.
다음의 추가 패키지가 설치될 것입니다 :
  bridge-utils cgroupfs-mount containerd pigz runc ubuntu-fan
제안하는 패키지:
  aufs-tools btrfs-progs debootstrap docker-doc rinse zfs-fuse | zfsutils
다음 새 패키지를 설치할 것입니다:
  bridge-utils cgroupfs-mount containerd docker.io pigz runc ubuntu-fan
0개 업그레이드, 7개 새로 설치, 0개 제거 및 6개 업그레이드 안 함.
63.8 M바이트 아카이브를 받아야 합니다.
이 작업 후 320 M바이트의 디스크 공간을 더 사용하게 됩니다.
받기:1 http://kr.archive.ubuntu.com/ubuntu bionic/universe amd64 pigz amd64 2.4-1 [57.4 kB]
받기:2 http://kr.archive.ubuntu.com/ubuntu bionic/main amd64 bridge-utils amd64 1.5-15ubuntu1 [30.1 kB]
받기:3 http://kr.archive.ubuntu.com/ubuntu bionic/universe amd64 cgroupfs-mount all 1.4 [6,320 B]
받기:4 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 runc amd64 1.0.0~rc10-0ubuntu1~18.04.2 [2,000 kB]
받기:5 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 containerd amd64 1.3.3-0ubuntu1~18.04.4 [21.7 MB]
받기:6 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 docker.io amd64 19.03.6-0ubuntu1~18.04.3 [39.9 MB]
받기:7 http://kr.archive.ubuntu.com/ubuntu bionic/main amd64 ubuntu-fan all 0.12.10 [34.7 kB]       
내려받기 63.8 M바이트, 소요시간 38초 (1,692 k바이트/초)                                             
패키지를 미리 설정하는 중입니다...
Selecting previously unselected package pigz.
(데이터베이스 읽는중 ...현재 255805개의 파일과 디렉터리가 설치되어 있습니다.)
Preparing to unpack .../0-pigz_2.4-1_amd64.deb ...
Unpacking pigz (2.4-1) ...
Selecting previously unselected package bridge-utils.
Preparing to unpack .../1-bridge-utils_1.5-15ubuntu1_amd64.deb ...
Unpacking bridge-utils (1.5-15ubuntu1) ...
Selecting previously unselected package cgroupfs-mount.
Preparing to unpack .../2-cgroupfs-mount_1.4_all.deb ...
Unpacking cgroupfs-mount (1.4) ...
Selecting previously unselected package runc.
Preparing to unpack .../3-runc_1.0.0~rc10-0ubuntu1~18.04.2_amd64.deb ...
Unpacking runc (1.0.0~rc10-0ubuntu1~18.04.2) ...
Selecting previously unselected package containerd.
Preparing to unpack .../4-containerd_1.3.3-0ubuntu1~18.04.4_amd64.deb ...
Unpacking containerd (1.3.3-0ubuntu1~18.04.4) ...
Selecting previously unselected package docker.io.
Preparing to unpack .../5-docker.io_19.03.6-0ubuntu1~18.04.3_amd64.deb ...
Unpacking docker.io (19.03.6-0ubuntu1~18.04.3) ...
Selecting previously unselected package ubuntu-fan.
Preparing to unpack .../6-ubuntu-fan_0.12.10_all.deb ...
Unpacking ubuntu-fan (0.12.10) ...
runc (1.0.0~rc10-0ubuntu1~18.04.2) 설정하는 중입니다 ...
cgroupfs-mount (1.4) 설정하는 중입니다 ...
containerd (1.3.3-0ubuntu1~18.04.4) 설정하는 중입니다 ...
Created symlink /etc/systemd/system/multi-user.target.wants/containerd.service → /lib/systemd/system/containerd.service.
bridge-utils (1.5-15ubuntu1) 설정하는 중입니다 ...
ubuntu-fan (0.12.10) 설정하는 중입니다 ...
Created symlink /etc/systemd/system/multi-user.target.wants/ubuntu-fan.service → /lib/systemd/system/ubuntu-fan.service.
pigz (2.4-1) 설정하는 중입니다 ...
docker.io (19.03.6-0ubuntu1~18.04.3) 설정하는 중입니다 ...
그룹 `docker' (GID 129) 추가 ...
완료.
Created symlink /etc/systemd/system/sockets.target.wants/docker.socket → /lib/systemd/system/docker.socket.
docker.service is a disabled or a static unit, not starting it.
Processing triggers for systemd (237-3ubuntu10.44) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for ureadahead (0.100.0-21) ...
ureadahead will be reprofiled on next reboot
$ docker --version
Docker version 19.03.6, build 369ce74a3c
$ sudo docker run hello-worldUnable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
0e03bdcc26d7: Pull complete 
Digest: sha256:31b9c7d48790f0d8c50ab433d9c3b7e17666d6993084c002c2ff1ca09b96391d
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

$ sudo groupadd docker
groupadd: 'docker' 그룹이 이미 있습니다
$ sudo usermod -aG docker $USER
$ sudo systemctl enable docker
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /lib/systemd/system/docker.service.
$ 
```

### Step 2. NVIDIA Docker를 설치합니다.





* [NVIDIA/nvidia-docker](https://github.com/NVIDIA/nvidia-docker)

> **Getting Started**
>
> Make sure you have installed
>
> *  the [NVIDIA driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver)
>   * Note that you do not need to install the CUDA Toolkit on the host system, but the NVIDIA driver needs to be installed
> * Docker engine
>
> for your Linux distribution. 

```bash
$ nvidia-smi
Thu Jan 28 11:11:40 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.32.03    Driver Version: 460.32.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 1080    On   | 00000000:01:00.0  On |                  N/A |
| 27%   38C    P8     8W / 180W |    279MiB /  8118MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX 1080    On   | 00000000:02:00.0 Off |                  N/A |
| 27%   29C    P8     5W / 180W |      2MiB /  8119MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1119      G   /usr/lib/xorg/Xorg                145MiB |
|    0   N/A  N/A      1302      G   /usr/bin/gnome-shell               52MiB |
|    0   N/A  N/A     24718      G   ...AAAAAAAAA= --shared-files       44MiB |
|    0   N/A  N/A     26141      G   ...gAAAAAAAAA --shared-files       32MiB |
+-----------------------------------------------------------------------------+
$
```

