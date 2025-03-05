# 去除字符串首尾的空格
def trim(s):
    tmp_str = s
    if not tmp_str:
        return ''

    # 处理字符串开头的 空格
    first_char = tmp_str[:1]
    if first_char.isspace():
        # 第一个字符是 空格
        tmp_str = trim(tmp_str[1:])

    # 判断去除开头的字符串之后是否为空
    if not tmp_str:
        return ''

    # 处理字符串结尾的 空格
    last_char = tmp_str[-1]
    if last_char.isspace():
        # 最后一个字符是 空格
        tmp_str = trim(tmp_str[:-1])

    # 返回最终的字符串
    return tmp_str


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')
