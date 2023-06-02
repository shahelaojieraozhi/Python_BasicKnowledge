''''''
# 1. 利用封装和继承的特性完成如下操作：
# 	小学生：
# 		属性： 姓名 学号 年龄 性别
# 		行为： 学习 打架
# 	中学生：
# 		属性： 姓名 学号 年龄 性别
# 		行为： 学习 谈恋爱
# 	大学生：
# 		属性： 姓名 学号 年龄 性别
# 		行为： 学习 打游戏
# 	调用：
# 		创建小学生对象
# 			调用学习的方法
# 				打印内容为： xx 学习的内容为：语文 数学 英语
# 		创建中学生对象
# 			调用学习的方法
# 				打印内容为：xx 学习的内容为：语数外 生物化 史地政
# 		创建大学生对象
# 			调用学习的方法：
# 				打印内容为： 逃课中...
'''
class Student:
    def __init__(self, name, sno, age, sex):
        self.name = name
        self.sno = sno
        self.age = age
        self.sex = sex

    def study(self):
        print('学习')

# 小学生
class Pupil(Student):
    def __init__(self, name, sno, age, sex):
        super().__init__(name, sno, age, sex)
        
    def study(self):
        print('小学生 学习的内容为：语文 数学 英语')

    def fight(self):
        print('打架')

# 中学生
class Middle(Student):
    def __init__(self, name, sno, age, sex):
        super().__init__(name, sno, age, sex)

    def study(self):
        print('中学生 学习的内容为：语数外 生物化 史地政')

    def love(self):
        print('谈恋爱')

# 大学生
class University(Student):
    def __init__(self, name, sno, age, sex):
        super().__init__(name, sno, age, sex)

    def study(self):
        print('逃课中...')

    def game(self):
        print('打游戏')
'''

# 2.主人杨夫人 向客人 李小姐介绍自己家的宠物狗和宠物猫
# 		宠物狗：
# 			昵称是：贝贝
# 			年龄是：2
# 			性别：雌
# 			才艺: 会两条腿行走的才艺
# 		宠物猫
# 			昵称是：花花
# 			年龄是 1
# 			性别是：雄
# 			才艺: 会装死的才艺
'''
class Pet:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def skill(self):
        print('技能')

class Dog(Pet):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
    
    def skill(self):
        print('会两条腿行走的才艺')


class Cat(Pet):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

    def skill(self):
        print('会装死的才艺')
'''

# 3.
# 	学生类：姓名、年龄、学号、成绩
# 	班级类：班级名称、学生列表
# 		显示所有学生(方法)
# 		根据学号查找学生(方法)
# 		添加一个学生(方法)
# 		删除一个学生（学生对象、学号）(方法)
# 		根据学号升序排序(方法)
# 		根据成绩降序排序(方法)

'''
# 提示:
#     class Student:
#         def __init__(self):
#             pass
#     class Class:
#         def __init__(self, name, stu_list):
#             self.name = name
#             self.stu_list = stu_list
#
#     c = Class('三年一班', [stu1, stu2, stu3, stu4, stu5])
'''
# 调用
from grade import Class
from students import Student

# 创建学生
stu1 = Student('张三', 30, 1001, 60)
stu2 = Student('李四', 40, 1004, 80)
stu3 = Student('王五', 50, 1003, 70)
stu4 = Student('赵六', 60, 1002, 90)
stu5 = Student('孙七', 70, 1005, 50)

# 创建班级
cls = Class('终极一班', [stu1, stu2, stu3, stu4, stu5])
cls.show_stu()
cls.find_stu(1003)
print()

# cls.add_stu(Student('周八', 80, 1006, 100))
# cls.del_stu(1003)
# cls.sort_by_sno()
cls.sort_by_score()
# cls.show_stu()
print(cls.stu_list)