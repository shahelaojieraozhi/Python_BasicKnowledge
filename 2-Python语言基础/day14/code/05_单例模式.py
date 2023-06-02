
# 单例模式：是一种设计模式
#       一个类只创建一个实例。
# 设计模式总共23种：单例模式，工厂模式，装饰器模式，代理模式，适配器模式等等。

class Single:
    # __init__(): 初始化属性时会自动调用
    def __init__(self, name):
        print('__init__')
        self.name = name

    # 类属性: 共享
    instance = None

    # __new__(): 创建对象时会自动调用
    @classmethod
    def __new__(cls, *args, **kwargs):
        print('__new__')

        if cls.instance == None:
            # 借用父类的new方法来创建对象
            cls.instance = super().__new__(cls)
        return cls.instance


s1 = Single('以色列')
s2 = Single('以色列')
s3 = Single('以色列')

print(s1 is s2)  # True
print(s1 is s3)  # True


