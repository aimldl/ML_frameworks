* Draft: 2021-04-26 (Mon)

# Setting up the Computing Environment



## Prepare a machine (Amazon EC2)

The official PyTorch image will not used because it lacks some essential commands such as `nvidia-smi`, `wget` and so on.

Create an Amazon EC2 instance with appropriate number of GPUs.

For details of the instance types, refer to [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/?nc1=h_ls) > [Accelerated Computing](https://aws.amazon.com/ec2/instance-types/?nc1=h_ls#Accelerated_Computing) for GPU-enabled instances.

- P4, P3, P2, Inf1, G4dn, G4ad, G3, F1

Some more details of P4 and P3 are below.

P4

|   Instance   | GPUs | vCPUs | Mem(GiB) |  Network Bandwidth   | GPUDirect RDMA | GPU Peer to Peer |      Storage      | EBS Bandwidth |
| :----------: | :--: | :---: | :------: | :------------------: | :------------: | :--------------: | :---------------: | :-----------: |
| p4d.24xlarge |  8   |  96   |   1152   | 400 Gbps ENA and EFA |      Yes       | 600GB/s NVSwitch | 8 x 1 TB NVMe SSD |    19 Gbps    |

P3

| **Instance**  | **GPUs** | **vCPU** | **Mem (GiB)** | **GPU Mem (GiB)** | **GPU P2P** | **Storage (GB)** | **Dedicated EBS Bandwidth** | **Networking Performance** |
| ------------- | -------- | -------- | ------------- | ----------------- | ----------- | ---------------- | --------------------------- | -------------------------- |
| p3.2xlarge    | 1        | 8        | 61            | 16                | -           | EBS-Only         | 1.5 Gbps                    | Up to 10 Gigabit           |
| p3.8xlarge    | 4        | 32       | 244           | 64                | NVLink      | EBS-Only         | 7 Gbps                      | 10 Gigabit                 |
| p3.16xlarge   | 8        | 64       | 488           | 128               | NVLink      | EBS-Only         | 14 Gbps                     | 25 Gigabit                 |
| p3dn.24xlarge | 8        | 96       | 768           | 256               | NVLink      | 2 x 900 NVMe SSD | 19 Gbps                     | 100 Gigabit                |

## Go to the machine

ssh to the created instance.

```bash
(local) $ ./ssh-deep_learning_ami_ver42_1-0-p3_8xlarge-ec2_seoul
  ...
Last login: Thu Apr 22 02:20:28 2021 from 234.567.890.12
ubuntu@node0:~$
```

For simplicity, `ubuntu@node0:~` will be omitted below. So 

```bash
ubuntu@node0:~$
# is equivalent to
$
```

The deep learning AMI ver 42.1 provides

* Ubuntu 18.04.5 LTS
* and the choice of deep learning framework.

## Prepare the PyTorch environment

To select PyTorch 1.4 with Python3 (CUDA 10.1 and Intel MKL), activate the virtual environment.

```bash
$ source activate pytorch_p36
(pytorch_p36) $
```

Notice the prompt has the leading `(pytorch_p36)` which indicates you are in the PyTorch 1.4. virtual environment.

```bash
(pytorch_p36) ubuntu@node0:~$
(pytorch_p36) $
```

## Verify the PyTorch environment

### Prepare the project directory

[py_files/intro2pytorch-quickstart-1.py](py_files/intro2pytorch-quickstart-1.py)Let's create the project directory `distributed_training`.

```bash
$ mkdir test-distributed_training
$ cd test-distributed_training/
```

### Prepare simple PyTorch source codes

Create the test code from [PyTorch > QUICKSTART](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html).

There are different ways to do it. I've copied and pasted the following files directly into the project directory.

```bash
$ ls
intro2pytorch-quickstart-1.py  intro2pytorch-quickstart-2.py
$
```

intro2pytorch-quickstart-1.py, https://github.com/aimldl/pytorch/blob/main/en/hands-on/py_files/intro2pytorch-quickstart-1.py

intro2pytorch-quickstart-2.py, https://github.com/aimldl/pytorch/blob/main/en/hands-on/py_files/intro2pytorch-quickstart-2.py

### Run the source codes to check if PyTorch runs successfully

Go to [PyTorch > QUICKSTART](01-intro2pytorch-quickstart.md) and run the PyTorch codes to verify the installation.