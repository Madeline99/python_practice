import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(-99, 0)
x2 = np.arange(1, 100)
y1 = 1/x1
y2 = 1/x2

plt.plot(x1, y1)  #绘制1/x的函数图像
plt.plot(x2, y2)
plt.show()
