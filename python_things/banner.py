#!/usr/bin/python

'''
usage:	python banner.py site_address port /
'''
	                                              
import httplib                                                
import sys
def main(host, port, url):                                    
	conn = httplib.HTTPConnection(host, port);                
	conn.request("HEAD", url)                                 
	response = conn.getresponse()                             
 
	print "[*] HTTP response code: ", response.status            
	print "[*] web server banner: ", response.getheader("Server")
 
if __name__ == '__main__':                                   
	host = sys.argv[1]                                       
	port = sys.argv[2]
	url = sys.argv[3]

main(host, port, url)
