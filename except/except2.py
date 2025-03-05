from functools import reduce


def str2num(s):
    try:
        # 尝试将字符串转换为整数
        return int(s)
    except ValueError:
        # 如果转换为整数失败，尝试转换为浮点数
        return float(s)


def calc(exp):
    # 分割字符串并去除每个元素的首尾空格
    ss = [s.strip() for s in exp.split('+')]
    # 将每个元素转换为数字
    ns = map(str2num, ss)

    # 使用 reduce 函数求和
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()

