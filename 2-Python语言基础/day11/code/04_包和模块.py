
# 包: package, 包含__init__.py文件的文件夹

# 模块: module, 一个python文件就是一个模块(模块名的名字要符合命名规范)

# 1.如何导入模块和包
# 2.如何安装第三方模块

# 模块
#  1.内置模块,标准模块, 比如: math, random, os, ....
#  2.自定义模块, 自己写的模块
#  3.第三方模块, 第三方提供的,一般需要单独安装

# 针对模块,导入方式:
# 1.使用import
# import random
# import module1
# import math, os, random

# import module1
# import module1
# print(module1.name)

# 2.使用from-import
from random import randint
print(randint(1, 10))

# 模糊导入
from random import *
print(choice([1,2,3]))

from module1 import name
print(name)


# 针对包,导入方式:
# 1. 使用import,  不推荐这样写,使用麻烦
# import package1.module2
# print(package1.module2.age)

# 2. 使用from-import
# from package1 import module2
# print(module2.place)

from package1.module2 import place
print(place)

# 别名: as
# import random as r
# print(r.randint(1, 10))




