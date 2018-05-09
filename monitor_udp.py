import socket
import time
import json
import config

class MonitorUDP:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM,
                                  socket.IPPROTO_UDP)

        self.start = time.time()
        self.probe()

        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM)
        self.sock.settimeout(5)
        self.sock.bind(config.udp_group)

        self.listenAnswer()



    def probe(self):

        message ='Hello, World!'
        #sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,2)
        self.sock.sendto(message.encode('utf-8'),config.mcast_group)


    def listenAnswer(self):

        while True:
            try:
                data, addr = self.sock.recvfrom(1024)
                end = time.time()
                what = end-self.start
                parsed = json.loads(data)
                print ('Time: ' + str(what))
                print ( json.dumps(parsed,indent=2))
                print('Address: %s' % (addr,))
            except socket.timeout:
                break

def main():
    MonitorUDP()

main()
