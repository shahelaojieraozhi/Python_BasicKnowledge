
# 迭代器 Iterator
# 可迭代对象 Iterable
from collections.abc import Iterator,Iterable

# type(): 查看数据类型
print(type(1))  # <class 'int'>

# isinstance(): 判断是否属于某个类(或多个类中的其中一个)的对象
print(isinstance(1, int))  # True
print(isinstance(1, (int, float, str, list)))  # True

# if isinstance(1, int):
#     pass

# 可迭代对象: 可以使用for-in循环的
#       有: list, tuple, str, dict, set, generator
print(isinstance(1, Iterable))  # False
print(isinstance(True, Iterable))  # False
print(isinstance(None, Iterable))  # False

print(isinstance([], Iterable))  # True
print(isinstance((), Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance({1}, Iterable))  # True
print(isinstance("abc", Iterable))  # True

# 迭代器: 可以使用for-in循环的,且可以用next调用
#   有: generator
print(isinstance(1, Iterator))  # False
print(isinstance(True, Iterator))  # False
print(isinstance(None, Iterator))  # False
print(isinstance([], Iterator))  # False
print(isinstance((), Iterator))  # False
print(isinstance({}, Iterator))  # False
print(isinstance({1}, Iterator))  # False
print(isinstance("abc", Iterator))  # False

# iter() : 可迭代对象 => 迭代器
print(isinstance(iter("abc"), Iterator))  # True

# next("abc")  # 报错
# g = iter("abc")
# print( next(g) )
# print( next(g) )
# print( next(g) )


