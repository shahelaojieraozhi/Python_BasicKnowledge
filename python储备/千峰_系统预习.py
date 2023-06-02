# x = 10,y = 20
# 语句非法

# x,y = 10,20
# print(x,y)

# 2 and 3
# print(2 and 3)

# # -1的索引倒着数第一个
# print(range(10)[-1])

# x = 10
# for x in range(1, 20, 2):
#     x += 2
#     print(x)

# print(chr(ord('a')-32))
#
#
# x = [1,2]
# y = x[:]
# print(y)
#
#
# print([1,2]+[3])
#
# # 列表的操作
# li_1 = [2,3,4]
# li_2 = [4,2,1]
# li_3 = (li_1,li_2)
# li_4 = li_1 + li_2
# print(li_3)
# print(li_4)
#
# x=[1,2,3]
# x[len(x)-1:]=[4,5,6]
# print(x)
#
#
#
# x=[1,2,3]
# a = x[-1]
# x.pop(0)
# print(x)
# print(a)    # 笔记：任意长度的Python列表、元组和字符串中最后-个元素的下标为-1
#
# # 去掉old_list = [1,1,1,3,4 ] 中的重复元素
# old_list = [1,1,1,3,4 ]
# new_list = list(set(old_list))
# print(new_list)



# # 集合
# set = {10,(1,2),'abs'}
# print(set)
# set2 = {10,100,20,100,40}
# print(set2)


# # 将列表转换成集合
# list1 = [1,1,2,2,3,4,2,4]
# set3 = set(list1)
# print(set3)
# # print(set)

# set1 = {1,2,3,4,5,6,}
# set2 = {4,5,6,7,8}
# # 并集
# print('并集为：',set1 | set2)
#
# # 集合1 > 集合2 -判断集合1中是否包含集合2
# set3 = {1,2,5,6,7,8,9}
# set4 = {1,2}
# print(set3 > set4)


#
# print({3:3})
# print(type({3:3}))

# print(y)
# print(y)
#
# print(r'\thabit'[2])

# # 定义阶乘函数
# def factorial(n):
#     sum1 = 1
#     for x in range(1,n+1):
#         sum1 *= x
#     print('%d的阶乘是：%d' % (n,sum1))
#
# factorial(5)

#   #  实参的传值方式：位置参数和关键字参数   两者也可以混用 #####
# def func1(a,b,c):
#     print('a:{},b:{},c:{}'.format(a,b,c))
#
# 位置参数
# func1(10,20,30)
#
# # 关键字参数
# func1(a=100,b=200,c=300)
# func1(c=10,a=11,b=22)
#
# # 混用
# # func1(a=300,100,c=200) #错误
#
# func1(100,c=30000,b=200)


# def func2(a=1,b=2,c=3):
#     print('a:{},b:{},c:{}'.format(a,b,c))
#
# func2()
# # 位置参数
# func2(10)
# func2(10,20)
# func2(b=200)


# 不定长参数
'''
    申明函数的时候可以通过不定长参数来让当前函数可以接受不定个数的实参，python中不定长参数有两种：
    1、声明函数的时候在参数名前加*，这个参数就会变成一个元组，元组的元素就是对应的多个实参
    note：
        a.调用的时候只能使用位置参数
        b.不定长参数后面如果有其他的定长参数，那么他后面的其他参数必须使用关键字参数传参
    2.声明函数的时候在参数名前加**，这个参数就会变成字典，字典中的元素——>关键字：实参值
    note：
        a.调用的时候只能使用关键字参数
        b。*和**同时使用时这个函数参数个数不确定，可以同时使用位置参数和关键字参数
'''


# # 写一个函数，求多个数的和
# def rz_sum(*x):
#     sum1 = 0
#     for num in x:
#         sum1 += num
#     print('x:',x,'和',sum1)
# # 声明函数的时候在参数名前加*，这个参数就会变成一个元组
# rz_sum()
# rz_sum(10)
# rz_sum(10,20)
# rz_sum(4,5,6,7,8)
#
# # 输出：
# # x: () 和 0
# # x: (10,) 和 10
# # x: (10, 20) 和 30
# # x: (4, 5, 6, 7, 8) 和 30


# # 声明一个函数，获取学生信息
# def get_student_info(**info):
#     print(info)
#
# # 声明函数的时候在参数名前加**，这个参数就会变成字典，字典中的元素——>关键字：实参值
# get_student_info(name='张三', age = 18)
# get_student_info(stu_name='小明',age=20,sex='女')
# # 输出：
# # {'name': '张三', 'age': 18}
# # {'stu_name': '小明', 'age': 20, 'sex': '女'}


