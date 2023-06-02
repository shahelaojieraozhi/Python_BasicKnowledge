
# 面向对象的特征:
#   封装: 类将属性和方法封装起来了
#   继承: 子类可以继承父类的属性和方法
#   多态
#   抽象

# 继承
# 父类
class Ipad(object):
    def __init__(self, color):
        self.color = color

    def play_lol(self):
        print('玩英雄联盟')

    def play_kingofhonour(self):
        print('玩王者荣耀')


# 子类
class Iphone(Ipad):
    def __init__(self, color, price):
        # 这里需要调用父类的init方法: 借用父类的init对color进行初始化
        super().__init__(color)  # 隐式调用
        # Ipad.__init__(self, color)  # 显式调用

        self.price = price

    def call(self):
        print('打电话')


iphone12 = Iphone('骚红色', 5000)
print(iphone12.color, iphone12.price)
iphone12.play_lol()
iphone12.call()


