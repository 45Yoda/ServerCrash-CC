import random
import socket
import struct
import time
import json
from src import calcs, config

#self.socket.setsockopt(socket.SOL_SOCKET,
#                   socket.SO_REUSEADDR, 1)


class AgentUDP:

    def __init__(self):
        self.hold = random.randint(0,10)
        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_DGRAM,
                                    socket.IPPROTO_UDP)

        self.socket.bind(config.mcast_group)
        mreq = struct.pack("4sl",
                           socket.inet_aton(config.MCAST_GRP),
                           socket.INADDR_ANY)
        self.socket.setsockopt(socket.IPPROTO_IP,
                               socket.IP_ADD_MEMBERSHIP,
                               mreq)

        self.listen()

    def listen(self):
        while True:
            data, addr = self.socket.recvfrom(1024)
            dt = json.loads(data.decode())
            print(dt)

            if dt['Type'] == 'request':
                time.sleep(self.hold)
                resp(self, addr)


def resp(self, addr):

    answer = {'Mem_Available': calcs.memAv(),
              'Load': calcs.load(),
              'IP_Addr': addr[0],
              'Port': addr[1]
             }

    self.socket.sendto(json.dumps(answer).encode("utf-8"), ("localhost",8888))


def main():
    agent = AgentUDP()
    agent.listen()


if __name__ == "__main__":
    main()