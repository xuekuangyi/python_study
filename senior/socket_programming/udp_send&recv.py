import socket

def send_msg(udp_socket):
	message_send = input(f'请输入要发送的信息>>>')
	# 配置发送
	udp_socket.sendto(message_send.encode('GBK'), ('192.168.1.12', 1234))


def recv_msg(udp_socket):
	message_recv = udp_socket.recvfrom(1024)
	print(f'{message_recv[1]}:', message_recv[0].decode('GBK'))

# 配置接收

def main():
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# 绑定端口
	udp_socket.bind(('', 8081))
	while True:
		# 获取键盘输入
		print('欢迎使用')
		print('1——发送消息')
		print('2——接收消息')
		print('0——退出系统')
		op = input('请输入指令>>>')
		if op == '1':
			send_msg(udp_socket)
		elif op == '2':
			recv_msg(udp_socket)
		elif op == '3':
			break
		else:
			break


if __name__ == '__main__':
    main()




