# 求一个3*3矩阵主对角线元素之和。
import numpy as np
# shape是np.array的属性，列表没有shape属性。
# 我把这个转成矩阵做了
mat = [[1, 2, 3],
       [3, 4, 5],
       [4, 5, 6]
       ]
mat1 = np.array(mat)
# print(mat[0])   # # [1, 2, 3]
# print(mat[0][1])    # 2
[r, c] = mat1.shape
list1 = []
for i in range(r):
    for j in range(c):
        if i == j:
            list1.append(mat1[i][j])
print(list1)
print(sum(list1))

# 参考答案
mat = [[1, 2, 3],
       [3, 4, 5],
       [4, 5, 6]
       ]
res = 0
for i in range(len(mat)):
    res += mat[i][i]
print(res)


# # 1. 一维数组 / 向量（由一维列表产生）
# a = [1,2,3]
# b = np.array(a)
# print(b.shape)
# # (3,)
#
# # 2. 二维数组（列表内嵌套一个列表)
# a = [[1, 2, 3]]
# b = np.array(a)
# print(b)  # [[1 2 3]]
# print(b.shape)  # (1, 3)
# print(b.transpose())
# # [[1]
# #  [2]
# #  [3]]

# # 3. 二维数组（列表内嵌套多个列表）
# a = [[1, 2, 3], [4, 5, 6]]
# b = np.array(a)
# print(b)
# # [[1 2 3]
# #  [4 5 6]]
# print(b.shape)  # (2, 3)

# # transpose()的说法：(博客里收藏————python基础里面)
# x = np.arange(4).reshape((2, 2))
# print(x)
# # [[0 1]
# #  [2 3]]
#
# # 对于二维 ndarray，transpose在不指定参数是默认是矩阵转置。
# print(x.transpose())
# # [[0 2]
# #  [1 3]]
#
# # 三维
# A = np.arange(16)
# # A是array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
#
# # 将A变换为三维矩阵
# A = A.reshape(2, 2, 4)
# print(A)
# # [[[ 0  1  2  3]
# #   [ 4  5  6  7]]
# #
# #  [[ 8  9 10 11]
# #   [12 13 14 15]]]
# B = A.transpose((1, 0, 2))  # 将 0轴 和 1轴 交换
# print(B)
# # [[[ 0  1  2  3]
# #   [ 8  9 10 11]]
# #
# #  [[ 4  5  6  7]
# #   [12 13 14 15]]]


