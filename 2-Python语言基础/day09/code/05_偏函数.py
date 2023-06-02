
# 偏函数: 了解
print(int('110'))
print(int('110', 2))  # 6

# 偏函数
import functools
int2 = functools.partial(int, base=2)

print(int2('110'))  # 6

# def int2(x):
#     return int(x, base=2)


