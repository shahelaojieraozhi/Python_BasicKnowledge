
# 列表: list, 数组Array
# 作用是: 保存多个值(一般是相同类型的值)

# 变量:
#  保存不同的汽车品牌
a = '奔驰'
b = '宝马'
c = '奥迪'
d = '红旗'
e = '保时捷'
f = '布加迪'
# 如果有100个品牌,我们就不能用上面的方式保存
# 可以使用列表来存储
cars = ['奔驰', '保时捷', '丰田']

# 列表的基本操作
# 1.创建列表
ages = [11, 22, 33]
# ages = [11, True, 'Porsche']

# 2.索引,下标, index, 从0开始
print(ages[0])  # 11
print(ages[1])  # 22
print(ages[2])  # 33
print(ages[-1])  # 33, 倒数第1个
# ages[0] = 10  # 修改

# 3.列表长度,列表中元素的个数
print(len(ages))  # 3

# 4.遍历列表
ages = [11, 22, 33]
for n in ages:
    print(n)  # 元素

for i in range(len(ages)):
    print(i, ages[i])  # 下标,元素

# enumerate: 枚举,列举
for i, n in enumerate(ages):
    print(i, n)  # 下标,元素

# x, y = 1, 2

# 5.切片: 从原来的列表中截取制定的一段数据,不会改变原列表,会生成新列表
ages = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print( ages[:] )  # 从头取到尾  [1, 2, 3, 4, 5, 6, 7, 8, 9]
print( ages[3:] )  # 从下标3开始到末尾  [4, 5, 6, 7, 8, 9]
print( ages[:3] )  # 从头开始取到下标3结束(不包括3)  [1, 2, 3]
print( ages[3:6] )  # 范围:[3,6)  [4, 5, 6]
print( ages[1:6:2] )  # [2, 4, 6]
print( ages[6:1:-1] )  # [7, 6, 5, 4, 3]
print( ages[::-1] )  # 倒序,逆序,反序 [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 6.合并
print([1,2,3] + [3,4,5])  # [1, 2, 3, 3, 4, 5]

# 7.重复
print([1,2,3] * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 8.成员
if 3 in [1,2,3]:
    print('3在列表中')

# 9.删除
list1 = [1, 2, 3, 4]
# del list1  # 删除列表
# del list1[1]  # 删除元素
del list1[1:3]  # 删除多个元素
print(list1)


