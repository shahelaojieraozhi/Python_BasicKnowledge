# # **题目：**输入三个整数x,y,z，请把这三个数由小到大输出。

# a = int(input('请输入第一个整数：'))
# b = int(input('请输入第二个整数：'))
# c = int(input('请输入第三个整数：'))
# if (a > b) and (a > c):
#     if b > c:
#         print(c,b,a)
#     else:
#         print(b,c,a)
# if (b > a) and (b > c):
#     if a > c:
#         print(c,a,b)
#     else:
#         print(a,c,b)
# if (c > a) and (c > b):
#     if a > b:
#         print(b,a,c)
#     else:
#         print(a,b,c)


# a = int(input('请输入第一个整数：'))
# b = int(input('请输入第二个整数：'))
# c = int(input('请输入第三个整数：'))
# list = (a,b,c)
# print(sorted(list))


# row1 = []
# for i in range(3):
#     a = int(input('输入一个整数：'))
#     row1.append(a)
# print(sorted(row1))

# 没看懂
raw = []
for i in range(3):
    a = int(input('输入一个整数：'))
    raw.append(a)
for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i] > raw[j]:
            raw[i],raw[j] = raw[j],raw[i]
print(raw)
