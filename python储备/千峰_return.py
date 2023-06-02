# print()只是控制台上显示的输出，但是return返回出来的才是函数的值
def add(a, b):
    result = a + b
    print(result)
    return 'aaa', 100, 345


x = add(2, 3)
# 5
print(x)
# ('aaa', 100, 345)
# 如果return返回的是多个，则输出是个元组

# 接受的时候也可以是多个：
x, y, z = add(2, 3)
print(x)
print(y)
print(z)
# aaa
# 100
# 345

