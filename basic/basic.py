"""该模块用于演示Python的基本数据类型和字符串操作。"""

str1 = "Hello World"
str2 = 'Py' 'thon'
print(str1, type(str1))
print(str2, type(str2))

num1 = 100
num2 = 3.14
num3 = 2e3
print(num1, type(num1))
print(num2, type(num2))
print(num3, type(num3))

real = True
print(real, type(real))

str3 = 'I\'m a great coder!'
str4 = "英文双引号是\"，中文双引号是“"
print(str3)
print(str4)

# 长字符串
str5 = 'It took me six months to write this Python tutorial. \
    Please give me more support. \
    I will keep it updated.'
str6 = '''
It took me 6 months to write this Python tutorial.
Please give me a to 'thumb' to keep it updated.
The Python tutorial is available at http://c.biancheng.net/python/.
'''
print(str5)
print(str6)

# 显示原始字符串
str7 = r'D:\Program Files\Python 3.8\python.exe'
print(str7)

# 格式化字符串
age = 10
name = "C语言中文网"
url = "https://c.biancheng.net/"
print("%s已经%d岁了,它的网址是%s。" % (name, age, url))

# format()
username = "alan"
score = 17.125
print("Hello, {0}, 成绩提升了 {1:.2f}%".format(username, score))

# f-string
rad = 2.5
area = 3.14 * rad ** 2
print(f"The area of a circle with radius {rad} is {area: .2f}")

# 数字分隔符
click = 1_301_547
print("Python教程阅读量：", click)

# 复数 complex
c1 = 12 + 0.2j
c2 = 6 - 1.2j
print(c2, type(c2))
print(c1, type(c1))
# 对复数进行简单计算
print("c1+c2: ", c1 + c2)
print("c1*c2: ", c1 * c2) 
