# socket 服务端

import socket
import threading

server = socket.socket()
# 绑定到 0.0.0.:8080端口上
server.bind(('0.0.0.0', 8000))
server.listen()

data = ""

def handle_sock(sock, addr):
    while True:
        # recv 方法是阻塞的
        tmp_data = sock.recv(1024)
        print(tmp_data.decode("utf8"))
        input_data = input()
        sock.send(input_data.encode("utf8"))

# 获取客户端连接并启动线程去处理
while True:
    # recv 方法是阻塞的
    # 阻塞等待连接
    sock, addr = server.accept()

    # 启动一个线程来处理新的连接
    client_thread = threading.Thread(target=handle_sock(), args=(sock, addr))
    client_thread.start()


if __name__ == "__main__":
    print(data)
    sock.close()



