* Draft: 2021-01-31 (Sun)

# How to Install `libjasper-dev` on Ubuntu 18.04

## Problem

The following command is run as a step to install OpenCV dependencies.

```bash
$ sudo apt -y install libjasper-dev
```

An error occurs.

```bash
E: Unable to locate package libjasper-dev
```

## Hint

Google search: libjasper

* [How to install libjasper-dev on Ubuntu 18 and above](http://flummox-engineering.blogspot.com/2020/02/how-to-install-libjasper-dev-on-ubuntu.html)

  > Unfortunately, libjasper-dev is not available on Ubuntu Bionic
  >
  > **Background**
  >
  > libjasper-dev was available on Ubuntu Xenial 16.04, so why has it been removed? Jasper was intentionally removed from Ubuntu and Debian from [this Debian bug report](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=812630).
  >
  >   ...
  >
  > Jasper is still a needed dependency for OpenCV. Here are the options.
  >
  >   ...
  >
  > **Compile Jasper from Source**
  >
  > Since Jasper is an [open source project and is available on Github](https://github.com/mdadams/jasper), you can [download the latest release](https://github.com/mdadams/jasper/releases) and compile it.
  >
  >   ...
  >
  > **libjasper-dev from Ubuntu Xenial**
  > Another alternative is to install libjasper-dev from an older release of Ubuntu, libjasper-dev 1.900.1 from Ubuntu Xenial 16.04. 

## Solution

The latest version at this point is 2.0.24, but I see no point of installing it. So let's just follow the instructions in the tutorial.

```bash
# Let's first install all the required build tools
sudo apt-get install -y build-essential cmake

# Download a release and compile it.
wget https://github.com/mdadams/jasper/archive/version-2.0.16.tar.gz -O jasper-version-2.0.16.tar.gz
tar xvf cd jasper-version-2.0.16.tar.gz
cd jasper-version-2.0.16/

# Now we can start building jasper
mkdir build
export SOURCE_DIR=~/jasper-version-2.0.16
export BUILD_DIR=~/jasper-version-2.0.16/build
cd $BUILD_DIR
cmake -G "Unix Makefiles" -H$SOURCE_DIR -B$BUILD_DIR
cd $BUILD_DIR
make clean all
make test
```
