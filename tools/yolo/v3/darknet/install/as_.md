* Draft: 2021-02-02 (Tue)

* [Ubuntu 18.04에 OpenCV 4.2.0 설치하는 방법](https://webnautes.tistory.com/1186)
  * 중간에 에러가 발생해서 중단...
  * 연관된 문서이므로 필요 시 나중에 참고.
    * [Ubuntu 18.04에서 Sublime Text 3를 사용하여 OpenCV 개발환경 만들기](https://webnautes.tistory.com/1187)
    * [Ubuntu 20.04에 CUDA를 사용하도록 OpenCV 4.4.0 설치하는 방법](https://webnautes.tistory.com/1435)

```bash
$ ./run_cmake 
-- Detected processor: x86_64
-- Looking for ccache - not found
-- Found ZLIB: /usr/lib/x86_64-linux-gnu/libz.so (found suitable version "1.2.11", minimum required is "1.2.3") 
-- Found ZLIB: /usr/lib/x86_64-linux-gnu/libz.so (found version "1.2.11") 
-- Could not find OpenBLAS include. Turning OpenBLAS_FOUND off
-- Could not find OpenBLAS lib. Turning OpenBLAS_FOUND off
-- Could NOT find Atlas (mitime make -j4ssing: Atlas_CLAPACK_INCLUDE_DIR) 
-- A library with BLAS API found.
-- A library with LAPACK API found.
-- Could NOT find JNI (missing: JAVA_INCLUDE_PATH JAVA_INCLUDE_PATH2 JAVA_AWT_INCLUDE_PATH) 
-- VTK is not found. Please set -DVTK_DIR in CMake to VTK build directory, or to VTK install subdirectory with VTKConfig.cmake file
-- OpenCV Python: during development append to PYTHONPATH: /home/k8smaster/opencv/opencv-4.2.0/build/python_loader
-- Checking for module 'libavresample'
--   No package 'libavresample' found
-- Caffe:   NO
-- Protobuf:   NO
-- Glog:   NO
-- freetype2:   YES (ver 21.0.15)
-- harfbuzz:    YES (ver 1.7.2)
-- HDF5: Using hdf5 compiler wrapper to determine C configuration
-- Module opencv_ovis disabled because OGRE3D was not found
-- No preference for use of exported gflags CMake configuration set, and no hints for include/library directories provided. Defaulting to preferring an installed/exported gflags CMake configuration if available.
-- Failed to find installed gflags CMake configuration, searching for gflags build directories exported with CMake.
-- Failed to find gflags - Failed to find an installed/exported CMake configuration for gflags, will perform search for installed gflags components.
-- Failed to find gflags - Could not find gflags include directory, set GFLAGS_INCLUDE_DIR to directory containing gflags/gflags.h
-- Failed to find glog - Could not find glog include directory, set GLOG_INCLUDE_DIR to directory containing glog/logging.h
-- Module opencv_sfm disabled because the following dependencies are not found: Glog/Gflags
-- Checking for module 'tesseract'
--   No package 'tesseract' found
-- Tesseract:   NO
-- HDF5: Using hdf5 compiler wrapper to determine C configuration
-- Registering hook 'INIT_MODULE_SOURCES_opencv_dnn': /home/k8smaster/opencv/opencv-4.2.0/modules/dnn/cmake/hooks/INIT_MODULE_SOURCES_opencv_dnn.cmake
-- opencv_dnn: filter out cuda4dnn source code

** (gedit:28390): WARNING **: 16:02:42.263: Error querying file info: “/home/k8smaster/opencv/opencv-4.2.0/build/cvconfig.h.tmp” 파일 정보를 가져오는 중 오류: 그런 파일이나 디렉터리가 없습니다
CMake Warning at cmake/OpenCVGenSetupVars.cmake:54 (message):
  CONFIGURATION IS NOT SUPPORTED: validate setupvars script in install
  directory
Call Stack (most recent call first):
  CMakeLists.txt:947 (include)


-- 
-- General configuration for OpenCV 4.2.0 =====================================
--   Version control:               unknown
-- 
--   Extra modules:
--     Location (extra):            /home/k8smaster/opencv/opencv_contrib-4.2.0/modules
--     Version control (extra):     unknown
-- 
--   Platform:
--     Timestamp:                   2021-02-02T06:49:53Z
--     Host:                        Linux 4.15.0-134-generic x86_64
--     CMake:                       3.10.2
--     CMake generator:             Unix Makefiles
--     CMake build tool:            /usr/bin/make
--     Configuration:               RELEASE
-- 
--   CPU/HW features:
--     Baseline:                    SSE SSE2 SSE3
--       requested:                 SSE3
--     Dispatched code generation:  SSE4_1 SSE4_2 FP16 AVX AVX2 AVX512_SKX
--       requested:        time make -j4         SSE4_1 SSE4_2 AVX FP16 AVX2 AVX512_SKX
--       SSE4_1 (14 files):         + SSSE3 SSE4_1
--       SSE4_2 (1 files):          + SSSE3 SSE4_1 POPCNT SSE4_2
--       FP16 (0 files):            + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 AVX
--       AVX (4 files):             + SSSE3 SSE4_1 POPCNT SSE4_2 AVX
--       AVX2 (27 files):           + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2
--       AVX512_SKX (3 files):      + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2 AVX_512F AVX512_COMMON AVX512_SKX
-- pkg-config --modversion opencv4
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++ Compiler:                /usr/bin/c++  (ver 7.5.0)
--     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
--     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
--     C Compiler:                  /usr/bin/cc
--     C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
--     C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
--     Linker flags (Release):      -Wl,--gc-sections  
--     Linker flags (Debug):        -Wl,--gc-sections  
--     ccache:                      NO
--     Precompiled headers:         NO
--     Extra dependencies:          dl m pthread rt
--     3rdparty dependencies:
-- 
--   OpenCV modules:
--     To be built:                 aruco bgsegm bioinspired calib3d ccalib core datasets dnn dnn_objdetect dnn_superres dpm face features2d flann freetype fuzzy gapi hdf hfs highgui img_hash imgcodecs imgproc line_descriptor ml objdetect optflow phase_unwrapping photo plot python2 quality reg rgbd saliency shape stereo stitching structured_light superres surface_matching text tracking video videoio videostab xfeatures2d ximgproc xobjdetect xphoto
--     Disabled:                    world
--     Disabled by dependency:      -
--     Unavailable:                 cnn_3dobj cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev cvv java js matlab ovis python3 sfm ts viz
--     Applications:                apps
--     Documentation:               NO
--     Non-free algorithms:         YES
-- 
--   GUI: 
--     GTK+:                        YES (ver 3.22.30)
--       GThread :                  YES (ver 2.56.4)
--       GtkGlExt:                  NO
--     OpenGL support:              NO
--     VTK support:                 NO
-- 
--   Media I/O: 
--     ZLib:                        /usr/lib/x86_64-linux-gnu/libz.so (ver 1.2.11)
--     JPEG:                        /usr/lib/x86_64-linux-gnu/libjpeg.so (ver 80)
--     WEBP:                        build (ver encoder: 0x020e)
--     PNG:                         /usr/lib/x86_64-linux-gnu/libpng.so (ver 1.6.34)
--     TIFF:                        /usr/lib/x86_64-linux-gnu/libtiff.so (ver 42 / 4.0.9)
--     JPEG 2000:                   /usr/lib/x86_64-linux-gnu/libjasper.so (ver 1.900.1)
--     OpenEXR:                     build (ver 2.3.0)
--     HDR:                         YES
--     SUNRASTER:                   YES
--     PXM:                         YES
--     PFM:                         YES
-- time make -j4
--   Video I/O:
--     FFMPEG:                      YES
--       avcodec:                   YES (57.107.100)
--       avformat:                  YES (57.83.100)
--       avuimagetil:                    YES (55.78.100)
--       swscale:                   YES (4.8.100)
--       avresample:                NO
--     GStreamer:                   YES (1.14.5)
--     v4l/v4l2:                    YES (linux/videodev2.h)
--     Xine:                        YES (ver 1.2.8)
-- 
--   Parallel framework:            pthreads
-- 
--   Trace:                         YES (with Intel ITT)
-- 
--   Other third-party libraries:
--     Lapack:                      NO
--     Eigen:                       YES (ver 3.3.4)
--     Custom HAL:                  NO
--     Protobuf:                    build (3.5.1)
-- 
--   OpenCL:                        YES (no extra features)
--     Include path:                /home/k8smaster/opencv/opencv-4.2.0/3rdparty/include/opencl/1.2
--     Link libraries:              Dynamic load
-- 
--   Python 2:
--     Interpreter:                 /usr/bin/python2.7 (ver 2.7.17)
--     Libraries:                   /usr/lib/x86_64-linux-gnu/libpython2.7.so (ver 2.7.17)
--     numpy:                       /usr/lib/python2.7/dist-packages/numpy/core/include/ (ver 1.13.3)
--     install path:                /usr/lib/python2.7/dist-packages/cv2/python-2.7
-- 
--   Python (for build):    time make -j4        /usr/bin/python2.7
-- 
--   Java:                          
--     ant:                         NO
--     JNI:                         NO
--     Java wrappers:               NO
--     Java tests:                  NO
-- 
--   Install to:                    /usr/local
-- -----------------------------------------------------------------
-- 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/k8smaster/opencv/opencv-4.2.0/build
[2]+  완료                  gedit Makefile
$
```



```bash
$ time make -j4
```

컴파일 결과물을 설치합니다.

```bash
$ sudo make install
  ...
[100%] Built target opencv_python2

real	6m41.782s
user	21m49.759s
sys	1m11.822s
$
```

/etc/ld.so.conf.d/ 디렉토리에 **/usr/local/lib**를 포함하는 설정파일이 있는지 확인합니다.

```bash
/etc/ld.so.conf.d$ ls
cuda-10-1.conf  cuda-10-2.conf  cuda-11-0.conf  libc.conf  x86_64-linux-gnu.conf
$
```

```bash
$ cat /etc/ld.so.conf.d/*
/usr/local/cuda-10.1/targets/x86_64-linux/lib
/usr/local/cuda-10.2/targets/x86_64-linux/lib
/usr/local/cuda-11.0/targets/x86_64-linux/lib
# libc default configuration
/usr/local/lib
# Multiarch support
/usr/local/lib/x86_64-linux-gnu
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu
$
```

아래 처럼 있기 때문에 설정파일이 있는 것으로 확인되었습니다.

```bash
# libc default configuration
/usr/local/lib

```

설치 결과 확인

```bash
$ g++ -o facedetect /usr/local/share/opencv4/samples/cpp/facedetect.cpp $(pkg-config opencv4 --libs --cflags)
Package opencv4 was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv4.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opencv4' found
g++: error: /usr/local/share/opencv4/samples/cpp/facedetect.cpp: 그런 파일이나 디렉터리가 없습니다
g++: fatal error: no input files
compilation terminated.
$ cd /usr/local/share/opencv4/samples/cpp/
bash: cd: /usr/local/share/opencv4/samples/cpp/: 그런 파일이나 디렉터리가 없습니다
$
```

> ## 5.2. Python
>
> \1. python 2.x와 python 3x에서 opencv 라이브러리를 사용가능한지는 다음처럼 확인합니다.
>
> 각각 OpenCV 버전이 출력되어야 합니다. 