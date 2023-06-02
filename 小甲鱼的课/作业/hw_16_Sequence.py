# 1请问分别使用什么BIF，可以把一个可迭代对象转换为列表、元组和字符串？
# list([iterable])
# 把可迭代对象转换为列表
# tuple([iterable])
# 把可迭代对象转换为元组
# str(obj)
# 把对象转换为字符串

# temp = 'I love FishC.com!'
# list1 = list(temp)
# print(list1)
# # ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'F', 'i', 's', 'h', 'C', '.', 'c', 'o', 'm', '!']
#
# temp = 'I love FishC.com!'
# tuple1 = tuple(temp)
# print(tuple1)
# # ('I', ' ', 'l', 'o', 'v', 'e', ' ', 'F', 'i', 's', 'h', 'C', '.', 'c', 'o', 'm', '!')

# 2你还能复述出“迭代”的概念吗？
# 所谓迭代，是重复反馈过程的活动，其目的通常是为了接近并到达所需的目标或结果。每一次对过程的重复被称为一次“迭代”，
# 而每一次迭代得到的结果会被用来作为下一次迭代的初始值。

# name = input('请输入待查找的用户名：')
# score = [['迷途', 85], ['黑夜', 80], ['小布丁', 65], ['福禄娃娃', 95], ['怡静', 90]]
# IsFind = False
#
# for each in score:
#     if name in each:
#         print(name + '的得分是：', each[1])
#         IsFind = True
#         break
#
# if IsFind==False:
#     print('查找的数据不存在！')
# # 请输入待查找的用户名：小布丁
# # 小布丁的得分是： 65

# # 猜想一下 min() 这个BIF的实现过程
# def min(x):
#     least = x[0]
#     for each in x:
#         if each < least:
#             least = each
#     return least
#
#
# print(min('123456789'))
# # 1


# # sum() 这个BIF有个缺陷，就是如果参数里有字符串类型的话就会报错，请写出一个新的实现过程，
# # 自动“无视”参数里的字符串并返回正确的计算结果
# def sum(x):
#     result = 0
#     for each in x:
#         if (type(each) == int) or (type(each) == float):
#             result += each
#         else:
#             continue
#     return result
#
#
# print(sum([1, 2.1, 2.3, 'a', '1', True]))
# # 5.4
