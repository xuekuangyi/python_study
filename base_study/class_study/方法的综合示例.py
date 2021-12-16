class Player(object):
	def __init__(self, player_name):
		self.player_name = player_name
	
	def get_player_name(self):
		return self.player_name


class Game(object):
	# 定义类属性
	top_score = 0;
	
	def __init__(self, player):
		self.player_name = player.get_player_name()
	
	# 类方法是类对象的方法不与具体某个对象实例有关，入参必有当前类
	@classmethod
	def show_top_score(cls):
		print(cls.top_score)
	
	# 静态方法不涉及对象属性或类属性，可以无入参
	@staticmethod
	def show_rules():
		print('阻止僵尸进入大门')
	
	# 对象方法与具体实例化的对象有关，入参必有当前对象
	def show_obj_name(self):
		print(f'当前用户的名字是{self.player_name}')


def main():
	Game.show_top_score()   # 类方法
	Game.show_rules()
	
	player = Player('张三')  # 实例化Player
	game = Game(player)     # 实例化Game，传入Player对象

	game.show_obj_name()    # 实例方法

if __name__ == '__main__':
	main()