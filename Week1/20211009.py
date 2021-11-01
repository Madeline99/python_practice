#对列表排序
cat = ['橘猫','布偶猫','田园猫','缅因猫','蓝猫','加菲猫']
sorted(cat)
print(cat)
cat.reverse()
print(cat)
cat.sort()
print(cat)
cat.sort(reverse = True)
print(cat)

for i in cat:
    print(i)

print(len(cat))
#翻转一个句子中的字符串
message = "Hello python world !"
message = message.split(" ")
message = message[-1::-1]
mess = ' '.join(message)
print(mess)
#反向输出一串数字或字符
# num = "56974568965"
# num = list(num)
# list.reverse(num)
# print(num)

#输出所有的水仙花数
num = 100
while num<1000:
    a = num//100
    b = (num-100*a)//10
    c = (num-100*a-10*b)//1
    if (a**3+b**3+c**3)==num:
        print(num)
    num+=1


