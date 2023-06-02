
# 单继承: 只有一个父类
# 多继承: 有多个父类

# 父类
class Father:
    def __init__(self, name):
        self.name = name
    def __smoke(self):  # 私有方法
        print('会抽烟')

class Mother:
    def __init__(self, age):
        self.__age = age  # 私有属性
    def cook(self):
        print('会做饭')
        print(self.__age)

# 子类
class Son(Father, Mother):
    def __init__(self, name, age):
        Father.__init__(self, name)
        Mother.__init__(self, age)
        # super(Son, self).__init__(name)
        # super(Father, self).__init__(age)

    def eat(self):
        print('会吃')
        # print(self.__age)  # 子类不能继承父类的私有属性
        # self.__smoke()  # 子类不能继承父类的私有方法


# 对象
son = Son('小明', 10)
# print(son.name, son.age)
# son.smoke()
son.cook()
son.eat()

print(Son.__mro__)  # 从左往右的一个继承链
# (
#    <class '__main__.Son'>,
#    <class '__main__.Father'>,
#    <class '__main__.Mother'>,
#    <class 'object'>
# )
