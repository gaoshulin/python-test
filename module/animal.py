# 类的继承
class Animal(object):
    def run(self):
        print('Animal is running...')


# Dog 类继承 Animal 类
class Dog(Animal):
    def run(self):
        print('Dog is running...')


# Cat 类继承 Animal 类
class Cat(Animal):
    def run(self):
        print('Cat is running...')


anima = Animal()
anima.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True
print(isinstance(dog, Cat))  # False
print(isinstance(anima, Dog))  # False
