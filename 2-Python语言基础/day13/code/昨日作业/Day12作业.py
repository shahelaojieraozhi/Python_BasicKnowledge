''''''

''' 基础题 '''
# 利用面向对象的思想写下面的程序：直接赋值
# 1.小美在朝阳公园溜旺财【注：旺财是狗】
class Person1:
    def __init__(self, name):
        self.name = name

    def walk_dog(self, place, dog):
        print(f'{self.name}在{place}溜{dog}')


xm = Person1('小美')
xm.walk_dog("朝阳公园", '旺财')


# 2.小明穿着白色的特步运动鞋在奥林匹克公园跑步
class Person2:
    def __init__(self, name, shoes):
        self.name = name
        self.shoes = shoes

    def run(self, place):
        print(f'{self.name}穿着{self.shoes.color}的{self.shoes.brand}运动鞋在{place}跑步')

class Shoes:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

s = Shoes('白色', '特步')
p = Person2('小明', s)
p.run("奥林匹克公园")

# 3.赵老师在讲台上讲课，小刚认真的听课做笔记
class Teacher:
    def __init__(self, name):
        self.name = name
    def teach(self):
        print(f'{self.name}在讲台上讲课')

class Student:
    def __init__(self, name):
        self.name = name
    def listen(self):
        print(f'{self.name}认真的听课做笔记')

# 4.张阿姨和李阿姨在物美超市买红富士
# 提示: 写一个阿姨类,创建2个阿姨对象
class Aunt:
    def __init__(self, name):
        self.name = name
    def buy(self):
        print(f'{self.name}在物美超市买红富士')

Aunt('张阿姨').buy()
Aunt('李阿姨').buy()


''' 进阶题 '''
# 1.李晓在家里开party，向朋友介绍家中的黄色的宠物狗【彩彩】具有两条腿走路的特异功能。
class Person11:
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog

    def party(self):
        print(f'{self.name}在家里开party，向朋友介绍家中的{self.dog.color}的宠物狗【{self.dog.name}】{self.dog.function()}。')

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def function(self):
        return '具有两条腿走路的特异功能'

d = Dog('彩彩', '黄色')

p = Person11('李晓', d)
p.party()


# 2.王梅家的荷兰宠物猪【笨笨】跑丢了，她哭着贴寻猪启示。
class Person22:
    def __init__(self, name, pig):
        self.name = name
        self.pig = pig
    def find_pig(self):
        print(f'{self.name}家的{self.pig.place}宠物猪【{self.pig.name}】跑丢了，她哭着贴寻猪启示。')

class Pig:
    def __init__(self, name, place):
        self.name = name
        self.place = place

p = Pig('笨笨', '荷兰')
wang = Person22('王梅', p)
wang.find_pig()


# 3.富二代张三向女朋友李四介绍自己的新跑车：白色的宾利
class Rich2:
    def __init__(self, name, car, girlfriend):
        self.name = name
        self.car = car
        self.girlfriend = girlfriend

    def introduce(self):
        print(f'富二代{self.name}向女朋友{self.girlfriend}介绍自己的新跑车：{self.car.color}的{self.car.brand}')

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

car = Car('白色', '宾利')
rich = Rich2('张三', car, '李四')
rich.introduce()

''' 挑战题 '''
# 使用构造函数的方式写下面的程序
# 1.定义一“圆”（Circle）类，圆心为“点”Point类，构造一圆，求圆的周长和面积，并判断某点与圆的关系
# 圆Circle:
#   属性: 半径,圆心(Point对象)
#   方法: 周长,面积
#
# 点Point:
#   属性: x,y
from math import pi, sqrt

class Circle:
    def __init__(self, r, center):
        self.r = r
        self.center = center
    def c(self):
        print(f'周长: {2 * pi * self.r}')
    def s(self):
        print(f'面积: {pi * self.r * self.r}')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 点和圆的关系
    def relation(self, circle):
        # 计算点到圆心的距离
        dis = sqrt((self.x - circle.center.x)**2 + (self.y - circle.center.y)**2)

        if dis == circle.r:
            print('点在圆上')
        elif dis > circle.r:
            print('点在圆外')
        else:
            print('点在圆内')

c = Circle(4, Point(3, 4))
c.c()
c.s()

p = Point(6, 8)
p.relation(c)

