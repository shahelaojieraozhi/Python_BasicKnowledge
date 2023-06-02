# **题目：**对10个数进行排序。
# row1 = []
# for i in range(10):
#     a = int(input('输入一个整数：'))
#     row1.append(a)
# print(sorted(row1))

raw = []
for i in range(10):
    x = int(input('int%d: ' % i))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i, len(raw)):
        if raw[i] > raw[j]:
            raw[i], raw[j] = raw[j], raw[i]
print(raw)
