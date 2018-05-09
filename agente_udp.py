import socket
import struct
import time
import json
import calcs
import config

class AgenteUDP:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM,
                                  socket.IPPROTO_UDP)


        self.sock.setsockopt(socket.SOL_SOCKET,
                             socket.SO_REUSEADDR,1)

        self.sock.bind(config.mcast_group)


        mreq = struct.pack("4sl",
                            socket.inet_aton(config.MCAST_GRP),
                            socket.INADDR_ANY)

        self.sock.setsockopt(socket.IPPROTO_IP,
                             socket.IP_ADD_MEMBERSHIP,
                             mreq)
        self.listen()

    def listen(self):

        while True:
            print (self.sock.recv(1024).decode())
            time.sleep(3)
            self.resp()

    def resp(self):
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM)
        answer = {'memAvailable': calcs.memAv(),
                  'Load': calcs.load(),
                 }
        self.sock.sendto(json.dumps(answer).encode("utf-8"),config.udp_group)

def main():
    AgenteUDP()

main()
