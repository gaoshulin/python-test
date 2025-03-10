"""
pymysql 库操作 mysql 数据库

@author: Galen
"""
import pymysql
import yaml

# 读取配置文件
env_conf = {}
config_file = '../env/env.yaml'
with open(config_file, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
    env_conf = config.get('mysql', {})    

# 连接数据库
conn = pymysql.connect(
    host=env_conf.get('host'),
    port=env_conf.get('port'),
    user=env_conf.get('user'),
    password=env_conf.get('password'),
    database=env_conf.get('database')
)    

# 获取游标, 字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


try:
    # 1.查询数据
    sql = "SELECT * FROM users ORDER BY id DESC LIMIT 10"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

    # 2.插入数据    
    sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
    val = ("james", 36)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.lastrowid, "record inserted.")

    # 3.更新数据
    sql = "UPDATE users SET age = %s WHERE name = %s"
    params = ("35", "james")
    cursor.execute(sql, params)
    conn.commit()
    print(cursor.rowcount, "record updated.")

    # 4.删除数据
    sql = "DELETE FROM users WHERE name = %s"
    params = ("james",)
    cursor.execute(sql, params)
    conn.commit()
    print(cursor.rowcount, "record deleted.")

except pymysql.MySQLError as e:
    print(f"数据库操作失败: {e}")
    conn.rollback()
finally:
    cursor.close()
    conn.close()
