
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__():
    #   1. 必须返回一个字符串
    #   2. 作用是让打印对象的时候，输出的是str函数的返回值
    # def __str__(self):
    #     return f'姓名:{self.name},年龄:{self.age}'

    # __repr__():
    def __repr__(self):
        return f'姓名2:{self.name},年龄2:{self.age}'


p = Person('周杰伦', 42)
print(p)

p1 = Person('周杰伦1', 42)
p2 = Person('周杰伦2', 42)
l = [p1, p2]
print(l)








