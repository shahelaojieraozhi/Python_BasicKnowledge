
class Animal:
    def eat(self):
        print('喜欢吃素')

class Dog(Animal):
    # 重写了父类的eat方法
    def eat(self):
        print('喜欢吃骨头')

class Cat(Animal):
    # 重写
    def eat(self):
        print('喜欢吃鱼')

class Panda(Animal):
    pass

dog = Dog()
dog.eat()

cat = Cat()
cat.eat()