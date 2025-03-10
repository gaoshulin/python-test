"""
mysql-connector-python 库操作 mysql 数据库

@author: Galen
"""
import mysql.connector
import yaml

# 读取配置文件
env_conf = {}
config_file = '../env/env.yaml'
with open(config_file, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
    env_conf = config.get('mysql', {})

# 判断是否存在mysql配置
if not env_conf:
    # 退出程序
    print("mysql config not found")
    exit()


# 连接数据库
def connet_db():
    try:
        conn = mysql.connector.connect(
            host=env_conf.get("host", "localhost"),
            user=env_conf.get("user", "root"),
            password=env_conf.get("password", ""),
            database=env_conf.get("database", "test"),
            port=env_conf.get("port", 3306),
        )

        return conn
    except mysql.connector.Error as e:
        print(f"mysql connent failed: {e}")   
        exit() 


# 定义全局 conn 和 cursor
conn = connet_db()

# 游标设置为字典类型
cursor = conn.cursor(dictionary=True)


""""
    插入数据                        
    :param name: 姓名
    :param age: 年龄
    :return: 插入数据
"""
def insert_users(name, age):
    sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
    val = (name, age)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "record inserted.")


"""
    查询数据
    :return: 查询数据
"""
def query_users():
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    # 获取所有记录列表
    result = cursor.fetchall()
    for row in result:
        print(row)


"""
    更新数据
    :param name: 姓名
    :param age: 年龄
    :return: 更新数据
"""
def update_users(name, age):
    sql = "UPDATE users SET age = %s WHERE name = %s"
    val = (age, name)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "record updated.")


"""
    删除数据
    :param name: 姓名
    :return: 删除数据
"""
def delete_users(name):
    sql = "DELETE FROM users WHERE name = %s"
    val = (name,)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "record deleted.")


"""
    关闭数据库连接
    :return: 关闭数据库连接
"""
def close_connection():
    cursor.close()
    conn.close()
    print("数据库连接已关闭")


# 1.查询数据
query_users()

# 2.插入数据
# insert_users("galen", 30)    

# 3.更新数据
# update_users("galen", 31)  

# 4.删除数据
# delete_users("galen")

# 关闭连接
close_connection()
 