
# 成员运算符
#   in, not in
print(1 in [1, 2, 3])  # True
print(1 not in [1, 2, 3])  # False

# 判断某个月是否是31天
month = 5
print(month in [1, 3, 5, 7, 8, 10, 12])


# 身份运算符: 了解
#   is, is not
#  判断内存地址是否相同
x = 10
y = 10

# id() : 查看内存地址, 掌握
print(id(x))  # 140711225054528
print(id(y))  # 140711225054528

print(x is y)  # True
print(x is not y)  # False


