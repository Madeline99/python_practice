import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random

# 饼状图
# label = ["A", "B", "C", "D"]
# num = [0.25, 0.3, 0.4, 0.05]
# ex = [0.2, 0, 0.1, 0]
# # plt.axis(args=1)#将整个圆等分
# plt.pie(x = num, autopct = "%.1f%%",explode = ex, labels = label, colors = ["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], shadow = True,
#         startangle = 30)
# plt.show()

#散点图(3D空间)
# x = np.random.normal(0,1,100)
# y = np.random.normal(0,1,100)
# z = np.random.normal(0,1,100)
#
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(x,y,z)
# plt.show()

#二维散点图
n = 1000
x = np.random.randn(n)
y = np.random.randn(n)
plt.scatter(x,y,color ="#48D1CC")
plt.show()
