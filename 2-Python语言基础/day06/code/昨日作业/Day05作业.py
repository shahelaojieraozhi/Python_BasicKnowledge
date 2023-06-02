
''' 基础题 '''
# 【注：以下6题功能全部自己使用循环实现，不能借助于Python内置函数: max, min, sort, reverse】

# 1.自定义一个数字列表，获取这个列表中的最小值
ages = [1, -3, 2, 5, -4, 99, 7, 8, 5, 3]

# 2. 自定义一个数字列表，元素为10个 ,找出列表中最大数连同下标一起输出
ages = [1, -3, 2, 5, -4, 99, 7, 8, 5, 3]

# 3. 自定义一个数字列表，求列表中第二大数的下标
ages = [1, -3, 2, 5, -4, 99, 7, 8, 5, 3]


# 4. B哥去参加青年歌手大奖赛 ,有10个评委打分 ,(去掉一个最高分一个最低分)求平均分
scores = [33, 44, 88, 88, 33, 66, 77, 88, 44, 55]
max1 = scores[0]
min1 = scores[0]
for n in scores:
    if n > max1:
        max1 = n
    if n < min1:
        min1 = n
print(f'max1: {max1}, min1: {min1}')
# 去掉一个最高分,最低分
scores.remove(max1)
scores.remove(min1)
# 求平均分
avg = sum(scores) / len(scores)
print(f'avg: {avg}')

# 5. 定义列表，存放5个学生的成绩【成绩值自己设定】，获得成绩之和，平均成绩，最小成绩，最大成绩。
scores2 = [66, 77, 88, 99, 100]
max1 = scores2[0]
min1 = scores2[0]
for n in scores2:
    if n > max1:
        max1 = n
    if n < min1:
        min1 = n
print(f'成绩和: {sum(scores2)}')
print(f'平均成绩: {sum(scores2)/len(scores2)}')
print(f'最小成绩: {min1}')
print(f'最大成绩: {max1}')


# 6. 将一个列表逆序输出, 提示: range(6,-1,-1), [::-1]
list1 = [66, 7, 88, 9, 20]
print(list1[::-1])

for i in range(len(list1)-1, -1, -1):
    print(list1[i])

# 7.完成猜拳游戏
# 		-----------------------------
# 		请输入你的选择:
# 		1. 石头
# 		2. 剪刀
# 		3. 布
# 		-----------------------------
# 		如: 你的选择是【布】, 电脑的选择是【石头】
# 		恭喜你获得了胜利！
#
# import random
# print('''
# -----------------------------
# 请输入你的选择(1/2/3):
# 1. 石头
# 2. 剪刀
# 3. 布
# -----------------------------
# ''')
# # 石头 > 剪刀
# # 剪刀 > 布
# # 布 > 石头
# computer = random.randint(1, 3)
# print('computer:', computer)
#
# me = int(input('输入你的选择:'))
# if me == computer:
#     print('平手')
# elif me-computer==-1 or me-computer==2:
#     print('恭喜您获得了胜利!')
# else:
#     print('您输了')


''' 进阶题:可以使用内置函数 '''
# 1.给定一个列表：将列表中指定的某个元素全部删除: count, remove
nums = [1, 2, 1, 1, 3, 3, 4, 1, 5]
x = 1
for _ in range(nums.count(x)):
    nums.remove(x)
print(nums)

# 2.自定义一个列表，最大的与第一个元素交换，最小的与最后一个元素交换，输出列表(不考虑特殊情况)
list1 = [2, 3, 4, 5, -6, 7, 8, 1]
# 提示: 要获取最大值和最小值的下标
max_index = 0
min_index = 0
for i in range(len(list1)):
    if list1[i] > list1[max_index]:
        max_index = i
    if list1[i] < list1[min_index]:
        min_index = i

# 交换
# 最大的与第一个元素交换
list1[max_index], list1[0] = list1[0], list1[max_index]
# 最小的与最后一个元素交换
list1[min_index], list1[-1] = list1[-1], list1[min_index]

print(list1)

# 交换列表的元素,要使用下标
# list1[0], list1[2] = list1[2], list1[0]


# 3,对称列表. 传入一个列表，元素类型与个数皆未知，返回新列表，由原列表的元素正序反序拼接而成;
# 如传入["One", "Two", "Three"] 返回['One', 'Two', 'Three', 'Three', 'Two', 'One']
list2 = ["One", "Two", "Three"]
print(list2 + list2[::-1])

# list3 = list2.copy()
# list3.reverse()
# print(list2 + list3)

# print(list2 + list(reversed(list2)))

# list3 = []
# for n in list2:
#     list3.insert(0, n)
# print(list2 + list3)

# 4, 给定一个不存在重复元素的整数列表，例如[6 ,4 ,7 ,2 ,5 ,8]和一个数字，例如10，
# 找出两个元素(或同一个元素加自身)，并且使这两个数的和为给定数字，并打印出来
# 例如[6 ,4 ,7 ,2 ,5 ,8]和数字10. 打印结果为: 6,4  2,8  5,5

# 提示: 需要使用for循环嵌套
list3 = [6, 4, 7, 2, 5, 8]
n = 10
for i in range(len(list3)):
    for j in range(i, len(list3)):
        # print(list3[i], list3[j])
        if list3[i] + list3[j] == n:
            print(list3[i], list3[j])

# 5,有一个从小到大排好序的列表。现输入一个数，要求按原来的规律将它插入列表中,
# 如: [2, 3, 4, 56, 67, 98]  如插入63, 100
nums = [2, 3, 4, 56, 67, 98]
n = 100

# nums.append(n)
# nums.sort()
# print(nums)

for i in range(len(nums)):
    if n < nums[i]:
        nums.insert(i, n)
        break
else:
    nums.append(n)

print(nums)

# 6,列表去重, 将下面的列表中重复的元素去除, 不能使用set()
# list1 = [1, 2, 3, 5, 4, 4, 4, 5, 5, 3, 2, 1]
list1 = [1, 2, 3, 5, 4, 4, 4, 5, 5, 3, 2, 1]
list2 = [1, 2, 3, 5, 4]
for n in list1:
    if n not in list2:
        list2.append(n)
print(list2)

list1 = [1, 2, 3, 5, 4, 4, 4, 5, 5, 3, 2, 1]
# for i in range(len(list1)):
#
#     for j in range(i+1, len(list1)):
#         if list1[i] == list1[j]:
#             list1.pop(j)

i = 0
while i < len(list1):

    j = i+1
    while j < len(list1):

        if list1[i] == list1[j]:
            list1.pop(j)
            j -= 1

        j += 1

    i += 1

print(list1)

list1 = [1, 2, 3, 5, 4, 4, 4, 5, 5, 3, 2, 1]
print(list(set(list1)))

