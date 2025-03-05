# 匿名函数
ls = map(lambda x: x * x, [1, 2, 3, 4])
print(list(ls))


def f(x):
    return x * x


ls2 = map(f, [1, 2, 3, 4])
print(list(ls2))

# 使用匿名函数，返回奇数
ls3 = list(filter(lambda n: n % 2, range(1, 20)))
print(ls3)

