
# 集合 set
#   特点: 唯一,无序,不可变类型

# 1.创建集合
s = {}  # 空字典
s = set()  # 空集合
s = {1, 2, 3, 1, 1, 1, 2, 3}
s = {'a', 'b', 'c'}
print(s, type(s))

# 2.索引: 没有
# 3.长度
print(len(s))

# 4.遍历
for n in s:
    print(n)

# 5.切片: 没有
# 6.合并: 没有
# print({1} + {2})
# 7.重复: 没有
# 8.成员
print('a' in s)

# 其他功能
# 增删改查
# 增
s = {1, 2, 3, 4}
s.add(5)
s.update({7, 8})
print(s)

# 删
s = {1, 2, 3, 4}
# s.pop()
# s.remove(33)
# s.discard(33)
s.clear()
print(s)

# 集合之间的关系
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1 & s2)  # 交集  {4, 5}
print(s1 | s2)  # 并集  {1, 2, 3, 4, 5, 6, 7, 8}
print(s1 - s2)  # 差集  {1, 2, 3}
print(s1 ^ s2)  # 对称差集  {1, 2, 3, 6, 7, 8}
print(s1 > s2)  # s1是否包含s2  False
print(s1 <= s2)  # s2是否包含s1   False


# 集合中大家需要掌握的: 去重
list1 = [1, 1, 1, 2, 2, 2, 4, 5, 5, 5, 4, 3, 5]
print(list(set(list1)))
# [1, 2, 3, 4, 5]

