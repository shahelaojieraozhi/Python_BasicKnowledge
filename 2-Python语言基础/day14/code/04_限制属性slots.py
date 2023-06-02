
class Pig:
    # 限制属性： 限制可以使用那些属性名
    __slots__ = ['name', 'age', 'sex']

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


p = Pig('猪猪侠', 8, '公')


