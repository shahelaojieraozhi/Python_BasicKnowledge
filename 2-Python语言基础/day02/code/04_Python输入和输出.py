
# 输出
print(10)  # 打印1个数
print(10, 20, 30)  # 同时打印多个值
print(10, 20, 30, sep='++++')  # sep表示分隔符,默认是空格
print(200, 250, end='==')  # end表示结束符,默认是\n换行符
print(300)

# 输入
# input:
#   1.会让程序暂停,需要在控制台输入内容后按回车.
#   2.得到的一定是一个字符串,不是整数
# input('请输入您的名字:')
# print('ok')

age = input('请输入年龄:')

print(age)
# type() : 查看数据类型, int整数, float小数, str字符串
print(type(age))  # <class 'str'>

# int(): interger 转成整数
# float(): 转成小数
# str(): 转成字符串
print(int(age) + 10)


# 练习：从控制台输入两个数，计算两个数的和，并将结果输出
a = int(input('a:'))
b = int(input('b:'))
print(a + b)








