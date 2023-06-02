# 将一个数组逆序输出。
# lis = [1, 10, 100, 1000, 10000, 100000]
# print('第一种实现：')
# L = len(lis) - 1
# lis2 = []
# for i in range(len(lis)):
#     # print(lis[L - i])
#     lis2.append(lis[L - i])
# print(lis2)

# lis = [1, 10, 100, 1000, 10000, 100000]
# print('第二种实现：')
# lis.reverse()
# print(lis)

# 底层（不用特殊函数）：
# lis = [1, 2, 3, 4]
# print('第三种实现：')
# L = len(lis) - 1
# for i in range(len(lis)):
#     lis[i] = lis[L - i]
# print(lis)


lis = [1, 2, 3, 4, 5]
# print(int(len(lis) / 2)) # 2
for i in range(int(len(lis) / 2)):
    lis[i], lis[len(lis) - 1 - i] = lis[len(lis) - 1 - i], lis[i]
print('第三种实现：')
print(lis)

