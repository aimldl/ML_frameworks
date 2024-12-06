



```makefile
GPU=1
CUDNN=0
OPENCV=1
```

을

```bash
GPU=1
CUDNN=0
OPENCV=1
```

로 변경해서 컴파일하면

```bash
# make
  ...
No package 'opencv' found
  ...
#
```

라는 에러가 발생합니다.

CUDNN을 먼저 설정해도 상관없습니다만, OpenCV는 설치하고 컴파일하는데 시간이 많이 걸립니다. 그렇기 때문에 컴파일을 하면서 `CUDNN`문제를 해결하는 편이 낫습니다.

## OpenCV 설치하는 방법

Google search: opencv install

* [Installation in Linux](https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html)

> **Build with opencv_contrib**
>
> ```bash
> # Install minimal prerequisites (Ubuntu 18.04 as reference)
> sudo apt update && sudo apt install -y cmake g++ wget unzip
> # Download root@b865d9c1f5da:/home/user/darknet# nano install_opencv_contrib
> root@b865d9c1f5da:/home/user/darknet# chmod +x install_opencv_contrib 
> root@b865d9c1f5da:/home/user/darknet# ./install_opencv_contrib 
> and unpack sources
> wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip
> wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/master.zip
> unzip opencv.zip
> unzip opencv_contrib.zip
> # Create build directory and switch into it
> mkdir -p build && cd build
> # Configure
> cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-master/modules ../opencv-master
> # Build
> cmake --build .
> ```
>
> **Install**
>
> ```bash
> sudo make install$ 
> ```

아래 코드를 

```bash
#!/bin/bash
# install_opencv_contrib

# Install minimal prerequisites (Ubuntu 18.04 as reference)
apt update && apt install -y cmake g++ wget unzip
# Download and unpack sourcesls /usr/lib/x86_64-linux-gnu | grep libopencv
wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/master.zip
unzip opencv.zip
unzip opencv_contrib.zip
# Create build directory and switch into it
mkdir -p build && cd build
# Configure
cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-master/modules ../opencv-master
# Build
cmake --build .

# install
make install
```

생성해서 실행합니다.

```bash
root@b865d9c1f5da:/home/user/darknet# nano install_opencv_contrib
root@b865d9c1f5da:/home/user/darknet# chmod +x install_opencv_contrib 
root@b865d9c1f5da:/home/user/darknet# ./install_opencv_contrib 
```

무사히 설치가 끝나면

```bash
  ...
-- Set runtime path of "/usr/local/bin/opencv_version" to "/usr/local/lib"
root@b865d9c1f5da:/home/user/darknet# 
```

OpenCV가 설치되었습니다. 참고로 `/home/user/darknet` 디렉토리에 설치했으므로 아래처럼 추가로 파일과 디렉토리가 생겼습니다.

```bash
root@b865d9c1f5da:/home/user/darknet# ls
LICENSE       LICENSE.mit  build     include                 opencv-master          python
LICENSE.fuck  LICENSE.v1   cfg       install_opencv_contrib  opencv.zip             results
LICENSE.gen   Makefile     darknet   libdarknet.a            opencv_contrib-master  scripts
LICENSE.gpl   README.md    data      libdarknet.so           opencv_contrib.zip     src
LICENSE.meta  backup       examples  obj                     predictions.jpg        yolov3.weights
root@b865d9c1f5da:/home/user/darknet# 
```

 `/home/user/darknet/build` 디렉토리의 내용은 아래와 같습니다.

```bash
root@b865d9c1f5da:/home/user/darknet# ls build/
3rdparty                    cmake_install.cmake    opencv_data_config.hpp
CMakeCache.txt              cmake_uninstall.cmake  opencv_python_config.cmake
CMakeDownloadLog.txt        configured             opencv_python_tests.cfg
CMakeFiles                  custom_hal.hpp         opencv_tests_config.hpp
CMakeVars.txt               cv_cpu_config.h        python_loader
CPackConfig.cmake           cvconfig.h             setup_vars.sh
CPackSourceConfig.cmake     data                   share
CTestTestfile.cmake         doc                    test-reports
Makefile                    downloads              text_config.hpp
OpenCVConfig-version.cmake  include                tmp
OpenCVConfig.cmake          install_manifest.txt   unix-install
OpenCVModules.cmake         lib                    version_string.tmp
apps                        modules
bin                         opencv2
root@b865d9c1f5da:/home/user/darknet# 
```

