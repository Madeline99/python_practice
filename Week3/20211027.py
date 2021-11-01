import matplotlib.pyplot as plt
import numpy as np

# #sinx和cosx的函数图
# x = np.linspace(0, 2 * np.pi, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.title("sin&cos")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.show()

# 堆叠柱状图
# name_list = ["A","B","C","D"]
# num_list = [6,9,8,3]
# num_list1 = [1,2,8,9]
#
# plt.bar(range(len(name_list)),num_list,color = "r",tick_label = name_list)
# plt.bar(range(len(name_list)),num_list1,color = "g",tick_label = name_list)
# plt.legend()  #将两个柱状图堆在一起
# plt.show()

# 并列柱状图
name_list = ["A", "B", "C", "D"]
num_list = [6, 9, 8, 3]
num_list1 = [1, 2, 8, 9]
x = list(range(len(name_list)))
w = 0.4
plt.bar(x, num_list, width = w, color = "r", tick_label = name_list)
for i in range(4):
    #将两个柱子隔开来，x控制的是柱子开始的位置，每次循环使x动态调整
    x[i] += w
plt.bar(x, num_list1, width = w, color = "g", tick_label = name_list)
plt.show()
