

## Problem



## Actions

Uncommenting the following part in `.bashrc` didn't solve the problem.

```bash
# CUDA
export PATH=/usr/local/cuda-11.0/bin${PATH:+:${PATH}}
```



### Diagnosis

```bash
$ nvidia-smi
NVIDIA-SMI couldn't find libnvidia-ml.so library in your system. Please make sure that the NVIDIA Display Driver is properly installed and present in your system.
Please also try adding directory that contains libnvidia-ml.so to your system PATH.
$
```

```bash
$ sudo lshw -c video
[sudo] password for k8snode: 
  *-display UNCLAIMED       
       description: VGA compatible controller
       product: GP104 [GeForce GTX 1080]
       vendor: NVIDIA Corporation
       physical id: 0
       bus info: pci@0000:01:00.0
       version: a1
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress vga_controller bus_master cap_list
       configuration: latency=0
       resources: memory:de000000-deffffff memory:c0000000-cfffffff memory:d0000000-d1ffffff ioport:e000(size=128) memory:c0000-dffff
  *-display UNCLAIMED
       description: VGA compatible controller
       product: GP104 [GeForce GTX 1080]
       vendor: NVIDIA Corporation
       physical id: 0
       bus info: pci@0000:02:00.0
       version: a1
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress vga_controller cap_list
       configuration: latency=0
       resources: memory:dc000000-dcffffff memory:a0000000-afffffff memory:b0000000-b1ffffff ioport:d000(size=128) memory:dd000000-dd07ffff
  *-display UNCLAIMED
       description: Display controller
       product: Intel Corporation
       vendor: Intel Corporation
       physical id: 2
       bus info: pci@0000:00:02.0
       version: 00
       width: 64 bits
       clock: 33MHz
       capabilities: pciexpress msi pm bus_master cap_list
       configuration: latency=0
       resources: memory:db000000-dbffffff memory:90000000-9fffffff ioport:f000(size=64)
$
```



I tried to reinstall the graphics card driver.

```bash
$ sudo apt-get -y install cuda
Reading package lists... Done
Building dependency tree       
Reading state information... Done
cuda is already the newest version (11.0.1-1).
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 cuda-drivers-450 : Depends: libnvidia-compute-450 (>= 450.36.06) but it is not going to be installed
 libnvidia-decode-450 : Depends: libnvidia-compute-450 (= 450.36.06-0ubuntu1) but it is not going to be installed
 nvidia-compute-utils-450 : Depends: libnvidia-compute-450 but it is not going to be installed
 nvidia-driver-450 : Depends: libnvidia-compute-450 (= 450.36.06-0ubuntu1) but it is not going to be installed
                     Recommends: libnvidia-compute-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-decode-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-encode-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-ifr1-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-fbc1-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-gl-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
 nvidia-utils-450 : Depends: libnvidia-compute-450 but it is not going to be installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
$
```

```bash
$ sudo apt --fix-broken install
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Correcting dependencies... Done
The following packages were automatically installed and are no longer required:
  libatomic1:i386 libbsd0:i386 libdrm-amdgpu1:i386 libdrm-intel1:i386 libdrm-nouveau2:i386
  libdrm-radeon1:i386 libdrm2:i386 libedit2:i386 libelf1:i386 libexpat1:i386 libffi6:i386 libgl1:i386
  libgl1-mesa-dri:i386 libglapi-mesa:i386 libglvnd0:i386 libglx-mesa0:i386 libglx0:i386 libllvm9:i386
  libnvidia-common-440 libnvidia-extra-440 libpciaccess0:i386 libsensors4:i386 libstdc++6:i386
  libx11-6:i386 libx11-xcb1:i386 libxau6:i386 libxcb-dri2-0:i386 libxcb-dri3-0:i386 libxcb-glx0:i386
  libxcb-present0:i386 libxcb-sync1:i386 libxcb1:i386 libxdamage1:i386 libxdmcp6:i386 libxext6:i386
  libxfixes3:i386 libxshmfence1:i386 libxxf86vm1:i386
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libnvidia-compute-450
The following NEW packages will be installed:
  libnvidia-compute-450
0 upgraded, 1 newly installed, 0 to remove and 10 not upgraded.
124 not fully installed or removed.
Need to get 0 B/21.8 MB of archives.
After this operation, 115 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvidia-compute-450 450.36.06-0ubuntu1 [21.8 MB]
(Reading database ... 220201 files and directories currently installed.)
Preparing to unpack .../libnvidia-compute-450_450.36.06-0ubuntu1_amd64.deb ...
Unpacking libnvidia-compute-450:amd64 (450.36.06-0ubuntu1) ...
dpkg: error processing archive /var/cuda-repo-ubuntu1804-11-0-local/./libnvidia-compute-450_450.36.06-0ubuntu1_amd64.deb (--unpack):
 trying to overwrite '/usr/lib/x86_64-linux-gnu/libnvidia-allocator.so', which is also in package libnvidia-extra-440:amd64 440.82-0ubuntu0~0.18.04.2
Errors were encountered while processing:
 /var/cuda-repo-ubuntu1804-11-0-local/./libnvidia-compute-450_450.36.06-0ubuntu1_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
$
```



