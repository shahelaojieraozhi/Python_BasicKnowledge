
class Cat:
    # 类属性
    name = '毛球'
    age = 1
    likes = ['鱼']

    def __init__(self, name, color):
        # 对象属性
        self.name = name
        self.color = color
        self.likes2 = ['鱼']


# 对象
cat = Cat('咪咪', '白色')

# 得到属性值
'''
print(Cat.age)
print(cat.age)
print(Cat.name)  # '毛球'
print(cat.name)  # '咪咪'
# print(Cat.color)  # 报错, 类.对象属性 会报错
print(cat.color)
'''
# 修改属性值
# Cat.name = '毛球2'
# cat.name = '毛球3'
# print(Cat.name)  # 毛球
# print(cat.name)  # 毛球3

# Cat.age = 2
# cat.age = 3
# print(Cat.age, cat.age)

# 原则: 使用类名调用类属性, 使用对象调用对象属性

# 类属性: 是共享的
#  同一个类的不同对象共享类属性
c1 = Cat('汤姆', '蓝色')
c2 = Cat('加菲', '黄色')

print(c1.likes)  # ['鱼']
print(c2.likes)  # ['鱼']

c1.likes.append('老鼠')
print(c1.likes)  # ['鱼', '老鼠']
print(c2.likes)  # ['鱼', '老鼠']
print()

# 对象属性: 不同对象内存独立
print(c1.likes2)  # ['鱼']
print(c2.likes2)  # ['鱼']

c1.likes2.append('老鼠')
print(c1.likes2)  # ['鱼', '老鼠']
print(c2.likes2)  # ['鱼']



