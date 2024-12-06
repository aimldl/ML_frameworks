* Draft: 2020-10-16 (Fri)

# Install PyTorch

## Standard installation

[GET STARTED](https://pytorch.org/get-started/locally/) > [START LOCALLY](https://pytorch.org/get-started/locally/#start-locally)

```bash
$ sudo apt install python
```

## Docker installation

The official pytorch image released by pytorch is available at [pytorch/pytorch](https://hub.docker.com/r/pytorch/pytorch)

Assuming docker has been installed already,


```bash
$ docker pull pytorch/pytorch
```

The full message looks like:

```bash
$ docker pull pytorch/pytorch
Using default tag: latest
latest: Pulling from pytorch/pytorch
23884877105a: Pull complete 
bc38caa0f5b9: Pull complete 
2910811b6c42: Pull complete 
36505266dcc6: Pull complete 
3472d01858ba: Pull complete 
4a98b57681ff: Pull complete 
f3b419d1e6d5: Pull complete 
Digest: sha256:9c3aa4653f6fb6590acf7f49115735be3c3272f4fa79e5da7c96a2c901631352
Status: Downloaded newer image for pytorch/pytorch:latest
docker.io/pytorch/pytorch:latest
$
```

To verify if the `pytorch/pytorch` exists in the local machine, run:

```bash
$ docker images
REPOSITORY                            TAG                        IMAGE ID            CREATED             SIZE
  ...
pytorch/pytorch                       latest                     6a2d656bcf94        2 months ago        3.47GB
  ...
$
```

To run the image, use the `docker run` command.

```bash
$ docker run -it pytorch/pytorch bash
root@8b185ecaa66e:/workspace# 
```

Check to see if the PyTorch package exists in the container.

```bash
root@8b185ecaa66e:/workspace# python
Python 3.8.8 (default, Feb 24 2021, 21:46:12) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> 
```

Of course, `import torch` does not spit any error.

However `nvidia-smi` is not available.

```bash
root@8b185ecaa66e:/workspace# nvidia-smi
bash: nvidia-smi: command not found
root@8b185ecaa66e:/workspace# 
>>>
```

`wget` does not exist, too.

```bash
root@8b185ecaa66e:/workspace# wget https://github.com/aimldl/pytorch/blob/main/en/hands-on/py_files/intro2pytorch-quickstart-1.py
bash: wget: command not found
root@8b185ecaa66e:/workspace#
```

Exiting the `pytorch/pytorch` container...

```bash
root@8b185ecaa66e:/workspace# exit
exit
$
```

Let's delete the official image.

The `docker rmi` command may not work with the following error.

```bash
$ docker rmi pytorch/pytorch
Error response from daemon: conflict: unable to remove repository reference "pytorch/pytorch" (must force) - container 61784122a0bb is using its referenced image 5ffed6c83695
$
```

Stop and remove the container first before removing the image.

```bash
$ docker ps -a | grep pytorch
61784122a0bb   pytorch/pytorch                      "/bin/bash"              23 minutes ago      Exited (127) About a minute ago                        recursing_wilbur
$ docker rm recursing_wilbur
recursing_wilbur
$
```

Note the container has already been stopped at the time of exiting the container.

Now remove the image with the same command which failed previously.

```bash
$ docker rmi pytorch/pytorch
Untagged: pytorch/pytorch:latest
Untagged: pytorch/pytorch@sha256:9ebb176339b25a2d155e6f127c5948968b3f61e5f720c4598ef79cf450db8bfe
Deleted: sha256:5ffed6c836956ef474d369d9dfe7b3d52263e93b51c7a864b068f98e02ea8c51
  ...
Deleted: sha256:837d6facb613e572926fbfe8cd7171ddf5919c1454cf4d5b4e78f3d2a7729000
$
```



