''''''

''' 简答题 '''
# 1， Python中的循环有几种:
# while   for

# 2， Python的数据类型有哪些:
# int float bool str NoneType  list tuple dict set bytes

# 3， Python中空类型特殊值是:
#  None

# 4， 判断下列赋值方式正确与否（True or False）
'''
    x = y = z = 1           =>  True
    x=1, y=2                =>  False
    x, *y, z = 1,2,3,4      =>  True
    x, y, z = (1,2,3)       =>  True
'''
x, *y, z = 1,2,3,4,5,6,7
print(y)  # [2, 3, 4, 5, 6]

# 5, 列举至少5种常用的内置函数,并解释函数的作用：
# sorted()
# sum()
# max()
# min()
# print()

# 6，判断下面变量名不正确的有哪些：
# ABC, aBC, a-bc, a_bc， _num123, 123num, NUM123, num_123，
# True, false, true1, false0， print, id, __id__, python
# 不正确的:  a-bc  123num  True

# 7，列举列表list中的至少6个函数，且说明每个函数对应的作用
# append(), insert()  extend()
# pop()  remove()  clear()
# sort()  reverse()
# copy()
# index()  count()

# 8，列举字典dict中的至少3个函数，且说明每个函数对应的作用
#  get()  pop()  popitem()  update()  clear()
#  keys()   values()  items()
#  copy()


''' 编程题 '''
# 1， 将列表中元素去重, 使用至少2种方式
# 方式1:
l = [3, 3, 3, 3, 4, 4, 4, 2, 1, 2, 2, 2, 3, 4, 5]
print(list(set(l)))

# 方式2:
l = [3, 3, 3, 3, 4, 4, 4, 2, 1, 2, 2, 2, 3, 4, 5]
l2 = []
for n in l:
    if n not in l2:
        l2.append(n)
print(l2)

# 2、编写一个函数gcd(x,y) 求最大公约数，编写一个函数lcm(x,y)求最小公倍数。
# 最大公约数
def gcd(x, y):
    for n in range(min(x,y), 0, -1):
        if x%n==0 and y%n==0:
            return n

print(gcd(8, 12))

# 最小公倍数
def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(6, 8))


# 3、使用Python编程实现下面图形打印,n行：
'''
    *
   **
  ***
 ****
*****
'''
n = 8
for i in range(1, n+1):
    print( ('*' * i).rjust(n) )


# 4、使用Python编程实现下面图形打印,n行：
'''
    *
   ***
  *****
 *******
********* 
'''
n = 5
for i in range(1, n+1):
    print( ('*' * (2*i-1)).center(2*n-1) )

'''          i    *    规律
    *        1    1    2i-1
   ***       2    3    2i-1
  *****      3    5    2i-1
 *******     4    7    2i-1
*********    5    9    2i-1
 *******     6    7    2(2n-i)-1
  *****      7    5    2(2n-i)-1
   ***       8    3    2(2n-i)-1
    *        9    1    2(2n-i)-1
'''
n = 8
for i in range(1, 2*n):
    if i <= n:
        print( ('*' * (2*i-1)).center(2*n-1) )
    else:
        print( ('*' * (2*(2*n-i)-1)).center(2*n-1) )

# 5，将字典的key和value置换，
# 如使用字典: d1 = {'a':1,'b':2,'c':3}，
# 置换后生成字典: d2 = {1:'a', 2:'b', 3:'c'}
d1 = {'a': 1,'b': 2,'c': 3}

d2 = {v: k for k,v in d1.items()}
print(d2)

d2 = {}
for k, v in d1.items():
    d2[v] = k
print(d2)

# 6、使用Python写一个按照下面方式调用都能正常工作的 my_sum() 方法
'''
    print(my_sum(2,3))     输出 5
    print(my_sum(2)(3))    输出 5
'''
# 提示:
#   通过参数数量判断不同的情况
#   1.有1个参数, 嵌套函数
#   2.有2个参数, 返回和
def my_sum(*args):
    if len(args) >= 2:
        return sum(args)
    else:
        def inner(n):
            return n + args[0]
        return inner

print(my_sum(2,3))
print(my_sum(2)(3))

# 7， 封装函数，传入不定数量的数值型参数，返回所有数字的乘积,
# 提示: *args
def fn7(*args):
    s = 1
    for n in args:
        s *= n
    return s

# 8， 封装一个函数random_color，该函数的返回值为随机十六进制颜色。
# 说明： 十六进制颜色#开头后面接6个十六进制数， 例: #FFFFFF， #000000， #0033CC
# 提示: colors = '0123456789ABCDEF'
#      random模块
import random
def random_color():
    colors = '0123456789ABCDEF'
    s = '#'
    for i in range(6):
        s += random.choice(colors)
    return s

print(random_color())

#  #940FD3
#   94 表示红色 R  red  0~255
#   0F 表示绿色 G  green 0~255
#   D3 表示蓝色 B  blue  0~255


# 9， 封装函数，
# 第一个函数create_persons()，
#   创建并返回包含5个字典(例如:{"name":"xx","age":xx, "faceValue":100})的列表
#      其中name的值：从["张三","李四","王五","赵六","钱七"]依次取
#      其中age的值：10-100之间的随机整数
#      其中faceValue的值：0-100之间的随机整数
# 第二个函数get_old(), 传入第一个函数创建的列表, 找出列表中年龄最大的人，并将其所有信息打印
# 第三个函数sort_facevalue(), 传入第一个函数创建的列表, 根据颜值升序排列，并打印排序后的信息

def create_persons():
    l = []
    name_list = ["张三", "李四", "王五", "赵六", "钱七"]
    for name in name_list:
        age = random.randint(10, 15)
        face_value = random.randint(0, 100)
        d = {"name": name, "age": age, "faceValue": face_value}
        l.append(d)

    # 打印
    for d in l:
        print(d)

    return l

def get_old(persons):
    old = max(persons, key=lambda d: d['age'])['age']
    print('old:', old)

    # for d in persons:
    #     if d['age'] == old:
    #         print(d)
    print( [d for d in persons if d['age']==old] )

def sort_facevalue(persons):
    persons.sort(key=lambda d: d['faceValue'])
    print(persons)

# 调用
persons = create_persons()
get_old(persons)
sort_facevalue(persons)






