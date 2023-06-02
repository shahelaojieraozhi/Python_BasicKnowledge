# **题目：**利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
# 不是递归：
# list1 = []
# str1 = input('请输入5个字符：')
# for i in range(5):
#     list1.append(str1[4 - i])
# print(list1)

def rec(string):
    if len(string) != 1:
        rec(string[1:])
    print(string[0], end=' ')


rec(input('string here:'))

