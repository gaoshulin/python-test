# 操作文件和目录 IO
import os

print(os.name)
print(os.getcwd())
print(os.path.abspath('.'))
# 获取环境变量
print(os.environ.get('PATH'))
# 两个路径合成一个
print(os.path.join('../file', 'test-dir'))


# ## 操作文件和目录 ## #

# 创建一个目录:
os.mkdir("./test-dir")

# 删除一个目录
os.rmdir("./test-dir")

# 对文件重命名
os.rename('./test.txt', "test2.txt")

# 删除文件
os.remove('./test2.txt')

# 拆分路径
ss = os.path.split('/Applications/project/python/test/file/io.py')
print(ss)

# 获取文件扩展名
s2 = os.path.splitext('/Applications/project/python/test/file/io.py')
print(s2)
