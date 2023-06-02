
class User:
    def __init__(self, age):
        self.__age = age

    def fn(self):
        return self.__age + 10

    @property  # 作用是让方法属性化: 可以让原来调用方法的方式变成调用属性
    def age(self):
        return self.__age + 10

    @age.setter
    def age(self, new_age):
        self.__age = new_age


user = User(10)
print(user.fn())
print(user.age)

user.age = 100
print(user.age)

