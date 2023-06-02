# # zip
# a = [1,2,3]
# b = [4,5,6]
# print(list(zip(a,b)))
# # 输出[(1, 4), (2, 5), (3, 6)]
#
#
# for i,j in zip(a,b):
#     print(i/2,j*2)
# # 输出
# # 0.5 8
# # 1.0 10
# # 1.5 12
#
# print(list(zip(a,a,b)))
# # 输出[(1, 1, 4), (2, 2, 5), (3, 3, 6)]


# lambda
def fun1(x, y):
    return (x + y)


print(fun1(4, 5))

fun2 = lambda x, y: x + y
print(fun2(4, 5))


# map
def fun2(x, y):
    return (x + y)


print(list(map(fun2, [1], [2])))
# 输出：[3]
# 把参数1和2带入到fun1中去；

print(list(map(fun2, [1, 3], [2, 5])))
# 输出：[3, 8]


def square(x):
    return x ** 2


print(map(square, [1, 2, 3, 4, 5]))

# 结果如下:
# <map object at 0x000001085FC7E7C8>
print(list(map(square, [1, 2, 3, 4, 5])))
# [1, 4, 9, 16, 25]

# 通过使用lambda匿名函数的方法使用map()函数：
print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))
# 结果如下：
# [3, 7, 11, 15, 19]

# 通过lambda函数使返回值是一个元组：
print(list(map(lambda x, y: (x ** y, x + y),[2, 4, 6], [3, 2, 1])))
# 结果如下:
# [(8, 5), (16, 6), (6, 7)]
