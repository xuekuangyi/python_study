import socket

# 创建套接字对象
file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
file_socket.connect(('192.168.1.12', 1200))
# 输入下载文件名
file_name = input('请输入文件名称>>>')
# 将文件名传送至服务器
file_socket.send(file_name.encode('GBK'))
# 接收服务器指定内容
file_content = file_socket.recv(1024)
# 使用上下文管理器打开文件
with open('副本'+file_name, "wb") as ff:
	# 将服务器推送的内容，写入文件内容
	ff.write(file_content)
# 关闭套接字
file_socket.close()

