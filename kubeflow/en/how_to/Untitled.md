

* Draft: 2020-04-27 (Mon)



```bash
# Dockerfile-baseimage_kubeflow_jupyter_lab_python_3     Dockerfile for Kubeflow Jupyter Lab Base Image
#   * Draft: 2020-04-27 (Mon)
#
# Commands
#   For details, refer to "docker build" at https://docs.docker.com/engine/reference/commandline/build/
#
# Step 1. Change the file name to Dockerfile
#     $ mv Dockerfile-baseimage_kubeflow_jupyter_lab_python_3 Dockerfile
#
# Step 2. Build a Docker image from Dockerfile.
#     $ docker build -t aimldl/baseimage_kubeflow_jupyter_lab_python_3 - < Dockerfile
#
#     Options
#       --tag, -t  Name and optionally a tag in the ‘name:tag’ format
#
#   Note: If you want to skip step 1 and don't want to change the file name, run:
#     $ docker build -t aimldl/baseimage_kubeflow_jupyter_lab -f Dockerfile-baseimage_kubeflow_jupyter_lab_python_3
#
#     Options
#       --file, -f Name of the Dockerfile (Default is ‘PATH/Dockerfile’)
#
#   Note: without the tag, REPOSITORY and TAG will be <none>.
#     $ docker images
#     REPOSITORY  TAG     IMAGE ID      CREATED         SIZE
#     <none>      <none>  24aa5a9ca7e3  10 minutes ago  1.51GB
#     $
#   You can rename the built image later.
#     $ docker tag 24aa5a9ca7e3 aimldl/baseimage_kubeflow_jupyter_lab:latest
#     $ docker images
#     REPOSITORY                             TAG     IMAGE ID      CREATED         SIZE
#     aimldl/baseimage_kubeflow_jupyter_lab  latest  24aa5a9ca7e3  33 minutes ago  1.51GB
#     $
#   But I'd rather add the tag when the image is built. So use the -t option.

#####################
#   Base Container  #
#####################
# Refer to https://hub.docker.com/_/python
#   How to use this image > Create a Dockerfile in your Python app project

ARG BASE_CONTAINER="python:3"
FROM $BASE_CONTAINER
MAINTAINER "Tae-Hyung T Kim, Ph.D."

#####################################
#   Dockerfile-ubuntu_base_image    #
#####################################
# Use two ampersands to merge two commands, e.g. "command 1 && command 2" 
# Install basic packages for Linux

# -q, --quiet
# Quiet. Produces output suitable for logging, omitting progress indicators. More q's will produce more quiet up to a maximum of two. 
# You can also use -q=# to set the quiet level, overriding the # configuration file. Note that quiet level 2 implies -y, 
# you should never use -qq without a no-action modifier such as -d, --print-uris or -s as APT may decided to do something you did not expect.

# It's fine to put all of them together.
# But I prefer to grouping related commands.
# It's a matter of style.

RUN apt-get update -y
RUN apt-get install -yq --no-install-recommends \
  lsb-release \
  locales \
  build-essential \
  cmake \
  g++ \
  sudo
RUN apt-get install -yq --no-install-recommends \
  curl \
  wget \
  openssh-client \
  ca-certificates \
  net-tools \
  iproute2 \
  strace\
  diffstat\
  pkg-config \
  tcpdump
RUN apt-get install -yq --no-install-recommends \
  zip \
  bzip2 \
  unzip
RUN apt-get install -yq --no-install-recommends \
  vim \
  nano \
  emacs
RUN apt-get install -yq --no-install-recommends \
  tree \
  screen

# Install extended packages for Linux
RUN apt-get install -yq --no-install-recommends \
  git \
  graphviz

# Clean up
RUN apt-get clean && \
  rm -rf /var/lib/apt/lists/*

#####################################
#   Dockerfile-python3_base_image   #
#####################################
# Install packages for Python3
RUN apt-get update -y && apt-get install -y \
  python3 \
  python3-pip \
  python3-dev \
  python3-setuptools

RUN pip3 install --upgrade pip
RUN pip3 install ipython
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install matplotlib
RUN pip3 install scipy
RUN pip3 install sympy
RUN pip3 install scikit-learn
RUN pip3 install h5py
RUN pip3 install pillow
RUN pip3 install pydotplus
RUN pip3 install seaborn
RUN pip3 install pyyaml

############### Dockerfile-baseimage_kubeflow_jupyter_lab_python_3     Dockerfile for Kubeflow Jupyter Lab Base Image
#   * Draft: 2020-04-27 (Mon)
#
# Commands
#   For details, refer to "docker build" at https://docs.docker.com/engine/reference/commandline/build/
#
# Step 1. Change the file name to Dockerfile
#     $ mv Dockerfile-baseimage_kubeflow_jupyter_lab_python_3 Dockerfile
#
# Step 2. Build a Docker image from Dockerfile.
#     $ docker build -t aimldl/baseimage_kubeflow_jupyter_lab_python_3 - < Dockerfile
#
#     Options
#       --tag, -t  Name and optionally a tag in the ‘name:tag’ format
#
#   Note: If you want to skip step 1 and don't want to change the file name, run:
#     $ docker build -t aimldl/baseimage_kubeflow_jupyter_lab -f Dockerfile-baseimage_kubeflow_jupyter_lab_python_3
#
#     Options
#       --file, -f Name of the Dockerfile (Default is ‘PATH/Dockerfile’)
#
#   Note: without the tag, REPOSITORY and TAG will be <none>.
#     $ docker images
#     REPOSITORY  TAG     IMAGE ID      CREATED         SIZE
#     <none>      <none>  24aa5a9ca7e3  10 minutes ago  1.51GB
#     $
#   You can rename the built image later.
#     $ docker tag 24aa5a9ca7e3 aimldl/baseimage_kubeflow_jupyter_lab:latest
#     $ docker images
#     REPOSITORY                             TAG     IMAGE ID      CREATED         SIZE
#     aimldl/baseimage_kubeflow_jupyter_lab  latest  24aa5a9ca7e3  33 minutes ago  1.51GB
#     $
#   But I'd rather add the tag when the image is built. So use the -t option.

#####################
#   Base Container  #
#####################
# Refer to https://hub.docker.com/_/python
#   How to use this image > Create a Dockerfile in your Python app project

ARG BASE_CONTAINER="python:3"
FROM $BASE_CONTAINER
MAINTAINER "Tae-Hyung T Kim, Ph.D."

#####################################
#   Dockerfile-ubuntu_base_image    #
#####################################
# Use two ampersands to merge two commands, e.g. "command 1 && command 2" 
# Install basic packages for Linux

# -q, --quiet
# Quiet. Produces output suitable for logging, omitting progress indicators. More q's will produce more quiet up to a maximum of two. 
# You can also use -q=# to set the quiet level, overriding the # configuration file. Note that quiet level 2 implies -y, 
# you should never use -qq without a no-action modifier such as -d, --print-uris or -s as APT may decided to do something you did not expect.

# It's fine to put all of them together.
# But I prefer to grouping related commands.
# It's a matter of style.

RUN apt-get update -y
RUN apt-get install -yq --no-install-recommends \
  lsb-release \
  locales \
  build-essential \
  cmake \
  g++ \
  sudo
RUN apt-get install -yq --no-install-recommends \
  curl \
  wget \
  openssh-client \
  ca-certificates \
  net-tools \
  iproute2 \
  strace\
  diffstat\
  pkg-config \
  tcpdump
RUN apt-get install -yq --no-install-recommends \
  zip \
  bzip2 \
  unzip
RUN apt-get install -yq --no-install-recommends \
  vim \
  nano \
  emacs
RUN apt-get install -yq --no-install-recommends \
  tree \
  screen

# Install extended packages for Linux
RUN apt-get install -yq --no-install-recommends \
  git \
  graphviz

# Clean up
RUN apt-get clean && \
  rm -rf /var/lib/apt/lists/*

#####################################
#   Dockerfile-python3_base_image   #
#####################################
# Install packages for Python3
RUN apt-get update -y && apt-get install -y \
  python3 \
  python3-pip \
  python3-dev \
  python3-setuptools

RUN pip3 install --upgrade pip
RUN pip3 install ipython
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install matplotlib
RUN pip3 install scipy
RUN pip3 install sympy
RUN pip3 install scikit-learn
RUN pip3 install h5py
RUN pip3 install pillow
RUN pip3 install pydotplus
RUN pip3 install seaborn
RUN pip3 install pyyaml

##############
#   jupyter  #
##############
#RUN pip install jupyter -U && pip install jupyterlab
RUN pip3 install jupyter -U && pip install jupyterlab

# Why install jupyter lab twice?
#RUN pip install jupyterlab && \
RUN pip3 install jupyterlab && \
  jupyter serverextension enable --py jupyterlab --sys-prefix

# Port for Jupyter
#   UDP port 8888 uses the Datagram Protocol
#   For details, refer to https://www.auditmypc.com/udp-port-8888.asp
EXPOSE 8888

##############
#   kubectl  #
##############
# Install and Set Up kubectl
#   Source: https://kubernetes.io/docs/tasks/tools/install-kubectl/
#   sudo is removed from the commands in the above document.
RUN apt-get update && sudo apt-get install -y apt-transport-https gnupg2
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
RUN echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update
RUN apt-get install -y kubectl

# Change WORKDIR so the directory starts from WORKDIR, not from /
ARG NB_USER=jovyan
WORKDIR /home/jovyan
ENV HOME /home/$NB_USER

# TODO: I'm not sure if these are necessary.
ENV NB_USER $NB_USER
ENV NB_UID=1000

USER root
# Note USER is root, not user as follows.
# Q: Is this Kubeflow requirement?
#RUN chown -R user: /home/user
#USER user

# Requirements for custom Jupyter Image
#   Documentation / Jupyter Notebooks / Create a Custom Jupyter Image
# Source: https://www.kubeflow.org/docs/notebooks/custom-notebook/
#
# Summary: When this image is launched, the command "jupyter lab ..." is executed.

ENV NB_PREFIX /
CMD ["sh","-c", "jupyter lab --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser --allow-root --port=8888 --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*' --NotebookApp.base_url=${NB_PREFIX}"]
#   jupyter  #
##############
#RUN pip install jupyter -U && pip install jupyterlab
RUN pip3 install jupyter -U && pip install jupyterlab

# Why install jupyter lab twice?
#RUN pip install jupyterlab && \
RUN pip3 install jupyterlab && \
  jupyter serverextension enable --py jupyterlab --sys-prefix

# Port for Jupyter
#   UDP port 8888 uses the Datagram Protocol
#   For details, refer to https://www.auditmypc.com/udp-port-8888.asp
EXPOSE 8888

##############
#   kubectl  #
##############
# Install and Set Up kubectl
#   Source: https://kubernetes.io/docs/tasks/tools/install-kubectl/
#   sudo is removed from the commands in the above document.
RUN apt-get update && sudo apt-get install -y apt-transport-https gnupg2
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
RUN echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update
RUN apt-get install -y kubectl

# Change WORKDIR so the directory starts from WORKDIR, not from /
ARG NB_USER=jovyan
WORKDIR /home/jovyan
ENV HOME /home/$NB_USER

# TODO: I'm not sure if these are necessary.
ENV NB_USER $NB_USER
ENV NB_UID=1000

USER root
# Note USER is root, not user as follows.
# Q: Is this Kubeflow requirement?
#RUN chown -R user: /home/user
#USER user

# Requirements for custom Jupyter Image
#   Documentation / Jupyter Notebooks / Create a Custom Jupyter Image
# Source: https://www.kubeflow.org/docs/notebooks/custom-notebook/
#
# Summary: When this image is launched, the command "jupyter lab ..." is executed.

ENV NB_PREFIX /
CMD ["sh","-c", "jupyter lab --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser --allow-root --port=8888 --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*' --NotebookApp.base_url=${NB_PREFIX}"]
```

