import configparser

config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")
# 获取所有的节点
sec = sections_show = config.sections()

# 获取指定的options项
opt = config.options("db_config")

# 获取指定section下指定的option的值
opt_value = config.get('db_config', 'db_name')

# 获取指定section所使用的配置信息
# for item in config.items('db_config'):
# 	print(item)     # 元组
config.items('db_config').index('')
print(config.items('db_config'))




