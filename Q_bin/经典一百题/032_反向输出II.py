# **题目：**按相反的顺序输出列表的值。

# # 用外挂
# list1 = [1, 2, 3, 4]
# print(list1[::-1])

# for循环
list1 = [1, 2, 3, 4]
for i in range(len(list1)):
    print(list1[3 - i])
