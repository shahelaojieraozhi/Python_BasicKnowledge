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
    pass


# 3.赵老师在讲台上讲课，小刚认真的听课做笔记
class Teacher:
    pass

class Student:
    pass

# 4.张阿姨和李阿姨在物美超市买红富士
# 提示: 写一个阿姨类,创建2个阿姨对象



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
        pass


# 3.富二代张三向女朋友李四介绍自己的新跑车：白色的宾利
class Rich2:
    pass


''' 挑战题 '''
# 使用构造函数的方式写下面的程序
# 1.定义一“圆”（Circle）类，圆心为“点”Point类，构造一圆，求圆的周长和面积，并判断某点与圆的关系
# 圆Circle:
#   属性: 半径,圆心(Point对象)
#   方法: 周长,面积
#
# 点Point:
#   属性: x,y

class Circle:
    pass


class Point:
    pass




