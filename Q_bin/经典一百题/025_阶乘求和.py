# **题目：**求1+2!+3!+...+20!的和。
# s = 0
#
#
# def fn(n):
#     if n <= 1:
#         return 1
#     return n * fn(n - 1)
#
#
# for i in range(1, 21):
#     #   print(fn(i))
#     s += fn(i)
# print(s)

# 参考答案：
# **程序分析：**1+2!+3!+...+20!=1+2(1+3(1+4(...20(1))))
res = 1
for i in range(20, 1, -1):
    res = i * res + 1
print(res)
