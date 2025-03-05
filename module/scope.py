# 作用域

# private函数
def _private_1(name):
    return 'hello, %s' % name


# private函数
def _private_2(name):
    return 'hi, %s' % name


# public
def greeting(name):
    if len(name) > 3:
        str2 = _private_1(name)
    else:
        str2 = _private_2(name)

    return str2


print(greeting('tom'))
print(greeting('galen'))
