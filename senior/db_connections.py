
import pymysql
import configparser

def read_config(config_file = 'D:\python\CoreERP\src\core\config.ini', opt='db_config'):
	cf = configparser.ConfigParser()
	cf.read(config_file)

	db_host = cf.get(opt, 'db_host')
	db_user = cf.get(opt, 'db_user')
	db_passwd = cf.get(opt, 'db_passwd')
	db_port = cf.getint(opt, 'db_port')
	db_database = cf.get(opt, 'db_database')
	select_limit = cf.get(opt, 'select_limit')

	return db_host, db_user, db_passwd, db_port, db_database, select_limit


# sql_s = f"select * from po_details"


# sql_s = f"select * from po_details limit " \
# 	"{read_config('config.ini', 'db_config', key='db_host')}"
#
# sql_i = f"insert into po_details(unique_id, goods_no, quantity) " \
# 	       f"values('{str(main_functions.id_generator('uuid1')).replace('-','')}','{12345}','{100}')"


def db_operation(sql):

	# 配置文件方式开始
	# 参数已经在read_config()方法中给所默认值
	config = read_config()
	db_conn = pymysql.connect(host=config[0],
	                          user=config[1],
	                          password=config[2],
	                          port=config[3],
	                          database=config[4],
	                          )

	# 创建游标
	cursor = db_conn.cursor()   # cursor=pymysql.cursors.DictCursor

	# 游标的.execute()方法执行脚本，并使用元组对待绑定内容赋值，pymysql本身就可过滤非法的脚本字符串内容，防止SQL注入
	cursor.execute(sql)
	db_conn.commit()

	result = cursor.fetchall()
	return result
	# print(result)

	# 关闭游标和数据库
	cursor.close()
	db_conn.close()
