

## [Toward a Containerized Nvidia CUDA, TensorFlow and OpenCV](https://www.datamachines.io/blog/toward-a-containerized-nvidia-cuda-tensorflow-and-opencv)

* The summary/excerpt of the above tutorial is below.
* Eventually, the tutorial directs to GitHub repository [datamachines](https://github.com/datamachines) / [cuda_tensorflow_opencv](https://github.com/datamachines/cuda_tensorflow_opencv).

> **Setting up the host system to run Nvidia Docker (v2)**
>
> * Install Ubuntu Linux 18.04
> * Install CUDA 10.1 drivers & libraries
> * Install Docker Community Edition
> * Install Nvidia Docker
>
> **DMC's CUDA/TensorFlow/OpenCV**
>
> TensorFlow [https://www.tensorflow.org/] is an open source library to help users develop and train ML models using a comprehensive, flexible ecosystem of tools and libraries. TensorFlow is available as a GPU-optimized container image, running CUDA 9.0 on an Ubuntu 16.04, to create virtual environments that isolate a TensorFlow installation from the rest of the system while sharing the resources of the host machine.
>
> OpenCV (Open Source Computer Vision Library) [https://opencv.org/] is an open source computer vision and machine learning software library, with more than 2500 optimized algorithms to support classic and state-of-the-art computer vision and machine learning algorithms. OpenCV can be built to support CUDA (for GPU support) and OpenMP (for shared-memory and high-level parallelism on multi-core CPUs) [https://www.openmp.org/].
>
> DMC has built a `cuda_tensorflow_opencv` container image by compiling a CUDA/OpenMP-optimized OpenCV `FROM `the GPU-optimized TensorFlow container image. This image is designed to contain many needed tools to be used by data scientists and to support machine learning research, with frameworks such as NumPy [https://www.numpy.org/], pandas [https://pandas.pydata.org/], and Keras [https://keras.io/].
>
> Because of its integration of many core tools and libraries useful to researchers, the image can be used as a `FROM` for further Docker images to build from. For example, it has successfully been used to build a GPU/OpenMP/OpenCV-optimized Darknet (Open Source Neural Networks in C) [https://pjreddie.com/darknet/] "You Only Look Once" (v3) [https://pjreddie.com/darknet/yolo/] processor using Python bindings [https://github.com/madhawav/YOLO3-4-Py].
>
> The container image also has support for X11 display for interactive use, such that a user can call the provided `runDocker.sh` script from any location. That location will then be automatically mounted as `/dmc` and be accessible to the user as an interactive shell to perform quick code prototyping without needing to set up a complex environment. For example, using `numpy` and OpenCV to load and display on the user's X11 through the container, a picture can be found in the directory mounted as `/dmc`.
>
> DMC has made the `Dockerfile` and supporting files, including usage and build instructions, publicly available on its GitHub at https://github.com/datamachines/cuda_tensorflow_opencv.
>
> Building this container image is a long process; it was originally intended to be auto-built using Docker Hub from the repository provided on GitHub, but the original try took over 4h on Docker Hub and was automatically canceled by the build system. On a 2.8GHz quad core 7th gen i7, using a SSD, and running 8 concurrent `make`, it still takes 1h hour (per `tag`) to build. As such, we have made available on our Docker Hub the final builds for different tags, which can directly be used as `FROM` for your Docker containers at https://hub.docker.com/r/datamachines/cuda_tensorflow_opencv.

## GitHub repository [datamachines](https://github.com/datamachines) / [cuda_tensorflow_opencv](https://github.com/datamachines/cuda_tensorflow_opencv)

* [cuda_tensorflow_opencv](https://github.com/datamachines/cuda_tensorflow_opencv)/[Dockerfile](https://github.com/datamachines/cuda_tensorflow_opencv/blob/master/Dockerfile)
  * This Dockerfile installs CUDA, TensorFlow, OpenCV and that's it.
  * I wasn't able to use it for video. I felt like it's incomplete to do what I need.

