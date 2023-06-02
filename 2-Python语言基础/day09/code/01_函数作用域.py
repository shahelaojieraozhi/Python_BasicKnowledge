
# 作用域: 起作用的范围

if True:
    x = 10
print(x)

for i in range(1):
    y = 20
print(y)

# if,for,while没有作用域

# 函数: 有作用域
b = 20  # 全局变量
def fn():
    a = 10  # 局部变量
    print('a:', a)
    print('b:', b)
fn()
# fn()
# fn()
# fn()
# print('a2:', a)  # 报错
print('b2:', b)

# 局部变量
# 全局变量

# 内建作用域: Built-in
# 全局作用域: Global
# 函数作用域: Enclosing 闭包
# 局部作用域: Local

c = 1  # 全局作用域: Global
def fn2():
    d = 2  # 函数作用域: Enclosing 闭包

    def fn3():
        e = 3  # 局部作用域: Local

# print(max)  # 内建作用域: Built-in
print()

# global
# nonlocal

# global关键字
f = 100

def fn3():
    global f  # 声明使用的是全局变量f
    # f = 200
    f = f + 1
    print(f)  # 101

fn3()
print('f2:', f)  # 101

# nonlocal关键字
g = 1
def fn4():
    g = 2

    def fn5():
        # g = 3
        # global g  # 这里使用的g=1
        # nonlocal g  # 这里使用的g=2
        # g = g + 3
        print('g:', g)
    fn5()

    # print('locals: ', locals())  # 所有局部变量

fn4()
print('g2:', g)


# print(globals())  # 所有全局变量

