# # iteration for 斐波那契数列
# def function_F(n):
#     n1 = 1
#     n2 = 1
#     n3 = 1
#     if n < 1:
#         print('输入有误！')
#         return -1
#     while (n - 2) > 0:
#         n3 = n2 + n1
#         n1 = n2
#         n2 = n3
#         n -= 1
#     return n3
#
#
# result = function_F(20)
# if result != -1:
#     print('总共有%d对小兔崽子诞生！' % result)


#   recursion for 斐波那契数列
def function_F(n):
    if n < 1:
        print('输入有误！')
        return -1
    if n == 1 or n == 2:
        return 1
        print('1')
    else:
        x = function_F(n - 1) + function_F(n - 2)
        return x


print(function_F(8))



