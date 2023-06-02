import copy
# 第一种copy
a = [1,2,3]
b = a
print(id(a))
print(id(b))
# 输出:
# 3127206361160
# 3127206361160

b[0] = 11
print(a)
# 输出：[11, 2, 3]

a[1] = 22
print(b)
print((id(a)) == id(b))
# 输出：
# [11, 22, 3]
# True


# 第二种copy
# 浅拷贝
c = copy.copy(a)
print(c)
print(id(a) == id(c))
# 输出：
# [11, 22, 3]
# False

c[1] = 2222
print(a)
print(c)
# 输出：
# [11, 22, 3]
# [11, 2222, 3]

a = [1,2,[3,4]]
d = copy.copy(a)
print(id(a) == id(d))
print((id(a[2])) == id(d[2]))
# 输出：
# False
# True

a[0] = 11
print(a)
# [11, 2, [3, 4]]
print(d)
a[2][0] = 333
print(a)
print(d)
# [1, 2, [3, 4]]
# [11, 2, [333, 4]]
# [1, 2, [333, 4]]

# #第三种copy
e = copy.deepcopy(a)
print(id(e[2]) == id(a[2]))
# False
# 深度拷贝得出的对象内存空间完全不一样；
