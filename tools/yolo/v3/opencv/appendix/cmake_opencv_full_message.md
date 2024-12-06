* Draft: 2021-01-26 (Tue)

# cmake 시 성공적으로 컴파일한 경우

(base) k8smaster@k8smaster-Alienware-Aurora-R7:~/opencv/opencv-4.5.1/build`$에서 실행되었습니다.

contrib 폴더와 함께 실행한 경우입니다.

```bash
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
> -D CMAKE_INSTALL_PREFIX=/usr/local \
> -D WITH_TBB=OFF \
> -D WITH_IPP=OFF \
> -D WITH_1394=OFF \
> -D BUILD_WITH_DEBUG_INFO=OFF \
> -D BUILD_DOCS=OFF \
> -D INSTALL_C_EXAMPLES=ON \
> -D INSTALL_PYTHON_EXAMPLES=ON \
> -D BUILD_EXAMPLES=OFF \
> -D BUILD_TESTS=OFF \
> -D BUILD_PERF_TESTS=OFF \
> -D WITH_QT=OFF \
> -D WITH_GTK=ON \
> -D WITH_OPENGL=ON \
> -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.5.1/modules \
> -D WITH_V4L=ON  \
> -D WITH_FFMPEG=ON \
> -D WITH_XINE=ON \
> -D BUILD_NEW_PYTHON_SUPPORT=ON \
> -D OPENCV_GENERATE_PKGCONFIG=ON ../
```

```bash
-- Detected processor: x86_64
-- Looking for ccache - not found
-- Found ZLIB: /usr/lib/x86_64-linux-gnu/libz.so (found suitable version "1.2.11", minimum required is "1.2.3") 
Cleaning INTERNAL cached variable: WEBP_LIBRARY
Cleaning INTERNAL cached variable: WEBP_INCLUDE_DIR
-- Could NOT find OpenJPEG (minimal suitable version: 2.0, recommended version >= 2.3.1). OpenJPEG will be built from sources
-- OpenJPEG: VERSION = 2.3.1, BUILD = opencv-4.5.1-openjp2-2.3.1
-- OpenJPEG libraries will be built from sources: libopenjp2 (version "2.3.1")
-- Found ZLIB: /usr/lib/x86_64-linux-gnu/libz.so (found version "1.2.11") 
-- Could not find OpenBLAS include. Turning OpenBLAS_FOUND off
-- Could not find OpenBLAS lib. Turning OpenBLAS_FOUND off
-- Could NOT find Atlas (missing: Atlas_CLAPACK_INCLUDE_DIR) 
-- A library with BLAS API found.
-- A library with LAPACK API found.
-- Could NOT find JNI (missing: JAVA_INCLUDE_PATH JAVA_INCLUDE_PATH2 JAVA_AWT_INCLUDE_PATH) 
-- VTK is not found. Please set -DVTK_DIR in CMake to VTK build directory, or to VTK install subdirectory with VTKConfig.cmake file
-- OpenCV Python: during development append to PYTHONPATH: /home/k8smaster/opencv/opencv-4.5.1/build/python_loader
-- Checking for module 'libavresample'
--   No package 'libavresample' found
-- Module opencv_alphamat disabled because the following dependencies are not found: Eigen
-- Caffe:   NO
-- Protobuf:   NO
-- Glog:   NO
-- Checking for module 'freetype2'
--   Found freetype2, version 21.0.15
-- Checking for module 'harfbuzz'
--   Found harfbuzz, version 1.7.2
-- freetype2:   YES (ver 21.0.15)
-- harfbuzz:    YES (ver 1.7.2)
-- HDF5: Using hdf5 compiler wrapper to determine C configuration
-- Found HDF5: /home/k8smaster/anaconda3/lib/libhdf5.so;/usr/lib/x86_64-linux-gnu/librt.so;/usr/lib/x86_64-linux-gnu/libpthread.so;/home/k8smaster/anaconda3/lib/libz.so;/usr/lib/x86_64-linux-gnu/libdl.so;/usr/lib/x86_64-linux-gnu/libm.so (found version "1.10.4")  
-- Julia not found. Not compiling Julia Bindings. 
-- Module opencv_ovis disabled because OGRE3D was not found
-- No preference for use of exported gflags CMake configuration set, and no hints for include/library directories provided. Defaulting to preferring an installed/exported gflags CMake configuration if available.
-- Failed to find installed gflags CMake configuration, searching for gflags build directories exported with CMake.
-- Failed to find gflags - Failed to find an installed/exported CMake configuration for gflags, will perform search for installed gflags components.
-- Failed to find gflags - Could not find gflags include directory, set GFLAGS_INCLUDE_DIR to directory containing gflags/gflags.h
-- Failed to find glog - Could not find glog include directory, set GLOG_INCLUDE_DIR to directory containing glog/logging.h
-- Module opencv_sfm disabled because the following dependencies are not found: Eigen Glog/Gflags
-- Checking for module 'tesseract'
--   No package 'tesseract' found
-- Tesseract:   NO
-- Allocator metrics storage type: 'long long'
-- HDF5: Using hdf5 compiler wrapper to determine C configuration
-- Registering hook 'INIT_MODULE_SOURCES_opencv_dnn': /home/k8smaster/opencv/opencv-4.5.1/modules/dnn/cmake/hooks/INIT_MODULE_SOURCES_opencv_dnn.cmake
-- opencv_dnn: filter out cuda4dnn source code
-- rgbd: CERES support is disabled. Ceres Solver is Required for Posegraph optimization
-- xfeatures2d/boostdesc: Download: boostdesc_bgm.i
-- xfeatures2d/boostdesc: Download: boostdesc_bgm_bi.i
-- xfeatures2d/boostdesc: Download: boostdesc_bgm_hd.i
-- xfeatures2d/boostdesc: Download: boostdesc_binboost_064.i
-- xfeatures2d/boostdesc: Download: boostdesc_binboost_128.i
-- xfeatures2d/boostdesc: Download: boostdesc_binboost_256.i
-- xfeatures2d/boostdesc: Download: boostdesc_lbgm.i
-- xfeatures2d/vgg: Download: vgg_generated_48.i
-- xfeatures2d/vgg: Download: vgg_generated_64.i
-- xfeatures2d/vgg: Download: vgg_generated_80.i
-- xfeatures2d/vgg: Download: vgg_generated_120.i
-- data: Download: face_landmark_model.dat
-- 
-- General configuration for OpenCV 4.5.1 =====================================
--   Version control:               unknown
-- 
--   Extra modules:
--     Location (extra):            /home/k8smaster/opencv/opencv_contrib-4.5.1/modules
--     Version control (extra):     unknown
-- 
--   Platform:
--     Timestamp:                   2021-01-26T09:29:16Z
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
--       requested:                 SSE4_1 SSE4_2 AVX FP16 AVX2 AVX512_SKX
--       SSE4_1 (15 files):         + SSSE3 SSE4_1
--       SSE4_2 (1 files):          + SSSE3 SSE4_1 POPCNT SSE4_2
--       FP16 (0 files):            + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 AVX
--       AVX (4 files):             + SSSE3 SSE4_1 POPCNT SSE4_2 AVX
--       AVX2 (29 files):           + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2
--       AVX512_SKX (4 files):      + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2 AVX_512F AVX512_COMMON AVX512_SKX
-- 
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++ standard:                11
--     C++ Compiler:                /usr/bin/c++  (ver 7.5.0)
--     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
--     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
--     C Compiler:                  /usr/bin/cc
--     C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
--     C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
--     Linker flags (Release):      -Wl,--gc-sections -Wl,--as-needed  
--     Linker flags (Debug):        -Wl,--gc-sections -Wl,--as-needed  
--     ccache:                      NO
--     Precompiled headers:         NO
--     Extra dependencies:          dl m pthread rt
--     3rdparty dependencies:
-- 
--   OpenCV modules:
--     To be built:                 aruco bgsegm bioinspired calib3d ccalib core datasets dnn dnn_objdetect dnn_superres dpm face features2d flann freetype fuzzy gapi hdf hfs highgui img_hash imgcodecs imgproc intensity_transform line_descriptor mcc ml objdetect optflow phase_unwrapping photo plot python2 quality rapid reg rgbd saliency shape stereo stitching structured_light superres surface_matching text tracking video videoio videostab xfeatures2d ximgproc xobjdetect xphoto
--     Disabled:                    world
--     Disabled by dependency:      -
--     Unavailable:                 alphamat cnn_3dobj cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev cvv java julia matlab ovis python3 sfm ts viz
--     Applications:                apps
--     Documentation:               NO
--     Non-free algorithms:         NO
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
--     WEBP:                        build (ver encoder: 0x020f)
--     PNG:                         /usr/lib/x86_64-linux-gnu/libpng.so (ver 1.6.34)
--     TIFF:                        /usr/lib/x86_64-linux-gnu/libtiff.so (ver 42 / 4.0.9)
--     JPEG 2000:                   build (ver 2.3.1)
--     OpenEXR:                     build (ver 2.3.0)
--     HDR:                         YES
--     SUNRASTER:                   YES
--     PXM:                         YES
--     PFM:                         YES
-- 
--   Video I/O:
--     FFMPEG:                      YES
--       avcodec:                   YES (57.107.100)
--       avformat:                  YES (57.83.100)
--       avutil:                    YES (55.78.100)
--       swscale:                   YES (4.8.100)
--       avresample:                NO
--     GStreamer:                   YES (1.14.5)
--     v4l/v4l2:                    YES (linux/videodev2.h)
--     Xine:                        NO
-- 
--   Parallel framework:            pthreads
-- 
--   Trace:                         YES (with Intel ITT)
-- 
--   Other third-party libraries:
--     Lapack:                      NO
--     Eigen:                       NO
--     Custom HAL:                  NO
--     Protobuf:                    build (3.5.1)
-- 
--   OpenCL:                        YES (no extra features)
--     Include path:                /home/k8smaster/opencv/opencv-4.5.1/3rdparty/include/opencl/1.2
--     Link libraries:              Dynamic load
-- 
--   Python 2:
--     Interpreter:                 /usr/bin/python2.7 (ver 2.7.17)
--     Libraries:                   /usr/lib/x86_64-linux-gnu/libpython2.7.so (ver 2.7.17)
--     numpy:                       /usr/lib/python2.7/dist-packages/numpy/core/include (ver 1.13.3)
--     install path:                lib/python2.7/dist-packages/cv2/python-2.7
-- 
--   Python (for build):            /usr/bin/python2.7
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
-- Build files have been written to: /home/k8smaster/opencv/opencv-4.5.1/build
$
```
