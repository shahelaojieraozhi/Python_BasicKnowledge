''''''

# C语言: 面向过程的语言, 没有类, 有结构体
# Python: 面向对象的语言, 一切皆对象

# 面向过程: 一种编程思想, 注重的是解决问题的步骤.
# 面向对象: 一种编程思想, 注重的是解决某个问题中出现的对象.

# 理解面向对象
# 示例： 小狗吃食（闻一闻smell、舔一舔lick、咬一咬bite）
# 	  分别采用面向过程和面向对象来分析
#
# 面向过程:  先闻一闻, 然后再舔一舔, 最后再咬一咬 (注重过程)
# 面向对象:  小狗是一个对象, 它可以闻一闻食物, 可以舔一舔食物, 可以咬一咬食物.      (不注重过程, 注重对象)

# 面向过程
'''
def smell():
    print('闻一闻')

def lick():
    print('舔一舔')

def bite():
    print('咬一咬')

smell()
lick()
bite()
'''


# 面向对象
# 类: 类名一般遵守大驼峰的写法
class Dog:
    name = '旺财'

    def smell(a):
        print(a.name, '闻一闻')

    def lick(self):
        print(self.name, '舔一舔')

    def bite(self):
        print(self.name, '咬一咬')

# 对象: 是由类来创建
dog = Dog()
# dog2 = Dog()
dog.smell()
dog.lick()
dog.bite()


# 人类
# class Person:
#     name = '张三'
#
#     def code(self):
#         print(self.name, '写代码')


# 面向对象
#   一个公司的各个部门可以看做不同的对象
#   一个国家的各个省也可以看做不同的对象


# 类 :  class 一系列事物的统称, 是抽象的,泛指
# 对象 : object 由类创建出来的具体存在的实例

#  电脑 => 类
#  我桌上的这台电脑 => 对象
#  人  => 类
#  男人  => 类
#  你的那个女朋友  => 对象
#  你的初恋  => 对象
#   美国总统拜登  => 对象
#   美国总统  => 类

# 类: 作用是用来创建对象
#   属性: 变量, 表示特征,静态的, 比如:人的年龄,身高,体重等..
#   方法: 函数, 表示功能,动态的, 比如:吃饭,游泳等

# class Person:
# object: Python提供的类, 父类/基类, 根类,超类
class Person(object):
    # 类属性
    # name = '胡歌'
    # age = 39

    # 初始化函数/构造函数
    #   1. 会在创建对象时被自动调用
    #   2. 作用是用来初始化属性
    def __init__(self, name2, age2):
        print('初始化函数__init__被调用了')
        # 对象属性
        self.name = name2
        self.age = age2

    # 方法
    def sing(self):
        print(self.name, '唱歌贼6')

# 对象
p1 = Person('王一博', 24)
print(p1.name)
print(p1.age)
p1.sing()

p1 = Person('狗头萝莉', 18)
print(p1.name)
print(p1.age)
p1.sing()

