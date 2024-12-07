* Draft: 2020-05-22 (Fri)

# Use Auto-Sklearn on Kubeflow

[Create a Docker Image for auto-sklearn](python3/packages/auto-sklearn/how-to/create_a_docker_image_for_auto-sklearn.md)

[error: unable to listen on any of the requested ports: [{8080 80}]](../troubleshoot/error-unable_to_listen_on_any_of_the_requested_ports.md)

[커스텀 도커 이미지 만들기](create_and_use_a_custom_image.md)

To create a Docker image for Kubeflow, add these lines in a Dockerfile.

```dockerfile
# Kubeflow requirements for custom images
USER root
ENV NB_PREFIX /
CMD ["sh","-c", "jupyter notebook --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser --allow-root --port=8888 --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*' --NotebookApp.base_url=${NB_PREFIX}"]
```



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

<img src="images/dockerhub-aimldl_baseimage-kubeflow-autosklearn0.7.0_openml0.10.2_python3_ubuntu18.04.png">



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

<img src="images/kubeflow-dashboard-notebook_servers-anonymous-2020-05-23.png">

Enter `auto-sklearn` under `Name`. Check `Custom Image`.

<img src="images/kubeflow-dashboard-notebook_servers-anonymous-new_server-name.png">

<img src="images/kubeflow-dashboard-notebook_servers-anonymous-new_server-custom_image.png">

Click `Launch`.

Under `StatusName`, there is an animated circle. When initializing Pod and other stuff are done, it will look like below. 

<img src="images/kubeflow-dashboard-notebook_servers-anonymous-auto-sklearn.png">

Click `CONNECT` to open a new notebook server.



Go to `Launcher` and click `Terminal`.

------

다음: [Use H2O.ai on Kubeflow](use_h2o_ai_on_kubeflow.md)
