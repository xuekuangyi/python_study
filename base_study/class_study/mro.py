# mro = method resolution order 方法搜索顺序

class A:
	def method_test(self):
		print("A类方法1")


class B:
	def method_test(self):
		print("B类方法1")


class C(A, B):
	pass


def main():
	cc = C()
	cc.method_test()
	print(C.__mro__)  # mro的顺序是先在当前类/对象中查找，再往父类中找，最后到object类中找，如果还找不到，则报找不到方法的错；


if __name__ == '__main__':
	main()
