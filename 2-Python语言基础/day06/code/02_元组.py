
# 列表: 可变数组
# 元组: 不可变数组

# 基本操作
# 1.创建元组
t = ()
t = (1,)  # 1个元素的元组
t = (1, 2, 3)
print(t, type(t))

# 2.索引
print(t[0])
print(t[-1])

# 3.长度
print(len(t))

# 4.遍历
t = (11, 22, 33)
for n in t:
    print(n)
for i in range(len(t)):
    print(i)
for i,n in enumerate(t):
    print(i, n)

# 5.切片
print(t[1:3])  # (22, 33)
print(t[::-1])  # (33, 22, 11)

# 6.合并
print((1,2) + (3,4))  # (1, 2, 3, 4)

# 7.重复
print((1,2) * 3)  # (1, 2, 1, 2, 1, 2)

# 8.成员
print(11 in t)

# 9.删除
t = (1, 2, 3, 4, 5)
# del t


# 元组的功能
# 增删改查
# 元组是不可变的: 元组的元素不可以改变
# 没有增删改操作
# 查: t[0] 或 遍历

# 排序
#  sort, sort(reverse=True), reverse() 都不可以用于元组,因为它们都会改变原对象

# t = (1, 3, 2, 5, 4)
# print(sorted(t))  # [1, 2, 3, 4, 5]
# print(sorted(t, reverse=True))  # [5, 4, 3, 2, 1]
# print(list(reversed(t)))  # [4, 5, 2, 3, 1]

# 快速取值: 掌握
x, y = 1, 2
x, y = (3, 4)
x, y = [3, 4]
print(x, y)  # 3 4

# 元组和列表之间的切换
print(list((1,2,3)))  # [1, 2, 3]
print(tuple([1,2,3]))  # (1, 2, 3)
# int()
# float()
# str()
# list()
# tuple()
# dict()
# set()
# bool()

# 元组中包含列表

t = (1, 2, [3, 4])
t[2][0] = 100
print(t)  # (1, 2, [100, 4])


