# QQ服务器

# 转发消息
# 处理登录
# 处理退出
# 维护历史消息  维护在线用户和维护用户连接

import socket
import json
import threading
from collections import defaultdict

def ini_user():
    return {
        "name":"bobby",
        "sock":"sock"
    }
# 维护用户连接
online_users = defaultdict(ini_user())
online_users["bobby"] = {
    "name":"bobby",
    "sock":"sock"
}
online_users["bobby"]["name"] = "bobby"
print(online_users)
# online_users["a"]
a = online_users.get("a", "lmc")
print(a)

# 处理退出

# 维护历史消息， 维护在线用户和维护用户的连接
online_users = defaultdict(dict)
# 维护用户历史消息
user_msgs = defaultdict(list)

server = socket.socket()

# 绑定 IP
server.bind("0.0.0.0", 8000)
server.listen()

def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        json_data = json.loads(data.decode("utf8"))
        action = json_data.get("action", "")
        if action == "login":
            online_users[json_data["user"]] = sock
            sock.send("登录成功！".encode("utf8"))
        elif action == "list_user":
            # 获取当前在线用户
            all_users = [user for user, sock in online_users.items()]
            sock.send(json.dumps(all_users).encode("utf8"))
        elif action == "history_msg":
            sock.send(json.dumps(user_msgs.get(json_data["user"], [])).encode("utf8"))
            # if json_data["user"] in action:
            #     sock.send(json.dumps(user_msgs[json_data["user"]]).encode("utf8"))
        elif action == "send_msg":
            online_users.get(json_data["to"], None).send()

# 多线程
while True:
    # 阻塞等待连接
    sock, addr = server.accept()
    # 启动一个线程去处理新的用户连接
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

