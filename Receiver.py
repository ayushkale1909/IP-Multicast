import socket
import struct

MCAST_GROUP = '224.1.1.1'  
MCAST_PORT = 5007          

def multicast_receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', MCAST_PORT))

    group = socket.inet_aton(MCAST_GROUP)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        print('Waiting for message...')
        data, address = sock.recvfrom(1024)
        print('Received message:', data.decode(), 'from', address)

if __name__ == "__main__":
    multicast_receiver()
