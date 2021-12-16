class Furniture:
	def __init__(self, name, area):
		self.name = name
		self.f_area = area
	def __str__(self):
		return f"[{self.name}] 占地{self.f_area}平方米"


class House:
	def __init__(self, house_type, area):
		self.house_type = house_type
		self.area = area
		self.rest_area = area
		self.furniture_list = []

	def add_furniture(self, *furnitures: Furniture):
		# 拆解入参元组（新加入的家具）
		for furniture in furnitures:
			# 错误写法：self.furniture_list = self.furniture_list.append(furniture)
			self.rest_area -= furniture.f_area
			self.furniture_list.append(furniture)
			# print(furniture.f_area)
		# 以循环，将房屋总面积减去各家具面积减去
		# for list_item in self.furniture_list:
		# 	# print(list_item.f_area)
		# 	self.rest_area -= list_item.f_area
	def __str__(self):
		return (f'户型：{self.house_type}\n'
		        f'总面积：{self.area}, 剩余面积{self.rest_area}\n'
		        f'家具列表：{self.furniture_list}')


my_house = House('开间', 100)
desk = Furniture('桌子', 5)
bed = Furniture('床', 8)
chair = Furniture('椅子', 2)
my_house.add_furniture(desk, bed, chair)
print(my_house)
print(desk)
