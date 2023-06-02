
# 列表推导式,列表生成式
list1 = [1, 2, 3]
list1 = list(range(1, 101))

list1 = []
for i in range(1, 6):
    list1.append(i)

# 列表推导式
list2 = [i for i in range(1, 6)]  # [1, 2, 3, 4, 5]
list2 = [i*2 for i in range(1, 6)]  # [2, 4, 6, 8, 10]
list2 = [i**2 for i in range(1, 6)]  # [1, 4, 9, 16, 25]
list2 = [i for i in range(1, 10) if i%2 and i<6]  # [1, 3, 5]
list2 = [i+j for i in "abc" for j in "123"]  # ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
print(list2)

# 练习
# 1~20之间的偶数的立方组成的列表
list3 = [i**3 for i in range(1, 21) if i%2==0]
print(list3)  # [8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]

# 字典生成式
# d = {i: i**2 for i in range(1, 5)}
# print(d)  # {1: 1, 2: 4, 3: 9, 4: 16}

# 集合生成式
# s = {i for i in range(1, 5)}
# print(s)  # {1, 2, 3, 4}


# 生成器: generator
g = (i for i in range(3, 6))
# print(g)  # generator对象

# 使用next
# print(next(g))  # 3
# print(next(g))  # 4
# print(next(g))  # 5
# print(next(g))  # 报错 StopIteration

# 使用for
for i in g:
    print('i:', i)

print()

# 生成器函数
#   yield关键字:
#       1.存在函数中,作用是让普通函数变成生成器函数,生成器函数需要用next或for来调用
#       2.运行过程中碰到yield则会暂停
#       3.yield后面加值,则可以和return一样把该值返回,但是不会终止函数
def ff():
    print(100)
    yield 'AA'

    print(200)
    yield 'BB'

    print(300)
    yield 'CC'

g = ff()
# print('g:', g)  # generator

print('yield:', next(g))
print('yield:', next(g))
print('yield:', next(g))



