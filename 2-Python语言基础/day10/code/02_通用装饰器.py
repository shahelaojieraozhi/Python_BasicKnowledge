
# 参数

# 通用装饰器
def outer(fn):
    def inner(*args, **kwargs):
        print('-- before --')
        r = fn(*args, **kwargs)
        print('-- after --')

        print('r:', r)
        return r

    return inner

@outer
def sleep(name, t, age, sex):
    print(f'{name}在{t}点睡觉, {age}, {sex}')
    return 100

# @outer
# def sleep2(name):
#     print(name, '睡觉2')

# print(sleep.__name__)  # inner
result = sleep('罗志祥', 3, age=42, sex='男')  # inner()
print("result:", result)

# print(sleep2.__name__)
# sleep2('鹿晗')  # inner('鹿晗')


# 同时添加多个装饰器
def outer1(fn):
    def inner():
        print('-- before1 --')
        fn()
        print('-- after1 --')
    return inner

def outer2(fn):
    def inner():
        print('-- before2 --')
        fn()
        print('-- after2 --')
    return inner

@outer1
@outer2
def eat():
    print('吃津味源了')


eat()







