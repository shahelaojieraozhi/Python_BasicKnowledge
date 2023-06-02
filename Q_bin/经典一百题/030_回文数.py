# **题目：**一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
#
# **程序分析：**用字符串比较方便,就算输入的不是数字都ok。

# # 专门的五位数：
# number1 = input('请输入一个5位数：')
# if (number1[0] == number1[4]) and (number1[1] == number1[3]):
#     print('{}是回文数'.format(number1))
# else:
#     print('{}不是回文数'.format(number1))

# # 任意输入的数：
# number1 = input('请输入一个整数：')
# a = len(number1)-1
# flag = 0
# for i in range(len(number1)):
#     if number1[i] == number1[a - i]:
#         flag += 1
# if flag == len(number1):
#     print('{}是回文数'.format(number1))
# else:
#     print('{}不是回文数'.format(number1))

# 参考：
n = input("随便你输入啥啦：")
a = 0
b = len(n) - 1
flag = True
while a < b:
    if n[a] != n[b]:
        print('不是回文串')
        flag = False
        break
    a, b = a + 1, b - 1
if flag:
    print('是回文串')
