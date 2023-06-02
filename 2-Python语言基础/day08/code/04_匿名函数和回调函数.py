
# 匿名函数 : 没有名字的函数
#   lambda  λ

# 普通函数
def f(n):
    return n*2

# 匿名函数
f2 = lambda n: n*2

print(f(10))
print(f2(20))

# 多个参数
f3 = lambda a, b: a+b
# def f3(a, b):
#   return a + b
print(f3(3, 4))

print()


# 回调函数: 难
def A(x, f):  # f = lambda n: n**2
    print('x:', x)
    r = f(x)
    print('r:', r)

# 调用
A(10, lambda n: n*2)

print()


def B(x, f):  # f = C
    print('x:', x)
    r = f(x+1)  # 相当于调用C()
    print('r:', r)  # 121

# 回调函数
def C(n):
    print('我是C函数, n:', n)
    return n**2

# def D(n):
#     print('我是D函数, n:', n)
#     return n**3

# 调用
B(10, C)
# B(5, D)

# C 既是函数名, 也是指向该函数的一个变量
# a = C
# C()  # '我是C函数'
# a()  # '我是C函数'


# sort(key)
stu_list = [
    {'name': '刘一', 'age': 18, 'score': 8, 'tel': 18866669999, 'sex': '男'},
    {'name': '陈二', 'age': 13, 'score': 88, 'tel': 17777778888, 'sex': '不明'},
    {'name': '张三', 'age': 9, 'score': 99, 'tel': 18866669999, 'sex': '不明'},
    {'name': '李四', 'age': 20, 'score': 77, 'tel': 16666667778, 'sex': '不明'},
    {'name': '王五', 'age': 80, 'score': 55, 'tel': 18866669999, 'sex': '女'},
    {'name': '赵六', 'age': 60, 'score': 99, 'tel': 18866669999, 'sex': '不明'},
]

# 使用匿名函数
# stu_list.sort(key=lambda n: n['age'])
# 使用普通函数
def fn(n):
    return n['age']
stu_list.sort(key=fn)

# 打印
for stu in stu_list:
    print(stu)

print()
# max中key
m = min(stu_list, key=lambda stu: stu['age'])
print(m)


