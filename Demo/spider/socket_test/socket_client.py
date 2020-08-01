# socket 客户端

import socket

client = socket.socket()
client.connect(('192.168.1.113', 8000))
# 发送数据  要保证编码解码一致
# client.send("lmc".encode("utf8"))
server_data = client.recv(1024)
print("server response: {}".format(server_data.decode("utf8")))
while True:
    input_data = input()
    client.send(input_data.encode("utf-8"))
    server_data = client.recv(1024)
    print("server response: {}".format(server_data.decode("utf8")))

