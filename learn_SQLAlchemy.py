# coding: UTF-8
# Ubuntu
# 安装MySQL：
#   apt-get install mysql-server
#   apt-get install mysql-client
#   apt-get install libmysqlclient15-dev
# 安装python-mysqldb
#   apt-get install python-mysqldb
# 安装SQLAlchemy
#   easy_install SQLAlchemy

from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(String(20), primary_key=True)
	name = Column(String(20))

# mysql+mysqldb://用户名:密码@主机名:端口号/数据库
engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/test')
DBSession = sessionmaker(bind=engine)

session = DBSession()

new_user = User(id='5', name='Bob')
session.add(new_user)
session.commit()
session.close()