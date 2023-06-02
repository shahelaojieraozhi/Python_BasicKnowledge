
# 	学生类：姓名、年龄、学号、成绩
class Student:
    def __init__(self, name, age, sno, score):
        self.name = name
        self.age = age
        self.sno = sno
        self.score = score

    def __repr__(self):
        return f'({self.name}, {self.age}, {self.sno}, {self.score})'
