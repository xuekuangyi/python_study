import socket

# 1.创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 2.端口绑定
address = ('', 3721)
udp_socket.bind(address)
# 3.接收数据 socket.recvfrom(接受最大字节数)
while True:
	data = udp_socket.recvfrom(1024)
	# 4.展示数据
	# print(data)
	rev_message = data[0]
	print(f"地址{data[1][0]}端口{data[1][1]}说:{data[0].decode('GBK')}")
# 5.关闭套接字
udp_socket.close()

