* Draft: 2021-04-26 (Mon)

<<<<<<< HEAD
# [PyTorch > QUICKSTART](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html)
## Overview

* This document explain a quick way to test PyTorch.
* Basically, the source code in [PyTorch > QUICKSTART](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html) is executed.

  * The code in the quick start has been separated into two files
    * [py_files/intro2pytorch-quickstart-1.py](py_files/intro2pytorch-quickstart-1.py)
    * [py_files/intro2pytorch-quickstart-2.py](py_files/intro2pytorch-quickstart-2.py)

* The first file 
  * downloads the FASHION MNIST dataset,
  * train a simple `linear_relu_stack`,
  * and save the trained mode into a file `model.pth`.

* The second file
  * Run the first fileloads the saved model
  * and make predictions for small test samples.
  * There are two parts in the second file.
    * The second part is the core part of the code explained in the QUICKSTART tutorial.
    * Running the second part alone results in errors.
    * So the first part is added to make this code run.

## Running the codes with PyTorch

### Run the first file

```bash
$ python intro2pytorch-quickstart-1.py 
Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz to data/FashionMNIST/raw/train-images-idx3-ubyte.gz
 96%|█████████████████████████████████████████████▏ | 25403392/26421880 [00:05<00:00, 7074918.00it/s]
  ...
Shape of X [N, C, H, W]:  torch.Size([64, 1, 28, 28])
Shape of y:  torch.Size([64]) torch.int64
Using cuda device
NeuralNetwork(
  (flatten): Flatten()
  (linear_relu_stack): Sequential(
    (0): Linear(in_features=784, out_features=512, bias=True)
    (1): ReLU()
    (2): Linear(in_features=512, out_features=512, bias=True)
    (3): ReLU()
    (4): Linear(in_features=512, out_features=10, bias=True)
    (5): ReLU()
  )
)
Epoch 1
-------------------------------
loss: 2.307811  [    0/60000]
loss: 2.299018  [ 6400/60000]
loss: 2.289791  [12800/60000]
loss: 2.285959  [19200/60000]
loss: 2.265438  [25600/60000]
loss: 2.264678  [32000/60000]
loss: 2.247811  [38400/60000]
loss: 2.237546  [44800/60000]
loss: 2.245918  [51200/60000]
26427392it [00:19, 7074918.00it/s]                                                                   loss: 2.215613  [57600/60000]
Test Error: 
 Accuracy: 36.1%, Avg loss: 0.034933 
  ...
Epoch 5
-------------------------------
loss: 1.602853  [    0/60000]
loss: 1.706681  [ 6400/60000]
loss: 1.610328  [12800/60000]
loss: 1.756509  [19200/60000]
loss: 1.524418  [25600/60000]
loss: 1.612534  [32000/60000]
loss: 1.471268  [38400/60000]
loss: 1.436631  [44800/60000]
loss: 1.532282  [51200/60000]
loss: 1.543261  [57600/60000]
Test Error: 
 Accuracy: 52.6%, Avg loss: 0.024452 

Done!
Saved PyTorch Model State to model.pth
26427392it [00:56, 466710.18it/s]
$
```

### Check the files

```bash
$ ls
data  intro2pytorch-quickstart-1.py  intro2pytorch-quickstart-2.py  model.pth
$ ls data
FashionMNIST
$
```

The `tree` command, installed separately, shows the directory structure under the `data` directory.

```bash
$ tree -d data
data
└── FashionMNIST
    ├── processed
    └── raw

3 directories
$
```

### Run the second file

According to the QUICKSTART tutorial, the expected output is

```bash
Predicted: "Ankle boot", Actual: "Ankle boot"
```

In actually,

```bash
$ python intro2pytorch-quickstart-2.py 
Predicted: "Ankle boot", Actual: "Ankle boot"
$
```

I got the same result.



## Appendix A. The first file

 [py_files/intro2pytorch-quickstart-1.py](py_files/intro2pytorch-quickstart-1.py)
=======
# [QUICKSTART](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html)
* This document explain a quick way to test PyTorch.
* Basically, the source code in [PyTorch > QUICKSTART](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html) is executed.

