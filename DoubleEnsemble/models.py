from sklearn import neural_network
import torch
import torch.nn as nn

class BasicMLP(torch.nn.Modules):
    def __init__(self, n_feats):
        super(BasicMLP, self).__init__()
        self.fc1 = nn.Linear(n_feats, 64)
        self.mish1 = nn.Mish()
        self.fc2 = nn.Linear(64, 64)
        self.mish2 = nn.Mish()
        self.fc3 = nn.Linear(64, 1)
        self.dropout = nn.Dropout()
        self.batchnorm = nn.BatchNorm1d(1)

    def forward(self, x):
        out = self.fc1(x)
        out = self.mish1(out)
        out = self.fc2(out)
        out = self.mish2(out)
        out = self.fc3(out)
        out = self.dropout(out)
        out = self.batchnorm(out)
        return out

