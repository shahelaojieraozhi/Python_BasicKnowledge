
# abs既是函数名,也是指向该函数的变量
def abs(n):
    if n < 0:
        return -n
    return n

# print( abs(-100) )

f = abs
print( f(-100) )
# print(id(f), id(abs))


# 回调函数
def fn(x, f):  # f = b
    print('x:', x)
    f(10)


def a(n):
    print(n ** 2)
def b(n):
    print(n ** 3)


fn(10, b)
print()

# 闭包
# 需要在函数嵌套的情况下
def f1(x):
    print('f1 x:', x)

    def f2(y):
        print('f2 y:', y)

    return f2

# r = f1()  # r = f2
# r()  # 相当于 f2()

f1(3)(4)


# 全局变量: 1.不会被释放, 2.可能会在其他方被修改
c = 10
def fn1():
    global c
    c += 1
    print('c:', c)

fn1()

# 局部变量: 1.使用完后就会被释放, 2.不会被函数外的其他地方修改
def fn2():
    d = 20
fn2()
# print(d)

# 闭包 Enclose: 在函数嵌套的情况下,且返回内部函数,则外部函数的参数或变量不会被释放
def outer():
    x = 10
    def inner():
        # print('inner')
        nonlocal x
        x += 1
        print('x:', x)

    return inner


f = outer()
f()  # 11
f()  # 12
f()  # 13

# print(f.__name__)  # inner
# f2 = f
# print(f2.__name__)  # inner


# 形参也相当于局部变量
# def f3(y=10):
#     print('y:', y)
#
# f3()
# print(y)

