* Draft: 2020-05-28 (Thu)

# Use H2O.ai on Kubeflow

[Create a Docker Image for auto-sklearn](python3/packages/auto-sklearn/how-to/create_a_docker_image_for_auto-sklearn.md)



## Step 1. Create a Docker image for Kubeflow

The Docker file used to create a Docker image is [../dockerfiles/Dockerfile-baseimage_kubeflow_h2o_ai_openml](../dockerfiles/Dockerfile-baseimage_kubeflow_h2o_ai_openml). This Dockerfile installs

* Python3 base image (with Ubuntu 18.04) 
* extended Linux commands such as zip, unzip, and so on.
* extended Python packages such as numpy, pandas, and so on.
* Jupyter and Jupyter Lab.
* Kubectl

and configures the set-up for `Kubeflow`. Refer to  [커스텀 도커 이미지 만들기](create_and_use_a_custom_image.md) [TODO: link the English version] for the details about making a custom Docker image for Kubeflow.

It also installs:

* OpenML and
* H2O.

While `OpenML` provides the benchmark datasets, H2O installation is a multi-step process which installs:

* H2O.ai server
* Java (Oracle JDK) for H2O 
* relevant Python dependencies for H2O.ai
* H2O Python package

H2O.ai server is a Java application started by a command `java -jar h2o.jar`; so Java must be installed. The H2O Python package is a client that requires several Python dependencies (requests, tabulate, colorama, future).

For details, refer to:

* [Install Java on Ubuntu via Oracle JDK](https://www.hostinger.com/tutorials/install-java-ubuntu)
* [Downloading & Installing H2O](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/downloading.html)

Without Java



RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:linuxuprising/java
RUN apt-get update -y
RUN apt-get install oracle-java14-installer

The essence to make a Docker image for Kubeflow is to add the following lines in a Dockerfile.

```dockerfile
# Kubeflow requirements for custom images
USER root
ENV NB_PREFIX /
CMD ["sh","-c", "jupyter notebook --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser --allow-root --port=8888 --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*' --NotebookApp.base_url=${NB_PREFIX}"]
```

The final Dockerfile includes the above lines as well as some tweaks. 



```
$ docker build -t aimldl/baseimage-kubeflow-autosklearn0.7.0_openml0.10.2_python3_ubuntu18.04 - < Dockerfile

```

```bash
$ docker images
REPOSITORY                                                                   TAG     ... 
aimldl/baseimage-kubeflow-autosklearn0.7.0_openml0.10.2_python3_ubuntu18.04  latest  ...          
... IMAGE ID            CREATED             SIZE
... 3224bf455e5d        5 minutes ago       2.25GB
$ docker login
$ docker push aimldl/baseimage-kubeflow-autosklearn0.7.0_openml0.10.2_python3_ubuntu18.04
$
```

<img src="/home/aimldl/github/computing_environments/kubeflow/how_to/images/dockerhub-aimldl_baseimage-kubeflow-autosklearn0.7.0_openml0.10.2_python3_ubuntu18.04.png">



Make sure this image works properly.

```bash
$ docker run -it aimldl/baseimage-kubeflow-autosklearn0.7.0_openml0.10.2_python3_ubuntu18.04 bash
root@f60de631c947:~# python -c "import autosklearn; print(autosklearn.__version__)"
0.7.0
root@f60de631c947:~# python -c "import openml; print(openml.__version__)"
0.10.2
root@f60de631c947:~# exit
exit
$
```



Go to Notebook Servers. Select `anonymous` for `Select Namespace`. 

Click `NEW SERVER`.

<img src="/home/aimldl/github/computing_environments/kubeflow/how_to/images/kubeflow-dashboard-notebook_servers-anonymous-2020-05-23.png">

Enter `auto-sklearn` under `Name`. Check `Custom Image`.

<img src="/home/aimldl/github/computing_environments/kubeflow/how_to/images/kubeflow-dashboard-notebook_servers-anonymous-new_server-name.png">

<img src="/home/aimldl/github/computing_environments/kubeflow/how_to/images/kubeflow-dashboard-notebook_servers-anonymous-new_server-custom_image.png">

Click `Launch`.

Under `StatusName`, there is an animated circle. When initializing Pod and other stuff are done, it will look like below. 

<img src="/home/aimldl/github/computing_environments/kubeflow/how_to/images/kubeflow-dashboard-notebook_servers-anonymous-auto-sklearn.png">

Click `CONNECT` to open a new notebook server.



Go to `Launcher` and click `Terminal`.

------

다음: [Use H2O.ai on Kubeflow](use_h2o_ai_on_kubeflow.md)
