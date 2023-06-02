
class Pig:
    def __init__(self, name, age, sex):
        self.name = name
        # 私有属性:
        #   1.在属性名前加两个下划线则是私有属性
        #   2.私有属性只能在当前类的内部使用
        self.__age = age
        self.sex = sex  # 公有属性

    # 成员方法: 对象方法
    def get_age(self):
        print('age:', self.__age)
        self.__eat()
        return self.__age + 10

    # 私有方法
    def __eat(self):
        print('喜欢吃白菜')

peiqi = Pig('佩奇', 3, '女')
print(peiqi.name)
# print(peiqi.__age)  # 报错,私有属性不可以在类外部使用
print(peiqi.sex)

# 间接使用
print(peiqi.get_age())

# peiqi.__eat()  # 报错, 不可以在类外部调用私有方法


# 不推荐这么写
# print(peiqi._Pig__age)
# peiqi._Pig__eat()

