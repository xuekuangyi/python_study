class SuperClass_01:
	def super_method_01(self):
		print("父类01方法01")
	def super_method_02(self):
		print("父类01方法02")
	def __super_private(self):
		print("父类01的私有方法")

class SuperClass_02:
	def super_method_01(self):
		print("父类02方法01")
	def super_method_02(self):
		print("父类02方法02")
	def __super_private(self):
		print("父类02的私有方法")


class ChildClass(SuperClass_01, SuperClass_02):
	# 重写父类方法——覆盖
	def super_method_01(self):
		print("重写父类方法01")

	def super_method_02(self):
		# 沿用父类中的方法
		super().super_method_01()
		super().super_method_02()
		# 扩展子类的方法
		print("子类方法中02的扩展部分")
	# 只能重写，父类中私有方法并不能继承
	def __super_private(self):
		super()._SuperClass__super_private()