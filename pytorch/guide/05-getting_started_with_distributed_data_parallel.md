* Draft: 2021-04-26 (Mon)

# PyTorch Tutorials > 

# Getting Started with Distributed Data Parallel (DDP)

## Overview

* DDP is multi-process and works for both single- and multi- machine training.
* This tutorial requires 8 GPUs. Otherwise you'll encounter the following error.

```bash
$ python pytorch_tutorials-distributed_data_parallelism.py
Requires at least 8 GPUs to run, but got 4.
$
```

* [GETTING STARTED WITH DISTRIBUTED DATA PARALLEL](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html), Shen Li (Joe Zhu)

  > * Prerequisites:
  >
  >   - [PyTorch Distributed Overview](https://pytorch.org/tutorials/beginner/dist_overview.html)
  >   - [DistributedDataParallel API documents](https://pytorch.org/docs/master/generated/torch.nn.parallel.DistributedDataParallel.html)
  >   - [DistributedDataParallel notes](https://pytorch.org/docs/master/notes/ddp.html)
  > * This tutorial
  >   * starts from a basic DDP use case
  >   * demonstrates more advanced use cases including:
  >     * checkpointing models 
  >     * and combining DDP with model parallel.
  > * In DDP, the constructor, the forward pass, and the backward pass are distributed synchronization points. 

## Summary of the tutorial

> * [DistributedDataParallel](https://pytorch.org/docs/stable/nn.html#torch.nn.parallel.DistributedDataParallel) (DDP) implements data parallelism at the module level which can run across multiple machines. 
> * Applications using DDP should spawn multiple processes and create a single DDP instance per process.
> * DDP uses collective communications in the [torch.distributed](https://pytorch.org/tutorials/intermediate/dist_tuto.html) package to synchronize gradients and buffers.
>   * DDP registers an autograd hook for each parameter given by `model.parameters()`.
>   * The hook will fire when the corresponding gradient is computed in the backward pass.
>   * DDP uses that signal to trigger gradient synchronization across processes.
>
> * The recommended way to use DDP
>   * is to spawn one process for each model replica
>     * where a model replica can span multiple devices
> * DDP processes can be placed on the same machine or across machines.
> * GPU devices cannot be shared across processes.

## Some important details about DDP

Skewed Processing Speeds

> * In DDP, distributed synchronization points are
>   * the constructor,
>   * the forward pass, and
>   * the backward pass. 
> * Different processes are expected to 
>   * launch the same number of synchronizations and 
>   * reach these synchronization points in the same order and 
>   * enter each synchronization point at roughly the same time. 
> * Otherwise, fast processes might arrive early and timeout on waiting for stragglers. 
>   * Hence, users are responsible for balancing workloads distributions across processes.
>
> * Sometimes, skewed processing speeds are inevitable due to, e.g., 
>   * network delays,
>   * resource contentions,
>   * unpredictable workload spikes.
> * To avoid timeouts in these situations, make sure that you pass a sufficiently large `timeout` value when calling [init_process_group](https://pytorch.org/docs/stable/distributed.html#torch.distributed.init_process_group).

Save and Load Checkpoints

> * It’s common to use `torch.save` and `torch.load` to checkpoint modules during training and recover from checkpoints. 
> * When using DDP, one optimization is 
>   * to save the model in only one process and then load it to all processes, 
>     * reducing write overhead.
>   * This is correct because all processes start from the same parameters and gradients are synchronized in backward passes, and hence optimizers should keep setting parameters to the same values. 
> * If you use this optimization, make sure all processes do not start loading before the saving is finished. 
>   * Besides, when loading the module, you need to provide an appropriate `map_location` argument to prevent a process to step into others’ devices. 
>     * If `map_location` is missing, `torch.load` will first load the module to CPU and then copy each parameter to where it was saved, 
>       * which would result in all processes on the same machine using the same set of devices.
> * For more advanced failure recovery and elasticity support, please refer to [TorchElastic](https://pytorch.org/elastic).

## Run the code on Amazon EC2

```bash
$ mkdir 04-distributed_data_parallelism
$ cd 04-distributed_data_parallelism
```

### Basic Use Case

> DDP wraps lower-level distributed communication details and provides a clean API as if it is a local model. Gradient synchronization communications take place during the backward pass and overlap with the backward computation. When the `backward()` returns, `param.grad` already contains the synchronized gradient tensor. For basic use cases, DDP only requires a few moSave and Load Checkpointsre LoCs to set up the process group. When applying DDP to more advanced use cases, some caveaCombine DDP with Model Parallelismts require caution.

Copy and paste the source code

```bash
$ nano pytorch_tutorials-distributed_data_parallelism.py
```

Run it on a machine or machines with 8 GPUs.

```bash
$ python pytorch_tutorials-distributed_data_parallelism.py
Running basic DDP example on rank 0.
Running basic DDP example on rank 4.
Running basic DDP example on rank 3.
Running basic DDP example on rank 5.
Running basic DDP example on rank 2.
Running basic DDP example on rank 1.
Running basic DDP example on rank 6.
Running basic DDP example on rank 7.
Running DDP checkpoint example on rank 1.
Running DDP checkpoint example on rank 3.
Running DDP checkpoint example on rank 5.
Running DDP checkpoint example on rank 2.
Running DDP checkpoint example on rank 7.
Running DDP checkpoint example on rank 4.
Running DDP checkpoint example on rank 0.
Running DDP checkpoint example on rank 6.
Running DDP with model parallel example on rank 2.
Running DDP with model parallel example on rank 0.
Running DDP with model parallel example on rank 1.
$
```

Otherwise, the following error occurs.

```bash
$ python pytorch_tutorials-distributed_data_parallelism.py 
Requires at least 8 GPUs to run, but got 4.
$
```

## Appendix. Source code

This source code is available at [py_files/pytorch_tutorials-distributed_data_parallelism.py](py_files/pytorch_tutorials-distributed_data_parallelism.py). 

```python
# pytorch_tutorials-distributed_data_parallelism.py

# PyTorch Tutorials > GETTING STARTED WITH DISTRIBUTED DATA PARALLEL
# https://pytorch.org/tutorials/intermediate/ddp_tutorial.html#comparison-between-dataparallel-and-distributeddataparallel

# To create DDP modules, first set up process groups properly. More details can be found in Writing Distributed Applications with PyTorch.
# https://pytorch.org/tutorials/intermediate/dist_tuto.html

import os
import sys
import tempfile
import torch
import torch.distributed as dist
import torch.nn as nn
import torch.optim as optim
import torch.multiprocessing as mp

from torch.nn.parallel import DistributedDataParallel as DDP

# On Windows platform, the torch.diCombine DDP with Model Parallelismstributed package only
# supports Gloo backend, FileStore and TcpStore.
# For FileStore, set init_method parameter in init_process_group
# to a local file. Example as follow:
# init_method="file:///f:/libtmp/some_file"
# dist.init_process_group(
#    "gloo",
#    rank=rank,
#    init_method=init_method,
#    world_size=world_size)
# For TcpStore, same way as on Linux.

def setup(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'-
    os.environ['MASTER_PORT'] = '12355'

    # initialize the process group
    dist.init_process_group("gloo", rank=rank, world_size=world_size)

def cleanup():
    dist.destroy_process_group()
    
# Create a toy module, wrap it with DDP, and feed it with some dummy input data.

class ToyModel(nn.Module):
    def __init__(self):
        super(ToyModel, self).__init__()
        self.net1 = nn.Linear(10, 10)- Basic Use Case
        self.relu = nn.ReLU()
        self.net2 = nn.Linear(10, 5)

    def forward(self, x):
        return self.net2(self.relu(self.net1(x)))

def demo_basic(rank, world_size):
    print(f"Running basic DDP example on rank {rank}.")
    setup(rank, world_size)

    # create model and move it to GPU with id rank
    model     = ToyModel().to(rank)
    ddp_model = DDP(model, device_ids=[rank])

    loss_fn   = nn.MSELoss()
    optimizer = optim.SGD(ddp_model.parameters(), lr=0.001)

    optimizer.zero_grad()
    outputs = ddp_model(torch.randn(20, 10))
    labels  = torch.randn(20, 5).to(rank)
    loss_fn(outputs, labels).backward()
    optimizer.step()

    cleanup()

def run_demo(demo_fn, world_size):
    mp.spawn(demo_fn,
             args=(world_size,), - Basic Use Case
             nprocs=world_size,
             join=True)

# Save and Load Checkpoints

def demo_checkpoint(rank, world_size):
    print(f"Running DDP checkpoint example on rank {rank}.")
    setup(rank, world_size)

    model     = ToyModel().to(rank)
    ddp_model = DDP(model, device_ids=[rank])

    loss_fn   = nn.MSELoss()
    optimizer = optim.SGD(ddp_model.parameters(), lr=0.001)

    CHECKPOINT_PATH = tempfile.gettempdir() + "/model.checkpoint"
    if rank == 0:
        # All processes should see same parameters as they all start from same
        # random parameters and gradients are synchronized in backward passes.
        # Therefore, saving it in one process is sufficient.
        torch.save(ddp_model.state_dict(), CHECKPOINT_PATH)

    # Use a barrier() to make sure that process 1 loads the model after process
    # 0 saves it.
    dist.barrier()
    # configure map_location properly
    map_location = {'cuda:%d' % 0: 'cuda:%d' % rank}
    ddp_model.load_state_dict(
        torch.load(CHECKPOINT_PATH, map_location=map_location))- Basic Use Case

    optimizer.zero_grad()
    outputs = ddp_model(torch.randn(20, 10))
    labels  = torch.randn(20, 5).to(rank)
    loss_fn = nn.MSELoss()
    loss_fn(outputs, labels).backward()
    optimizer.step()

    # Not necessary to use a dist.barrier() to guard the file deletion below
    # as the AllReduce ops in the backward pass of DDP already served as
    # a synchronization.

    if rank == 0:
        os.remove(CHECKPOINT_PATH)

    cleanup()
    
# Combine DDP with Model Parallelism - Basic Use Case
class ToyMpModel(nn.Module):
    def __init__(self, dev0, dev1):
        super(ToyMpModel, self).__init__()
        self.dev0 = dev0
        self.dev1 = dev1
        self.net1 = torch.nn.Linear(10, 10).to(dev0)
        self.relu = torch.nn.ReLU()
        self.net2 = torch.nn.Linear(10, 5).to(dev1)

    def forward(self, x):
        x = x.to(self.dev0)
        x = self.relu(self.net1(x))
        x = x.to(self.dev1)
        return self.net2(x)

def demo_model_parallel(rank, world_size):
    print(f"Running DDP with model parallel example on rank {rank}.")
    setup(rank, world_size)

    # setup mp_model and devices for this process
    dev0 = rank * 2
    dev1 = rank * 2 + 1
    mp_model = ToyMpModel(dev0, dev1)
    ddp_mp_model = DDP(mp_model)

    loss_fn = nn.MSELoss()
    optimizer = optim.SGD(ddp_mp_model.parameters(), lr=0.001)

    optimizer.zero_grad()
    # outputs will be on dev1
    outputs = ddp_mp_model(torch.randn(20, 10))
    labels = torch.randn(20, 5).to(dev1)
    loss_fn(outputs, labels).backward()
    optimizer.step()

    cleanup()

if __name__ == "__main__":
    n_gpus = torch.cuda.device_count()
    if n_gpus < 8:
      print(f"Requires at least 8 GPUs to run, but got {n_gpus}.")
    else:
      run_demo(demo_basic, 8)
      run_demo(demo_checkpoint, 8)
      run_demo(demo_model_parallel, 4)
```



