import torch
import matplotlib.pyplot as plt
from torch import nn
import random

#解决非线性问题
xs = torch.unsqueeze(torch.arange(-20., 20.), dim = 1)/20#归一化
ys = [e.pow(3) * random.randint(1, 6) for e in xs]
ys = torch.stack(ys)

class Line(nn.Module):
    def __init__(self):
        super().__init__()
        #将整个神经网络封装起来
        self.fc_layer = nn.Sequential(
            nn.Linear(1, 20),
            nn.ReLU(),
            nn.Linear(20, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 20),
            nn.ReLU(),
            nn.Linear(20, 1),
        )

    def forward(self, x):
        return self.fc_layer(x)


if __name__ == '__main__':
    net = Line()
    loss_func = nn.MSELoss()
    # opt = torch.optim.SGD(net.parameters(), lr =0.01)
    opt = torch.optim.Adam(net.parameters())

    for epoch in range(3000):
        out = net.forward(xs)
        loss = loss_func(out, ys)

        opt.zero_grad()
        loss.backward()
        opt.step()

        if epoch % 5 == 0:
            print(loss.item())

            plt.cla()
            plt.title("loss%.4f" % loss.item())
            plt.plot(xs, ys, '.')
            plt.plot(xs, out.detach())
            plt.pause(0.001)

    plt.ioff()
    plt.show()
