# 递归函数
def fact(n):
    if n == 1:
        return 1

    print('%d x %d = ' % (n, n - 1), n * (n - 1))
    return n * fact(n - 1)


print(fact(5))


# 递归实现汉诺塔的移动
def move(n, a, b, c):
    if n == 1:
        global cnt
        cnt += 1
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


cnt = 0
move(6, 'A', 'B', 'C')
print('count: %d' % cnt)
