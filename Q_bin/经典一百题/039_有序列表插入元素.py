# **题目：**有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
#
# **程序分析：**首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。


# # 用了sorted函数：
# list1 = [1, 10, 100, 1000, 10000, 100000]
# a = int(input('输入需要要插进去的数：'))
# list1.append(a)
# print(sorted(list1))

# for——loop
# 还需要修补
# list1 = [1, 10, 100, 1000, 10000, 100000]
# a = int(input('输入需要要插进去的数：'))
# for i in range(6):
#     if (list1[5 - i]) <= a:
#         list1.insert(6-i, a)
# print(list1)

lis = [1, 10, 100, 1000, 10000, 100000]
n = int(input('insert a number: '))
lis.append(n)
for i in range(len(lis) - 1):
    if lis[i] >= n:
        for j in range(i, len(lis)):
            lis[j], lis[-1] = lis[-1], lis[j]
        break
print(lis)
