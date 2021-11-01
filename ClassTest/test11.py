import torch
import matplotlib.pyplot as plt
from torch import nn

xs = torch.unsqueeze(torch.arange(0.01, 1, 0.01), dim = 1)
ys = 3 * xs + 4




class Line(nn.Module):
    # 设计神经网络
    def __init__(self):
        super().__init__()
        self.w1 = nn.Parameter(torch.randn(1, 20))
        self.b1 = nn.Parameter(torch.randn(20))
        self.w2 = nn.Parameter(torch.randn(20, 64))
        self.b2 = nn.Parameter(torch.randn(64))
        self.w3 = nn.Parameter(torch.randn(64, 128))
        self.b3 = nn.Parameter(torch.randn(128))
        self.w4 = nn.Parameter(torch.randn(128, 20))
        self.b4 = nn.Parameter(torch.randn(20))
        self.w5 = nn.Parameter(torch.randn(20, 1))
        self.b5 = nn.Parameter(torch.randn(1))

    # 模型的前向计算
    def forward(self, x):
        fc1 = torch.matmul(x, self.w1) + self.b1
        fc2 = torch.matmul(fc1, self.w2) + self.b2
        fc3 = torch.matmul(fc2, self.w3) + self.b3
        fc4 = torch.matmul(fc3, self.w4) + self.b4
        fc5 = torch.matmul(fc4, self.w5) + self.b5
        return fc5


if __name__ == '__main__':
    net = Line()
    loss_func = nn.MSELoss()
    # opt = torch.optim.SGD(net.parameters(), lr = 0.1)
    opt = torch.optim.Adam(net.parameters())

    plt.ion()
    for epoch in range(30000000):
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
