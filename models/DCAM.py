import torch
import torch.nn as nn
from thop import profile

class PrimaryChanAttention(nn.Module):
    def __init__(self, in_planes, ratio=16):
        super(PrimaryChanAttention, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveMaxPool2d(1)
        self.fc1 = nn.Conv2d(in_planes, in_planes // ratio, 1, bias=False)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Conv2d(in_planes // ratio, in_planes, 1, bias=False)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = self.fc2(self.relu1(self.fc1(self.avg_pool(x))))
        max_out = self.fc2(self.relu1(self.fc1(self.max_pool(x))))
        out = avg_out + max_out
        return self.sigmoid(out)

class ChanContextSampling(nn.Module):
    def __init__(self, kernel_size=3):
        super(ChanContextSampling, self).__init__()
        assert kernel_size in (3, 7)
        self.gap = nn.AdaptiveAvgPool2d(1)
        self.conv = nn.Conv1d(1, 1, kernel_size=kernel_size, padding=(kernel_size - 1) // 2)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        y = self.gap(x)
        y = y.squeeze(-1).permute(0, 2, 1)
        y = self.conv(y)
        y = self.sigmoid(y)
        y = y.permute(0, 2, 1).unsqueeze(-1)
        return y.expand_as(x)

class DCAM(nn.Module):
    def __init__(self, in_planes, ratio=16, kernel_size=7):
        super(DCAM, self).__init__()
        self.pca = PrimaryChanAttention(in_planes, ratio)
        self.ccs = ChanContextSampling(kernel_size)

    def forward(self, x):
        out = x * self.pca(x)
        result = out * self.ccs(out)
        return result