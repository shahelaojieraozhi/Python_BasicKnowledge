
class Dog:

    # 魔法方法/魔术方法
    # 初始化方法: 构造方法/构造函数, 在对象创建时会自动被调用
    def __init__(self, name):
        self.name = name
        print('__init__')

    # 析构函数: 析构方法 , 在对象销毁时会被自动调用
    def __del__(self):
        print('__del__')


d = Dog('柴犬')
# 引用计数 1
# d2 = d  # 引用计数 2
# d = 1  # 引用计数 1
# d2 = 2 # 引用计数 0

# print(d.name)  # getter
# d.name = 'shib'  # setter
# print(d.name)

del d
print('Doge')