There are two files:
1. [py_files/intro2pytorch-quickstart-1.py](py_files/intro2pytorch-quickstart-1.py)
2. [py_files/intro2pytorch-quickstart-2.py](py_files/intro2pytorch-quickstart-2.py)

## 1. [py_files/intro2pytorch-quickstart-1.py](py_files/intro2pytorch-quickstart-1.py)
>>>>>>> 4fc7aa8f9740edb69415801d34e375a62922098b

```python
# Source: PyTorch > QUICKSTART
#   https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
# Refer to https://github.com/aimldl/pytorch/blob/main/en/hands-on/01-intro2pytorch-quickstart.md

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import dataset[py_files/intro2pytorch-quickstart-1.py](py_files/intro2pytorch-quickstart-1.py)

[py_files/intro2pytorch-quickstart-2.py](py_files/intro2pytorch-quickstart-2.py)

s
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt

# Download training data from open datasets.
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)

# Download test data from open datasets.
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)

batch_size = 64

# Create data loaders.
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

for X, y in test_dataloader:
    print("Shape of X [N, C, H, W]: ", X.shape)
    print("Shape of y: ", y.shape, y.dtype)
    break
    
# Get cpu or gpu device for training.
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using {} device".format(device))

# Define model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),[py_files/intro2pytorch-quickstart-1.py](py_files/intro2pytorch-quickstart-1.py)

[py_files/intro2pytorch-quickstart-2.py](py_files/intro2pytorch-quickstart-2.py)


            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
            nn.ReLU()
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)
print(model)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # Compute prediction error
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")
            
def test(dataloader, model):
    size = len(d[py_files/intro2pytorch-quickstart-1.py](py_files/intro2pytorch-quickstart-1.py)ataloader.dataset)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item[py_files/intro2pytorch-quickstart-1.py](py_files/intro2pytorch-quickstart-1.py)

[py_files/intro2pytorch-quickstart-2.py](py_files/intro2pytorch-quickstart-2.py)

()
    test_loss /= size
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
    
epochs = 5
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_dataloader, model, loss_fn, optimizer)
    test(test_dataloader, model)
print("Done!")

torch.save(model.state_dict(), "model.pth")
print("Saved PyTorch Model State to model.pth")
```

<<<<<<< HEAD
## Appendix B. The second file

[py_files/intro2pytorch-quickstart-2.py](py_files/intro2pytorch-quickstart-2.py)

The core (or second) part of the second file is below.
=======
## [py_files/intro2pytorch-quickstart-2.py](py_files/intro2pytorch-quickstart-2.py)
* Load the previously saved model and make predictions for small test samples.
* There are two parts in the second file.
  * The second part shown below is the core.
  * Running the second part alone results in errors.
  * The first part is added to make this code work without the  errors.
>>>>>>> 4fc7aa8f9740edb69415801d34e375a62922098b

```python

model = NeuralNetwork()
model.load_state_dict(torch.load("model.pth"))

classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

model.eval()
x, y = test_data[0][0], test_data[0][1]
with torch.no_grad():
    pred = model(x)
    predicted, actual = classes[pred[0].argmax(0)], classes[y]
    print(f'Predicted: "{predicted}", Actual: "{actual}"')
```

<<<<<<< HEAD
The entire code is below.

```python
# Source: PyTorch > QUICKSTART
#   https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
# Refer to https://github.com/aimldl/pytorch/blob/main/en/hands-on/01-intro2pytorch-quickstart.md

# The first part
#   is added to make the second part run without errors.
import torch
from torch import nn
from torchvision import datasets
from torchvision.transforms import ToTensor
=======
The expected output is
>>>>>>> 4fc7aa8f9740edb69415801d34e375a62922098b

# Define model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
            nn.ReLU()
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

# Download test data from open datasets.
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)

# The second part:
#   Error occurs in the following lines without the above lines which are taken from the first file.

model = NeuralNetwork()
model.load_state_dict(torch.load("model.pth"))

classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

model.eval()
x, y = test_data[0][0], test_data[0][1]
with torch.no_grad():
    pred = model(x)
    predicted, actual = classes[pred[0].argmax(0)], classes[y]
    print(f'Predicted: "{predicted}", Actual: "{actual}"')
```
