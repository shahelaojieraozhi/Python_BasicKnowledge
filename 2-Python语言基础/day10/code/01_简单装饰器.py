
# 装饰器
#   作用: 给原本存在的函数额外增加新功能,但是不改变原函数的功能

def eat():
    print('吃饭')

def eat2():
    print('唱歌')
    eat()

#
def run1():
    print('张三跑步')
def run2():
    print('李四跑步')

def run(fn):
    print('先唱歌')
    fn()
    print('再跳舞')

run(run1)
run(run2)
print()


# Python 装饰器
def outer(fn):  # fn = 原swim2

    def inner():
        print('先唱歌')
        fn()  # 原swim2
        print('再跳舞')
    return inner

def swim1():
    print('张三 游泳')
def swim2():
    print('李四 游泳')

# 装饰器原理
# swim1 = outer(swim1)
# swim1()  # inner()

swim2 = outer(swim2)
swim2()
print(swim2.__name__)  # inner函数

# 练习
# 3.写一个装饰器来统计函数运行的时间
import time

# outer:装饰器函数
def outer(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print("消耗时间:", end-start)
    return inner

@outer  # 相当于 sing = outer(sing)
def sing():
    time.sleep(1)

# sing = outer(sing)
sing()


# 练习: 使用装饰器,给函数set_age控制: 传入的n范围是1-100之间,如果超出范围则传入-1
def outer2(fn):
    def inner(n):
        if 1 <= n <= 100:
            fn(n)
        else:
            fn(-1)

    return inner

@outer2
def set_age(n):
    print(n)

set_age(400)

