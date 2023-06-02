# **题目：**给一个不多于5位的正整数，
# 要求：一、求它是几位数，二、逆序打印出各位数字。
#
# **程序分析：**学会分解出每一位数,用字符串的方法总是比较省事。

# String_test = input('输入一个不多于5位数的正整数：')
# # print(type(String_test))
# # # 输入一个不多于5位数的正整数：3345
# # # <class 'str'>
# degree1 = len(String_test)
# print('输入的数字是{}位数'.format(degree1))
# print('逆序打印：', end='')
#
#
# def rec(string):
#     if len(string) != 1:
#         rec(string[1:])
#     print(string[0], end=' ')
#
#
# rec(String_test)

n = int(input('输入一个正整数：'))
n = str(n)
print('%d位数' % len(n))
# 反向输出
print(n[::-1])
