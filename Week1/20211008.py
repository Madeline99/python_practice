# 输出语句

print("Hello world!")

message = "Hello python world!"
print(message)

name = "刘" + \
       "德" + \
       "华"
print(name)

a = 3
b = 3.0
c = True
d = 3 + 2j
print(type(a))
print(type(b))
print(type(c), type(d))
print(type(message))

i, j = 2, 3
m = n = 1
print(i, j)
print(m, n)

age = 23
mess = "Happy " + str(age) + "rd Birthday!"
print(mess)

cat = ['橘猫', '布偶猫', '田园猫', '缅因猫', '蓝猫', '加菲猫']
print(cat)
print(cat[3])
print(cat[1:])
cat[0] = '英短'
print(cat[0])
cat.append('美短')
cat.insert(3, '无毛猫')
del cat[4]
cat.pop(2)
cat.remove('无毛猫')
print(cat)
