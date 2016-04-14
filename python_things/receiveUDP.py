import socket

def main():
	IPADDR = str(raw_input("SERVER IP: "))
	PORT = int(raw_input("PORT: "))
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((IPADDR, PORT))
	
	while True:
		data, addr = sock.recvfrom(1024)
		print "received msg: ", data
main()