## 설치 확인하기

OpenCV가 잘 설치되었는지 확인해봅니다.

### `python`으로 설치 확인하기

```bash
root@b865d9c1f5da:/home/user/darknet# python -c 'import cv2; print(cv2.__version__)'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named cv2
root@b865d9c1f5da:/home/user/darknet# 
```

파이썬 버전을 확인해봅니다.

```bash
root@b865d9c1f5da:/home/user/darknet# python --version
Python 2.7.17
root@b865d9c1f5da:/home/user/darknet#
```

`python3`가 별도로 있겠네요.

```bash
root@b865d9c1f5da:/home/user/darknet# python3 --version
Python 3.6.9
root@b865d9c1f5da:/home/user/darknet#
```

```bash
root@b865d9c1f5da:/home/user/darknet# python3 -c 'import cv2; print(cv2.__version__)'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'cv2'
root@b865d9c1f5da:/home/user/darknet# 
```

### `pkg-config`로 설치 확인하기

```bash
pkg-config --modversion opencv
```

```bash
root@b865d9c1f5da:/home/user/darknet# pkg-config --modversion opencv
Package opencv was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opencv' found
root@b865d9c1f5da:/home/user/darknet#
```

### 라이브러리로 설치 확인하기

```bash
$ ls /usr/lib/x86_64-linux-gnu | grep libopencv
```

로 라이브러리를 확인할 수 있습니다.

```bash
root@b865d9c1f5da:/home/user/darknet# ls /usr/lib/x86_64-linux-gnu | grep libopencv
root@b865d9c1f5da:/home/user/darknet# 
```

Ubuntu 18.04에서 설치된 라이브러리를 다음 명령어로 볼 수 있습니다.

#### Hint

앞서 설치할 때 `libjasper-dev`의 설치가 실패했습니다.

```bash
apt -y install libjasper-dev
  ...
E: Unable to locate package libjasper-dev
```

#### Action

수동으로 설치를 했습니다.

```bash

apt-get install -y build-essential cmake

wget https://github.com/mdadams/jasper/archive/version-2.0.16.tar.gz -O jasper-version-2.0.16.tar.gz
tar xvf jasper-version-2.0.16.tar.gz
cd jasper-version-2.0.16/

mkdir build

#### Change the directory accordingly

export SOURCE_DIR=/home/user/darknet/jasper-version-2.0.16
export BUILD_DIR=/home/user/darknet/jasper-version-2.0.16/build
cd $BUILD_DIR
cmake -G "Unix Makefiles" -H$SOURCE_DIR -B$BUILD_DIR
cd $BUILD_DIR
make clean all
make test
```

#### Action

OpenCV를 다시 컴파일 했습니다.

```bash
root@b865d9c1f5da:/home/user/darknet# cd build/
root@b865d9c1f5da:/home/user/darknet#cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-master/modules ../opencv-master
root@b865d9c1f5da:/home/user/darknet#cmake --build .
root@b865d9c1f5da:/home/user/darknet#make install
```

대부분 컴파일이 끝났기 때문에 이번에는 금방 컴파일 및 설치가 끝났습니다.

하지만 여전히 문제군요.



```bash
$ ls /usr/lib/x86_64-linux-gnu | grep libopencv
libopencv_aruco.a
  ...
libopencv_xphoto.so.3.2.0
$
```

재설치 후

```bash
root@b865d9c1f5da:/home/user/darknet/build# make install
  ...
- Up-to-date: /usr/local/lib/libopencv_stereo.so
  ...
-- Up-to-date: /usr/local/share/opencv4/lbpcascades/lbpcascade_silverware.xml
   ...
-- Up-to-date: /usr/local/bin/opencv_version
root@b865d9c1f5da:/home/user/darknet/build# 

```

