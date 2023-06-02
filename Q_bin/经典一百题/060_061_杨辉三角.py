# # **题目60：**计算字符串长度。
# s='zhangguang101'
# print(len(s))

# 实例061：杨辉三角
#
# **题目：**打印出杨辉三角形前十行。　　
# 解析：杨辉三角的两个腰边的数都是 1，从第3行起，除第一个数和最后一个数外，其它位置的数都是上顶上两个数之和。
#                               1
#                            1     1
#                         1     2     1
#                      1     3     3     1
#                   1     4     6     4     1
#                1     5     10    10    5     1
#             1     6     15    20    15    6     1
#          1     7     21    35    35    21    7     1
#       1     8     28    56    70    56    28    8     1
#    1     9     36    84    126   126   84    36    9     1

# # 参考答案一：
# def generate(numRows):
#     r = [[1]]
#     for i in range(1, numRows):
#         r.append(list(map(lambda x, y: x + y, [0] + r[-1], r[-1] + [0])))
#     return r[:numRows]
#
#
# a = generate(10)
# for i in a:
#     print(i)

# # 参考答案二（平板python里面有步骤）：
# def generate(numRows):
#     """
#     :type numRows: int
#     :rtype: List[List[int]]
#     """
#     if numRows == 0:
#         return []
#     if numRows == 1:
#         return [[1]]
#     if numRows == 2:
#         return [[1], [1, 1]]
#     numRows -= 2
#     rList = [[1], [1, 1]]
#     while numRows > 0:
#         newList = [1]
#         for i in range(len(rList[-1]) - 1):
#             newList.append(rList[-1][i] + rList[-1][i + 1])
#         newList.append(1)
#         rList.append(newList)
#         numRows -= 1
#     return rList
#
#
# a = generate(6)
# # 学习一下列表里的小列表打印方式：
# for i in a:
#     print(i)
# # 还要学习大列表、小列表的思想；

# 参考答案三：
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    l1 = [1]
    l2 = []
    n = 0
    while n < numRows:
        l2.append(l1)
        l1 = [sum(t) for t in zip([0] + l1, l1 + [0])]
        n += 1
    return l2


a = generate(6)
for i in a:
    print(i)

# ceng = int(input('请输入杨辉三角的层数：'))
# if ceng == 1:
#     print('1')
# elif ceng == 2:
#     print('1   1')
# else:
#     for i in range(ceng):
#         lis = []
#         lis.append(1)

# # 复习
# # lambda
# def fun1(x, y):
#     return (x + y)
#
#
# print(fun1(4, 5))
#
# fun2 = lambda x, y: x + y
# print(fun2(4, 5))
#
#
# # map
# def fun2(x, y):
#     return (x + y)
#
#
# print(list(map(fun2, [1], [2])))
# # 输出：[3]
# # 把参数1和2带入到fun1中去；
#
# print(list(map(fun2, [1, 3], [2, 5])))
# # 输出：[3, 8]


# # list1 = [1, 1, 1, 1, 1, 1, 1, ]
# # 第一层：
# list1 = [1]
# print(list1)
# # 第二层：
# list2 = [1, 1]
# print(list2)
# # 第三层
# list3 = []
# for i in range(3):
#     list3.append(1)
# list3[1] = list3[0] + list3[1]
# print(list3)
# # 第四层：
# list4 = []
# for i in range(4):
#     list4.append(1)
# list4[1] = list3[0] + list3[1]
# list4[2] = list3[1] + list3[2]
# print(list4)
# # 第五层：
# list5 = []
# for i in range(5):
#     list5.append(1)
# list5[1] = list4[0] + list4[1]
# list5[2] = list4[1] + list4[2]
# list5[3] = list4[2] + list4[3]
# print(list5)

