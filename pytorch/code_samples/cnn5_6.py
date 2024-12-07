# p.72

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.init as init
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

batch_size = 256
learning_rate = 0.0002
num_epoch = 10

mnist_train = dset.MNIST("./", train=True, transform=transforms.ToTensor(), target_transform=None, download=True)
mnist_test = dset.MNIST("./", train=False, transform=transforms.ToTensor(), target_transform=None, download=True)

train_loader = torch.utils.data.DataLoader( mnist_train, batch_size=batch_size, shuffule=True, num_workers=2, drop_last=True)
test_loader = torch.utils.data.DataLoader( mnist_test, batch_size=batch_size, shuffule=False, num_workers=2, drop_last=True)

class CNN( nn.module ):
    def __init__(self):
        super(CNN,self).__init__()

        self.layer =nn.Sequential(
            nn.Conv2d(1,16,5),
            nn.ReLU(),
            nn.Conv2d(16,32,5),

        )
