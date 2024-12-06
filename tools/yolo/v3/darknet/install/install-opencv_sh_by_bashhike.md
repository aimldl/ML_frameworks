* Draft: 2021-02-02 (Tue)

google search: opencv bash script 

## [milq](https://github.com/milq/milq)/[scripts](https://github.com/milq/milq/tree/master/scripts)/[bash](https://github.com/milq/milq/tree/master/scripts/bash)/[install-opencv.sh](https://github.com/milq/milq/blob/master/scripts/bash/install-opencv.sh)

```bash
$ ./install-opencv.sh
```

fails with the following error message.

```bash
[ 28%] Linking CXX executable ../../bin/opencv_test_core
../../lib/libopencv_imgcodecs.so.4.2.0: undefined reference to `TIFFReadDirectory@LIBTIFF_4.0'
  ...
undefined reference to `TIFFReadRGBAStrip@LIBTIFF_4.0'
collect2: error: ld returned 1 exit status
modules/core/CMakeFiles/opencv_test_core.dir/build.make:1274: recipe for target 'bin/opencv_test_core' failed
make[2]: *** [bin/opencv_test_core] Error 1
CMakeFiles/Makefile2:2505: recipe for target 'modules/core/CMakeFiles/opencv_test_core.dir/all' failed
make[1]: *** [modules/core/CMakeFiles/opencv_test_core.dir/all] Error 2
Makefile:162: recipe for target 'all' failed
make: *** [all] Error 2
$
```



[bashhike](https://gist.github.com/bashhike)/[install-opencv.sh](https://gist.github.com/bashhike/ebb59a541ea4a559daa0b6e798fd5ffa)

* Let's use this script if the previous attempt fails.
* Also refer to [How to install OpenCV 4.2.0 with CUDA 10.0 in Ubuntu distro 18.04](https://gist.github.com/raulqf/f42c718a658cddc16f9df07ecc627be7)

```bash
  ...

-- Configuring incomplete, errors occurred!
See also "/home/k8smaster/opencv-3.1.0/build/CMakeFiles/CMakeOutput.log".
See also "/home/k8smaster/opencv-3.1.0/build/CMakeFiles/CMakeError.log".
Starting compilation ...
make: *** 타겟이 지정되지 않았고 메이크파일이 없습니다.  멈춤.
Installing to /usr/local/ ...
make: *** 타겟 'install'을(를) 만들 규칙이 없습니다.  멈춤.
Configuring linker ...
Voila! All done. OpenCV-3.1.0 is now installed.
$
```

