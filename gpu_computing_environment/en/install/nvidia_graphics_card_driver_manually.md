* Rev.3: 2020-06-25 (Thu)
* Rev.2: 2020-06-10 (Wed)
* Rev.1: 2019-10-10 (Thu)
* Draft: 2019-03-03 (Sun)

# Install NVIDIA Graphics Card Driver on Ubuntu Manually

## Summary

1. Check the information on the graphics card.

```bash
$ ubuntu-drivers devices
  ...
model    : GP104 [GeForce GTX 1080]
  ...
$
```

2. Download the right model of NVIDIA Graphics Card Driver installation file at the [download page](https://www.nvidia.com/download/index.aspx?lang=en-us ).   

```bash
$ cd ~/Downloads/
$ ls
NVIDIA-Linux-x86_64-440.82.run
$
```

​        In this example, `./NVIDIA-Linux-x86_64-440.82.run` is the downloaded file.

3. Install the graphics card driver
   Step 1. Switch to TTY2 by entering `Ctrl+Alt+F2` and log in.

   ```bash
   Ubuntu 18.04.02 LTS GPU-Dektop tty2
   GPU-Desktop login: aimldl
   Password:
     ...
   $
   ```

   Step 2. Exit X Windows system or the GUI.

   ```bash
   $ sudo service lightdm stop
   [sudo] password for aimldl:
   $
   ```

   Step 3. Install NVIDIA Graphics Driver.

   ```bash
   $ cd Downloads/
   $ chmod +x ./NVIDIA-Linux-x86_64-440.82.run
   $ sudo ./NVIDIA-Linux-x86_64-440.82.run
   [sudo] password for aimldl:
   ```

4. Verify the installation

```bash
$ nvidia-smi
Wed Jun 10 15:00:17 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.82       Driver Version: 440.82       CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 108...  Off  | 00000000:01:00.0  On |                  N/A |
| 23%   34C    P8    13W / 250W |    174MiB / 11177MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX 108...  Off  | 00000000:02:00.0 Off |                  N/A |
| 23%   29C    P8     7W / 250W |      2MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
  ...
$
```

## 1. Check the information on the graphics card

```bash
$ ubuntu-drivers devices
== /sys/devices/pci0000:00/0000:00:01.1/0000:02:00.0 ==
modalias : pci:v000010DEd00001B80sv00001028sd00003366bc03sc00i00
vendor   : NVIDIA Corporation
model    : GP104 [GeForce GTX 1080]
driver   : nvidia-driver-415 - third-party free
driver   : nvidia-driver-390 - distro non-free
driver   : nvidia-driver-435 - distro non-free
driver   : nvidia-driver-440 - third-party free recommended
driver   : nvidia-driver-410 - third-party free
driver   : xserver-xorg-video-nouveau - distro free builtin

$
```

The model of my graphics card is `GP104 [GeForce GTX 1080]`. I thought it is `1080Ti`, but it turned out it is `1080`. It was good to double-check because the memory may fade away.

## 2. Download the driver installation file

Go to the download page at https://www.nvidia.com/download/index.aspx?lang=en-us and download the driver installation file  `./NVIDIA-Linux-x86_64-440.82.run`. Other languages are supported at the download page. To search the page, you may use the following keywords.

> Google search: nvidia graphics driver download

### Download steps

Select the right options for the graphics card. In this example, I need a driver for `GeForce GTC 1080Ti` on Linux.

<img src="images/nvidia_driver_downloads-geforce_gtx_1080ti_linux_64bit.png">

Click the `SEARCH` button.

<img src="images/nvidia-drivers-linux_x64_amd64_em64t_display_driver.png">

Click the DOWNLOAD button and the download confirmation page will show up.

<img src="images/nvidia_home-download_drivers-download_confirmation.png">

Click the DOWNLOAD button. When the pop-up window shows up, click the `Save File` button and the file download begins.

<img src="images/nvidia_home-download_drivers-opening_nvidia-linux-x86_64-440_82_run.png">

### Verify the download

When the download is finished, check the downloaded file.  `./NVIDIA-Linux-x86_64-440.82.run` exists in the `Downloads` directory.  The download directory may differ from web browser to web browser.

```bash
$ cd ~/Downloads/
$ ls
NVIDIA-Linux-x86_64-440.82.run
$
```

### Check the current graphics driver

Go to `Settings > Details > About` and check `Graphics`. In this example, `NV134` is set up for the graphics card because Ubuntu sets up the default graphics card driver to make the system works. In the following process, the driver designated to the given NVIDIA graphics card will be installed to use the graphics card at its full capacity.

<img src="images/ubuntu_18_04-settings-details-about.png">

## Install the graphics card driver

### Step 1. Switch to TTY2 by entering `Ctrl+Alt+F2` and log in.

```bash
Ubuntu 18.04.02 LTS GPU-Dektop tty2
GPU-Desktop login: aimldl
Password:
  ...
$
```

**Warning:  The order matters. Do not skip this step.**

If you run the next command with X Windows system on or on the GUI, the screen will turn black and everything will disappear. The only thing left on the screen will be a blinking cursor in the color of white. When I tried to switch to TTY2 by pressing the `Ctrl+Alt+F2` keys, it didn't work. The only way to escape this stage was to reboot the system either by `$ reboot` or pressing the power button. For details, refer to `Problem3` in the bottom of this page (Appendix).

### Step 2. Exit X Windows system or the GUI

```bash
$ sudo service lightdm stop
[sudo] password for aimldl:
$
```

**Warning:  The order matters. Do not skip this step.**

If you skip this step and proceed to the next step, the installation will fail at any rate. In other words, if you do not exit X Windows system and try to install the driver, it will fail anyways. The following error message will be shown and you can not proceed.

<img src="images/nvidia_accelerated_graphics_driver_for_linux-x86_64-the_distribution-provided_pre-install_script_failed.png">

When `Continue installation` is selected, things get messy. [TODO: summary what what happens]

When `Abort installation` is selected, the following message shows up.

<img src="images/nvidia_accelerated_graphics_driver_for_linux-x86_64-the_distribution-provided_pre-install_script_failed-warning.png">

### Step 3. Install NVIDIA Graphics Driver.

```bash
$ cd Downloads/
$ chmod +x ./NVIDIA-Linux-x86_64-440.82.run
$ sudo ./NVIDIA-Linux-x86_64-440.82.run
[sudo] password for aimldl:
```

```bash
There appears to already be a driver installed on your system (version:
440.44). As part of installing this driver (version: 440.82), the existing
driver will be uninstalled. Are you sure you want to continue?

               Continue installation      Abort installation
```

Select `Continue installation`.

```bash
The distribution-provided pre-install script failed! Are you sure you want
to continue?
               Continue installation      Abort installation
```

Select `Continue installation` and the installation will start.

```bash
Install NVIDIA's 32-bit compatibility libraries?
                        Yes                      No
```

Select `Yes`(default)

```bash
Would you like to run the nvidia-xconfig utility to automatically update
your X configuration file so that the NVIDIA X driver will be used when you
restart X?  Any pre-existing X configuration file will be backed up.
                        Yes                       No
```

Select `Yes`

## Verify the installation

Run `nvidia-smi` and see if the graphics card(s) is/are properly recognized.

```bash
$ nvidia-smi
```

A sample message is presented below.

```bash
Wed Jun 10 15:00:17 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.82       Driver Version: 440.82       CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 108...  Off  | 00000000:01:00.0  On |                  N/A |
| 23%   34C    P8    13W / 250W |    174MiB / 11177MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX 108...  Off  | 00000000:02:00.0 Off |                  N/A |
| 23%   29C    P8     7W / 250W |      2MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0       994      G   /usr/lib/xorg/Xorg                           105MiB |
|    0      2078      G   /usr/bin/gnome-shell                          66MiB |
+-----------------------------------------------------------------------------+
$
```

In the above example, there are two GPUs on the machine which are up and running.

## Appendix: Solutions to Frequently Occurring Errors

### Problem 1: nvidia-installer must be run as root

```bash
$ ./NVIDIA-Linux-x86_64-440.82.run
#   incurs the following error message

ERROR: nvidia-installer must be run as root
```

NVIDIA graphics driver must be run as a root.

### Solution 1: 

```bash
$ sudo ./NVIDIA-Linux-x86_64-440.82.run
```

### Problem 2: You appear to be running an X server

You must exit the X Server. Otherwise the following error occurs:

```bash
$ sudo ./NVIDIA-Linux-x86_64-440.82.run
#   incurs the following error message

ERROR: You appear to be running an X server; please exit X before
       installing. For further details, please see the section INSTALLING
       THE NVIDIA DRIVER in the README available on the Linux driver
       download page at www.nvidia.com.
```

### Solution 2: 

***Caution: Save all your previous works before following the insturction here.***

#### Step 1. Swith to other TTY terminal

Enter `Ctrl+Alt+F2` and the black background will be switched to a command-line terminal. The new screen looks like:

```bash
Ubuntu 18.04.02 LTS GPU-Dektop tty2
GPU-Desktop login: _
```

Instead of `F2`, you may enter any key between `F2 through F6`. In other words, `Ctrl+Alt+F3` instead of `Ctrl+Alt+F2` or `Ctrl+Alt+F5` instead of `Ctrl+Alt+F2`. There are multiple TTY and you're free to choose any of them. For `Ctrl+Alt+F4`, the last word in the first line is, now, `tty4`.

```bash
Ubuntu 18.04.02 LTS GPU-Dektop tty4
GPU-Desktop login: _
```

In general, `Ctrl+Alt+F7` brings you back to the GUI part. But what's the use of doing so when you see a black screen with a blinking prompt?

#### Step 2. Enter ID and password to log in

```bash
Ubuntu 18.04.02 LTS GPU-Dektop tty2
GPU-Desktop login: aimldl
Password:
  ...
$
```

#### Step 3. Exit the X Windows system or the GUI

```bash
$ sudo service lightdm stop
[sudo] password for aimldl:
$
```

Note the order to run each step is important. If `$ sudo service lightdm stop` is ran before the previous steps, you may get into a trouble. Refer to Problem 3 below for details.

### Problem 3: `$ sudo service lightdm stop` turns everything on the monitor black.

The GUI or X Windows dissapears and everything turns black on the monitor. On the left top corner of the monitor, there is a prompt blinking periodically indicating the Ubuntu is up and running in the background.

Don't panic. It's supposed to be this way if you run this command on the GUI. Only the GUI or X Windows system has been turned off. But the problem in this installation process is you haven't done it in a TTY terminal.

### Solution 3: Switch to a TTY Terminal first and then run `$ sudo service lightdm stop`

* Did you run `$ sudo service lightdm stop` in the "normal" Ubuntu with the GUI or X Windows, not in one of the TTY terminals?
* If so, switch to a TTY terminal by pressing `Ctrl+Alt+F2` and run the command `$ sudo service lightdm stop`.

```bash
Ubuntu 18.04.02 LTS GPU-Dektop tty2
GPU-Desktop login: aimldl
Password:
  ...
$ sudo service lightdm stop
[sudo] password for aimldl:
$
```

All the letters in the monitor should remain as it was.

## References

* [How to install the NVIDIA drivers on Ubuntu 18.04 Bionic Beaver Linux](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux)
* [006. GPGPU 환경 설정](https://m.blog.naver.com/PostView.nhn?blogId=aimldl&logNo=221478837620&referrerCode=0&searchKeyword=linux)