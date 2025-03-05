# 文件读写 IO

# 打开文件
f = open("./test.txt", "r", encoding="utf-8")
# 获取文件内容
ct = f.read()
print(ct)

# 关闭文件
f.close()


# 读取文件内容，读完自动关闭
with open("./test.txt", "r") as file:
    fs = file.read()
    print('---------')
    print(fs)


# 写入文件内容
with open("./test.txt", "a") as file:
    file.write("Hello world! \r\n")

