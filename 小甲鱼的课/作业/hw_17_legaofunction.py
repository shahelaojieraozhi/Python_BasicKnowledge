# 都是重复一段代码，为什么我要使用函数（而不使用简单的拷贝黏贴）呢？
# 0) 可以降低代码量（调用函数只需要一行，而拷贝黏贴需要N倍代码）
# 1) 可以降低维护成本（函数只需修改def部分内容，而拷贝黏贴则需要每一处出现的地方都作修改）
# 2) 使序更容易阅读（没有人会希望看到一个程序重复一万行“I love FishC.com”）

# 2.
# 函数可以有多个参数吗？
# 可以的，理论上你想要有多少个就可以有多少个，只不过如果函数的参数过多，在调用的时候出错的机率就会大大提高，
# 因而写这个函数的程序员也会被相应的问候祖宗，所以，尽量精简吧，在Python的世界里，精简才是王道！

# 3.
# 创建函数使用什么关键字，要注意什么？使用“def ”关键字
# ，要注意函数名后边要加上小括号“()”，然后小括号后边是冒号“:”，然后缩进部分均属于函数体的内容，例如：
# def MyFun():
# # 我是函数体
# # 我也是函数体
# # 我们都属于函数MyFun()
#
# # 噢，我不属于MyFun()函数的了

# # 4.
# # 请问这个函数有多少个参数？
# def MyFun((x, y), (a, b)):
#     return x * y - a * b
# # 如果你回答两个，那么恭喜你错啦，答案是0，因为类似于这样的写法是错误的！
# # 我们分析下，函数的参数需要的是变量，而这里你试图用“元祖”的形式来传递是不可行的。
# # 我想你如果这么写，你应该是要表达这么个意思：
# def MyFun(x, y):
#     return x[0] * x[1] - y[0] * y[1]
#
#
# result = MyFun((3, 4), (1, 2))
# print(result)
# # 10

# # 5. 请问调用以下这个函数会打印什么内容？
# def hello():
#     print('Hello World!')
#     return
#     print('Welcome To FishC.com!')
#
#
# hello()
# # Hello World!
# # 因为当Python执行到return语句的时候，Python认为函数到此结束，需要返回了（尽管没有任何返回值）。

# **********动动手***************

# # 0. 编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。
# def power(x, y):
#     sum = 1
#     for i in range(y):
#         sum *= x
#     return sum
#
#
# print(power(2, 5))
# # 32

# # 1. 编写一个函数，利用欧几里得算法（脑补链接）求最大公约数，例如gcd(x, y)返回值为参数x和参数y的最大公约数。
# def gcd(x, y):
#     if x % y == 0:
#         print('最大公约数是：', y)
#     else:
#         r = x % y
#         while r:
#             r = x % y
#             x = y
#             y = r
#             if x % y == 0:
#                 print('最大公约数是：', y)
#                 break
#
#
# print(gcd(98, 63))
# # 最大公约数是： 7
# # None

# #   参考答案：
# def gcd(x, y):
#     while y:
#         t = x % y
#         x = y
#         y = t
#     return x
#
#
# print(gcd(4, 6))
# # 2


# 2. 编写一个将十进制转换为二进制的函数，要求采用“除2取余”（脑补链接）的方式，结果与调用bin()一样返回字符串形式。
def Dec2Bin(dec):
    temp = []
    result = ''
    while dec:
        quo = dec % 2  # 5/2 = 2。。。。1
        dec = dec // 2  # quo取1，dec取2
        temp.append(quo)  # 向列表从后背添加一个一个quo
    # 比如10，上面的得到的temp = [0101],下面的相当于把数倒过来
    while temp:
        result += str(temp.pop())  # 取列表最后一个值
    return result


#   return返回通过函数得到的因变量
print(Dec2Bin(10))
# 1010
