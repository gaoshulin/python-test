# student 类
class Student(object):
    def __init__(self, name, age, score=0):
        self.name = name
        self.age = age
        self.__score = score

    def get_name(self):
        print(self.name)

    def get_age(self):
        if self.age > 18:
            print("adult")
        else:
            print("minor")

    # 设置私有变量的值
    def set_score(self, score):
        self.__score = score

    # 获取私有变量的值
    def get_score(self):
        print(self.__score)


bart1 = Student("alan", 10, 60)
bart2 = Student("galen", 20, 80)

bart1.get_name()
bart2.get_name()

bart1.get_age()
bart2.get_age()

bart1.get_score()
bart2.set_score(99)
bart2.get_score()

