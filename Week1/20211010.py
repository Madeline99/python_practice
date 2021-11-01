# # 遍历列表中的所有元素，并为每一个元素都打印一条消息
cat = ['橘猫', '布偶猫', '田园猫', '缅因猫', '蓝猫', '加菲猫']
message = "长的真可爱啊！"
for i in cat:
    print(i + message)

# # 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
a = 2.0
b = 1.0
sum = 0
for i in range(1, 21):
    sum += a / b
    c = a + b
    b = a
    a = c
print(sum)

# 求1+2!+3!+...+20!的和
n = input('请输入要计算的整数：')
n = int(n)
a = 1
#l1 = []#检测用
sum1 = 0
for i in range(1, n+1):
    num = i
    for j in range(i-1, 0, -1):
        num *= j
#   l1.append(num)#检测用
#   print l1
sum1 += num
print(sum1)

#找到2000到3200间所有可被7整除，但不可被5整除的数字
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i)

#当tuple中只包含一个元素时，需要给该元素后边加一个’，‘  否则（1）会被python认为是数字而非元组

a1 = (1)
print(type(a1))
a2 = (1,)
print(type(a2))
