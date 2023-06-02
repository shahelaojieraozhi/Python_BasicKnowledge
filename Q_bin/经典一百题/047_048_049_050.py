import random
from numpy import random
# 这两个random 不一样

# # **题目47：**两个变量值用函数互换。
#
# def exc(a, b):
#     return (b, a)
#
#
# a = 0
# b = 10
# a, b = exc(a, b)
# print(a, b)

# # **题目48：**数字比较。
# a = int(input('a='))
# b = int(input('b='))
# if a < b:
#     print('a<b')
# elif a > b:
#     print('a>b')
# else:
#     print('a=b')

# # 实例049：lambda
# Max = lambda x, y: x * (x >= y) + y * (y > x)
# Min = lambda x, y: x * (x <= y) + y * (y < x)
#
# a = int(input('1:'))
# b = int(input('2:'))
#
# print(Max(a, b))
# print(Min(a, b))

# 随机生成数
print(random.uniform(10, 20, size=(3)))
#   [13.47030991 18.77321242 17.95190481]
print(random.uniform(10, 20, size=(2, 3)))
# [[18.33978761 13.33058547 16.00235145]
#  [12.43052926 10.42627393 18.83103697]]

