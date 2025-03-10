"""
python ORM框架-SQLAlchemy

@author: Galen
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import yaml

# 读取配置文件
env = {}
config_file = '../env/env.yaml'
with open(config_file, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
    env = config.get('mysql', {}) 

# 创建数据库引擎，这里使用 pymysql 作为驱动
engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s" % (env['user'], env['password'], env['host'], env['port'], env['database']))

# 创建一个基类，用于定义数据库模型
Base = declarative_base()


# 定义一个 User 模型
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# 创建数据库表
# Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = Session()


# 新增数据
def add_user(name, age):
    user = User(name=name, age=age)
    session.add(user)
    session.commit()


# 查询数据 - 全部
def get_user():
    users = session.query(User).order_by(User.id.desc()).limit(10).all()
    return users


# 更新数据
def update_user(user_id, name, age):
    # 根据 ID 查询用户
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        user.age = age
        session.commit() 


# 删除数据
def delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()


# 1.新增数据   
# add_user('jack', 25)     

# 2.更新数据
# update_user(1, 'john', 30)

# 3.删除数据
# delete_user(1)

# 4.查询数据
users = get_user()    
for user in users:
    print(f"ID: {user.id}, 姓名: {user.name}, 年龄: {user.age}")


# 关闭会话
session.close()