
# 函数参数
# 1.位置参数,必需参数
def f1(a, b, c):
    print(a, b, c)

f1(1, 2, 3)


# 2. 默认参数: 存在于形参中
def f2(a, b, c=5):
    print(a, b, c)

f2(1, 2)  # 1 2 5
f2(1, 2, 3)  # 1 2 3


# 3.关键字参数: 存在于实参中
def f3(a, b, c=5, d=6):
    print(a, b, c, d)

f3(3, 4)  # 3 4 5 6
# f3(a=3, b=4)  # 3 4 5 6
# f3(b=4, a=3)  # 3 4 5 6
# f3(3, 4, 55)  # 3 4 55 6
# f3(3, 4, 55, 66)  # 3 4 55 66
f3(3, 4,  d=66)  # 3 4 5 66


# 4.可变长参数,不定长参数
# *args   : arguments参数
# **kwargs  : keyword arguments 关键字参数

# *args : 可以接收任意多个位置参数,得到的是一个元组
def f4(*args):
    print(args)

f4(1, 2, 3, 4)  # args=(1, 2, 3, 4)
f4(1, 2)  # args=(1, 2)

# **kwargs : 可以接收任意多个关键字参数,得到的是一个字典
def f5(**kwargs):
    print(kwargs)

f5(a=1, b=2)  # kwargs={'a': 1, 'b': 2}


# 形参参数顺序: 位置参数, *args,   默认参数, **kwargs
# 实参参数顺序: 位置参数,          关键字参数

def fn(a, b, *args,   e=5, f=6, **kwargs):
    print(a, b, args, e, f, kwargs)

fn(1, 2, 3, 4, 5, 6, 7,  e=8,  g=9, h=10)


# 通用参数的写法
def fn2(*args, **kwargs):
    print(args, kwargs)


# *
# **


