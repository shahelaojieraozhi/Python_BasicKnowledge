# # 0. 使用递归编写一个十进制转换为二进制的函数（要求采用“取2取余”的方式，结果与调用bin()一样返回字符串形式）。
# # using factorial:
# temp = []
#
#
# def Dec2Bin(n):
#     if n == 1:
#         return 1
#     else:
#         x = n % 2
#         return x
#
#
# number = int(input('请输入一个正整数：'))
# result = bin(number)
# print('%d 的二进制是： %d' % (number, result))
# # 报错

# # 2. 编写一个将十进制转换为二进制的函数，要求采用“除2取余”（脑补链接）的方式，结果与调用bin()一样返回字符串形式。
# def Dec2Bin(dec):
#     temp = []
#     result = ''
#     while dec:
#         quo = dec % 2  # 5/2 = 2。。。。1
#         dec = dec // 2  # quo取1，dec取2
#         temp.append(quo)  # 向列表从后背添加一个一个quo
#     # 比如10，上面的得到的temp = [0101],下面的相当于把数倒过来
#     while temp:
#         result += str(temp.pop())  # 取列表最后一个值
#     return result
#
#
# #   return返回通过函数得到的因变量
# print(Dec2Bin(10))
# # 1010

# def Dec2Bin(dec):
#     result = ''
#     if dec:
#         result = Dec2Bin(dec // 2)
#         return result + str(dec % 2)
#     #   能被2整除 result 加个0,不能就加个1
#     else:
#         return result
#
#
# print(Dec2Bin(11))
# # 1011
# # Dec2Bin(11) = Dec2Bin(5) + ‘1’
# # Dec2Bin(5) =  Dec2Bin(2) + ‘1’
# # Dec2Bin(2) =  Dec2Bin(1) + ‘0’
# # Dec2Bin(1) =  Dec2Bin(0) + ‘1’
# # Dec2Bin(0) =  result

# # using factorial:
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#     #   设 n = 3, factorial(3) = 3 * factorial（2） = 3 * 2 * factorial（1） = 3*2*1
#
#
# number = int(input('请输入一个正整数：'))
# result = factorial(number)
# print('%d 的阶乘是： %d' % (number, result))
# # 请输入一个正整数：6
# # 6 的阶乘是： 720

# #   写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。举例：get_digits(12345) ==> [1, 2, 3, 4, 5]
# #   解题思路：利用除以10取余数的方式，每次调用get_digits(n//10)，并将余数存放到列表中即可。要注意的是结束条件设置正确。
# result = []
#
#
# def get_digits(n):
#     if n > 0:
#         result.insert(0, n % 10)
#         get_digits(n // 10)
#
#
# get_digits(12345)
# print(result)
# # [1, 2, 3, 4, 5]


# 3. 使用递归编程求解以下问题：
# 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

# # made by myself
# def ages(n):
#     if n == 1:
#         return 10
#     else:
#         return 2 + ages(n - 1)
#
#
# ages_5 = ages(5)
# print(ages_5)
# # 18

#   made by little turtle
def age(n):
    if n == 1:
        return 10
    else:
        return age(n - 1) + 2


print('哈哈，我知道了，第五个人的年龄是 %d 岁，啵啵脆！' % age(5))
# 哈哈，我知道了，第五个人的年龄是 18 岁，啵啵脆！
