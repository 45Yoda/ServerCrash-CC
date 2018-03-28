import socket

#AGENTE UDP ENVIA EM UNICAST

##UNICAST
UCAST_GRP = "239.8.8.8"
UCAST_PORT = 8888

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)

sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,2)
sock.sendto("Hello, World!",(UCAST_GRP,UCAST_PORT))

##MONITOR UDP ENVIA EM MULTICAST

#MCAST_GRP = "239.8.8.8"
#MCAST_PORT = 8888

#sock = socket.socket(socket.AF_INET,
#                     socket.SOCK_DGRAM,
#                     socket.IPPROTO_UDP)

#sock.setsockopt(socket.IPPROTO_IP,
#                socket.IP_MULTICAST_TTL,2)

#sock.sendto("Hello, World!",(MCAST_GRP,MCAST_PORT))
