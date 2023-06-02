
# sorted(key=lambda x:x*2)

# map() : 批量将列表中的元素处理
l = [1, 2, 3, 4, 5]
# l2 = [i**2 for i in l]  # 列表推导式
l2 = map(lambda x: x**2, l)
print(l2, list(l2))

# print( list(reversed(l)) )
l3 = map(lambda x,y: x*y, [1, 2, 3], [4, 5, 6])
print(list(l3))  # [4, 10, 18]

# reduce() : 累计运算, 了解
from functools import reduce
n = reduce(lambda x,y: x+y, [1, 2, 3, 4, 5])  # 累加
print(n)
# 累乘
def fn(x, y):
    print('x:', x)
    return x * y
n = reduce(fn, [1, 1, 2, 3, 5])
print(n)

# filter() : 过滤
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = filter(lambda x: x%2, l)
print(l2, list(l2))

# 取出l列表中的3的倍数
l3 = filter(lambda x: x%3==0, l)
print(list(l3))








