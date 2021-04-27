import os
import sys
import errno
import select
import socket


class Client(object):
    def __init__(self, my_username, IP="127.0.0.1", PORT=1234):
        self.my_username = my_username
        self.HEADER_LENGTH = 10

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((IP, PORT))
        self.client_socket.setblocking(False)

        username = my_username.encode('utf-8')
        username_header = f"{len(username):<{self.HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(username_header + username)


if __name__ == "__main__":
    os.system("clear")
    user = input("Enter username  >> ")
    client = Client(user)
    while True:
        message = input(f"{client.my_username}  >> ")
        if message:
            message = message.encode('utf-8')
            message_header = f"{len(message):<{client.HEADER_LENGTH}}".encode('utf-8')
            client.client_socket.send(message_header + message)
        try:
            while True:
                username_header = client.client_socket.recv(client.HEADER_LENGTH)
                if not len(username_header):
                    print("\nConnection terminated by the server!")
                    sys.exit()
                username_length = int(username_header.decode('utf-8').strip())
                username = client.client_socket.recv(username_length).decode('utf-8')
                message_header = client.client_socket.recv(client.HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                message = client.client_socket.recv(message_length).decode('utf-8')
                print(f'{username}  >> {message}')
        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print(f'Reading error: {str(e)}')
                sys.exit()
            continue
        except Exception as e:
            print(f'Reading error: {str(e)}')
            sys.exit()
