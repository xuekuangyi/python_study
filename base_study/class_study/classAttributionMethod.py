
class Tool:
	count = 0   # 定义在__init__之外的属性，类属性

	def __init__(self, name):
		self.name = name
		Tool.count += 1

	@classmethod
	def show_count(cls):
		print(cls.count)

def main():
	tool = Tool('锤子')
	tool_2 = Tool('钳子')
	tool.count = 50 # 其实这个是补加属性的语句，因为tool对象并没有count属性
	print(f'Tool类被实例化了{Tool.count}次')   # 使用类名.属性方式调用
	print(f'tool对象的count属性值为{tool.count}次')   # 使用对象名.属性方式调用
	print(f'{tool_2.count}')
	print(f'tool对象的属性清单{tool.__dir__()}')
	print(f'toos_2对象的属性清单{tool_2.__dir__()}')
	Tool.show_count()


if __name__ == '__main__':
	main()