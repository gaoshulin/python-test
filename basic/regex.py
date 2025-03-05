import re


# 验证邮箱
def is_valid_email(addr):
    patter = r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
    res = re.match(patter, addr)
    return bool(res)


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
