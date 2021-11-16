# 了解HTTP及网络基础

web 使用HTTP超文本传输协议作为规范，完成从客户端到服务器端的一系列流程。
- 协议是规则的约定

基于传输层协议的套接字编程
套接字这个词对很多不了解网络编程的人来说显得非常晦涩和陌生，其实说得通俗点，套接字就是一套用[C语言]
(https://zh.wikipedia.org/wiki/C%E8%AF%AD%E8%A8%80)
写成的应用程序开发库，主要用于实现进程间通信和网络编程，在网络应用开发中被广泛使用。
在Python中也可以基于套接字来使用传输层提供的传输服务，
并基于此开发自己的网络应用。实际开发中使用的套接字可以分为三类：流套接字（TCP套接字）、数据报套接字和原始套接字。

## TCP套接字

所谓TCP套接字就是使用TCP协议提供的传输服务来实现网络通信的编程接口。
在Python中可以通过创建socket对象并指定type属性为SOCK_STREAM来使用TCP套接字。
由于一台主机可能拥有多个IP地址，而且很有可能会配置多个不同的服务，所以作为服务器端的程序，需要在创建套接字对象后将其绑定到指定的IP地址和端口上 。
这里的端口并不是物理设备而是对IP地址的扩展，用于区分不同的服务，例如我们通常将HTTP服务跟80端口绑定，而MySQL数据库服务默认绑定在3306端口，
这样当服务器收到用户请求时就可以根据端口号来确定到底用户请求的是HTTP服务器还是数据库服务器提供的服务。
端口的取值范围是0~65535，而1024以下的端口我们通常称之为“著名端口”（留给像FTP、HTTP、SMTP等“著名服务”使用的端口，有的地方也称之为“周知端口”），
自定义的服务通常不使用这些端口，除非自定义的是HTTP或FTP这样的著名服务。
  
- _**客户端代码**_
```python
import socket

def main():
	# 创建套接字时，构造函数参数使用socket.SOCK_STEAM
	tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
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
```
需要注意的是，上面的服务器并没有使用多线程或者异步I/O的处理方式，这也就意味着当服务器与一个客户端处于通信状态时，
其他的客户端只能排队等待。。
- 服务器端代码

```python
import socket
def main():
	# 创建套接字，套接字类型为SOCK_STREAM TCP类型
	tcp_server_socket = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
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

```
## UDP套接字
> 传输层除了有可靠的传输协议TCP之外，还有一种非常轻便的传输协议叫做用户数据报协议，简称UDP。
在Python中可以通过创建socket对象并指定type属性为`SOCK_DGRAM`来使用TCP套接字。
TCP和UDP都是提供端到端传输服务的协议，二者的差别就如同打电话和发短信的区别，

后者不对传输的可靠性和可达性做出任何承诺从而避免了TCP中握手和重传的开销，
所以在强调性能和而不是数据完整性的场景中（例如传输网络音视频数据），UDP可能是更好的选择。
在观看网络视频时，有时会出现卡顿，有时会出现花屏，这无非就是部分数据传丢或传错造成的。
在Python中也可以使用UDP套接字来创建网络应用。


```python

import socket
def main_method():
    # type=SOCK_DGRAM，UDP套接字
	s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	s.bind(('', 1234))
	while True:
		var = input('请输入内容>>>')
		s.sendto(var.encode('GBK'),("192.168.1.12", 8080))
		if var == 'exit':
			break

	s.close()
```

HTTP 协议：
HTTP协议作用`应用层协议`，是基于`传输层协议UDP`的，客户端浏览器和服务器之间先要建立一个TCP/IP连接（socket套接字）
