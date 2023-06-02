# 带参装饰器: 难
def dec(n):

    def outer(fn):
        def inner():
            print('before', n)
            fn()
            print('after', n)
        return inner

    return outer

@ dec(8)  # 相当于 @ outer
# dec(8) => outer
def dance():
    print('跳舞')


dance()



