# scocket编程

```python
import socket


def send_file_to_client(comm_socket, client_address):
	# 获取客客端提交的请求下载的文件名
	file_name = comm_socket.recv(1024).decode('GBK')
	print('客户机想要下载的文件为%s' % file_name)
	file_content = ''
	# 读取要下载的文件，存入变量file_content中
	try:
		# 按客户端请求的文件名打开文件
		file_obj = open(file_name, "rb")
		file_content = file_obj.read()
		file_obj.close()
	except Exception as ret:
		print('查无此文件')

	if file_content:
		# 发送文件内容到客户端
		comm_socket.send(file_content)


def main():
	# 创建套接字对象
	tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
	# 将套接字做端口绑定
	tcp_socket.bind(('', 1200))
	# 将套接字转为被动
	tcp_socket.listen(128)
	print('监听客户机接入…')
	# 等待客户端连接,方法返回元组——新的通信用套接字和客户机信息
	while True:
		comm_socket, address = tcp_socket.accept()
		print(address, f'接入中')
		# 调用发送文件函数
		send_file_to_client(comm_socket, address)
		# 关闭套接字
		comm_socket.close()
	tcp_socket.close()
"""
if __name__ == '__main__':的作用
一个python文件通常有两种使用方法，第一是作为脚本直接执行，
第二是 import 到其他的 python 脚本中被调用（模块重用）执行。
因此 if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，
在 if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，
而 import 到其他脚本中是不会被执行的

"""

if __name__ == '__main__':
	main()

```

