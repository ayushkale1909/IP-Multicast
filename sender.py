import socket

MCAST_GROUP = '224.1.1.1'
MCAST_PORT = 5007

def multicast_sender(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    sock.sendto(message.encode(), (MCAST_GROUP, MCAST_PORT))

if __name__ == "__main__":
    while True:
        message = input("Enter a message to send: ")
        multicast_sender(message)
