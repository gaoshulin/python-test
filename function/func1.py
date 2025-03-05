# 函数
def number_calculate(a, b, operator='+'):
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case _:
            print('invalid operator')
            return ''


# 计算乘方
def power(x, n=2):
    return x ** n


# 可变参数
def calc(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


print(number_calculate(10, 20, '*'))
print(power(3, 3))
print(calc(1, 2, 3))
print(person('galen', 30, city='wuhan', job='Engineer'))


# 参数组合 - 计算两个数的乘积
def mul(x, *y):
    s = x
    for n in y:
        s *= n
    return s


# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    print('测试成功!')
