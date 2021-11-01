import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 3, 0.1) #0.1为步长
y = 0.3**x

plt.plot(x, y)  #指数函数图像
plt.show()