위치를 확인해봤습니다.

```bash
root@b865d9c1f5da:/home/user/darknet/build# cd /usr/local/share/
root@b865d9c1f5da:/usr/local/share# ls
ca-certificates  fonts  licenses  man  opencv4
root@b865d9c1f5da:/usr/local/share# 
```

파일이 있습니다.

```bash
root@b865d9c1f5da:/usr/local/share# cd /usr/local/bin/
root@b865d9c1f5da:/usr/local/bin# ls
opencv_annotation               opencv_version        opencv_waldboost_detector
opencv_interactive-calibration  opencv_visualisation  setup_vars_opencv4.sh
root@b865d9c1f5da:/usr/local/bin# ./opencv_version
4.5.1-dev
root@b865d9c1f5da:/usr/local/bin# 
```



#### Problem

```bash
root@b865d9c1f5da:/home/user/darknet# make
   ...
Package opencv was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opencv' found
./src/image_opencv.cpp:5:10: fatal error: opencv2/opencv.hpp: No such file or directory
 #include "opencv2/opencv.hpp"
          ^~~~~~~~~~~~~~~~~~~~
compilation terminated.
Makefile:86: recipe for target 'obj/image_opencv.o' failed
make: *** [obj/image_opencv.o] Error 1
root@b865d9c1f5da:/home/user/darknet#
```

#### Hint

Google search: Package opencv was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opencv' found

