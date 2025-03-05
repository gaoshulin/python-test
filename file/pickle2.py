import pickle

# 序列化
d = dict(name='Bob', age=20, score=88)
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

# 反序列化
with open('dump.txt', 'rb') as f2:
    d2 = pickle.load(f2)
    print(d2)
