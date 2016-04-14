#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import requests
import os

url = raw_input("[*] Enter URL: ")

def main():
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	title = soup.head.title
	head = soup.head
	body = soup.body
	links = soup.findAll('a')
	print ("[*] 1. <HEAD> \n[*] 2. <BODY>\n[*] 3. title\n[*] 4. hrefs\n ")
	choose = int(input("Choose: "))
	if choose == 1:
		print head
	elif choose == 2:
		print body
	elif choose == 3:
		print title
	elif choose == 4:
		print links
	else:
		print ("FUCK YOU IDIOT!") 
while True:
	main()
