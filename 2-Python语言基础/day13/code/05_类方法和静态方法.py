
# 对象方法: 成员方法
# 私有方法
# 类方法
# 静态方法

class Person:
    # 类属性
    name = '莫迪'

    def __init__(self, age):
        self.age = age  # 对象属性

    # 对象方法
    def swim(self):
        print('游泳')

    # 私有方法
    def __fly(self):
        print('飞')

    # 类方法
    #   1.可以使用对象和类来调用,但是建议使用类来调用
    #   2.类方法中没有self,不能调用对象属性,对象方法,私有方法
    #   3.类方法中有cls,可以调用类属性,类方法,静态方法
    @classmethod
    def eat(cls):  # cls : class
        print('吃:', cls == Person)
        # cls.swim()  # 错误写法
        print(cls.name)

    # 静态方法
    #   1.可以使用对象和类来调用,但是建议使用类来调用
    #   2.类方法中没有self,不能调用对象属性,对象方法,私有方法
    #   3.类方法中没有cls,不建议调用类属性,类方法,静态方法
    @staticmethod
    def sleep():
        print('睡觉')


p = Person(80)
p.eat()
Person.eat()

# p.swim()
# Person.swim(p)  # 不要这么写

p.sleep()
Person.sleep()
