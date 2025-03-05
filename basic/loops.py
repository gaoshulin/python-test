# for 循环
names = ["galen", "emma", "james"]
for name in names:
    print(name)

# 循环 dict
languages = {"name": "php", "site": "https://www.php.net", "age": 18}
for index, value in languages.items():
    print("%s: %s" % (index, value))

# 循环 0-10
lists = []
for index in range(10):
    lists.append(index)
print('循环[0-10]: ', lists)

# while
num = sums = 0
while num <= 10:
    sums += num
    num = num + 1
print("0-10累加: ", sums)

# break
n = 1
ns = []
while n <= 10:
    if n > 5:
        # break语句会结束当前循环
        break
    ns.append(n)
    n = n + 1
print('END: ', ns)

# continue
m = 0
ms = []
while m < 10:
    m = m + 1
    if m % 2 == 0:
        # continue语句会直接继续下一轮循环，后续的print()语句不会执行
        continue
    ms.append(m)
print('END: ', ms)

# 循环生成列表
ls = [x * x for x in range(1, 10)]
print(ls)

# 两层嵌套生成列表
ls2 = [m + n for m in 'ABC' for n in 'XYZ']
print(ls2)

# 修改列表生成式，通过添加if语句保证列表生成式能正确地执行
# 使用内建的 isinstance 函数可以判断一个变量是不是字符串
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

