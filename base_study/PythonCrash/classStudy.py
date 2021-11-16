class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year}{self.make}{self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"此辆车已经开了{self.odometer_reading}公里了")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print('不允许向后调整里程表')

	def increment_odometer(self, miles):
		self.odometer_reading = miles + self.odometer_reading


class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make)
	# super().__init__(self.make, self.model, self.year)
	# print('这是一辆电动车')


# print(ElectricCar('特斯拉', 'model_s', 2019).get_descriptive_name())


class A:
	def to_show_A_itself(self, args):
		print('A类中的方法')
		# def inner_method(argss):
		# 	to_return_args = argss + 1
		# 	return to_return_args

		# self.private_args = args + 1
		# private_args = args + 2
		# print('A中的方法')
		# print(args)
		# print(self.private_args)
		# print(private_args)

class B(A):
	print ('B类')
	# def to_show_B_itself(self, args):
	# 	print('B中的方法')
	# 	super().to_show_A_itself(args)




b = B()
b.to_show_A_itself(1)
print("-"*20)
# b.to_show_B_itself(1)
