import socket

IPADDR = str(raw_input("IP: "))
PORTNUM = int(raw_input("PORT: ")) 
def main():
	PACKETDATA = str(raw_input("msg: "))
	#PACKETDATA.decode('hex')

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
	s.connect((IPADDR, PORTNUM))
	s.send(PACKETDATA)
	s.close()
while True:
	main()
