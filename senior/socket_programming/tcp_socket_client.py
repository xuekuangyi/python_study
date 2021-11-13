import socket


def send_msg(input_msg, tcp_socket):
	send_msg = str(input_msg).encode('GBK')
	tcp_socket.send(send_msg)


def recv_msg(tcp_socket):
	recv_msg = str(tcp_socket.recv(1024)).decode('GBK')
	print(recv_msg)


def main():
	# 创建套接字时，构造函数参数使用socket.SOCK_STEAM
	tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
	# 端口绑定,OSError: [WinError 10048] 通常每个套接字地址(协议/网络地址/端口)只允许使用一次。
	# tcp_socket.bind(('', 1234))
	# 创建TCP连接
	tcp_socket.connect(('192.168.1.12', 1234))
	# 获取键盘输入并发送 使用的是socket.send()不是sendto()
	while True:
		input_msg = input(f'请输入要发送的内容>>>')
		if input_msg != '退出':
			send_msg(input_msg, tcp_socket)
			recv_msg(tcp_socket)
		# 关闭TCP连接
		else:
			tcp_socket.close()


if __name__ == '__main__':
	main()
