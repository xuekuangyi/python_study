import socket
def main_method():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('', 1234))
	while True:
		var = input('请输入内容>>>')
		s.sendto(var.encode('GBK'),("192.168.1.12", 8080))
		if var == 'exit':
			break

	s.close()


main_method()