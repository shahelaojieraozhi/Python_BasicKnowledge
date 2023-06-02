
# 变量
# age: 变量名字
# = : 赋值符号,  ==表示相等
# 10 : 值
age = 10
print(age)  # 10

age = 20
print(age)  # 20

# 连续赋值, a和b都是30
# a = b = 30
# print(a, b)  # 30 30

# 给不同的变量赋不同的值
c, d = 40, 50
print(c, d)  # 40 50

# e = 60; f = 70
# print(e, f)  # 60 70

# 交换2个变量的值
x = 20
y = 30

# 第1种方式: 重点掌握
x, y = y, x

# 第2种方式
# z = y  # z = 30
# y = x  # y = 20
# x = z  # x = z = 30

# 扩展
# x = x + y  # x=50; y=30
# y = x - y  # x=50; y=20
# x = x - y  # x=30; y=20

# ^ : 位异或
# x = x ^ y
# y = x ^ y
# x = x ^ y

# ^异或: 相同为0,不同为1
# x = x ^ y
#   x: 10100  => 20
#   y: 11110  => 30
# -------------
# x =  01010
#
# y = x ^ y
#   x: 01010
#   y: 11110
# -------------
# y =  10100  => 20
#
# x = x ^ y
#   x: 01010
#   y: 10100
# -------------
# x =  11110  => 30

print(x, y)


# 变量的命名规范
#   规则: 必须遵守
#       1.由数字,字母,下划线组成, 且不能以数字开头.
#       2.不能使用关键字.
#   规范: 建议遵守
#       1.区分大小写,比如age和Age是2个不同的变量.
#       2.尽量见名知意,比如age, name, sex
#       3.多个单词之间使用下划线 my_like 或 小驼峰 myLike

A1_1 = 1

# 国家 = '中国'  # 不推荐
# print(国家)

# 关键字
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(len(keyword.kwlist))  # 35


# 删除变量
# del x
print('x =', x)


