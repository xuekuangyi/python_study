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


if __name__ == '__main__':
	main()
```

