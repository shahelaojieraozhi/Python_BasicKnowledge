# **题目：**计算两个矩阵相加。
#
# **程序分析：**创建一个新的矩阵，使用 for 迭代并取出 X 和 Y 矩阵中对应位置的值，相加后放到新矩阵的对应位置中。
import numpy as np

# w = np.random.randint(2, 5, (3, 3))
# print(w)
# v = np.random.randint(0, 4, (3, 3))
# print(v)
# [x, y] = w.shape
# for i in range(x):
#     for j in range(y):
#         w[i][j] = w[i][j] + v[i][j]
# print(w)

# 参考答案，没我的吊
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

res = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]
for i in range(len(res)):
    for j in range(len(res[0])):
        res[i][j] = X[i][j] + Y[i][j]
print(res)
