# **题目：**打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
# 其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# by myself
# for i in range(100, 1000):
#     a = i // 100
#     b = i % 100
#     c = b // 10
#     d = i % 10
#     if (a ** 3 + c ** 3 + d ** 3) == i:
#         print(i)
# 153
# 370
# 371
# 407

# # 高级一点的
# for i in range(100, 1000):
#     sum = 0
#     temp = i
#     while temp:
#         sum = sum + (temp % 10) ** 3
#         temp = temp // 10
#     if sum == i:
#         print(i)
# # 153
# # 370
# # 371
# # 407

# 通过字符
for i in range(100, 1000):
    s = str(i)  # 转成字符
    one = int(s[-1])
    ten = int(s[-2])
    hun = int(s[-3])
    if i == one ** 3 + ten ** 3 + hun ** 3:
        print(i)
