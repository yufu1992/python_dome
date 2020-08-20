import socket
import re
import multiprocessing

def sercvice_client(new_socket):
	""" 为这个客户端返回数据 """
	# 1.接收浏览器发送过来的请求，即http请求
	# GET / HTTP/1.1
	# ...
	#requst = new_socket.recv(1024).decode("utf-8")
	request = new_socket.recv(1024).decode("utf-8")

	#requst_lines = requst.splitlines()
	request_lines = request.splitlines()
	print("")
	print(">"*20)
	print(request_lines)

	# GET /index.html HTTP/1.1
	# get post put del
	file_name = ""
	#ret = re.match(r"[^/]+(/[^ ]*)", requst_lines[0])
	ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])

	#if ret:
	#	file_name = ret.group(1)
	#	if file_name == "/":
	#		file_name = "/index.html"
	if ret:
		file_name = ret.group(1)
		# print("*"*50, file_name)
		if file_name == "/":
			file_name = "/index.html"


	# 2.返回http格式的数据，给浏览器
	# try:
	# 	f = open("./html" + file_name, "rb")
	# except:
	# 	response = "HTTP/1.1 404 NOT FOUND\r\n"
	# 	response += "\r\n"
	# 	response += "------file not found------"
	# 	new_socket.send(response.encode("utf-8"))
	# else:
	# 	html_content = f.read()
	# 	f.close()
	# 	# 2.1 准备发送给浏览器的数据---header
	# 	response = "HTTP/1.1 200 OK\r\n"
	# 	response = "\r\n"
	# 	# 2.2 准备发送给浏览器的数据---boy

	# 	# 将response header发送给浏览器
	# 	new_socket.send(response.encode("utf-8"))
	# 	# 将response boy发送给浏览器
	# 	new_socket.send(html_content)
	try:
		f = open("./html" + file_name, "rb")
	except:
		response = "HTTP/1.1 404 NOT FOUND\r\n"
		response += "\r\n"
		response += "------file not found-----"
		new_socket.send(response.encode("utf-8"))
	else:
		html_content = f.read()
		f.close()

		response = "HTTP/1.1 200 OK\r\n"
		response += "\r\n"

		new_socket.send(response.encode("utf-8"))

		new_socket.send(html_content)

	# 关闭套接
	new_socket.close()


def main():
	"""用来完成完整的控制"""
	# 1. 创建套接字
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# 2. 绑定
	tcp_server_socket.bind(("", 7890))
	# 3. 变为监听套接字
	tcp_server_socket.listen(128)

	while True:
		# 4. 等待新客户的链接
		new_socket, client_addr = tcp_server_socket.accept()

		# 5. 为这个客户端服务
		p = multiprocessing.Process(target=sercvice_client, args=(new_socket,))
		p.start()

		new_socket.close()

	# 关闭套接字
	tcp_server_socket.close()

if __name__ == "__main__":
	main()