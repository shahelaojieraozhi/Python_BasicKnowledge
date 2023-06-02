''''''

''' 基础题 '''
# 1.简述必需参数、关键字参数、默认参数、不定长参数的区别
#   位置参数: 必须按照顺序传参,必须给值,一般写在参数列表的前面
#   关键字参数: 写在实参中, 在参数列表的后面,一般和默认参数搭配使用
#   默认参数: 写在形参中, 在位置参数之后, 给参数默认值,可以不给默认参数传值.
#   不定长参数:
#       *args: 接收任意多个位置参数, 得到一个元组
#       **kwargs: 接收任意多个关键字参数, 得到一个字典

# 2.封装函数，计算传入字符串中单个【数字】、【字母】、【空格] 以及 【其他字符】的个数
def fn2(s='fa34234,,.dfas, fs df sd '):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for c in s:
        if c.isalpha():
            count2 += 1
        elif c.isdigit():
            count1 += 1
        elif c.isspace():
            count3 += 1
        else:
            count4 += 1
    return count1, count2, count3, count4



# 3.封装函数，判断用户传入的参数（字符串、列表、元组其中之一）长度是否大于5, len(x)>5
def fn3(x):
    return len(x)>5


# 4.封装函数，计算1到n的和, 并返回结果打印出来; (n为函数参数)
def fn4(n):
    return sum(range(1, n+1))
print(fn4(100))

# 5.封装函数，计算n的阶乘, 并返回结果打印出来
import math
def fn5(n):
    return math.factorial(n)
print(fn5(10))

# 6.封装函数，传入不定个数的数字，返回所有数字的和, 提示: *args
def fn6(*args):
    return sum( args )

print(fn6(1,2,3,4))

# 7.封装函数，判断一个年份是不是闰年
def fn7(y):
    if y%4==0 and y%100!=0 or y%400==0:
        return True
    return False


''' 进阶题 '''
# 1.写一个函数，识别字符串是否符合python语法的变量名, 返回True或False
#   1.数字字母下划线，且不能以数字开头. 2.不能使用关键字
#
import keyword

def f1(name):
    if not name:
        return False

    if name in keyword.kwlist:
        return False

    if name[0].isdigit():
        return False

    for c in name:
        if c.isalnum() or c=='_':
            pass
        else:
            return False

    return True

print(f1('heladf2'))


# 2.写一个函数计算两个数的最小公倍数; 并返回结果打印出来
def f2(a=9, b=6):
    for i in range(max(a, b), a*b+1):
        if i%a==0 and i%b==0:
            return i
print(f2())


# 3. 年月日分别为自定义函数的参数，判断某一个日期是否为合法的日期;
# 	    如: 2020年12月33日不是合法的日期
# 	        2021年2月29日是不合法的日期

def f3(year, month, day):
    if month<1 or month>12:
        return False

    days = 31
    if month==2:
        if fn7(year):
            days = 29
        else:
            days = 28
    elif month in [4, 6, 9, 11]:
        days = 30

    if day<1 or day>days:
        return False

    return True

# 请写出你对今天授课内容最疑惑的地方(或者有困难的知识点)