* [Package opencv was not found in the pkg-config search path](https://stackoverflow.com/questions/15320267/package-opencv-was-not-found-in-the-pkg-config-search-path)

> **-------UPDATE-------**
>
> OK, I figured out how to solve the problem...
>
> I made a file named "opencv.pc" and copied it to "/usr/local/lib/pkgconfig" Then i added these two lines to ".bashrc":
>
> ```
> PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
> export PKG_CONFIG_PATH
> ```
>
> that's it! everything is OK now.
>
> the contents of the file are:
>
> ```
> prefix=/usr
> exec_prefix=${prefix}
> includedir=${prefix}/include
> libdir=${exec_prefix}/lib
> 
> Name: opencv
> Description: The opencv library
> Version: 2.x.x
> Cflags: -I${includedir}/opencv -I${includedir}/opencv2
> Libs: -L${libdir} -lopencv_calib3d -lopencv_imgproc -lopencv_contrib -lopencv_legacy -lopencv_core -lopencv_ml -lopencv_features2d -lopencv_objdetect -lopencv_flann -lopencv_video -lopencv_highgui
> ```
>
> **UPDATE - 2014**



```bash
root@b865d9c1f5da:/usr/local/lib# mkdir pkgconfig
root@b865d9c1f5da:/usr/local/lib# cd pkgconfig/
root@b865d9c1f5da:/usr/local/lib/pkgconfig# nano opencv.pc
root@b865d9c1f5da:/usr/local/lib/pkgconfig# PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfigroot@b865d9c1f5da:/usr/local/lib/pkgconfig# export PKG_CONFIG_PATH
root@b865d9c1f5da:/usr/local/lib/pkgconfig# 
```

컴파일해봅니다

```bash
root@b865d9c1f5da:/usr/local/lib/pkgconfig# cd /home/user/darknet/
root@b865d9c1f5da:/home/user/darknet# make
```

#### Problem

앞의 문제는 사라졌지만 다른 에러가 발생했습니다.

```bash
g++ -Iinclude/ -Isrc/ -DOPENCV `pkg-config --cflags opencv`  -DGPU -I/usr/local/cuda/include/ -Wall -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -fPIC -Ofast -DOPENCV -DGPU -c ./src/image_opencv.cpp -o obj/image_opencv.o
./src/image_opencv.cpp:5:10: fatal error: opencv2/opencv.hpp: No such file or directory
 #include "opencv2/opencv.hpp"
          ^~~~~~~~~~~~~~~~~~~~
compilation terminated.
Makefile:86: recipe for target 'obj/image_opencv.o' failed
make: *** [obj/image_opencv.o] Error 1
root@b865d9c1f5da:/home/user/darknet# 

```

#### Hint

Google search: darknet opencv ./src/image_opencv.cpp:5:10: fatal error: opencv2/opencv.hpp: No such file or directory #include "opencv2/opencv.hpp"

* [./src/image_opencv.cpp:5:10: fatal error: opencv2/opencv.hpp: No such file or directory #1886](https://github.com/pjreddie/darknet/issues/1886)
* 

#### Action

```bash
root@b865d9c1f5da:/home/user/darknet# pkg-config --libs opencv4
Package opencv4 was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv4.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opencv4' found
root@b865d9c1f5da:/home/user/darknet# pkg-config --libs opencv 
-lopencv_calib3d -lopencv_imgproc -lopencv_contrib -lopencv_legacy -lopencv_core -lopencv_ml -lopencv_features2d -lopencv_objdetect -lopencv_flann -lopencv_video -lopencv_highgui
root@b865d9c1f5da:/home/user/darknet# 

```

#### Action

`.bashrc`를 업데이트 합니다.

```bash
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkg export PKG_CONFIG_PATH
```

```bash
root@b865d9c1f5da:/home/user/darknet# nano /home/user/.bashrc
root@b865d9c1f5da:/home/user/darknet# source /home/user/.bashrc
root@b865d9c1f5da:/home/user/darknet# echo $PKG_CONFIG_PATH
:/usr/local/lib/pkgconfig:/usr/local/lib/pkg
root@b865d9c1f5da:/home/user/darknet# 
```

그냥...



* [yolov3 ./src/image_opencv.cpp:5:10: fatal error: opencv2/opencv.hpp: No such file or directory](https://www.programmersought.com/article/59515928706/)

  > Solution:
  >
  > sudo apt install libopencv-dev
  >
  > After installing this library, make it ok.

```bash
root@b865d9c1f5da:/home/user/darknet# apt install -y libopencv-dev
  ...
------------------

Please select the geographic area in which you live. Subsequent configuration questions will narrow
this down by presenting a list of cities, representing the time zones in which they are located.

  1. Africa   3. Antarctica  5. Arctic  7. Atlantic  9. Indian    11. SystemV  13. Etc
  2. America  4. Australia   6. Asia    8. Europe    10. Pacific  12. US
Geographic area: 6

Please select the city or region corresponding to your time zone.

  1. Aden         19. Chongqing    37. Jerusalem     55. Novokuznetsk   73. Taipei
  2. Almaty       20. Colombo      38. Kabul         56. Novosibirsk    74. Tashkent
  3. Amman        21. Damascus     39. Kamchatka     57. Omsk           75. Tbilisi
  4. Anadyr       22. Dhaka        40. Karachi       58. Oral           76. Tehran
  5. Aqtau        23. Dili         41. Kashgar       59. Phnom_Penh     77. Tel_Aviv
  6. Aqtobe       24. Dubai        42. Kathmandu     60. Pontianak      78. Thimphu
  7. Ashgabat     25. Dushanbe     43. Khandyga      61. Pyongyang      79. Tokyo
  8. Atyrau       26. Famagusta    44. Kolkata       62. Qatar          80. Tomsk
  9. Baghdad      27. Gaza         45. Krasnoyarsk   63. Qostanay       81. Ujung_Pandang
  10. Bahrain     28. Harbin       46. Kuala_Lumpur  64. Qyzylorda      82. Ulaanbaatar
  11. Baku        29. Hebron       47. Kuching       65. Rangoon        83. Urumqi
  12. Bangkok     30. Ho_Chi_Minh  48. Kuwait        66. Riyadh         84. Ust-Nera
  13. Barnaul     31. Hong_Kong    49. Macau         67. Sakhalin       85. Vientiane
  14. Beirut      32. Hovd         50. Magadan       68. Samarkand      86. Vladivostok
  15. Bishkek     33. Irkutsk      51. Makassar      69. Seoul          87. Yakutsk
  16. Brunei      34. Istanbul     52. Manila        70. Shanghai       88. Yangon
  17. Chita       35. Jakarta      53. Muscat        71. Singapore      89. Yekaterinburg
  18. Choibalsan  36. Jayapura     54. Nicosia       72. Srednekolymsk  90. Yerevan
Time zone: 69
  ...
root@b865d9c1f5da:/home/user/darknet# 
```

빙고!!! 다음 스텝으로 넘어갔습니다.

```bash
# make
  ...
cal/cuda/lib64 -lcuda -lcudart -lcublas -lcurand -lstdc++ 
/usr/bin/ld: cannot find -lopencv_contrib
/usr/bin/ld: cannot find -lopencv_legacy
collect2: error: ld returned 1 exit status
Makefile:83: recipe for target 'libdarknet.so' failed
make: *** [libdarknet.so] Error 1
root@b865d9c1f5da:/home/user/darknet# 
```



```bash
root@b865d9c1f5da:/home/user/darknet# nano /home/user/.bashrc
root@b865d9c1f5da:/home/user/darknet# source /home/user/.bashrc
root@b865d9c1f5da:/home/user/darknet# echo $LD_LIBRARY_PATH
/usr/local/cuda/lib64:/usr/local/nvidia/lib:/usr/local/nvidia/lib64
root@b865d9c1f5da:/home/user/darknet# 
root@b865d9c1f5da:/home/user/darknet# nano /home/user/.bashrc
root@b865d9c1f5da:/home/user/darknet# source /home/user/.bashrc

```

```bash
root@b865d9c1f5da:/home/user/darknet# cat /home/user/.bashrc
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkg
export PKG_CONFIG_PATH

export PATH=/usr/local/cuda/bin:/$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
root@b865d9c1f5da:/home/user/darknet# 

```

확인합니다.

```bash
root@b865d9c1f5da:/home/user/darknet# make
  ...
64 -lcuda -lcudart -lcublas -lcurand -lstdc++ 
/usr/bin/ld: cannot find -lopencv_contrib
/usr/bin/ld: cannot find -lopencv_legacy
collect2: error: ld returned 1 exit status
Makefile:83: recipe for target 'libdarknet.so' failed
make: *** [libdarknet.so] Error 1
root@b865d9c1f5da:/home/user/darknet#

```

밤 10시 5분. 머리가 도저히 안 돌아간다. 이건 바로 못 고칠 지도... 집에 가서 해야겠다.



```bash
$ docker ps
CONTAINER ID  IMAGE                     COMMAND        NAMES
1e6bdeec1030  baseimage-darknet:ver0.2  "bash"   ...   vibrant_bartik
b865d9c1f5da  baseimage-darknet:ver0.2  "bash"   ...   quirky_engelbart
  ...
$ docker commit b865d9c1f5da baseimage-darknet:ver0.3
sha256:9ed3aa90a41c8f2d490b2c5b0d5380c7072eef5458bbd4d21e96202942c25a8c
$ docker images
REPOSITORY         TAG     IMAGE ID      CREATED         SIZE
baseimage-darknet  ver0.3  9ed3aa90a41c  17 seconds ago  10.2GB
baseimage-darknet  ver0.2  40b7c6a87c86  3 hours ago     8.36GB
baseimage-darknet  latest  3d0a19184aa9  4 hours ago     7.27GB
  ...
$ docker export b865d9c1f5da > baseimage-darknet_ver0_3.tar
$ ls
  ...
baseimage-darknet_ver0_3.tar
  ...
$
```

USB로 복사. 파일 사이즈가 크기 때문에 `NTFS` 혹은 `exFAT`으로 포맷이 되어있어야 합니다. `FAT`으로 포맷이 되어 있을 경우, 4.3GB 까지만 복사를 하고 에러가 발생합니다.





