class Cat:
	pass


# print("猫")


# 为变量增加类型提示
# tom: Cat = Cat()
# 为对象（而不是类）单独增加属性，不建议使用；
# tom.name = 'tom'


def print_attr(cat):
	attrs = dir(cat)
	for attr in attrs:
		print(attr)


# print(print_attr(tom))
#
# print(tom.name)

class Person:
	# print('对象定义/对象实例化') # 类即使没被显式地实例化，但也的确生成了对象，通过此语句可证明

	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		print('__init__()方法被调用，Person类被实例化为一个名为%s的对象' % self.name)

	# 需要打印对象时打印自定义信息，就需要重写__str__方法，务必要字符串型的返回值,替代原有的打印类名及内存地址
	def __str__(self):
		# 必须返回字符串
		return f'我是{self.name},我的体重是{self.weight}'

	def __del__(self):
		print('__del__()方法被调用，%s被销毁' % self.name)

	def eat(self):
		self.weight += 1

	def run(self, times):
		self.weight -= times*0.5

	def eat(self, times):
		self.weight += times*1


zhang = Person("小张", 75)
zhang.run(10)
zhang.eat(6)

print(zhang.weight)
print(zhang)
