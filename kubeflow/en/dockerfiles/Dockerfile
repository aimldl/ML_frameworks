# Dockerfile-baseimage_kubeflow_simple_jupyter_notebook_python_3     Dockerfile for Kubeflow Jupyter Notebook Base Image
#   * Rev.2: 2020-04-29 (Wed)
#   * Rev.1: 2020-04-28 (Tue)
#   * Draft: 2020-04-27 (Mon)
#
# Commands
#   For details, refer to "docker build" at https://docs.docker.com/engine/reference/commandline/build/
#
# Step 1. Change the file name to Dockerfile
#     $ cp Dockerfile-baseimage_kubeflow_simple_jupyter_notebook_python_3 Dockerfile
#
# Step 2. Build a Docker image from Dockerfile.
#     $ docker build -t aimldl/baseimage_kubeflow_simple_jupyter_notebook_python_3 - < Dockerfile
#
#     Options
#       --tag, -t  Name and optionally a tag in the ‘name:tag’ format
#
#   Note: If you want to skip step 1 and don't want to change the file name, run:
#     $ docker build -t aimldl/baseimage_kubeflow_jupyter_notebook -f Dockerfile-baseimage_kubeflow_simple_jupyter_notebook_python_3
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
#     $ docker tag 24aa5a9ca7e3 aimldl/baseimage_kubeflow_jupyter_notebook:latest
#     $ docker images
#     REPOSITORY                             TAG     IMAGE ID      CREATED         SIZE
#     aimldl/baseimage_kubeflow_jupyter_notebook  latest  24aa5a9ca7e3  33 minutes ago  1.51GB
#     $
#   But I'd rather add the tag when tGoogle search: kubeflow create a custom image and notebook servershe image is built. So use the -t option.

# Dockerfile

# Base Container
FROM python:3
LABEL version="0.1"

# Kubeflow requirements for custom images
#USER root
ENV NB_PREFIX /
CMD ["sh","-c", "jupyter notebook --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser --allow-root --port=8888 --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*' --NotebookApp.base_url=${NB_PREFIX}"]
