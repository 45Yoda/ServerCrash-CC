import socket
import struct
import time
import json
import calcs
import config

#class AgenteUDP:

#    def __init__(self):

def listen():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM,
                         socket.IPPROTO_UDP)


    sock.setsockopt(socket.SOL_SOCKET,
                    socket.SO_REUSEADDR,1)

    sock.bind(config.mcast_group)


    mreq = struct.pack("4sl",
                        socket.inet_aton(config.MCAST_GRP),
                        socket.INADDR_ANY)

    sock.setsockopt(socket.IPPROTO_IP,
                    socket.IP_ADD_MEMBERSHIP,
                    mreq)

    while True:
        print (sock.recv(1024).decode())
        time.sleep(3)
        resp()

def resp():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)

    answer = {'memAvailable': calcs.memAv(),
              'Load': calcs.load(),
             }

    sock.sendto(json.dumps(answer).encode("utf-8"),config.udp_group)


listen()

#def main():
#    AgenteUDP()

#main()
