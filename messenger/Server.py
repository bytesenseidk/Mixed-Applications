import os
import select
import socket


class Server(object):
    def __init__(self, IP="127.0.0.1", PORT=1234):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((IP, PORT))
        self.server_socket.listen()
        self.HEADER_LENGTH = 10
        self.sockets_list = [self.server_socket]
        self.clients = {}
        os.system("clear")
        print(f"[ SERVER UP AND RUNNING ]\n[IP: {IP}]\n[Port: {PORT}]\n")

    def receive_message(self, client_socket):
        try:
            message_header = client_socket.recv(self.HEADER_LENGTH)
            if not len(message_header):
                return False
            message_length = int(message_header.decode("utf-8").strip())
            return {"header": message_header, "data": client_socket.recv(message_length)}
        except:
            return False


if __name__ == "__main__":
    server = Server()
    while True:
        read_sockets, _, exception_sockets = select.select(server.sockets_list, [], server.sockets_list)
        for notified_socket in read_sockets:
            if notified_socket == server.server_socket:
                client_socket, client_address = server.server_socket.accept()
                user = server.receive_message(client_socket)
                if user is False:
                    continue
                server.sockets_list.append(client_socket)
                server.clients[client_socket] = user
                ip, port = client_address
                print(f"\n[ USER CONNECTED: {user['data'].decode('utf-8')} ]\n"
                      f"[IP: {ip}]\n[Port: {port}]\n")
            else:
                message = server.receive_message(notified_socket)
                if message is False:
                    print(f"[ CONNECTION TERMINATED: {user['data'].decode('utf-8')} ]")
                    server.sockets_list.remove(notified_socket)
                    del server.clients[notified_socket]
                    continue
                user = server.clients[notified_socket]
                print(f"{user['data'].decode('utf-8')}  >> {message['data'].decode('utf-8')}")
                for server.client_socket in server.clients:
                    if server.client_socket != notified_socket:
                        server.client_socket.send(user["header"] + user["data"] + message["header"] + message["data"])
        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del server.clients[notified_socket]
