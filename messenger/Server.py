import os
import select
import socket

class Server(object):
    def __init__(self,  IP="127.0.0.1", POORT=1234):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((IP, PORT))
        self.server_socket.listen()

        self.sockets_list = [server_socket]
        self.clients = {}

        os.system("clear")
        print(f"[ Server running on IP: {IP} port: {PORT} ]\n")

    def receive_message(self, client_socket):
        try:
            message_header = client_socket.recv(HEADER_LENGTH)
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
                print(f"-- > New connection established from IP: {*client_address} user: {user['data'].decode('utf-8')}")
            else:
                message = server.receive_message(notified_socket)
                if message is False:
                    print(f"Connection terminated for user: {user['data'].decode('utf-8')}")
                    server.sockets_list.remove(notified_socket)
                    del server.clients[notified_socket]
                    continue
                user = server.clients[notified_socket]
                print(f"{user['data'].decode('utf-8')}  >> {message['data'].decode('utf-8')}")
                for server.client_socket in clients:
                    if server.client_socket != notified_socket:
                        server.client_socket.send(user["header"] + user["data"] + message["header"] + message["data"])
        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del server.clients[notified_socket]