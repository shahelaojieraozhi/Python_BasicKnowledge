# **题目：**有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 不用递归，越用越有问题
# def fn(n):
#     if  n<=1:
#         a = 1
#         b = 2
#         return b / a
#     else:
#         str1 = str(fn(n))
#         x = list(str1.split("/"))
#         a = x[0]
#         b = x[1]
#     return (a+b)/a
#
#
# print(fn(3))

#  参考答案
a = 2.0
b = 1.0
s = 0
for n in range(1, 21):
    s += a / b
    a, b = a + b, a
print(s)
