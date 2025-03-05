# 函数
from functools import reduce


def f(n):
    return n * n


# map()
r = map(f, [1, 2, 3, 4, 5])
print(list(r))

s = map(str, [1, 2, 3, 4, 5])
print(list(s))


def fn(x, y):
    return x * 10 + y


# reduce()
ss = reduce(fn, [1, 3, 5, 7])
print(ss)


def is_odd(x):
    return x % 2 == 1


# filter()
d = filter(is_odd, [1, 2, 3, 4, 5, 6])
print(list(d))


# sorted()
sl = [36, 5, -12, 9, -21]
print(sorted(sl))
# 反向排序
print(sorted(sl, reverse=True))


L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t


def by_score(t):
    print(t)
    return t[1]


L2 = sorted(L1, key=by_name)
L3 = sorted(L1, key=by_score, reverse=True)
print(L2)
print(L3)
