class Private:

	def __private(self):
		print(f'这是私有方法')


private_var = Private();
# _类名__属性或方法()
var = private_var._Private__private()
