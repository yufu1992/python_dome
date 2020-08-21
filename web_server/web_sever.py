import socket
import re
import multiprocessing
import time
import mini_frame


class WSGIServer(object):
    def __init__(self):
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定
        self.tcp_server_socket.bind(("", 7890))
        # 3. 变为监听套接字
        self.tcp_server_socket.listen(128)


    def sercvice_client(self, new_socket):
        """ 为这个客户端返回数据 """
        # 1.接收浏览器发送过来的请求，即http请求
        # GET / HTTP/1.1
        # ...
        # requst = new_socket.recv(1024).decode("utf-8")
        request = new_socket.recv(1024).decode("utf-8")

        # requst_lines = requst.splitlines()
        request_lines = request.splitlines()
        print("")
        print(">" * 20)
        print(request_lines)

        # GET /index.html HTTP/1.1
        # get post put del
        file_name = ""
        # ret = re.match(r"[^/]+(/[^ ]*)", requst_lines[0])
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])

        # if ret:
        #	file_name = ret.group(1)
        #	if file_name == "/":
        #		file_name = "/index.html"
        if ret:
            file_name = ret.group(1)
            # print("*"*50, file_name)
            if file_name == "/":
                file_name = "/index.html"


        # 2.返回http格式的数据，给浏览器
        # 2.0 如果请求的资源不是以.py结尾的就是以为是静态资源
        if not file_name.endswith(".py"):
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
        else:
            # 2.0.1 如果是以.py结尾ide，就是动态请求
            header = "HTTP/1.1 200 OK\r\n"
            header += "\r\n"

            body = mini_frame.application(file_name)

            response = header+body
            # 发送response给浏览器
            new_socket.send(response.encode("utf-8"))


        # 关闭套接
        new_socket.close()

    def run_forever(self):
        """用来完成完整的控制"""

        while True:
            # 4. 等待新客户的链接
            new_socket, client_addr = self.tcp_server_socket.accept()

            # 5. 为这个客户端服务
            p = multiprocessing.Process(target=self.sercvice_client, args=(new_socket,))
            p.start()

            new_socket.close()

        # 关闭套接字
        tcp_server_socket.close()


def main():
    """控制整体，创建一个web服务器对象，然后调用这个对象的run_forever方法运行"""
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()

if __name__ == "__main__":
	main()