```bash
$ dpkg -l | grep -i "nvidia"
iU  cuda-nsight-compute-11-0                   11.0.1-1                                         amd64        NVIDIA Nsight Compute
iU  cuda-nsight-systems-11-0                   11.0.1-1                                         amd64        NVIDIA Nsight Systems
iU  cuda-nvtx-11-0                             11.0.167-1                                       amd64        NVIDIA Tools Extension
iU  libnvidia-cfg1-450:amd64                   450.36.06-0ubuntu1                               amd64        NVIDIA binary OpenGL/GLX configuration library
ii  libnvidia-common-440                       440.82-0ubuntu0~0.18.04.2                        all          Shared files used by the NVIDIA libraries
iU  libnvidia-common-450                       450.36.06-0ubuntu1                               all          Shared files used by the NVIDIA libraries
rc  libnvidia-compute-440:amd64                440.82-0ubuntu0~0.18.04.2                        amd64        NVIDIA libcompute package
iU  libnvidia-decode-450:amd64                 450.36.06-0ubuntu1                               amd64        NVIDIA Video Decoding runtime libraries
iU  libnvidia-encode-450:amd64                 450.36.06-0ubuntu1                               amd64        NVENC Video Encoding runtime library
ii  libnvidia-extra-440:amd64                  440.82-0ubuntu0~0.18.04.2                        amd64        Extra libraries for the NVIDIA driver
iU  libnvidia-fbc1-450:amd64                   450.36.06-0ubuntu1                               amd64        NVIDIA OpenGL-based Framebuffer Capture runtime library
iU  libnvidia-gl-450:amd64                     450.36.06-0ubuntu1                               amd64        NVIDIA OpenGL/GLX/EGL/GLES GLVND libraries and Vulkan ICD
iU  libnvidia-ifr1-450:amd64                   450.36.06-0ubuntu1                               amd64        NVIDIA OpenGL-based Inband Frame Readback runtime library
iU  nsight-compute-2020.1.0                    2020.1.0.33-1                                    amd64        NVIDIA Nsight Compute
rc  nvidia-compute-utils-440                   440.82-0ubuntu0~0.18.04.2                        amd64        NVIDIA compute utilities
iU  nvidia-compute-utils-450                   450.36.06-0ubuntu1                               amd64        NVIDIA compute utilities
rc  nvidia-dkms-440                            440.82-0ubuntu0~0.18.04.2                        amd64        NVIDIA DKMS package
iU  nvidia-dkms-450                            450.36.06-0ubuntu1                               amd64        NVIDIA DKMS package
iU  nvidia-driver-450                          450.36.06-0ubuntu1                               amd64        NVIDIA driver metapackage
rc  nvidia-kernel-common-440                   440.82-0ubuntu0~0.18.04.2                        amd64        Shared files used with the kernel module
iU  nvidia-kernel-common-450                   450.36.06-0ubuntu1                               amd64        Shared files used with the kernel module
iU  nvidia-kernel-source-450                   450.36.06-0ubuntu1                               amd64        NVIDIA kernel source package
iU  nvidia-modprobe                            450.36.06-0ubuntu1                               amd64        Load the NVIDIA kernel driver and create device files
ii  nvidia-prime                               0.8.8.2                                          all          Tools to enable NVIDIA's Prime
iU  nvidia-settings                            450.36.06-0ubuntu1                               amd64        Tool for configuring the NVIDIA graphics driver
iU  nvidia-utils-450                           450.36.06-0ubuntu1                               amd64        NVIDIA driver support binaries
iU  xserver-xorg-video-nvidia-450              450.36.06-0ubuntu1                               amd64        NVIDIA binary Xorg driver
$
```

