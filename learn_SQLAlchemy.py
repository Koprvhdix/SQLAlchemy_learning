# coding=utf-8
# Ubuntu
# 安装MySQL：
#   apt-get install mysql-server
#   apt-get install mysql-client
#   apt-get install libmysqlclient15-dev
# 安装python-mysqldb
#   apt-get install python-mysqldb
# 安装SQLAlchemy
#   easy_install SQLAlchemy

from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class user_list(Base):
	__tablename__ = 'user'

	user_id = Column(String(20), primary_key=True)
	user_name = Column(String(20))


class special_user_list(Base):
	__tablename__ = 'special_user'

	# ForeignKey must be in front of primary_key
	special_user_id = Column(String(20), ForeignKey('user.user_id'), primary_key=True)

# 创建所有表格
def create_All(engine):
    Base.metadata.create_all(engine)

# 删除所有表格
def drop_All(engine):
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
	# mysql+mysqldb://用户名:密码@主机名:端口号/数据库
	engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/test')
	DBSession = sessionmaker(bind=engine)

	session = DBSession()

	drop_All(engine)

	create_All(engine)

	new_user = User(id='5', name='Bob')
	session.add(new_user)
	session.commit()
	session.close()