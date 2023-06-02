

class User:
    sex = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        pass

    # 运算符重载：了解
    def __add__(self, other):
        return f'{self.name}和{other.name}的年龄是：{self.age},{other.age}'

user = User('库克', 60)
# print(User.__name__)  # 类名
# print(__name__)  # '__main__'

print(user.__dict__)  # {'name': '库克', 'age': 60}
# print(User.__dict__)

# print(user.__class__)  # <class '__main__.User'>
# print(User.__class__)

# print(user.__module__)  # '__main__'
# print(User.__bases__)  # 所有父类、基类


# 运算符重载
user1 = User('强东', 40)
user2 = User('奶茶妹妹', 26)

print(user1 + user2)

