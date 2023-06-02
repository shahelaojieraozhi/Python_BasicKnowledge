
class Person:
    age = 10
    def __init__(self, name):
        self.name = name
        print('init:', id(self))
        sex = '男'

    def eat(self):
        print('吃饭:', id(self), self.name, self.age)

    # self:
    #   1.self不是关键字,但是建议写成self
    #   2.不要给self传值,内部会自动去赋值一个对象
    #   3.self是指向当前类的对象: 哪个对象调用了方法,则该方法中的self就是这个对象
    #   4.self的作用是: 用来调用类中的其他属性和方法

p1 = Person('胡歌')
print('p1:', id(p1))
p1.eat()
print()

p2 = Person('霍建华')
print('p2:', id(p2))
p2.eat()