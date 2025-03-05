import json

d = dict(name='Bob', age=20, score=88)

# dumps() 方法返回一个str，内容就是标准的JSON
d1 = json.dumps(d)
print(d1)

# loads() 方法把JSON反序列化为Python对象
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
d2 = json.loads(json_str)
print(d2)


# dump() 方法可以直接把JSON写入一个文件
with open('./json.txt', 'w', encoding='utf-8') as file:
    json.dump(d, file)


# load() 方法读取文件中的 JSON内容
with open('./json.txt', 'r', encoding='utf-8') as file:
    d3 = json.load(file)
    print(d3)


# JSON进阶, 把 class 类序列化为 json 对象
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Alan', 18, 86)
print(json.dumps(s, default=lambda obj: obj.__dict__))


obj = dict(name='小明', age=20)
ss = json.dumps(obj, ensure_ascii=True)
print(ss)
