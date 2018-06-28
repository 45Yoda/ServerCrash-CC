import socket

import client
from monitor_udp import MonitorUDP
from stat_table import StatTable


def main():
    stat = StatTable()
    mon = MonitorUDP(stat)
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp.bind(('localhost', 8003))
    threads = []

    while True:
        tcp.listen(30)
        print("TCP listening")
        (client_socket, (ip, port)) = tcp.accept()
        print("Communication received")
        top_server = stat.top_server()
        print("Connecting to server:")
        print(top_server)
        t1 = client.ClientThread(client_socket, top_server)
        t1.start()
        print("Thread Client-Server on")
        threads.append(t1)


if __name__ == "__main__":
    main()

