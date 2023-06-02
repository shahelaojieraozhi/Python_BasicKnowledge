
# 异常: 写的时候不报错，运行就可能报错
# 错误: 写的时候就出错，运行一定出错的情况

# 异常处理:
#   1.使用try-except捕获异常，不会让程序报错。
#   2.作用是让程序不报错

try:
    a = 1/1
except:
    print('报错了')


# 重点掌握
try:
    a = 1/0
except Exception as e:
    print('出错了')
    print(e, type(e))
    # division by zero <class 'ZeroDivisionError'>

# try:
#     a = 1/0
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# except NameError as e:
#     print('NameError:', e)

# try-except-finally
try:
    a = 1/0
except:
    print('出错了')
finally:
    print('不管是否报错，finally一定会执行')

# try-except-else
try:
    a = 1/0
except:
    print('出错了')
else:
    print('没报错')


# 抛出异常：主动报错
# raise
# raise NameError('哈哈哈，报错了')

# 常见的异常
#   NameError  变量名未定义
#   TypeError   数据类型错误
#   IndexError   下标越界
#   ZeroDivisionError   除0错误
#   FileExistsError   文件已经存在
#   FileNotFoundError   文件不存在
#   ImportError   导入错误
#   ModuleNotFoundError   模块没有找到
#   AttributeError   属性名错误
#   KeyError   字典的key出错
#   SyntaxError  语法错误


# 自定义异常, 一般和raise结合使用
class MyException(Exception):
    def __init__(self, name, url):
        self.name = name
        self.url = url

# raise MyException('hello', 'baidu')


# 断言: assert, 了解
def fn(n):
    # 认定n不等于0，如果和我认定的不一致，则抛出错误
    assert n!=0, "报错了，n不能为0"

    print(1/n)

fn(0)
# AssertionError: 报错了，n不能为0








