import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-9, 10, 0.1)
y1 = 1/(1+np.exp(-x))
y2 = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

plt.plot(x, y1)   #sinmold与tanh的函数图像
plt.plot(x, y2)
plt.show()
