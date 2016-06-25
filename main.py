__author__ = 'barrycahill'

import socket
import netifaces as ni
import struct

ni.ifaddresses('en0')
UDP_IP = ni.ifaddresses('en0')[2][0]['addr']
#This will automatically now get the best
UDP_PORT = 5003
buffer_size = 110   # buffer size is 110 bytes

print 'Current using IP address: ',  UDP_IP, 'Port : ', UDP_PORT
sock = socket.socket(socket.AF_INET,   # Internet
                     socket.SOCK_DGRAM)    # UDP
sock.bind((UDP_IP, UDP_PORT))
#tp1 is touch point one, x and y values. tp2 is touch point 2

while True:
    data, addr = sock.recvfrom(buffer_size)
    # print "received message:", data
    tp1x = struct.unpack('i', data[94:98])
    #unpack the data
    # print tp1x

sock.close()