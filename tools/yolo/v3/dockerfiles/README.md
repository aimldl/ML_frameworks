



Google search: nvidia cuda cudnn docker image with develop options

[How to Properly Use the GPU within a Docker Container](https://towardsdatascience.com/how-to-properly-use-the-gpu-within-a-docker-container-4c699c78c6d1)

> **The Downsides of the Brute Force Approach —** First of all, every time you rebuild the docker image you will have to reinstall the image, slowing down development. Second, if you decide to lift the docker image off of the current machine and onto a new one that has a different GPU, operating system, or you would like new drivers — you will have to re-code this step every time for each machine. This kind of defeats the purpose of build a Docker image. Third, you might not remember the commands to install the drivers on your local machine, and there you are back at configuring the GPU again inside of Docker.
>
> **The Best Approach —** The best approach is to use the NVIDIA Container Toolkit. The NVIDIA Container Toolkit is a docker image that provides support to automatically recognize GPU drivers on your base machine and pass those same drivers to your Docker container when it runs. So if you are able to run **nvidia-smi**, on your base machine you will also be able to run it in your Docker container (and all of your programs will be able to reference the GPU). In order to use the NVIDIA Container Toolkit, you simply pull the NVIDIA Container Toolkit image at the top of your Dockerfile like so — **nano Dockerfile**:
>
> Now we run the container from the image by using the command **docker run — gpus all nvidia-test.** Keep in mind, we need the **— gpus all** or else the GPU will not be exposed to the running container.

> ```dockerfile
> FROM nvidia/cuda:10.2-base
> CMD nvidia-smi
> #set up environment
> RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl
> RUN apt-get install unzip
> RUN apt-get -y install python3
> RUN apt-get -y install python3-pip
> COPY app/requirements_verbose.txt /app/requirements_verbose.txt
> RUN pip3 install -r /app/requirements_verbose.txt
> #copies the applicaiton from local path to container path
> COPY app/ /app/
> WORKDIR /app
> ENV NUM_EPOCHS=10
> ENV MODEL_TYPE='EfficientDet'
> ENV DATASET_LINK='HIDDEN'
> ENV TRAIN_TIME_SEC=100
> CMD ["python3", "train_and_eval.py"]
> ```





```bash
# Above is from the base image
# The lines below must be organized.
RUN apt update && apt install --no-install-recommends --no-install-suggests -y curl
RUN apt install -y unzip
RUN apt install -y python3
RUN apt install -y python3-pip

RUN apt install -y nano 

apt install -y wget unzip git tree
apt install -y build-essential cmake pkg-config 
apt -y install libjpeg-dev libpng-dev libtiff-dev

apt -y install libjasper-dev
wget https://github.com/mdadams/jasper/archive/version-2.0.16.tar.gz -O jasper-version-2.0.16.tar.gz
tar xvf cd jasper-version-2.0.16.tar.gz
cd jasper-version-2.0.16/

mkdir build
export SOURCE_DIR=~/jasper-version-2.0.16
export BUILD_DIR=~/jasper-version-2.0.16/build
cd $BUILD_DIR
cmake -G "Unix Makefiles" -H$SOURCE_DIR -B$BUILD_DIR
cd $BUILD_DIR
make clean all
make test

apt install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev v4l-utils libxvidcore-dev libx264-dev

apt install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev 

apt install -y libgtk-3-dev

apt install -y mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev

apt install -y libatlas-base-dev gfortran libeigen3-dev

apt-get install -y python3-dev

```

