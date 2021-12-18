from sqlalchemy import create_engine, orm, text
import sqlalchemy
from sqlalchemy import orm, text
import configparser


# print(sqlalchemy.__version__)

def read_config():
	cf = configparser.ConfigParser()
	cf.read('config.ini')
	return cf


def get_engine():
	cf = read_config()
	# 初始化数据库连接:
	engine = create_engine(cf.get('db_config', 'sqlalchemy_config'))
	Session = orm.sessionmaker(engine)
	return engine, Session


# 调用engine.connect()方法获得Connect对象
def hello_world():
	engine = get_engine()
	with engine.connect() as conn:
		result = conn.execute(sqlalchemy.text("select * from goods"))
		print(result.all())

def table_init_by_conn():
	engine = get_engine()[0]
	with engine.connect() as conn:
		# 建表
		conn.execute(text("CREATE TABLE persons ("
		                  "uid int,"
		                  "user_name varchar(255)"
		                  ")"
		                  )
		             )
		# 插数据
		conn.execute(
			text("INSERT INTO persons (uid, user_name) VALUES (:uid, :user_name)"),
			[{"uid": 1000, "user_name": '张三'}, {"uid": 1001, "user_name": '李四'}]
		)
		conn.commit()


# session方案
def tabel_init_by_session():
	Session = get_engine()[1]
	
	with Session() as sess:
		# 建表
		sess.execute(text("CREATE TABLE user ("
		                  "uid int,"
		                  "user_name varchar(255)"
		                  ")"
		                  )
		             )
		# 插数据
		sess.execute(
			text("INSERT INTO user (uid, user_name) VALUES (:uid, :user_name)"),
			[{"uid": 1000, "user_name": '张三'}, {"uid": 1001, "user_name": '李四'}]
		)
		sess.commit()


def dml_test():
	engine = get_engine()[0]
	with engine.connect() as conn:
		result = conn.execute(sqlalchemy.text(
			f"select * from user"))
		
		for row in result:
			print(type(row))
			print(f"uid:{row.uid} username:{row.user_name}")

def main():
	dml_test()
	
if __name__ == '__main__':
    main()