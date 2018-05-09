import socket
import time

MCAST_GRP = "239.8.8.8"
MCAST_PORT = 8888

UDP_IP = "127.0.0.1"
UDP_PORT = 8888



def probe():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM,
                         socket.IPPROTO_UDP)

    sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,2)
    sock.sendto("Hello, World!",(MCAST_GRP,MCAST_PORT))


def listenAnswer():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    sock.bind((UDP_IP,UDP_PORT))

    while True:
        data = sock.recvfrom(1024)
        end = time.time()
        what = end-start
        
        print "WHUT: " + str(what), data




start = time.time()
probe()

listenAnswer()
