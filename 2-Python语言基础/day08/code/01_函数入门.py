
# 函数:
#   作用: 封装一个具有特定功能的代码

# 数学中的函数:
#    f(x) = 2x + 1

# Python中函数:
#   def f(x):
#       return 2*x + 1

# 1.函数定义
def f():
    print('这是f函数')

# 2.函数调用: 可以重复调用
f()
f()
f()


# 参数
# 求任意2个数的和
# 参数:
#   形参: 形式参数, x,y, 函数定义时括号中的变量
#   实参: 实际参数, 10,20, 函数调用时括号中的变量或值
def sum(x, y):
    s = x + y
    print(s)

sum(10, 20)
sum(3, 4)

print('*' * 100)

# 返回值
#   return:
#       1.存在于函数中, 作用是返回结果(可以是1个或多个)
#       2.会立刻终止函数, 后面的代码不再执行
#       3.如果没有return或return后没有值,则默认返回None
def sum2(x, y):
    s = x + y
    return s
    # return 100, 200
    # print('我永远都不会执行')

# 调用
r = sum2(10, 20)
print('r:', r)
print(sum2(30, 40))

# f(x) = 2*(x+y) - 3

# print(print(print(1)))

# 练习
# 封装一个函数: is_leap(year) 判断传入的年份是否为闰年, 返回True或False
def is_leap(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

def is_leap2(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    return False

def is_leap3(year):
    return year%4==0 and year%100!=0 or year%400==0


