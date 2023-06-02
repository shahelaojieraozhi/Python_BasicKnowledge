# list1 = [1, 3, 2, 9, 7, 8]
# print(list1[2:5])
# [2, 9, 7]

# # discrepancy
# print(list1[0])
# print(list1[0:1])
# # 1
# # [1]

# # 如果你每次想从列表的末尾取出一个元素，并将这个元素插入到列表的最前边
# print(list1.pop())  # 取最后一个数并且把它也删了
# # 8
# list1.insert(0, list1.pop())
# print(list1)
# # [8, 1, 3, 2, 9, 7]

# list1 = [1, 3, 2, 9, 7, 8]
# # # 正常索引是从左到右索引，负数索引是从右到左。
# # print(list1[-3:-1])
# # # [9, 7]
#
# # list2 = list1[:]，那事实上可不可以直接写成 list2 = list1 更加简洁呢？
# list1 = [1, 3, 2, 9, 7, 8]
# list2 = list1[:]
# print(list2)
# # [1, 3, 2, 9, 7, 8]
# list3 = list1
# print(list3)
# # [1, 3, 2, 9, 7, 8]
#
# list1.sort()
# print(list1)
# # [1, 2, 3, 7, 8, 9]
# print(list2)
# # [1, 3, 2, 9, 7, 8]
# print(list3)
# # [1, 2, 3, 7, 8, 9]


# #  如何将下边这个列表的'小甲鱼'修改为'小鱿鱼'？
# list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
# list1[1][2] = '小鱿鱼'
# print(list1)
# # [1, [1, 2, '小鱿鱼'], 3, 5, 8, 13, 18]

# #   顺序和逆序
# list1 = [1, 3, 2, 9, 7, 8]
# list1.sort()
# print(list1)
# # [1, 2, 3, 7, 8, 9]
# list1.sort(reverse=True)
# print(list1)
# # [9, 8, 7, 3, 2, 1]

# #   列表推导式或列表解析
# list8 = [i * i for i in range(10)]
# print(list8)
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# # 相当于
# list1 = []
# for x in range(10):
#     list1.append(x ** 2)
# print(list1)
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# # 列表推导式（List comprehensions）也叫列表解析，灵感取自函数式编程语言 Haskell。Ta 是一个非常有用和灵活的工具，
# # 可以用来动态的创建列表，语法如：[有关A的表达式 for A in B]
# list1 = [x**3 for x in range(10)]
# print(list1)
# # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# list1 = [(x, y) for x in range(10) for y in range(10) if x % 2 == 0 if y % 2 != 0]
# print(list1)
# # [(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (2, 1), (2, 3), (2, 5), (2, 7), (2, 9), (4, 1),
# # (4, 3), (4, 5), (4, 7), (4, 9), (6, 1), (6, 3), (6, 5), (6, 7),
# # (6, 9), (8, 1), (8, 3), (8, 5), (8, 7), (8, 9)]
#
# # 等效为：
# list1 = []
# for x in range(10):
#     for y in range(10):
#         if x % 2 == 0 and y % 2 != 0:
#             list1.append((x, y))
# print(list1)
# # [(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (2, 1), (2, 3), (2, 5), (2, 7),
# # (2, 9), (4, 1), (4, 3), (4, 5), (4, 7), (4, 9), (6, 1),
# # (6, 3), (6, 5), (6, 7), (6, 9), (8, 1), (8, 3), (8, 5), (8, 7), (8, 9)]

#   活学活用：请使用列表推导式补充被小甲鱼不小心涂掉的部分
list1 = ['1.just do it','2.一切皆有可能','3.让编程改变世界','4.impossible is nothing']
list2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]
for each in list3:
    print(each)
# 1.耐克：just do it
# 2.李宁：一切皆有可能
# 3.鱼C工作室：让编程改变世界
# 4.阿迪达斯：impossible is nothing
