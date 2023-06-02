
# 逻辑运算符
#   and 且/与, or 或, not 非

# and :
#   2边都为True则为True, 有1边为False则为False
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
print()

# or :
#   2边都为False则为False, 有1边为True则为True
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
print()

# not
#   取反, 会得到一个bool值
print(not True)  # False
print(not False)  # True
print(not 0)  # True
print(not '')  # True
print(not ' ')  # False
print(not None)  # True
print(not [])  # True
print(not ())  # True
print(not {})  # True

# bool隐式转换 (牢记)
#   数值: 0为假,其他为真
#   字符串: 空字符串('')是假,其他为真
#   None: None就是假
#   list: 空列表([])是假,其他为真
#   tuple: 空元组()是假,其他为真
#   dict: 空字典({})为假,其他为真
print()

# and和or的短路操作

# and:
#   2边都为True则为True, 有1边为False则为False
#   从左往右: 判断每个值是否为False,如果为False则直接返回该值,否则继续判断第二个数...
print(0 and 4)  # 0
print(None and 3 and 5)  # None
print(3 and [] and 6)  # []
print(10 and print(666) and print(888))  # 666   None
print()

# or:
#   2边都为False则为False, 有1边为True则为True
#   从左往右: 判断每个值是否为True,如果为True则直接返回该值,否则继续判断第二个数...
print(0 or 4)  # 4
print(3 or 4)  # 3
print(-2 or print(666) or print(888))
print()

# True => 1
# False => 0
print(int(True))  # 1
print(int(False))  # 0

# 练习
x = 6 and True  # x=True
y = False or 3  # y=3
z = x**2 + x*3 + y
print(x, y)  # True 3
print(z)  # 7





