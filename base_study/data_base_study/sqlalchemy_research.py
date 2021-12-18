import sqlalchemy
import configparser


def read_config():
	cf = configparser.ConfigParser()
	cf.read('config.ini')
	return cf

cf = read_config()
# 初始化数据库连接:
engine = sqlalchemy.create_engine()
engine = sqlalchemy.create_engine(cf.get('db_config', 'sqlalchemy_config'))
# 创建DBSession类型:
DBSession = sqlalchemy.sessionmaker(bind=engine)

# 定义基类
Base = sqlalchemy.ext.declarative.declarative_base()


# 定义User对象,继承基类
class User(Base):
	# 定义表名：
	__tablename__ = 'user'
	
	# 表结构定义:
	id = sqlalchemy.Column(sqlalchemy.String(20), primary_key=True)
	name = sqlalchemy.Column(sqlalchemy.String(20))
