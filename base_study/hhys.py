a = input(f'请输入a:')
b = input(f'请输入b:')
info='''
提示
1:乘法
2：加法
5：退出
'''
while True:
	print(info)
	if isinstance(a,(int, float)) and isinstance(b,(int,float)):
		choice = int(input(f'请输入你的选择：'))
		if choice == 1:
			print(f'a*b=',a * b)
		elif choice == 2:
			print(f'a+b=',a+b)
		elif choice ==5:
			break
	else:
		print(f'类型错误，类型不为浮点型或整型,a为{type(a)}，b为{type(b)}')
		break

