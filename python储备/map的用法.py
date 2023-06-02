a = (1, 2, 3, 4, 5)
b = [1, 2, 3, 4, 5]
c = "zhangkang"

la = list(map(str, a))
lb = list(map(str, b))
lc = list(map(str, c))

print(la)
print(lb)
print(lc)


# 输出：
# ['1', '2', '3', '4', '5']
# ['1', '2', '3', '4', '5']
# ['z', 'h', 'a', 'n', 'g', 'k', 'a', 'n', 'g']

# str()是python的内置函数，这个例子是把列表/元组/字符串的每个元素变成了str类型，然后以列表的形式返回。
# 当然我们也可以传入自定义的函数，看下面的例子:

def mul(x):
    return x * x


n = [1, 2, 3, 4, 5]
res = list(map(mul, n))
print(res)


# 输出：[1, 4, 9, 16, 25]

# 把列表n中的每个元素运行一次mul函数后得到的结果作为最终结果列表的元素。再看下有多个iterable参数的情况。
def add(x, y, z):
    return x + y + z


list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 3]
res = list(map(add, list1, list2, list3))
print(res)


# 输出：[3, 6, 9]

# 如果三个列表长度不一样怎么办，前面已经说了，对于短的那个iterable参数会用None填补
def dd(x, y, z):
    return x, y, z


list1 = [1, 2, 3]
list2 = [1, 2, 3, 4]
list3 = [1, 2, 3, 4, 5]
res = list(map(dd, list1, list2, list3))
print(res)

# 输出：
# [(1, 1, 1), (2, 2, 2), (3, 3, 3), (None, 4, 4), (None, None, 5)]
