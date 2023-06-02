
# 3大结构
#   顺序结构
#   分支结构
#   循环结构

# if 如果

# 单分支
sex = input('请输入你的性别:')
if sex == '男':
    print('鹿晗')
    print('蔡徐坤')

print('end')

# 双分支
if sex == '男':
    print('鹿晗')
else:
    print('关晓彤')

print('end')

# 多分支
if sex == '男':
    print('鹿晗')
elif sex == '女':
    print('关晓彤')
else:
    print('东方不败')


# if嵌套
# 1.x 为 0-99 取一个数, y 为 0-199 取一个数,
#   如果 x>y 则输出 x的值，
#   如果 x 等于 y 则输出 x+y的值，
#   否则输出y的值
import random
x = random.randint(0, 99)
y = random.randint(0, 199)
print(x, y)

if x > y:
    print(x)
elif x == y:
    print(x + y)
else:
    print(y)

if x >= y:
    if x > y:
        print(x)
    else:
        print(x + y)
else:
    print(y)


# 输入2个数, 得到较大的数
a = int(input('a:'))
b = int(input('b:'))

# 方法1
if a > b:
    print(a)
else:
    print(b)

# 方法2:
c = a if a>b else b
print(c)

# 其他语言: 三目运算符  ? :
# c = a>b ? a : b
