import socket
import struct
import time
import subprocess
import re

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
        time.sleep(3)
        resp()



def resp():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    answer = memAv() + load()
    sock.sendto(answer,(UDP_IP,UDP_PORT))

def memAv():
    out = subprocess.check_output("free -m",shell=True)
    lol = re.findall("Mem:\s{1,}.*\s{1,}([0-9].*)",out)

    return "Mem Available: " + lol[0]

def load():
    out = subprocess.check_output("uptime",shell=True)
    lol = re.findall("[0-9]\.[0-9].+",out);

    return "Load: " + lol[0]


listen()
