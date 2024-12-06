

* Draft: 2021-02-02 (Tue)

# OpenCV 설정하는 방법

[OpenCV configuration options reference](https://docs.opencv.org/master/db/d05/tutorial_config_reference.html)에 설정하는 방법에 대해 상세히 나와있습니다. 리눅스에서 darknet 및 YOLO를 사용할 때 연관이 있어 보이는 부분을 발췌해봅니다.

> # Introduction
>
> - Note
>
>   We assume you have read [OpenCV installation overview](https://docs.opencv.org/master/d0/d3d/tutorial_general_install.html) tutorial or have experience with CMake.
>
> Configuration options can be set in several different ways:
>
> - Command line: `cmake -Doption=value ...`
> - Initial cache files: `cmake -C my_options.txt ...`
> - Interactive via GUI
>
> In this reference we will use regular command line.



> ## Video reading and writing (videoio module)
>
> ### Video4Linux
>
> `WITH_V4L` (Linux; default: *ON* )
>
> Capture images from camera using [Video4Linux](https://en.wikipedia.org/wiki/Video4Linux) API. Linux kernel headers must be installed.
>
> ### FFmpeg
>
> `WITH_FFMPEG` (default: *ON*)
>
> Integration with [FFmpeg](https://en.wikipedia.org/wiki/FFmpeg) library for decoding and encoding video files and network streams. This library can read and write many popular video formats. It consists of several components which must be installed as prerequisites for the build:
>
> - *avcodec*
> - *avformat*
> - *avutil*
> - *swscale*
> - *avresample* (optional)
>
> Exception is Windows platform where a prebuilt [plugin library containing FFmpeg](https://github.com/opencv/opencv_3rdparty/tree/ffmpeg/master) will be downloaded during a configuration stage and copied to the `bin` folder with all produced libraries.
>
> - Note
>
>   [Libav](https://en.wikipedia.org/wiki/Libav) library can be used instead of FFmpeg, but this combination is not actively supported.
>
> ### GStreamer
>
> `WITH_GSTREAMER` (default: *ON*)
>
> Enable integration with [GStreamer](https://en.wikipedia.org/wiki/GStreamer) library for decoding and encoding video files, capturing frames from cameras and network streams. Numerous plugins can be installed to extend supported formats list. OpenCV allows running arbitrary GStreamer pipelines passed as strings to [cv::VideoCapture](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html) and [cv::VideoWriter](https://docs.opencv.org/master/dd/d9e/classcv_1_1VideoWriter.html) objects.
>
> Various GStreamer plugins offer HW-accelerated video processing on different platforms.

> ## Parallel processing
>
> Some of OpenCV algorithms can use multithreading to accelerate processing. OpenCV can be built with one of threading backends.
>
> | Backend  | Option             | Default | Platform  | Description                                                  |
> | -------- | ------------------ | ------- | --------- | ------------------------------------------------------------ |
> | pthreads | `WITH_PTHREADS_PF` | *ON*    | Unix-like | Default backend based on [pthreads](https://en.wikipedia.org/wiki/POSIX_Threads) library is available on Linux, Android and other Unix-like platforms. Thread pool is implemented in OpenCV and can be controlled with environment variables `OPENCV_THREAD_POOL_*`. Please check sources in *modules/core/src/parallel_impl.cpp* file for details. |

> ## GUI backends (highgui module)
>
> OpenCV relies on various GUI libraries for window drawing.
>
> | Option     | Default | Platform | Description                                                  |
> | ---------- | ------- | -------- | ------------------------------------------------------------ |
> | `WITH_GTK` | *ON*    | Linux    | [GTK](https://en.wikipedia.org/wiki/GTK) is a common toolkit in Linux and Unix-like OS-es. By default version 3 will be used if found, version 2 can be forced with the `WITH_GTK_2_X` option. |

> ## Deep learning neural networks inference backends and options (dnn module)
>
> OpenCV have own DNN inference module which have own build-in engine, but can also use other libraries for optimized processing. Multiple backends can be enabled in single build. Selection happens at runtime automatically or manually.
>
> | Option                                                       | Default      | Description                                                  |
> | ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ |
> | `WITH_PROTOBUF`                                              | *ON*         | Enables [protobuf](https://en.wikipedia.org/wiki/Protocol_Buffers) library search. OpenCV can either build own copy of the library or use external one. This dependency is required by the *dnn* module, if it can't be found module will be disabled. |
> | `BUILD_PROTOBUF`                                             | *ON*         | Build own copy of *protobuf*. Must be disabled if you want to use external library. |
> | `PROTOBUF_UPDATE_FILES`                                      | *OFF*        | Re-generate all .proto files. *protoc* compiler compatible with used version of *protobuf* must be installed. |
> | `OPENCV_DNN_OPENCL`                                          | *ON*         | Enable built-in OpenCL inference backend.                    |
> | `WITH_INF_ENGINE`                                            | *OFF*        | Enables [Intel Inference Engine (IE)](https://github.com/openvinotoolkit/openvino) backend. Allows to execute networks in IE format (.xml + .bin). Inference Engine must be installed either as part of [OpenVINO toolkit](https://en.wikipedia.org/wiki/OpenVINO), either as a standalone library built from sources. |
> | `INF_ENGINE_RELEASE`                                         | *2020040000* | Defines version of Inference Engine library which is tied to OpenVINO toolkit version. Must be a 10-digit string, e.g. *2020040000* for OpenVINO 2020.4. |
> | `WITH_NGRAPH`                                                | *OFF*        | Enables Intel NGraph library support. This library is part of Inference Engine backend which allows executing arbitrary networks read from files in multiple formats supported by OpenCV: Caffe, TensorFlow, PyTorch, Darknet, etc.. NGraph library must be installed, it is included into Inference Engine. |
> | `OPENCV_DNN_CUDA`                                            | *OFF*        | Enable CUDA backend. [CUDA](https://en.wikipedia.org/wiki/CUDA), CUBLAS and [CUDNN](https://developer.nvidia.com/cudnn) must be installed. |
> | `WITH_HALIDEIntroduction<br/>Note<br/>We assume you have read OpenCV installation overview tutorial or have experience with CMake.<br/>Configuration options can be set in several different ways:<br/><br/>Command line: cmake -Doption=value ...<br/>Initial cache files: cmake -C my_options.txt ...<br/>Interactive via GUI<br/>In this reference we will use regular command line.` | *OFF*        | Use experimental [Halide](https://en.wikipedia.org/wiki/Halide_(programming_language)) backend which can generate optimized code for dnn-layers at runtime. Halide must be installed. |
> | `WITH_VULKAN`                                                | *OFF*        | Enable experimental [Vulkan](https://en.wikipedia.org/wiki/Vulkan_(API)) backend. Does not require additional dependencies, but can use external Vulkan headers (`VULKAN_INCLUDE_DIRS`). |
> | `WITH_TENGINE`                                               | *OFF*        | Enable experimental [Tengine](https://github.com/OAID/Tengine) backend for ARM CPUs. Tengine library must be installed. |