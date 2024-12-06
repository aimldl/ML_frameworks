* Draft: 2021-04-26 (Mon)

# PyTorch Tutorials > Data Parallelism

## Overview

* Data parallel is single-process, multi-thread, and only works on a single machine.
* [PyTorch Tutorials](https://pytorch.org/tutorials/) > [OPTIONAL: DATA PARALLELISM](https://pytorch.org/tutorials/beginner/blitz/data_parallel_tutorial.html), Sung Kim and Jenny Kang
  *  how to use multiple GPUs using `DataParallel`

> DataParallel splits your data automatically and sends job orders to multiple models on several GPUs. After each model finishes their job, DataParallel collects and merges the results before returning it to you.

> You can put the model on a GPU:
>
> ```python
> device = torch.device("cuda:0")
> model.to(device)
> ```
>
> Then, you can copy all your tensors to the GPU:
>
> ```python
> mytensor = my_tensor.to(device)
> ```
>
> Pytorch will only use one GPU by default. You can easily run your operations on multiple GPUs by making your model run parallelly using `DataParallel`:
>
> ```python
> model = nn.DataParallel(model)
> ```

## Run the code on Amazon EC2

```bash
$ mkdir 03-data_parallelism
$ cd 03-data_parallelism
```

Copy and paste the source code

```bash
$ nano pytorch_tutorials-data_parallelism.py
```

Run it.

```bash
$ python pytorch_tutorials-data_parallelism.py 
Let's use 4 GPUs!
	In Model: input size torch.Size([8, 5]) output size torch.Size([8, 2])
	In Model: input size torch.Size([8, 5]) output size torch.Size([8, 2])
	In Model: input size torch.Size([8, 5]) output size torch.Size([8, 2])
	In Model: input size torch.Size([6, 5]) output size torch.Size([6, 2])
Outside: input size torch.Size([30, 5]) output_size torch.Size([30, 2])
	In Model: input size torch.Size([8, 5]) output size torch.Size([8, 2])
	In Model: input size torch.Size([8, 5]) output size torch.Size([8, 2])
	In Model: input size torch.Size([8, 5]) output size torch.Size([8, 2])
	In Model: input size torch.Size([6, 5]) output size torch.Size([6, 2])
Outside: input size torch.Size([30, 5]) output_size torch.Size([30, 2])
	In Model: input size torch.Size([8, 5]) output size torch.Size([8, 2])
	In Model: input size torch.Size([8, 5]a.py pytorch_tutorials-data_parallelism.py) output size torch.Size([8, 2])
	In Model: input size torch.Size([8, 5]) output size torch.Size([8, 2])
	In Model: input size torch.Size([6, 5]) output size torch.Size([6, 2])
Outside: input size torch.Size([30, 5]) output_size torch.Size([30, 2])
	In Model: input size torch.Size([3, 5]) output size torch.Size([3, 2])
	In Model: input size torch.Size([3, 5]) output size torch.Size([3, 2])
	In Model: input size torch.Size([3, 5]) output size torch.Size([3, 2])
	In Model: input size torch.Size([1, 5]) output size torch.Size([1, 2])
Outside: input size torch.Size([10, 5]) output_size torch.Size([10, 2])
$
```

## Appendix. Source code

This source code is available at [py_files/pytorch_tutorials-data_parallelism.py](py_files/pytorch_tutorials-data_parallelism.py). 

```python
# PyTorch Tutorials > Data parallel
#   https://pytorch.org/tutorials/beginner/blitz/data_parallel_tutorial.html

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# Parameters and DataLoaders
input_size = 5
output_size = 2

batch_size = 30
data_size = 100

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Dummy Dataset
class RandomDataset(Dataset):

    def __init__(self, size, length):
        self.len = length
        self.data = torch.randn(length, size)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return self.len

rand_loader = DataLoader(dataset=RandomDataset(input_size, data_size),batch_size=batch_size, shuffle=True)

# Simple Model
class Model(nn.Module):
    # Our model

    def __init__(self, input_size, output_size):
        super(Model, self).__init__()
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, input):
        output = self.fc(input)
        print("\tIn Model: input size", input.size(),
              "output size", output.size())

        return output

# Create Model and DataParallel
#  This is the core part of the tutorial. 
model = Model(input_size, output_size)
if torch.cuda.device_count() > 1:
  print("Let's use", torch.cuda.device_count(), "GPUs!")
  # dim = 0 [30, xxx] -> [10, ...], [10, ...], [10, ...] on 3 GPUs
  model = nn.DataParallel(model)

model.to(device)

# Run the Model
for data in rand_loader:
    input = data.to(device)
    output = model(input)
    print("Outside: input size", input.size(),
          "output_size", output.size())
```