Remove cuda-toolkit and its dependencies

```bash
$ sudo apt-get remove --auto-remove nvidia-cuda-toolkit
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Package 'nvidia-cuda-toolkit' is not installed, so not removed
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 cuda-drivers-450 : Depends: libnvidia-compute-450 (>= 450.36.06) but it is not going to be installed
 libnvidia-decode-450 : Depends: libnvidia-compute-450 (= 450.36.06-0ubuntu1) but it is not going to be installed
 nvidia-compute-utils-450 : Depends: libnvidia-compute-450 but it is not going to be installed
 nvidia-driver-450 : Depends: libnvidia-compute-450 (= 450.36.06-0ubuntu1) but it is not going to be installed
                     Recommends: libnvidia-compute-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-decode-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-encode-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-ifr1-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-fbc1-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-gl-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
 nvidia-utils-450 : Depends: libnvidia-compute-450 but it is not going to be installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
$
```

```bash
$ ubuntu-drivers devices

== /sys/devices/pci0000:00/0000:00:01.1/0000:02:00.0 ==
modalias : pci:v000010DEd00001B80sv00001028sd00003366bc03sc00i00
vendor   : NVIDIA Corporation
model    : GP104 [GeForce GTX 1080]
driver   : nvidia-driver-450 - third-party free recommended
driver   : nvidia-driver-435 - distro non-free
driver   : nvidia-driver-415 - third-party free
driver   : nvidia-driver-440 - distro non-free
driver   : nvidia-driver-390 - distro non-free
driver   : nvidia-driver-410 - third-party free
driver   : xserver-xorg-video-nouveau - distro free builtin
$
```



### Reinstall the driver

```bash
$ sudo ubuntu-drivers autoinstall
Reading package lists... Done
Building dependency tree       
Reading state information... Done
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 cuda-drivers-450 : Depends: libnvidia-compute-450 (>= 450.36.06) but it is not installed
 libnvidia-decode-450 : Depends: libnvidia-compute-450 (= 450.36.06-0ubuntu1) but it is not installed
 nvidia-compute-utils-450 : Depends: libnvidia-compute-450 but it is not installed
 nvidia-driver-450 : Depends: libnvidia-compute-450 (= 450.36.06-0ubuntu1) but it is not installed
                     Recommends: libnvidia-compute-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-decode-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-encode-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-ifr1-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-fbc1-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-gl-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
 nvidia-utils-450 : Depends: libnvidia-compute-450 but it is not installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
$
```

Action: remove nvidia display driver on ubuntu 18.04