# # 返回值 return
# def func1(x,y):
#     print('第一个函数：',x,y)
#
# def func2(x,y):
#     print('第二个函数：',x,y)
#     if x > y:
#         return x - y
#
# def func3(x,y):
#     print('第三个函数：',x,y)
#     return x - y
#
# result1 = func1(10,20)
# print('result1:',result1)
#
# result2 = func2(20,10)
# print('result2:',result2)
#
# result3 = func2(20,10)
# print('result3:',result3)
#
# result4 = func3(10,20)
# print('result4:',result4)
#
# # 输出：
# # 第一个函数： 10 20
# # result1: None
# # 第二个函数： 20 10
# # result2: 10
# # 第二个函数： 20 10
# # result3: 10
# # 第三个函数： 10 20
# # result4: -10


# 博客收藏——python基础
# class Computer:
#     screen = True
#
#     def start(self):
#         print('电脑正在开机中……')
#
#
# my_computer = Computer()  # 实例化类
# print(my_computer.screen)  # 打印类中的属性值
# my_computer.start()  # 启动类中的方法

# True
# 电脑正在开机中……


# # self总结，self就是实例化类的意思，传参时可以忽略。
# class Chinese:
#     name = '小张'  # 类属性name
#
#     def say(self, someone):  # 带有两个参数的方法
#         print(someone + '是中国人')
#
#
# person = Chinese()
# print(person.name)
# person.say('小张')
# # 小张
# # 小张是中国人

# # 报错
# class Chinese:
#     name = '小张'  # 类属性name
#
#     def say(self):  # 带有两个参数的方法
#         print(name + '是中国人')
#
#
# person = Chinese()
# print(person.name)
# person.say()

# 小总结：类的属性调用前面加self.属性名就可以了。self在类中就是Chinese()，我们完全可以把全部的self写成Chinese()，
# 有的人类的名字很长，写代码时很不有好所以出现了self，带代替的他的存在，传参时也不会传给他。

# 如果类里面有两个方法（函数）这么办？我们下一个方法（函数）要调用上一个方法（函数）这么调用
# class Chinese:
#
#     def greeting(self):
#         print('很高兴遇见你')
#
#     def say(self):
#         self.greeting()
#         print('我来自中国')
#
#
# # 创建实例person
# person = Chinese()
# # 调用say()方法
# person.say()
#
# # 很高兴遇见你
# # 我来自中国

# 综上，所以我们说self代表的是类的实例本身，方便数据的流转。对此，我们需要记住两点：
# 第一点：只要在类中用def创建方法时，就必须把第一个参数位置留给 self，并在调用方法时忽略它（不用给self传参）。
# 第二点：当在类的方法内部想调用类属性或其他方法时，就要采用self.属性名或self.方法名的格式。

# 类的初始化
# class Chinese:
#
#     def __init__(self):
#         print('很高兴遇见你，我是初始化方法')
#
#
# person = Chinese()

# 初始化方法的作用在于：实例对象创建时，该方法内的代码无须调用就会自动运行。
# 因为他是初始化，只要类的实例化创建出来就会自动运行，好比方说，你打开电脑，
# 他会自动加载C盘上的系统文件，直到你打开电脑桌面为止，剩下的才是你操作的内容，
# 前面打开电脑的过程都叫做类的初始化，自动运行了。

# 这时候有同学问，那我再初始化写一些代码赋值给函数，能调用吗？
# 在初始化中所有代码都是可以调用的，同理，在前面加一个self看下面的例子
# class Chinese:
#     def __init__(self):
#         self.mouth = 1  # self.不能丢
#         self.eye = 2
#
#     def body(self):
#         print('我有%s张嘴巴' % self.mouth)
#         print('我有%s只眼睛' % self.eye)
#
#
# person = Chinese()
# person.body()
# 我有1张嘴巴
# 我有2只眼睛

# 举例说明：
# class Person:
#     # 构建对象后 给对象特征进行初始化的
#     # 不同对象的特征值不一样 所以 name ,age, height 这些形参来接受特征值
#     '''人类'''
#
#     def __init__(self, name, age, height):
#         # self 那个对象来调用方法 self就是那个对象
#         self.name = name
#         self.age = age
#         self.height = height
#
#     def run(self):
#         '''跑步'''
#         print(f'{self.name}在跑步')
#
#     def eat(self):
#         '''吃东西'''
#         print(f'{self.name}在吃饭')
#
#
# # 输入三个参数
# p1 = Person('小明', 18, 1.75)
# # 使用person里的run 方法（函数）
# p1.run()
#
# p2 = Person('小红', 17, 1.65)
# p2.eat()
# 小明在跑步
# 小红在吃饭

# #类中的初始化
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get__gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ('男', '女'):
            self.__gender = gender
        else:
            self.__gender = '男'


p = Person('菜菜', '女')
# print(p.__gender)
print(p.get__gender())

p.set_gender('不男')
print(p.get__gender())

