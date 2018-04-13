import socket
import struct
import time

MCAST_GRP = "239.8.8.8"
MCAST_PORT = 8888

UDP_IP = "127.0.0.1"
UDP_PORT = 8888

def listen():
    sock = socket.socket(socket.AF_INET,
                        socket.SOCK_DGRAM,
                        socket.IPPROTO_UDP)


    sock.setsockopt(socket.SOL_SOCKET,
                    socket.SO_REUSEADDR,1)

    sock.bind((MCAST_GRP,MCAST_PORT))


    mreq = struct.pack("4sl",
                       socket.inet_aton(MCAST_GRP),
                       socket.INADDR_ANY)

    sock.setsockopt(socket.IPPROTO_IP,
                    socket.IP_ADD_MEMBERSHIP,
                    mreq)

    while True:
        print (sock.recv(1024))
        time.sleep(10)
        resp()



def resp():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    sock.sendto("Hello mah Friend!",(UDP_IP,UDP_PORT))

listen()
