
# 1.封装函数，比较某两个数的大小，返回较大的一个
def fn1(x, y):
    return max(x, y)

# 2.封装函数，判断某个数是否是素数，返回结果(True或False)
def fn2(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

# 3.封装函数，计算2-100之间素数的个数，返回结果
def fn3():
    count = 0
    for n in range(2, 101):
        if fn2(n):
            count += 1
    return count

print(fn3())
