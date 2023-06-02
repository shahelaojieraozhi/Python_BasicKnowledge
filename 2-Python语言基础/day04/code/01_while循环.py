
# while循环
# while: 当
# 语法:
#   循环初始值
#   while 循环条件:
#       循环体(代码)
#       循环改变量

# 从1循环到100, 将1+2+3+...+100
s = 0
i = 1

while i <= 100:
    # print(i, end=' ')
    s += i  # s = s + i
    i = i + 1

print()
print('i:', i)  # i: 101
print('s:', s)  # s: 5050

# 第1次循环, 循环前: i=1,s=0; 判断i<=100是否成立; 循环后: i=2,s=1
# 第2次循环, 循环前: i=2,s=1; 判断i<=100是否成立; 循环后: i=3,s=1+2
# 第3次循环, 循环前: i=3,s=1+2; 判断i<=100是否成立; 循环后: i=4,s=1+2+3
# 第4次循环, 循环前: i=4,s=1+2+3; 判断i<=100是否成立; 循环后: i=5,s=1+2+3+4
# ...
# 第99次循环, 循环前: i=99,s=1+2+3+..+98; 判断i<=100是否成立; 循环后: i=100,s=1+2+3+...+98+99
# 第100次循环, 循环前: i=100,s=1+2+3+..+99; 判断i<=100是否成立; 循环后: i=101,s=1+2+3+...+98+99+100
# 第101次循环, 循环前: i=101,s=1+2+3+..+100; 判断i<=100是否成立; 不成立,退出循环.
# s = 1+2+3+..+100
# i = 101


# 死循环: 循环不会结束
# 一般会结合: input(), time.sleep(1), break
'''
import time
while True:
    n = input('请输入您的年龄:')
    print(n)
    # time.sleep(2)  # 暂停2秒

print('end')
'''


# 练习
# 1.求1-100之间可以被7整除的数的个数
s = 0
count = 0

i = 1
while i <= 100:
    if i%7 == 0:
        # print(i, end=' ')
        s += i  # 求和
        count += 1  # 求次数
    i += 1

print('s:', s)
print('count:', count)

# 2.计算从1到100以内所有奇数的和。
s = 0
i = 1
while i <= 100:
    # if i%2:
    #     # print(i, end=' ')
    #     s += i
    # i += 1
    s += i
    i += 2

print('s:', s)

# 3.计算从1到100以内所有能被3或者17整除的数的和。
import time
start = time.time()  # 当前时间

s = 0
i = 1
while i <= 100:
    if i%3==0 or i%17==0:
        s += i
    i += 1

print('s:', s)
stop = time.time()  # 当前时间

print('时间消耗:', stop-start)

# 4.计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数。
count = 0
i = 1
while i <= 100:
    if (i%3==0 or i%7==0) and i%21!=0:
        # print(i, end=' ')
        count += 1
    i += 1
print('count:', count)

# 5.计算1到500以内能被7整除但不是偶数的数的个数。
count = 0
i = 1
while i <= 500:
    if i%7==0 and i%2!=0:
        count += 1
    i += 1

print('count:', count)


# 计算n的阶乘, 比如 5! = 1*2*3*4*5
n = 100

s = 1  # 乘积
i = 1
while i <= n:
    # print(i, end=' ')
    s *= i
    i += 1

print('s:', s)



