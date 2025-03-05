# list
classmates = ['Galen', 'Alan', 'Sam']

print(classmates)
print('len:', len(classmates))
print('index-0: %s, index-1: %s' % (classmates[0], classmates[1]))

# 追加元素
classmates.append('Newton')
print(classmates)

# 指定位置插入元素
classmates.insert(3, 'Jacky')
print(classmates)

# 替换元素
classmates[3] = 'Jack'
classmates[4] = ['Ross', 'Alice']
print(classmates)

# 删除指定位置的元素 - 默认删除最后一位
classmates.pop(3)
print(classmates)

# 切片
print('=============')
print(classmates[0:4])
print(classmates[:3])
print(classmates[2:])
print(classmates[-1])
print(classmates[:4:2])
