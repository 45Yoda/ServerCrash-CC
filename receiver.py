import socket
import struct

##AGENTE UDP recebe em MULTICAST

MCAST_GRP = "239.8.8.8"
MCAST_PORT = 8888

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)

#dunno what this part does i'll just leave it
#sock.setsockopt(socket.SOL_SOCKET,
#                socket.SO_REUSEADDR,1)

sock.bind((MCAST_GRP,MCAST_PORT))

mreq = struct.pack("4sl",
                   socket.inet_aton(MCAST_GRP),
                   socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP,
                socket.IP_ADD_MEMBERSHIP,
                mreq)

while True:
  print (sock.recv(1024))


#MONITOR UDP recebe em UNICAST

#UDP_IP = "239.8.8.8"
#UDP_PORT = 8888

#sock = socket.socket(socket.AF_INET,
#                     socket.SOCK_DGRAM)
#sock.bind((UDP_IP,UDP_PORT))

#while True:
#    data= sock.recvfrom(1024)
#    print "Whut: ", data
