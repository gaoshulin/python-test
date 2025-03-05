# dict
scores = {"galen": 98, "alan": 78, "jack": 52}

print(scores)
print('len: ', len(scores))
print(scores['galen'])
print(scores.get('alan', ''))

# 赋值
scores['alan'] = 87
scores['lili'] = 66
print(scores)

# 删除 key
scores.pop('lili')
print(scores)