[How to uninstall the NVIDIA drivers on Ubuntu 20.04 Focal Fossa Linux](https://linuxconfig.org/how-to-uninstall-the-nvidia-drivers-on-ubuntu-20-04-focal-fossa-linux)

```bash
# The following command will remove the proprietary Nvidia driver:
$ sudo dpkg -P $(dpkg -l | grep nvidia-driver | awk '{print $2}')
$ sudo apt autoremove
# Switch back to nouveau driver:
$ sudo apt install xserver-xorg-video-nouveau
$
```



```bash
$ sudo dpkg -P $(dpkg -l | grep nvidia-driver | awk '{print $2}')
[sudo] password for k8snode: 
dpkg: dependency problems prevent removal of nvidia-driver-450:
 cuda-drivers-450 depends on nvidia-driver-450 (>= 450.36.06); however:
  Package nvidia-driver-450 is to be removed.

dpkg: error processing package nvidia-driver-450 (--purge):
 dependency problems - not removing
Errors were encountered while processing:
 nvidia-driver-450
$
```



```bash
$ sudo apt autoremove
Reading package lists... Done
Building dependency tree       
Reading state information... Done
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 cuda-drivers-450 : Depends: libnvidia-compute-450 (>= 450.36.06) but it is not installed
 libnvidia-decode-450 : Depends: libnvidia-compute-450 (= 450.36.06-0ubuntu1) but it is not installed
 nvidia-compute-utils-450 : Depends: libnvidia-compute-450 but it is not installed
 nvidia-driver-450 : Depends: libnvidia-compute-450 (= 450.36.06-0ubuntu1) but it is not installed
                     Recommends: libnvidia-compute-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-decode-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-encode-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-ifr1-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-fbc1-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-gl-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
 nvidia-utils-450 : Depends: libnvidia-compute-450 but it is not installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
$
```



```bash
$ sudo apt install xserver-xorg-video-nouveau
Reading package lists... Done
Building dependency tree       
Reading state information... Done
xserver-xorg-video-nouveau is already the newest version (1:1.0.15-2).
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 cuda-drivers-450 : Depends: libnvidia-compute-450 (>= 450.36.06) but it is not going to be installed
 libnvidia-decode-450 : Depends: libnvidia-compute-450 (= 450.36.06-0ubuntu1) but it is not going to be installed
 nvidia-compute-utils-450 : Depends: libnvidia-compute-450 but it is not going to be installed
 nvidia-driver-450 : Depends: libnvidia-compute-450 (= 450.36.06-0ubuntu1) but it is not going to be installed
                     Recommends: libnvidia-compute-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-decode-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-encode-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-ifr1-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-fbc1-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
                     Recommends: libnvidia-gl-450:i386 (= 450.36.06-0ubuntu1) but it is not installable
 nvidia-utils-450 : Depends: libnvidia-compute-450 but it is not going to be installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
$
```



```bash
$ sudo apt --fix-broken install
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Correcting dependencies... Done
The following packages were automatically installed and are no longer required:
  libatomic1:i386 libbsd0:i386 libdrm-amdgpu1:i386
  libdrm-intel1:i386 libdrm-nouveau2:i386
  libdrm-radeon1:i386 libdrm2:i386 libedit2:i386
  libelf1:i386 libexpat1:i386 libffi6:i386 libgl1:i386
  libgl1-mesa-dri:i386 libglapi-mesa:i386 libglvnd0:i386
  libglx-mesa0:i386 libglx0:i386 libllvm9:i386
  libnvidia-common-440 libnvidia-extra-440
  libpciaccess0:i386 libsensors4:i386 libstdc++6:i386
  libx11-6:i386 libx11-xcb1:i386 libxau6:i386
  libxcb-dri2-0:i386 libxcb-dri3-0:i386 libxcb-glx0:i386
  libxcb-present0:i386 libxcb-sync1:i386 libxcb1:i386
  libxdamage1:i386 libxdmcp6:i386 libxext6:i386
  libxfixes3:i386 libxshmfence1:i386 libxxf86vm1:i386
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libnvidia-compute-450
The following NEW packages will be installed:
  libnvidia-compute-450
0 upgraded, 1 newly installed, 0 to remove and 10 not upgraded.
124 not fully installed or removed.
Need to get 0 B/21.8 MB of archives.
After this operation, 115 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvidia-compute-450 450.36.06-0ubuntu1 [21.8 MB]
(Reading database ... 220201 files and directories currently installed.)
Preparing to unpack .../libnvidia-compute-450_450.36.06-0ubuntu1_amd64.deb ...
Unpacking libnvidia-compute-450:amd64 (450.36.06-0ubuntu1) ...
dpkg: error processing archive /var/cuda-repo-ubuntu1804-11-0-local/./libnvidia-compute-450_450.36.06-0ubuntu1_amd64.deb (--unpack):
 trying to overwrite '/usr/lib/x86_64-linux-gnu/libnvidia-allocator.so', which is also in package libnvidia-extra-440:amd64 440.82-0ubuntu0~0.18.04.2
Errors were encountered while processing:
 /var/cuda-repo-ubuntu1804-11-0-local/./libnvidia-compute-450_450.36.06-0ubuntu1_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
$
```

