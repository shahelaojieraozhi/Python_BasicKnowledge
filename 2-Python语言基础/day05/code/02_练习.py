
# 1.自定义一个数字列表，获取这个列表中的最小值
ages = [1, -3, 2, 5, -4, 99, 7, 8, 5, 3]
min1 = ages[0]  # 默认第1个最小
for n in ages:
    if n < min1:
        min1 = n

print(min1)

# 1.自定义一个数字列表，获取这个列表中的最小值,和最小值下标
ages = [1, -3, 2, 5, -4, 99, -7, 8, 5, 3]
min1 = ages[0]  # 默认的最小数
min1_index = 0  # 默认的最小数下标
for i, n in enumerate(ages):
    if n < min1:
        min1 = n
        min1_index = i

print(min1, min1_index)


# 2. 自定义一个数字列表，元素为10个 ,找出列表中最大数连同下标一起输出
ages = [1, -3, 2, 5, -4, 99, 7, 8, 5, 3]
max1 = ages[0]
max1_index = 0
for i, n in enumerate(ages):
    if n > max1:
        max1 = n
        max1_index = i
print(max1, max1_index)


# 3. 自定义一个数字列表，求列表中第二大数的下标
ages = [1, -3, 2, 5, -4, 99, 7, 8, 5, 3]
# 1.先求最大数
max1 = ages[0]
for n in ages:
    if n > max1:
        max1 = n
print('max1:', max1)

# 2.求第二大数
max2 = ages[0]
max2_index = 0
for i, n in enumerate(ages):
    if n != max1 and n > max2:
        max2 = n
        max2_index = i
print("max2_index:", max2_index)

