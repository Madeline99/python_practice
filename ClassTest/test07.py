import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(0, 11, 0.1)
x2 = np.arange(-10, 0, 0.1)
y1 = x1
y2 = 0 * x2  #ReLU函数
y3 = 0.1 * x2   #leack ReLU函数
y4 = (np.exp(x2)-1)    #ELU函数

plt.plot(x1, y1)
plt.plot(x2, y4)
plt.show()

