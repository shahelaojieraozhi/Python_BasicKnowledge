''''''
'''
1. 函数的作用域
    内建作用域 
    全局作用域
    函数作用域
    局部作用域
    
    全局变量
    局部变量
    
    global
    nonlocal
    
2. 函数闭包
    函数嵌套
    函数闭包
        def outer():
            x = 10
            def inner():
                pass
            return inner
    
3. 函数名也是变量(指向该函数的变量)
def sum(a, b):
    print(a + b)

s = sum
s(1, 2)

# 回调函数
def fn(f):
    f(100)

def a(n):
    print(n**2)

fn(a)

4.列表推导式
    l = [i for i in range(10)]
    d = {i:i for i in range(10)}
    s = {i for i in range(10)}
    g = (i for i in range(10))

5. 生成器和生成器函数
    g = (i for i in range(10))
    
    # next()
    # for-in
    
    def fn():
        print("A")
        yield 100

6.迭代器和可迭代对象
    type()
    isinstance()
    
    迭代器: 生成器, iter()
    可迭代对象: list,str,dict,set,tuple.

7.偏函数:了解
8.栈和队列: 
    栈: 先进后出
    队列: 先进先出

'''

# 生成器函数
def fn():
    print("A")
    yield 100

g = fn()
a = next(g)
print(a)
