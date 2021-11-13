import socket

def main():
	# 创建套接字
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 绑定端口
	tcp_server_socket.bind(('', 5678))
	# 将套接字转为被动监听
	tcp_server_socket.listen(128)
	while True:
		# 等待客户端连接
		print('等待客户机接入…')
		new_socket, address = tcp_server_socket.accept()
		print(f'{address}已接入:')
		# print(new_socket)
		while True: # 循环为一个客户服务
			# 接收数据，使用socket.recv()方法，此方法中只有str，非元组
			recv_data = new_socket.recv(1024)
			print(f'{address}说：', recv_data.decode('GBK'))
			# 1、如果客户端关闭，则跳出当前的recv()方法
			if recv_data.decode('GBK'):
				# 直接返回数据给客户端
				respose = new_socket.send('成功接收信息，谢谢'.encode('GBK'))
				print(respose)
			else:
				break
		# 关闭监听套接字和通信套接字
		new_socket.close()
	tcp_server_socket.close()


if __name__ == "__main__":
	main()
