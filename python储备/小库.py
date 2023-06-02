import datetime
import numpy as np
import random
from numpy import random

# # 日期操作
# print(datetime.date.today())
# # 2021-09-19
# print(datetime.date(2333, 2, 3))
# # 2333-02-03
# print(datetime.date.today().strftime('%d/%m/%Y'))
# # 19/09/2021
#
# day = datetime.date(1111, 2, 3)
# day = day.replace(year=day.year + 22)
# # 日期的年加22
# print(day)
# # 1133-02-03


# # 语法：str.center(width , "fillchar")  -> str  返回字符串
# # 描述：返回一个长度为width,两边用fillchar(单字符)填充的字符串，即字符串str居中，
# # 两边用fillchar填充。
# str1 = "i love python"
# print(str1.center(20, "*"))
# print(str1.center(1, "*"))  # 若字符串的长度大于width,则直接返回字符串str
# print(str1.center(20, "8"))
# # ***i love python****
# # i love python
# # 888i love python8888

# if y:
#     return x * power(x, y - 1)
# if y就是if y>0


# # 生成1-10的整数
# x = random.randint(1, 10)
# print(x)
# # 生成10个0到10的整数：
# a = np.random.randint(0, 10, 10)
# print(a)
# # [3 1 7 3 2 4 4 2 9 3]

# # python 生成随机数和随机矩阵
# # 生成随机数
# print(random.random())  # 用于随机生成一个0到1的浮点数
# print(random.randint(2, 5))  # 随机生成[2,5]区间内的整数
# # 0.41915852917581986
# # 3

# # 生成随机矩阵
# print(np.random.rand(3, 4))
# print(np.random.randint(2, 5, (3, 3)))  # (3,3)表示矩阵大小
# # [[0.45639186 0.23366679 0.10665463 0.5106083 ]
# #  [0.62931873 0.89673632 0.77130182 0.43920822]
# #  [0.10175607 0.39612095 0.29659527 0.35922483]]
# # [[3 2 4]
# #  [2 2 2]
# #  [4 4 4]]

# # 随机生成数
# print(random.uniform(10, 20, size=(3)))
# #   [13.47030991 18.77321242 17.95190481]
# print(random.uniform(10, 20, size=(2, 3)))
# # [[18.33978761 13.33058547 16.00235145]
# #  [12.43052926 10.42627393 18.83103697]]

# Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# print(np.random.uniform(0.5, 1.0, 12))
# # 生成n个0.5到1.0的随机数
# # [0.94379506 0.54020561 0.69420618 0.77696505 0.92495455 0.87030901
# # 0.99222507 0.86920711 0.61241698 0.91201769 0.73266228 0.9310038 ]

# #463——OPENCV


# # 将分子分母分开
# String_test = "3/7"
# x = String_test.split("/")
# print(x)
# # ['3', '7']

# # 索引用[]
# str1 = 'hfowr'
# print(str1[1])
# # f

# # 索引里面能有变量
# number1 = 'nkdjf'
# a = len(number1)
# print(number1[a-2])
# # j

# # 列表的分块
# a = np.random.randint(0, 10, 5)
# print(a)
# # [9 1 3 0 1]
# print(a[-1])  # 取最后一个元素
# # 1
# print(a[:-1])  # 除了最后一个取全部
# # [9 1 3 0]
# print(a[::-1])  # 取从后向前（相反）的元素
# # [1 0 3 1 9]
# print(a[2::-1])  # 取从下标为2的元素翻转读取
# # [3 1 9]

# 多行缩进 全选
# （1）tab
# 整体取消缩进
# （1）tab+shift

# # # “将字符串abc中的每个成员以字符','分隔开再拼接成一个字符串”
# print(','.join('abc'))
# # a,b,c


# # transpose()的说法：(博客里收藏————python基础里面)
# x = np.arange(4).reshape((2, 2))
# print(x)
# # [[0 1]
# #  [2 3]]
# # 对于二维 ndarray，transpose在不指定参数是默认是矩阵转置。
# print(x.transpose())
# # [[0 2]
# #  [1 3]]


# # list 的运算操作
# list_a = [1, 12, 19, 4, 5, 9]
# total = sum(list_a)
# print(total)  # 打印效果为 50
# print(max(list_a))  # 打印结果为19
# print(min(list_a))  # 打印结果为1

# # 输出错误：
# list1 = [1, 3, 3]
# a = 1
# print(list1.append(a))
# # None


# # 如果我们在函数中定义一个同名的局部变量，那么函数会优先使用局部变量，对全局变量不会造成影响。
# a = 100  # 全局变量
#
#
# def test():
#     a = 200  # 局部变量
#     print(a)
#
#
# test()
# print(a)
# # 200
# # 100

# # 然而，如果我们想在函数中修改函数外变量 就会出现问题
# a = 100
#
#
# def test():
#     a = a * 3
#     print(a)
#
#
# test()
#
# # UnboundLocalError: local variable 'a' referenced before assignment
# # 这是因为，a = a * 3是一条赋值语句，Python解释器会将 a 认作局部变量，所以 a * 3 因为 a 这个局部变量还没有定义，而抛出这样的错误。

# # 那应该怎么做呢？
# # 在函数中用global声明，告诉python这个变量是全局变量。该声明仅在当前代码块中有效。
# a = 100
#
#
# def test():
#     global a
#     a = a * 3
#     print(a)
#
#
# test()
# # 300

# # 这个try可以学一下(100题中46)
# while True:
#     try:
#         n = float(input('输入一个数字：'))
#     except:
#         print('输入错误')
#         continue
#     dn = n ** 2
#     print('其平方为：', dn)
#     if dn < 50:
#         print('平方小于50，退出')
#         break

# # enumerate() 函数
# # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
# # 以下是 enumerate() 方法的语法:
# #
# # enumerate(sequence, [start=0])
#
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))
# # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
#
# print(list(enumerate(seasons, start=1)))    # 下标从 1 开始
# # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
#
# i = 0
# seq = ['one', 'two', 'three']
# for element in seq:
#     print(i, seq[i])
#     i += 1
# # 0 one
# # 1 two
# # 2 three
#
# seq = ['one', 'two', 'three']
# for i, element in enumerate(seq):
#     print(i, element)
# # 0 one
# # 1 two
# # 2 three
# print(list(enumerate(seq)))
# # [(0, 'one'), (1, 'two'), (2, 'three')]


# python调试技巧————断点操作
# 断点打到哪程序就执行到那，挂住等你用调试里的操作
import json


def paixu():
    alist = [3, 2, 5, 4, 9, 6, 7, 8]
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp
    print(alist)


if __name__ == '__main__':
    a = 'A'
    print('test')
    paixu()
    b = json.loads('{"test":123}')
    print(b)

# 两个函数：排序是自己写的代码，json.load是别人的包装好的函数
#
# 调试后有个特殊变量（Special Variables）里面有function 和 module；还有一个普通变量

# F7 进入函数内部，碰到函数就进入
# shift+F8 跳出函数 上箭头
# Alt+ shift + F8： 只进入自己的函数，第三方模块写的方法不进入
# F9 当大多个断点时。F9会到下一个断点，如果没有断点则执行至完成
# Alt + F9 移动到光标处

# python中用matplotlib作图汉字显示的是小方块的解决方法：
# 在代码开头加上以上代码指定中文字体即可


from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
