import socket
import struct
import logging
import signal
import sys
from datetime import datetime

MCAST_GROUP = '224.1.1.1'
MCAST_PORT = 5007

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def signal_handler(sig, frame):
    logging.info("Exiting gracefully...")
    sys.exit(0)

def multicast_receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    sock.bind(('', MCAST_PORT))

    group = socket.inet_aton(MCAST_GROUP)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    logging.info("Multicast Receiver started...")
    
    while True:
        try:
            data, address = sock.recvfrom(1024)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logging.info(f"Received message from {address} at {current_time}: {data.decode()}")
        except Exception as e:
            logging.error(f"Error while receiving message: {str(e)}")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    multicast_receiver()
