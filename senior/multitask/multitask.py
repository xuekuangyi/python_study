"""多任务进程练习，并发并行"""
import time
import threading


def task_01():
	for i in range(5):
		print(f'任务1执行第{i+1}次')
		time.sleep(1)


def task_02():
	for i in range(5):
		print(f'任务2执行第{i+1}次')
		time.sleep(1)


def main():
	# 创建Thread类，注意不能写成函数名加括号，只用函数名
	t1 = threading.Thread(target=task_01)
	t2 = threading.Thread(target=task_02)
	t1.start()  # 主线程，产生子线程
	t2.start()


if __name__ == '__main__':
	main()
