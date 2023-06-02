# **题目：**斐波那契数列。
# 自己的:
def fun12(i):
    if i <= 2:
        return 1
    else:
        return fun12(i-2) + fun12(i-1)
y = int(input('请输入一个整数：'))
print(fun12(y))
# 输入10输出55


# 递归实现
def Fib(n):
    return 1 if n <= 2 else Fib(n-1)+Fib(n-2)
x = int((input('请输入一个整数：')))
print(Fib(x))
# 输入10输出55

# 朴素实现
target=int(input())
res=0
a,b=1,1
for i in range(target-1):
    a,b=b,a+b
print(a)
# 输入10输出55
