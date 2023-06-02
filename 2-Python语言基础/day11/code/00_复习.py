''''''
'''
1. 装饰器
    def outer(fn):
        def inner(*args, **kwargs):
            print('before')
            r = fn(*args, **kwargs)
            print('after')
            return r
        return inner

    @outer
    def fn(a, b):
        return a + b
    
2. 函数递归
    1. 找公式
    2. 找临界值


'''