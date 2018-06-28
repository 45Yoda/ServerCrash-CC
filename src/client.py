import socket
import threading
from threading import Thread


class ClientThread(Thread):

    def __init__(self, client_socket, agent_ip):

        Thread.__init__(self)
        self.client_socket = client_socket
        self.agent_ip = agent_ip
        self.agent_socket = socket.socket(socket.AF_INET,
                                          socket.SOCK_STREAM)
        self.agent_socket.connect((self.agent_ip, 8008))

    def run(self):

        print("Client Connected")

        threading.Thread(target=answer, args=[self.agent_socket, self.client_socket]).start()
        data = self.client_socket.recv(4096)
        while True:
            if not data:
                self.client_socket.close()
                self.agent_socket.close()
                break
            self.agent_socket.send(data)
            data = self.client_socket.recv(4096)


def answer(self):
    data = self.agent_socket.recv(4096)
    while True:
        if not data:
            self.client_socket.close()
            self.agent_socket.close()
            break
        self.client_socket.send(data)
        data = self.agent_socket.recv(4096)
