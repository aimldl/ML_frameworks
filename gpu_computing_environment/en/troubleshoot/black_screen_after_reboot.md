* Draft: 2020-06-26 (Fri)

# Black Screen after Reboot

## Problem



## Hint

I was able to see this is a commong problem.

Google search

* ubuntu 18.04 black screen after boot
* ubuntu linux doesn't start after cuda toolkit installation
* ubuntu linux doesn't start after cuda  installation

[Can’t boot Ubuntu 14.04 LTS after CUDA 7 install](https://forums.developer.nvidia.com/t/cant-boot-ubuntu-14-04-lts-after-cuda-7-install/38192)

[Ubuntu not starting post cuda installation](https://askubuntu.com/questions/668130/ubuntu-not-starting-post-cuda-installation)

[Fixing Ubuntu Freezing at Boot Time](https://itsfoss.com/fix-ubuntu-freezing/)

Google search

* ubuntu 18.04 no grub black screen after boot

[Ubuntu boots to black screen, cannot access Grub](https://forum.level1techs.com/t/ubuntu-boots-to-black-screen-cannot-access-grub/88627)

## Solution

First, press the `ESC` key to enter the GRUB menu.

After booting up in the safe mode, change the grub configuration permanently.

```bash
$ sudo gedit /etc/default/grub
```

Change

```text
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```

to

```text
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"
```

in

```text
# If you change this file, run 'update-grub' afterwards to update
# /boot/grub/grub.cfg.
# For full documentation of the options in this file, see:
#   info -f grub -n 'Simple configuration'

GRUB_DEFAULT=0
GRUB_TIMEOUT_STYLE=hidden
GRUB_TIMEOUT=10
GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
GRUB_CMDLINE_LINUX=""

# Uncomment to enable BadRAM filtering, modify to suit your needs
# This works with Linux (no patch required) and with any kernel that obtains
# the memory map information from GRUB (GNU Mach, kernel of FreeBSD ...)
#GRUB_BADRAM="0x01234567,0xfefefefe,0x89abcdef,0xefefefef"

# Uncomment to disable graphical terminal (grub-pc only)
#GRUB_TERMINAL=console

# The resolution used on graphical terminal
# note that you can use only modes which your graphic card supports via VBE
# you can see them in real GRUB with the command `vbeinfo'
#GRUB_GFXMODE=640x480

# Uncomment if you don't want GRUB to pass "root=UUID=xxx" parameter to Linux
#GRUB_DISABLE_LINUX_UUID=true

# Uncomment to disable generation of recovery mode menu entries
#GRUB_DISABLE_RECOVERY="true"

# Uncomment to get a beep at grub start
#GRUB_INIT_TUNE="480 440 1"
```

Update grub.

```bash
$ sudo update-grub
```

The change in the grub setting solved the black screen problem.

However the graphics card set-up is not correct as follows.



So fix this by reinstalling the graphics card driver.

