''''''

'''

1. 函数定义, 函数声明
    def fn(a, b):
        print(a, b)
        return a + b

2. 函数调用
    fn(1, 2)
    print(fn(3, 4))
    r = fn(4, 5)
    print(r)

3. 函数参数
    形参: 在函数定义时括号中的参数
    实参: 在函数调用时括号中的参数

    位置参数/必需参数
    默认参数
    关键字参数
    不定长参数: *args, **kwargs

4. 返回值
    return 

5. 匿名函数
    lambda

6. 回调函数

7. 参数传递

'''

# *args, **kwargs
def fn(*args):
    print(args)

# fn()

l = [2, 3, 4]
fn(l)
fn(*l)  # *l会将列表展开, fn(2,3,4)


def fn2(**kwargs):
    print(kwargs)

# fn2()
fn2(name='李四')
d = {'name': '老王', 'age': 40}
fn2(**d)  # **d 将字典展开  fn2(name='老王', age=40)


