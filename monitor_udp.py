import socket
import time
import json
import config

#class MonitorUDP:

    #def __init__(self):



def probe():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM,
                         socket.IPPROTO_UDP)

    message ='Hello, World!'
    #sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,2)
    sock.sendto(message.encode('utf-8'),config.mcast_group)


def listenAnswer():

    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)

    sock.settimeout(5)
    sock.bind(config.udp_group)

    while True:
        try:
            data, addr = sock.recvfrom(1024)
            end = time.time()
            what = end-start
            parsed = json.loads(data)
            print ('Time: ' + str(what))
            print ( json.dumps(parsed,indent=2))
            print('Address: %s' % (addr,))
        except socket.timeout:
            break


start = time.time()
probe()

listenAnswer()


#def main():
#    while 1:
#        MonitorUDP()

#main()
