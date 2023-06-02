# **题目：**打印出如下图案（菱形）:
# for i in range(1,5):
#     print(' '*(5-i),'*'*(2*i-1))
#
# for j in range(1,4):
#     print(' ' * (j+1), '*' * (2*(4-j)-1))
# #      *
# #     ***
# #    *****
# #   *******
# #    *****
# #     ***
# #      *


# def draw(num):
#     a = "*" * (2 * (4 - num) + 1)
#     print(a.center(9, ' '))
#     if num != 1:
#         draw(num - 1)
#         print(a.center(9, ' '))
#
#
# draw(4)


# # 语法：str.center(width , "fillchar")  -> str  返回字符串
# # 描述：返回一个长度为width,两边用fillchar(单字符)填充的字符串，即字符串str居中，
# # 两边用fillchar填充。
# str1 = "i love python"
# print(str1.center(20, "*"))
# print(str1.center(1, "*"))  # 若字符串的长度大于width,则直接返回字符串str
# print(str1.center(20, "8"))
