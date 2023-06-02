

# 列表的增删改查
# 增
stars = ['吴亦凡', '鹿晗', '蔡徐坤', '黄子韬', '肖战']
stars.append('张艺兴')  # 在列表末尾追加元素
# stars.insert(2, '张艺兴')  # 在下标2的位置插入元素
# stars.extend([11, 22, 33])  # 一次追加多个元素(需要用列表或元组或字符串包裹)
print(stars)

# 删
nums = [33, 44, 55, 44, 1, 44, 66]
n = nums.pop(2)  # 弹出指定下标的元素,默认是弹出最后一个元素
# print(n, nums)

# nums.remove(44)  # 删除指定的第一个元素
# print(nums)

# nums.clear()  # 清空列表
# print(nums)

# count() : 统计某元素出现的次数
print(nums.count(44))


# 改
ages = [1, 2, 3]
ages[1] = 200
print(ages)  # [1, 200, 3]

# 查
print(ages[1])
# 使用循环遍历


print('*' * 100)

# index(): 获取元素第一次出现的下标位置
nums = [33, 44, 55, 44, 1, 44, 66]
print(nums.index(44))  # 1
# print(nums.index(444))  # 报错
if 44 in nums:
    print(nums.index(44))

# 排序
nums = [3, 4, 2, 1, -1, 6, 5]
# nums.sort()  # 升序, 会改变原列表
# nums.sort(reverse=True)  # 降序
# nums.reverse()  # 倒序,翻转,反序,逆序
print(nums)

nums = [3, 4, 2, 1, -1, 6, 5]
# nums2 = sorted(nums)  # 升序,不会改变原列表
# nums2 = sorted(nums, reverse=True)  # 降序,不会改变原列表
# nums2 = list(reversed(nums))  # 倒序,不会改变原列表
nums2 = nums[::-1]  # 倒序,不会改变原列表
print(nums2)
print(nums)


# copy() : 复制,拷贝
#   基本类型/不可变类型: int,float,str,bool,tuple
#   引用类型/可变类型: list, dict, set(了解)

# 赋值
# 不可变类型: 简单的赋值, 没有关联
a = 10
b = a
a = 99
print(a, b)  # 99  10

# 可变类型: 赋值,有关联
l1 = [1, 2, 3]
l2 = l1
l1[0] = 100
print(l1, l2)  # [100, 2, 3] [100, 2, 3]

# 复制,拷贝
# 浅拷贝,浅复制: 只拷贝列表的第一层
l1 = [1, 2, 3]
l2 = l1.copy()
l1[0] = 100
print(l1, l2)  # [100, 2, 3] [1, 2, 3]

# 深拷贝,深复制
# l1 = [1, 2, 3, [4, 5, 6]]
# l2 = l1.copy()
# l1[-1][-1] = 100
# print(l1, l2)  # [1, 2, 3, [4, 5, 100]]   [1, 2, 3, [4, 5, 100]]

import copy
l1 = [1, 2, 3, [4, 5, 6]]
l2 = copy.deepcopy(l1)
l1[-1][-1] = 100
print(l1, l2)  # [1, 2, 3, [4, 5, 100]]   [1, 2, 3, [4, 5, 6]]

# 数据内存可视化
# http://pythontutor.com/visualize.html#mode=edit


