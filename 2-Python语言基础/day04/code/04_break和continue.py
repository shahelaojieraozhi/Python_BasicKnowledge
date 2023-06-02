
# for循环: 一般用于已知循环次数
# while循环: 一般用于未知循环次数, 死循环

# break:
#   1. 存在于循环中, 立刻终止当前所在的这层循环
#   2. 循环内break之后的代码不执行
#   3. break可以和for-else,while-else结合使用

for i in range(1, 101):
    if i%7 == 0:
        print(i)
        break  # 立刻退出循环
        print('hello')

# for-else
#   1. 需要和break结合使用
#   2. 如果循环过程中执行了break则else不执行,否则会执行else

# 判断某个数是否为 合数或质数(素数)
n = 3777
# 思路: 从 2 到 n-1 范围内,是否有能被n除尽的数
for i in range(2, n):
    if n%i == 0:
        print(n, '是合数')
        break
else:
    print(n, '是质数')

# 方法2
b = True
for i in range(2, n):
    if n%i == 0:
        print(n, '是合数')
        b = False
        break
if b:
    print(n, '是质数')


# continue
#   1.在循环中使用, 终止当次循环,并进入下一次循环
#   2.continue之后的代码不执行

for i in range(1, 11):
    if i%3 == 0:
        continue
        print('ok')
    print(i)

for i in range(1, 11):
    if i%3 == 0:
        pass  # 空语句,占位语句,保证代码完整性,防止报错
    else:
        print(i)

for i in range(1, 11):
    if i%3 != 0:
        print(i)

