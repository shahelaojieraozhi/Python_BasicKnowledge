# **题目：**学习使用auto定义变量的用法。
#
# **程序分析：**python中的变量作用域。
i = 0
n = 0


def dummy():
    i = 0
    print(i)
    i += 1
# 每次用到这个函数时，i=0 （函数会优先使用局部变量）


def dummy2():
    global n
    print(n)
    n += 1


print('函数内部的同名变量')
for j in range(20):
    print(i)
    dummy()     # dummy里面i = i+1不起作用
    i += 1
print('global声明同名变量')
for k in range(20):
    print(n)
    dummy2()
    n += 10
