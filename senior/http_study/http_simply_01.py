import socket


def server_client(conn_socket):
	# 接受用户请求：
	print(conn_socket.recv(1024))
	# response += '<h1>你好，世界</h><body>你好，世界</body>'
	try:
		file_obj = open('classical_layout.html', "rb")
		print(f'html文件对象：{file_obj}')
		content = file_obj.read()
		print(f'输出内容为：{content}')
		file_obj.close()
	except Exception as ret:
		print('404 not found')
	# 将字节流使用encode转码后再与文件内容拼接
	conn_socket.send(str('HTTP / 1.1 200 OK \r\n\r\n').encode('GBK') + content)
	conn_socket.close()


def main():
	# 创建套接字对象
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 四次挥手
	udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
	print(f'1.套接字创建成功')
	# 绑定端口2345
	udp_socket.bind(('192.168.1.12', 1025))
	print(f'2.端口绑定成功')
	# 转为监听
	udp_socket.listen(128)
	print(f'3.套按字转为监听')
	while True:
		# 等待客户接入
		print(f'4.等待用户接入')
		conn_socket, address = udp_socket.accept()
		print(f'5.用户已接入，接入的用户为{address}')
		server_client(conn_socket)
	udp_socket.close()

if __name__ == '__main__':
    main()